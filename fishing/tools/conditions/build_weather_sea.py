#!/usr/bin/env python3
"""Workstreams 2 and 3 (numeric parts): build fishing/research/weather.md and sea_state.md from the CSVs written by
fetch_conditions.py, the saved Met Office text products and fresh Environment Agency river levels.
Usage: build_weather_sea.py <repo_root>"""
import sys, csv, math, json, re, html, glob, time, statistics as st, collections, datetime as dt, pathlib, urllib.request
ROOT = pathlib.Path(sys.argv[1]); R = ROOT/'fishing/research'; DATA = R/'data'
now = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
f = lambda x: float(x) if x not in ('', None) else None
def cmean(ds):
    s = sum(math.sin(math.radians(d)) for d in ds); c = sum(math.cos(math.radians(d)) for d in ds)
    return (math.degrees(math.atan2(s, c)) + 360) % 360
def cspread(ds):
    m = cmean(ds); return max(abs((d - m + 180) % 360 - 180) for d in ds)
COMP = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
comp = lambda d: COMP[int((d + 11.25) // 22.5) % 16]
wx = list(csv.DictReader(open(DATA/'weather_hourly_multimodel.csv')))
points = list(dict.fromkeys(r['point'] for r in wx)); models = sorted(set(r['model'] for r in wx))
W_ = collections.defaultdict(list)
for r in wx: W_[(r['point'], r['time'])].append(r)
def cons(pt, t):
    L = W_.get((pt, t), [])
    g = lambda k: [f(r[k]) for r in L if f(r[k]) is not None]
    return dict(sp=g('wind_speed_10m'), di=g('wind_direction_10m'), gu=g('wind_gusts_10m'), pr=g('pressure_msl'), pc=g('precipitation'), cc=g('cloud_cover'), lc=g('cloud_cover_low'), tt=g('temperature_2m'), vis=g('visibility'))
raws = sorted(glob.glob(str(R/'raw/conditions/wx_*.json'))); stamps = sorted(set(re.search(r'_(\d{8}T\d{4}Z)\.json', x).group(1) for x in raws))
o = []; A = o.append
A('# Workstream 2 - Weather for Sunday 22 November 2026 (multi-model)\n')
A(f"**Built {now}** by `fishing/tools/conditions/build_weather_sea.py` from `data/weather_hourly_multimodel.csv` (every model x every reference point x every hour, 19-24 Nov), `data/ensemble_spread_22nov.csv`, `data/weather_history_21d.csv`. Raw API responses: `raw/conditions/wx_<model>_<fetch time>.json` (fetch stamps {', '.join(stamps)}).\n")
A('**Source (grade A - numerical model output):** Open-Meteo forecast API (api.open-meteo.com), one request per model. Models obtained: ' + ', '.join(f'`{m}`' for m in models) + '. **Not obtained:** `icon_seamless` (HTTP 429 rate limit after 6 attempts; `icon_eu` was obtained and covers the same DWD model family). Open-Meteo does not expose the initialisation time of each model run in the response; fetch times are given instead (THIN: exact run cycle unknown - at 16:10-16:30 UTC the newest available runs would normally be the 06Z/12Z cycles). Wind speeds are in **knots** (requested `wind_speed_unit=kn`), directions are degrees true **from**, times GMT.\n')
A('Grid note: every model returns its nearest grid cell; for coastal points this may be a land or mixed cell, which under-reads wind over open water (global models at 10-25 km most of all). Treat speeds as lower bounds for exposed headlands.\n')
# 1 synoptic / frontal timing
A('## 1. What the models show (synoptic reading - my inference from the tables, grade D on interpretation, A on numbers)\n')
def veer_time(pt, m):
    seq = sorted(((r['time'], f(r['wind_direction_10m'])) for r in wx if r['point'] == pt and r['model'] == m and '2026-11-21T18' <= r['time'] <= '2026-11-22T23' and f(r['wind_direction_10m']) is not None))
    for (t0, d0), (t1, d1) in zip(seq, seq[1:]):
        if 60 <= d0 <= 200 and 225 <= d1 <= 330: return t1
    # slower veer: first hour with westerly quadrant after a south-easterly
    seen = False
    for t, d in seq:
        if 60 <= d <= 180: seen = True
        if seen and 240 <= d <= 330: return t
    return None
key = ["St Mary's (Scilly)", "Land's End", 'Newlyn/Penzance', 'Porthleven/Loe Bar', 'Lizard Point', 'Falmouth Pendennis', 'Mevagissey', 'Fowey mouth', 'Looe', 'Rame Head', 'St Ives Head', 'Newquay Towan Head', 'Stepper Point', 'Tintagel Head', 'Bude']
A('A deepening low tracks north-east across or just north-west of Cornwall overnight 21/22 Nov. Ahead of it the wind is **south-easterly (about 110-125 deg), 18-27 kn mean with gusts 32-45 kn** from the evening of the 21st until the trough/front passes; the wind then **veers abruptly to west / west-north-west (about 270-290 deg), 17-30 kn with gusts 30-47 kn** for the rest of the 22nd, easing after midnight. Pressure bottoms out near **997-1000 hPa around 03:00-06:00** then rises about 3 hPa per 3 h to 1013-1017 hPa by 21:00. Rain: persistent overnight and morning, heaviest in the east (see section 6). Cloud: overcast (100 %) virtually all day; breaks reach Scilly from about 21:00 and west Cornwall after midnight.\n')
A('**Time of the SE -> W wind veer (front / trough passage), per model, GMT 22 Nov** (first hour with a westerly wind after the south-easterly; "21d" = already on the evening of the 21st; "none" = model keeps a different regime):\n')
A('| Point | ' + ' | '.join(m.replace('_deterministic','').replace('meteofrance_','mf_').replace('_europe','').replace('_harmonie_arome','_harm') for m in models) + ' | median | spread (h) |\n|---|' + '---|'*(len(models)+2))
for pt in key:
    cells = []; hrs = []
    for m in models:
        t = veer_time(pt, m)
        if t is None: cells.append('none')
        else:
            h = int(t[11:13]) + (0 if t[8:10] == '22' else -24); hrs.append(h); cells.append(t[11:16] if t[8:10] == '22' else t[11:16] + ' (21d)')
    A(f"| {pt} | " + ' | '.join(cells) + f" | {('%02d:00' % (st.median(hrs) % 24)) if hrs else 'n/a'} | {(max(hrs)-min(hrs)) if hrs else 'n/a'} |")
A('\n**Robust across models:** the SE gale overnight, the veer to W/WNW, strong westerlies all afternoon and evening, the pressure fall-then-rise, full cloud cover. **Uncertain:** the hour of the veer (spread grows eastwards - Looe, Rame and Bude are the least certain), the peak post-frontal wind (median 21-28 kn in the west, model range roughly 17-34 kn), rain totals in the east (convective/frontal placement), and when cloud breaks arrive in the evening.\n')
# 2. all points 3-hourly consensus
A('## 2. Wind consensus, every reference point, 3-hourly, 22 November\n')
A('Cell = median direction (compass) / median speed kn (model min-max) / median gust kn. Median over the models listed above.\n')
hrs3 = [f'2026-11-22T{h:02d}:00' for h in range(0, 24, 3)] + ['2026-11-23T00:00']
A('| Point | ' + ' | '.join(t[11:13] + 'h' if t[8:10] == '22' else '24h' for t in hrs3) + ' |\n|---|' + '---|'*len(hrs3))
for pt in points:
    cells = []
    for t in hrs3:
        c = cons(pt, t)
        cells.append(f"{cmean(c['di']):.0f} {comp(cmean(c['di']))} / {st.median(c['sp']):.0f} ({min(c['sp']):.0f}-{max(c['sp']):.0f}) / g{st.median(c['gu']):.0f}" if c['sp'] and c['gu'] else 'n/a')
    A(f'| {pt} | ' + ' | '.join(cells) + ' |')
# 3. hourly detail for key points
A('\n## 3. Hour-by-hour consensus at key points, 22 November\n')
for pt in ['Bude', 'Stepper Point', 'Newquay Towan Head', 'St Ives Head', "Land's End", 'Newlyn/Penzance', 'Porthleven/Loe Bar', 'Lizard Point', 'Falmouth Pendennis', 'Mevagissey', 'Looe', 'Rame Head', "St Mary's (Scilly)"]:
    A(f'**{pt}**\n')
    A('| Hour | Dir (deg, spread +-) | Speed kn median (min-max) | Gust kn median (max) | MSLP hPa | 3 h tendency hPa | Rain mm/h median (max) | Cloud % (low %) | Temp C | Vis km (min) |\n|---|---|---|---|---|---|---|---|---|---|')
    for h in range(24):
        t = f'2026-11-22T{h:02d}:00'; c = cons(pt, t)
        if not c['sp']: continue
        tprev = (dt.datetime(2026, 11, 22, h) - dt.timedelta(hours=3)).strftime('%Y-%m-%dT%H:00'); cp = cons(pt, tprev)
        tend = f"{st.median(c['pr']) - st.median(cp['pr']):+.1f}" if cp['pr'] and c['pr'] else ''
        vis = f"{st.median(c['vis'])/1000:.0f} ({min(c['vis'])/1000:.1f})" if c['vis'] else ''
        A(f"| {h:02d} | {cmean(c['di']):.0f} {comp(cmean(c['di']))} (+-{cspread(c['di']):.0f}) | {st.median(c['sp']):.0f} ({min(c['sp']):.0f}-{max(c['sp']):.0f}) | {st.median(c['gu']):.0f} ({max(c['gu']):.0f}) | {st.median(c['pr']):.1f} | {tend} | {st.median(c['pc']):.1f} ({max(c['pc']):.1f}) | {st.median(c['cc']):.0f} ({st.median(c['lc']):.0f}) | {st.median(c['tt']):.1f} | {vis} |")
    A('')
# 4. per-model disagreement
A('## 4. Model-by-model comparison (direction deg / speed kn / gust kn) at 00, 06, 12, 18 GMT on 22 November\n')
for pt in ['Bude', 'Newquay Towan Head', "Land's End", 'Porthleven/Loe Bar', 'Falmouth Pendennis', 'Looe', "St Mary's (Scilly)"]:
    A(f'**{pt}**\n\n| Model | 00h | 06h | 12h | 18h | Rain total 22 Nov mm |\n|---|---|---|---|---|---|')
    for m in models:
        cells = []
        for h in (0, 6, 12, 18):
            r = [x for x in W_.get((pt, f'2026-11-22T{h:02d}:00'), []) if x['model'] == m]
            cells.append(f"{f(r[0]['wind_direction_10m']):.0f} / {f(r[0]['wind_speed_10m']):.0f} / {f(r[0]['wind_gusts_10m']):.0f}" if r and f(r[0]['wind_speed_10m']) is not None and f(r[0]['wind_gusts_10m']) is not None and f(r[0]['wind_direction_10m']) is not None else 'n/a')
        rain = [f(x['precipitation']) for x in wx if x['point'] == pt and x['model'] == m and x['time'].startswith('2026-11-22') and f(x['precipitation']) is not None]
        A(f"| {m} | " + ' | '.join(cells) + f" | {sum(rain):.1f} |" if rain else f"| {m} | " + ' | '.join(cells) + ' | n/a |')
    A('')
# 5. ensembles
A('## 5. Ensemble spread, 22 November (Open-Meteo ensemble API; wind speed kn, p10 / median / p90 across members)\n')
ens = list(csv.DictReader(open(DATA/'ensemble_spread_22nov.csv')))
em = sorted(set(r['model'] for r in ens)); A('Ensembles obtained: ' + ', '.join(f"`{m}` ({next(r['n'] for r in ens if r['model']==m)} members)" for m in em) + '.\n')
for var, lab in (('wind_speed_10m', 'Wind speed kn'), ('wind_gusts_10m', 'Gust kn'), ('pressure_msl', 'MSLP hPa')):
    A(f'**{lab}**\n\n| Point | Ensemble | 00h | 06h | 12h | 18h |\n|---|---|---|---|---|---|')
    for pt in list(dict.fromkeys(r['point'] for r in ens)):
        for m in em:
            cells = []
            for h in (0, 6, 12, 18):
                r = [x for x in ens if x['point'] == pt and x['model'] == m and x['var'] == var and x['time'] == f'2026-11-22T{h:02d}:00']
                cells.append(f"{float(r[0]['p10']):.0f} / {float(r[0]['median']):.0f} / {float(r[0]['p90']):.0f}" if r else 'n/a')
            if any(c != 'n/a' for c in cells): A(f'| {pt} | {m} | ' + ' | '.join(cells) + ' |')
    A('')
# direction spread from ensembles: share of members westerly at given hours
# 6. rain totals
A('## 6. Rainfall forecast totals (mm), multi-model median (min-max)\n')
A('| Point | 21 Nov 12-24h | 22 Nov 00-06h | 22 Nov 06-12h | 22 Nov 12-24h | 22 Nov total |\n|---|---|---|---|---|---|')
def rsum(pt, t0, t1):
    tot = collections.defaultdict(float); n = collections.Counter()
    for r in wx:
        if r['point'] == pt and t0 <= r['time'] < t1 and f(r['precipitation']) is not None: tot[r['model']] += f(r['precipitation']); n[r['model']] += 1
    v = [x for x in tot.values()]
    return f"{st.median(v):.1f} ({min(v):.1f}-{max(v):.1f})" if v else 'n/a'
for pt in points:
    A(f"| {pt} | {rsum(pt,'2026-11-21T12','2026-11-22T00')} | {rsum(pt,'2026-11-22T00','2026-11-22T06')} | {rsum(pt,'2026-11-22T06','2026-11-22T12')} | {rsum(pt,'2026-11-22T12','2026-11-23T00')} | {rsum(pt,'2026-11-22T00','2026-11-23T00')} |")
# 7. onshore / offshore by broad coast
A('\n## 7. Wind against the broad coasts (the 1 km segment analysis in `coastline.md` uses true segment aspects)\n')
A('| Period (22 Nov) | Wind | North coast (faces NW-N) | West Penwith (faces W) | Mount\'s Bay (faces S-SE) | Lizard east side / Falmouth Bay (faces E-SE) | Mevagissey-Fowey-Looe-Whitsand (faces S-SE) | Scilly |\n|---|---|---|---|---|---|---|---|')
A('| 00:00 to the veer (about 02-03h Scilly, 03-05h Penwith/Mount\'s Bay, 05-07h Lizard/Falmouth/Newquay, 07-10h Looe/Rame/Bude) | SE 18-27 kn, gusts 32-45 | offshore (flattening the residual W swell) | offshore / cross-off | onshore to cross-onshore, sea building | dead onshore, short steep sea | onshore to cross-onshore | SE: onshore on east/south-facing shores |')
A('| Veer to 24:00 | W / WNW 17-30 kn, gusts 30-47 | onshore, sea building rapidly | dead onshore | cross-shore to cross-offshore (W) | offshore, sea dropping | cross-offshore, sea dropping | W: onshore on west-facing shores, lee on the east sides |')
# 8. pressure + history
A('\n## 8. Pressure trace 20-23 November (multi-model median, hPa) and 3-hourly tendency\n')
A('| Time (GMT) | Newlyn/Penzance | tend. | Bude | tend. | Looe | tend. | St Mary\'s | tend. |\n|---|---|---|---|---|---|---|---|---|')
tt = [dt.datetime(2026, 11, 20, 0) + dt.timedelta(hours=3*i) for i in range(32)]
for t in tt:
    cells = []
    for pt in ('Newlyn/Penzance', 'Bude', 'Looe', "St Mary's (Scilly)"):
        c = cons(pt, t.strftime('%Y-%m-%dT%H:00')); cp = cons(pt, (t - dt.timedelta(hours=3)).strftime('%Y-%m-%dT%H:00'))
        cells += [f"{st.median(c['pr']):.1f}" if c['pr'] else 'n/a', f"{st.median(c['pr'])-st.median(cp['pr']):+.1f}" if c['pr'] and cp['pr'] else '']
    A(f"| {t:%d %b %H}h | " + ' | '.join(cells) + ' |')
A('\n## 9. The preceding three weeks (Open-Meteo best-match analysis/short-range data, `data/weather_history_21d.csv` - model analysis, not station observations: grade A- ; station observations were not retrieved, THIN)\n')
hist = list(csv.DictReader(open(DATA/'weather_history_21d.csv')))
for pt in ('Newlyn/Penzance', 'Bude', 'Looe'):
    A(f'**{pt}** - daily summary\n\n| Date | MSLP mean (min-max) hPa | Mean wind kn | Max gust kn | Dominant direction | Rain mm | Temp min-max C |\n|---|---|---|---|---|---|---|')
    days = collections.defaultdict(list)
    for r in hist:
        if r['point'] == pt: days[r['time'][:10]].append(r)
    for d in sorted(days):
        if d > '2026-11-23': continue
        L = days[d]; g = lambda k: [f(r[k]) for r in L if f(r[k]) is not None]
        pr, sp, gu, di, pc, te = g('pressure_msl'), g('wind_speed_10m'), g('wind_gusts_10m'), g('wind_direction_10m'), g('precipitation'), g('temperature_2m')
        if not pr: continue
        A(f"| {d} | {st.mean(pr):.0f} ({min(pr):.0f}-{max(pr):.0f}) | {st.mean(sp):.0f} | {max(gu):.0f} | {comp(cmean(di))} ({cmean(di):.0f}) | {sum(pc):.1f} | {min(te):.0f}-{max(te):.0f} |")
    A('')
# 10. official text
A('## 10. Official text products (Met Office, grade A) - pages saved 2026-11-21 15:23 UTC in `raw/weather/`\n')
def text(fn):
    s = open(fn, encoding='utf-8', errors='ignore').read()
    s = re.sub(r'(?is)<(script|style|svg|noscript).*?</\1>', ' ', s); s = re.sub(r'(?s)<[^>]+>', '\n', s); s = html.unescape(s)
    return [l.strip() for l in s.split('\n') if l.strip()]
try:
    T = text(glob.glob(str(R/'raw/weather/metoffice_inshore_*.html'))[0])
    iss = next((' '.join(T[i:i+2]) for i, l in enumerate(T) if l.startswith('Issued at')), 'issue time not found')
    A(f'**Inshore waters forecast** ({iss}):\n')
    for keyw in ('Lyme Regis to Lands End including the Isles of Scilly (8)', 'Lands End to St Davids Head including the Bristol Channel (9)'):
        idx = [i for i, l in enumerate(T) if l.startswith(keyw)]
        if idx:
            seg = T[idx[-1]:idx[-1]+26]; cut = next((j for j, l in enumerate(seg[1:], 1) if re.search(r'\(\d+\)$', l)), len(seg))
            A(f"- *{keyw}*: " + ' | '.join(seg[1:cut]))
        else: A(f'- *{keyw}*: NOT FOUND in saved page')
    S = text(glob.glob(str(R/'raw/weather/metoffice_shipping_*.html'))[0])
    iss = next((' '.join(S[i:i+2]) for i, l in enumerate(S) if l.startswith('Issued at')), 'issue time not found')
    A(f'\n**Shipping forecast** ({iss}):\n')
    for a in ('Lundy', 'Plymouth', 'Sole', 'Fastnet'):
        idx = [i for i, l in enumerate(S) if l.strip() == a]
        A(f"- *{a}*: " + (' | '.join(S[idx[-1]+1:idx[-1]+16]) if idx else 'NOT FOUND'))
    Rg = text(glob.glob(str(R/'raw/weather/metoffice_regional_sw_*.html'))[0])
    i0 = next(i for i, l in enumerate(Rg) if l.startswith('Headline')); i1 = next(i for i, l in enumerate(Rg) if l.startswith('Updated'))
    A('\n**Regional forecast, South West England** (' + ' '.join(Rg[i1:i1+2]) + '): ' + ' '.join(Rg[i0:i1]))
    A('\n**Warnings:** the saved Met Office warnings page (15:23 UTC) was not parsed reliably (JavaScript-rendered list) - NOT FOUND whether a yellow wind/rain warning covers Cornwall for 22 Nov; the Shipping Forecast gale warnings above are in force for Lundy, Plymouth, Sole and Fastnet.')
except Exception as e:
    A(f'Text extraction failed: {e}')
A('\n## 11. Gaps\n\n- Station observations (Culdrose, Camborne, St Mawgan, St Mary\'s, Bude) for the preceding days were NOT retrieved; section 9 uses model analysis.\n- Model initialisation times are not exposed by the API (fetch times given).\n- `icon_seamless` not obtained (rate limit). No BBC / other third-party text forecast was compared.\n- Phase 3 must re-pull every model on the latest runs and log the changes.')
(R/'weather.md').write_text('\n'.join(o) + '\n')

# ---------------------------------------------------------------- sea state
wv = list(csv.DictReader(open(DATA/'waves_hourly_multimodel.csv')))
wmodels = sorted(set(r['model'] for r in wv)); V = collections.defaultdict(list)
for r in wv: V[(r['point'], r['time'])].append(r)
def wc(pt, t):
    L = [r for r in V.get((pt, t), []) if f(r['wave_height']) not in (None, 0.0)]     # 0.0 = land-masked cell in that model
    g = lambda k: [f(r[k]) for r in L if f(r[k]) is not None]
    tp = [(f(r['wave_peak_period']) or f(r['wave_period'])) for r in L if (f(r['wave_peak_period']) or f(r['wave_period']))]
    stp = [(f(r['swell_wave_peak_period']) or f(r['swell_wave_period'])) for r in L if (f(r['swell_wave_peak_period']) or f(r['swell_wave_period']))]
    return dict(n=len(L), hs=g('wave_height'), di=g('wave_direction'), tp=tp, sh=g('swell_wave_height'), sd=g('swell_wave_direction'), stp=stp, wh=g('wind_wave_height'), wd=g('wind_wave_direction'))
o = []; A = o.append
A('# Workstream 3 - Sea state for Sunday 22 November 2026 (model forecasts, river levels; observations and clarity evidence in `sea_clarity_evidence.md`)\n')
A(f"**Built {now}** by `fishing/tools/conditions/build_weather_sea.py`. Assessed only for effect on fish and on presenting baits/lures.\n")
A('**Source (grade A - numerical wave model output):** Open-Meteo marine API (marine-api.open-meteo.com), one request per wave model with `cell_selection=sea`: ' + ', '.join(f'`{m}`' for m in wmodels) + ' (Meteo-France MFWAM, ECMWF WAM 0.25 deg, NCEP GFS-Wave 0.25 and 0.16 deg, DWD EWAM (Europe) and GWAM (global)). Raw: `raw/conditions/marine_<model>_<fetch time>.json`; tidy table `data/waves_hourly_multimodel.csv`. Hs = significant height (m), Tp = peak period where the model gives it (otherwise mean period), direction = degrees true FROM.\n')
A('**Caveat (important):** these are offshore-of-the-point grid cells (roughly 5-25 km resolution). They do NOT include nearshore sheltering, refraction or breaking. A value of 0.0 from a model at a point means that model has no sea cell there and is excluded. Segment-level exposure is handled geometrically in `coastline.md`.\n')
A('## 1. Total sea, every reference point, 3-hourly, 22 November\n')
A('Cell = Hs median (model min-max) m / direction / Tp s; n = models with a sea cell.\n')
A('| Point | n | ' + ' | '.join(t[11:13] + 'h' if t[8:10] == '22' else '24h' for t in hrs3) + ' |\n|---|---|' + '---|'*len(hrs3))
for pt in points:
    cells = []; n = 0
    for t in hrs3:
        c = wc(pt, t); n = max(n, c['n'])
        cells.append(f"{st.median(c['hs']):.1f} ({min(c['hs']):.1f}-{max(c['hs']):.1f}) / {cmean(c['di']):.0f} {comp(cmean(c['di']))} / {st.median(c['tp']):.0f}" if c['hs'] and c['di'] and c['tp'] else 'n/a')
    A(f'| {pt} | {n} | ' + ' | '.join(cells) + ' |')
A('\n## 2. Swell and wind-sea components, 3-hourly, 22 November\n')
A('Cell = swell Hs / period s / direction ; wind-sea Hs / direction (multi-model medians). Component splits differ between models (partitioning schemes) - treat as indicative.\n')
A('| Point | ' + ' | '.join(t[11:13] + 'h' if t[8:10] == '22' else '24h' for t in hrs3) + ' |\n|---|' + '---|'*len(hrs3))
for pt in points:
    cells = []
    for t in hrs3:
        c = wc(pt, t)
        cells.append((f"sw {st.median(c['sh']):.1f}/{st.median(c['stp']):.0f}/{cmean(c['sd']):.0f}" if c['sh'] and c['stp'] and c['sd'] else 'sw n/a') + ' ; ' + (f"ws {st.median(c['wh']):.1f}/{cmean(c['wd']):.0f}" if c['wh'] and c['wd'] else 'ws n/a'))
    A(f'| {pt} | ' + ' | '.join(cells) + ' |')
A('\n## 3. Hour-by-hour at key points, 22 November\n')
for pt in ['Bude', 'Stepper Point', 'Newquay Towan Head', 'Perranporth', 'St Ives Head', "Land's End", 'Newlyn/Penzance', 'Porthleven/Loe Bar', 'Lizard Point', 'Coverack/Manacles', 'Falmouth Pendennis', 'Mevagissey', 'Par', 'Looe', 'Whitsand Bay', "St Mary's (Scilly)"]:
    A(f'**{pt}**\n\n| Hour | Hs median (min-max) | Dir | Tp | Swell Hs/T/dir | Wind-sea Hs |\n|---|---|---|---|---|---|')
    for h in range(24):
        c = wc(pt, f'2026-11-22T{h:02d}:00')
        if not c['hs']: continue
        A(f"| {h:02d} | {st.median(c['hs']):.1f} ({min(c['hs']):.1f}-{max(c['hs']):.1f}) | {cmean(c['di']):.0f} {comp(cmean(c['di']))} | {st.median(c['tp']):.0f} | " + (f"{st.median(c['sh']):.1f}/{st.median(c['stp']):.0f}/{cmean(c['sd']):.0f}" if c['sh'] and c['stp'] and c['sd'] else 'n/a') + ' | ' + (f"{st.median(c['wh']):.1f}" if c['wh'] else 'n/a') + ' |')
    A('')
A('## 4. Model-by-model Hs (m) at 00 / 06 / 12 / 18 GMT, 22 November\n')
A('| Point | ' + ' | '.join(wmodels) + ' |\n|---|' + '---|'*len(wmodels))
for pt in points:
    cells = []
    for m in wmodels:
        v = []
        for h in (0, 6, 12, 18):
            r = [x for x in V.get((pt, f'2026-11-22T{h:02d}:00'), []) if x['model'] == m and f(x['wave_height']) not in (None, 0.0)]
            v.append(f"{f(r[0]['wave_height']):.1f}" if r else '-')
        cells.append(' / '.join(v))
    A(f'| {pt} | ' + ' | '.join(cells) + ' |')
A('\n## 5. Lead-in: modelled sea on 19-21 November (multi-model median Hs m, daily max / direction at the time of the max)\n')
A('| Point | 19 Nov | 20 Nov | 21 Nov | 22 Nov | 23 Nov |\n|---|---|---|---|---|---|')
for pt in points:
    cells = []
    for d in ('19', '20', '21', '22', '23'):
        best = None
        for h in range(24):
            c = wc(pt, f'2026-11-{d}T{h:02d}:00')
            if c['hs'] and (best is None or st.median(c['hs']) > best[0]): best = (st.median(c['hs']), cmean(c['di']) if c['di'] else 0)
        cells.append(f"{best[0]:.1f} / {comp(best[1])}" if best else 'n/a')
    A(f'| {pt} | ' + ' | '.join(cells) + ' |')
# SST + currents
A('\n## 6. Sea-surface temperature and modelled currents (Open-Meteo marine best-match; `data/sst_currents_hourly.csv`)\n')
sc = list(csv.DictReader(open(DATA/'sst_currents_hourly.csv')))
A('SST is a model/analysis field (grade A-); buoy SSTs are in `sea_clarity_evidence.md` (12.7-13.6 C on 21 Nov). Current = total surface current of the ocean model at an offshore cell (km/h converted to knots); it under-resolves inshore races and eddies (THIN for anything within ~2 km of headlands).\n')
A('| Point | SST 22 Nov mean C | Max current kn (time GMT, direction it flows towards*) | Second peak kn (time) | Weakest kn (time) |\n|---|---|---|---|---|')
for pt in points:
    L = [r for r in sc if r['point'] == pt and r['time'].startswith('2026-11-22')]
    sst = [f(r['sst']) for r in L if f(r['sst']) is not None]; cur = [(f(r['cur_kmh'])/1.852, r['time'][11:16], f(r['cur_dir'])) for r in L if f(r['cur_kmh']) is not None]
    if not cur: A(f"| {pt} | {st.mean(sst):.1f} | n/a | n/a | n/a |" if sst else f'| {pt} | n/a | n/a | n/a | n/a |'); continue
    mx = max(cur); rest = [c for c in cur if abs(int(c[1][:2]) - int(mx[1][:2])) >= 4 and abs(int(c[1][:2]) - int(mx[1][:2])) <= 20]; mx2 = max(rest) if rest else None; mn = min(cur)
    A(f"| {pt} | {st.mean(sst):.1f} | {mx[0]:.1f} ({mx[1]}, {mx[2]:.0f}) | " + (f"{mx2[0]:.1f} ({mx2[1]})" if mx2 else 'n/a') + f" | {mn[0]:.1f} ({mn[1]}) |" if sst else '| n/a |')
A('\n*Direction convention of `ocean_current_direction` is not documented in the response; assumed "towards" (oceanographic convention) - flagged.\n')
# EA rivers
A('## 7. River levels - Environment Agency flood-monitoring API (grade A, telemetry)\n')
def jget(u):
    for a in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'research-script'}), timeout=60).read())
        except Exception as e: err = e; time.sleep(3)
    return None
RAWE = R/'raw/conditions'; stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%MZ')
sts = jget('https://environment.data.gov.uk/flood-monitoring/id/stations?parameter=level&lat=50.40&long=-4.90&dist=85&_limit=1000')
rows = []
if sts:
    json.dump(sts, open(RAWE/f'ea_stations_{stamp}.json', 'w'))
    want = ['Tamar','Lynher','Tiddy','Looe','Fowey','Par','St Austell','Fal','Tresillian','Kenwyn','Allen','Truro','Helford','Cober','Hayle','Red River','Gannel','Menalhyl','Camel','Valency','Neet','Strat','Seaton','Inny','Ottery','De Lank','Carnon','Kennall','Tregeseal','Newlyn','Porthleven']
    for s in sts['items']:
        rn = s.get('riverName') or ''
        if not isinstance(rn, str) or not any(w.lower() in rn.lower() for w in want): continue
        if s.get('lat') is None or float(s['long'] if not isinstance(s['long'], list) else s['long'][0]) > -4.15: continue
        sid = s['stationReference']
        det = jget(f"https://environment.data.gov.uk/flood-monitoring/id/stations/{sid}")
        rd = jget(f"https://environment.data.gov.uk/flood-monitoring/id/stations/{sid}/readings?since=2026-11-11T00:00:00Z&_sorted&_limit=2000&parameter=level")
        if not det or not rd or not rd.get('items'): continue
        it = det['items']; ss = it.get('stageScale') if isinstance(it, dict) else None
        if isinstance(ss, str): ss = jget(ss.replace('http://', 'https://')); ss = ss['items'] if ss else None
        vals = sorted(((x['dateTime'], x['value']) for x in rd['items'] if isinstance(x.get('value'), (int, float))))
        if not vals: continue
        byday = collections.defaultdict(list)
        for t, v in vals: byday[t[:10]].append(v)
        rows.append(dict(river=rn, station=s.get('label'), ref=sid, latest=vals[-1], lo=(ss or {}).get('typicalRangeLow'), hi=(ss or {}).get('typicalRangeHigh'),
                         days={d: (st.mean(v), max(v)) for d, v in byday.items()}))
    json.dump(rows, open(RAWE/f'ea_river_summary_{stamp}.json', 'w'), default=str)
if rows:
    A(f'Fetched {now}. "Typical range" is the EA station stage-scale typical low-high. Position = where the latest level sits within that range (0 % = typical low, 100 % = typical high; >100 % = above normal).\n')
    dcols = [f'2026-11-{d:02d}' for d in range(14, 22)]
    A('| River | Station | Latest level m (time UTC) | Typical range m | Position | ' + ' | '.join('Max ' + d[8:] + ' Nov' for d in dcols) + ' | Trend |\n|---|---|---|---|---|' + '---|'*(len(dcols)+1))
    for r in sorted(rows, key=lambda r: (r['river'], str(r['station']))):
        lo, hi = r['lo'], r['hi']; lv = r['latest'][1]
        pos = f"{100*(lv-lo)/(hi-lo):.0f} %" if isinstance(lo, (int, float)) and isinstance(hi, (int, float)) and hi > lo else 'n/a'
        mx = [r['days'].get(d, (None, None))[1] for d in dcols]
        tr = ''
        if mx[-1] is not None and mx[-3] is not None: tr = 'falling' if mx[-1] < mx[-3] - 0.02 else ('rising' if mx[-1] > mx[-3] + 0.02 else 'steady')
        A(f"| {r['river']} | {r['station']} ({r['ref']}) | {lv:.2f} ({r['latest'][0][5:16]}) | {lo}-{hi} | {pos} | " + ' | '.join('' if v is None else f'{v:.2f}' for v in mx) + f' | {tr} |')
else:
    A('EA river data NOT FOUND (API call failed).')
A('\n**What it means for 22 Nov:** see the forecast rain in `weather.md` section 6 - rain arrives from about 21:00 on the 21st and is heaviest overnight/morning; small Cornish catchments respond within 3-12 h, so estuary heads will carry fresh, coloured water on the morning ebb (LW ~09:00-09:40) and through the afternoon flood. Whether that flush is large depends on the totals actually falling (model spread is wide in the east).\n')
A('## 8. Observations, storm history and water clarity\n\nSee `sea_clarity_evidence.md` (Channel Coastal Observatory buoys, Sevenstones lightship, satellite/webcam evidence, per-sector clarity estimate, weed). Headline observed facts used elsewhere: W/WNW groundswell 17-20 Nov (Perranporth daily max Hs 3.5 / 4.7 / 4.4 / 4.2 m, Tp to 18 s), decayed to about 1 m by 14:30 on 21 Nov; buoy SST 12.7-13.6 C.\n')
A('## 9. Gaps\n\n- No nearshore wave transformation (SWAN-type) model was available; nearshore heights are inferred geometrically per segment in `coastline.md`.\n- Met Office / Surfline / surf-forecast site forecasts were not compared numerically.\n- Phase 3 must re-pull all wave models and log changes.')
(R/'sea_state.md').write_text('\n'.join(o) + '\n')
print('weather.md + sea_state.md written; EA river stations:', len(rows))
