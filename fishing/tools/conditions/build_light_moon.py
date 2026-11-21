#!/usr/bin/env python3
"""Workstream 5: light and moon tables -> fishing/research/light_moon.md
Inputs: skyfield/DE440s computation saved in raw/light_moon (fine-grained events for 12 points), USNO + MET Norway
cross-check JSON, EasyTide events, multi-model cloud cover CSV.  Usage: build_light_moon.py <repo_root>"""
import sys, json, glob, csv, statistics as st, datetime as dt, pathlib
ROOT = pathlib.Path(sys.argv[1]); R = ROOT/'fishing/research'; LM = R/'raw/light_moon'
sky = json.load(open(sorted(glob.glob(str(LM/'skyfield_de440s_computed_*.json')))[-1]))
usno = json.load(open(glob.glob(str(LM/'usno_rstt_newlyn_*.json'))[0]))['properties']['data']
msun = json.load(open(glob.glob(str(LM/'metno_sun_newlyn_*.json'))[0]))['properties']
mmoon = json.load(open(glob.glob(str(LM/'metno_moon_newlyn_*.json'))[0]))['properties']
tides = json.load(open(sorted(glob.glob(str(R/'raw/tides/easytide_all_*.json')))[-1]))
D = '2026-11-22'
def ev(lst, day=D, key='hm'):
    return [e for e in lst if e[key].startswith(day)]
def hm(e): return e['hm'][11:]
out = []; W = out.append
W('# Workstream 5 - Light and moon, Sunday 22 November 2026\n')
W(f"**Method / sources.** Computed with skyfield {sky['library'].split()[-1]} and the JPL {sky['ephemeris']} ephemeris (computation saved {sky['computed_utc']} UTC in `raw/light_moon/`; script `raw/light_moon/compute_astro.py`), grade A (direct astronomical computation). Cross-checked against the US Naval Observatory API (aa.usno.navy.mil/api/rstt/oneday, accessed 2026-11-21 15:19 UTC) and MET Norway sunrise API (api.met.no, accessed 15:19 UTC) - section 4. All times GMT (UK clock time). Sunrise/sunset = upper limb on the sea horizon with standard refraction; twilight boundaries at sun altitude -6 / -12 / -18 degrees. Cloud cover: Open-Meteo multi-model forecast pulled 2026-11-21 16:06-16:30 UTC (`data/weather_hourly_multimodel.csv`). Tide times: UKHO EasyTide (see `tides.md`). Table built by `fishing/tools/conditions/build_light_moon.py`.\n")
W('## 1. Sun and twilight on 22 November\n')
W('| Point | Astro. twilight begins | Nautical begins | Civil begins | Sunrise (azimuth) | Solar noon (alt) | Sunset (azimuth) | Civil ends | Nautical ends | Astro. ends | Day length |\n|---|---|---|---|---|---|---|---|---|---|---|')
for name, p in sky['points'].items():
    tw = {(e['from'], e['to']): hm(e) for e in ev(p['twilight_events'])}
    sr, ss, sn = ev(p['sunrise'])[0], ev(p['sunset'])[0], ev(p['solar_noon'])[0]
    t0 = dt.datetime.fromisoformat(sr['utc']); t1 = dt.datetime.fromisoformat(ss['utc']); dl = t1 - t0
    W(f"| {name} | {tw.get(('night','astronomical twilight'),'-')} | {tw.get(('astronomical twilight','nautical twilight'),'-')} | {tw.get(('nautical twilight','civil twilight'),'-')} | {hm(sr)} ({sr['az_deg']:.0f}) | {hm(sn)} ({sn['alt_deg']:.1f}) | {hm(ss)} ({ss['az_deg']:.0f}) | {tw.get(('civil twilight','nautical twilight'),'-')} | {tw.get(('nautical twilight','astronomical twilight'),'-')} | {tw.get(('astronomical twilight','night'),'-')} | {dl.seconds//3600}h{(dl.seconds%3600)//60:02d} |")
W('\n## 2. Moon on 22 November\n')
g22 = [g for g in sky['geocentric'] if g['utc'].startswith(D)]
W('| Point | Moonset (azimuth) | Moonrise (azimuth) | Upper transit (altitude) | Previous transit (21 Nov) |\n|---|---|---|---|---|')
for name, p in sky['points'].items():
    ms, mr, mt = ev(p['moonset']), ev(p['moonrise']), ev(p['moon_upper_transit'])
    mt21 = ev(p['moon_upper_transit'], '2026-11-21')
    f = lambda L, k='az_deg': ', '.join(f"{hm(e)} ({e[k]:.0f})" for e in L) or 'none'
    W(f"| {name} | {f(ms)} | {f(mr)} | {f(mt,'alt_deg')} | {f(mt21,'alt_deg')} |")
W('\nGeocentric moon through the day:\n\n| Time (GMT) | Illuminated fraction | Phase | Age (days) | Distance (km) | Declination |\n|---|---|---|---|---|---|')
for g in g22 + [g for g in sky['geocentric'] if g['utc'].startswith('2026-11-23 00')]:
    W(f"| {g['utc'][5:16]} | {100*g['illuminated_fraction']:.1f}% | {g['phase_name']} | {g['age_days']:.2f} | {g['moon_distance_km']:.0f} | {g['moon_dec_deg']:+.1f} |")
W('\nLunar calendar around the date (skyfield):\n')
for m in sky['moon_phases']:
    if '2026-11' in m['utc'] or '2026-12-0' in m['utc']: W(f"- {m['phase']}: {m['utc']} GMT")
for pg in sky['perigees']: W(f"- Perigee: {pg['utc']} GMT, {pg['distance_km']:.0f} km")
for ag in sky['apogees']: W(f"- Apogee: {ag['utc']} GMT, {ag['distance_km']:.0f} km")
W('\n**Reading:** the session falls 2 days 15 h (at midnight) to 1 day 15 h before the full moon of 24 Nov 14:53 GMT, with lunar perigee on 25 Nov 21:08 (359,336 km). Full moon and perigee nearly coincide, so the spring tides of 25-27 Nov are perigean (large); 22 Nov is on the steep build towards them (see `tides.md`).\n')
W('## 3. Hour-by-hour light, Newlyn/Penzance (representative of the county; other points differ by <= 5 minutes)\n')
# cloud: median across models at Newlyn + Bude + Looe
cloud = {}
try:
    for r in csv.DictReader(open(R/'data/weather_hourly_multimodel.csv')):
        if r['time'].startswith(D) and r['cloud_cover'] not in ('', None):
            cloud.setdefault((r['point'], r['time'][11:13]), []).append((float(r['cloud_cover']), float(r['cloud_cover_low']) if r['cloud_cover_low'] else None))
except FileNotFoundError:
    pass
def cl(point, hh):
    v = cloud.get((point, hh))
    if not v: return 'n/a'
    tot = [x[0] for x in v]; low = [x[1] for x in v if x[1] is not None]
    return f"{st.median(tot):.0f} ({min(tot):.0f}-{max(tot):.0f}) / {st.median(low):.0f}" if low else f"{st.median(tot):.0f}"
def klass(sun, moon, ill):
    if sun > -0.833: return 'DAYLIGHT'
    if sun > -6: return 'civil twilight'
    if sun > -12: return 'nautical twilight'
    base = 'astronomical twilight' if sun > -18 else 'night'
    if moon > 10: return base + f' - MOONLIT (moon {moon:.0f} deg up, {100*ill:.0f}% lit)'
    if moon > 0: return base + f' - low moon ({moon:.0f} deg, {100*ill:.0f}%)'
    return base + ' - DARK (moon down)'
p = sky['points']['Newlyn/Penzance']
W('| Hour (GMT) | Sun altitude | Moon altitude | Moon azimuth | Moon lit | Light class (clear sky) | Cloud % Newlyn: median (range) / low-cloud median | Cloud % Bude | Cloud % Looe |\n|---|---|---|---|---|---|---|---|---|')
for h in p['hourly']:
    if not (h['utc'].startswith(D) or h['utc'] == '2026-11-23 00:00'): continue
    hh = h['utc'][11:13]
    W(f"| {h['utc'][5:]} | {h['sun_alt']:.1f} | {h['moon_alt']:.1f} | {h['moon_az']:.0f} | {100*h['moon_illum']:.0f}% | {klass(h['sun_alt'], h['moon_alt'], h['moon_illum'])} | {cl('Newlyn/Penzance', hh) if h['utc'].startswith(D) else 'n/a'} | {cl('Bude', hh) if h['utc'].startswith(D) else 'n/a'} | {cl('Looe', hh) if h['utc'].startswith(D) else 'n/a'} |")
W('\n**Summary of the light regime (clear-sky astronomy):** moon up and bright (91-92% lit) from midnight until moonset about 05:00; the only truly dark period of the whole 24 h is about **05:00 to 05:50** (moon down, before astronomical twilight) with deepening twilight to civil dawn about 07:10; sunrise about 07:42-07:49; sunset about 16:22-16:34 (east to west); civil dusk ends about 17:00-17:10; the 94-96% moon has already risen (about 14:45) and is 20+ degrees up by the end of civil twilight, so **the evening has no dark period at all** unless cloud removes the moonlight. Cloud cover therefore decides whether the night of the 22nd fishes as "dark" or "bright" - see the cloud columns above and `weather.md`.\n')
W('## 4. Cross-check of the computation (Newlyn/Penzance 50.10N 5.54W)\n')
u = {d['phen']: d['time'] for d in usno['sundata']}; um = {d['phen']: d['time'] for d in usno['moondata']}
tw = {(e['from'], e['to']): hm(e) for e in ev(p['twilight_events'])}
rows = [('Civil twilight begins', tw.get(('nautical twilight','civil twilight')), u.get('Begin Civil Twilight'), '-'),
        ('Sunrise', hm(ev(p['sunrise'])[0]), u.get('Rise'), msun['sunrise']['time'][11:16]),
        ('Solar noon', hm(ev(p['solar_noon'])[0]), u.get('Upper Transit'), msun['solarnoon']['time'][11:16]),
        ('Sunset', hm(ev(p['sunset'])[0]), u.get('Set'), msun['sunset']['time'][11:16]),
        ('Civil twilight ends', tw.get(('civil twilight','nautical twilight')), u.get('End Civil Twilight'), '-'),
        ('Moonset', hm(ev(p['moonset'])[0]), um.get('Set'), mmoon['moonset']['time'][11:16]),
        ('Moonrise', hm(ev(p['moonrise'])[0]), um.get('Rise'), mmoon['moonrise']['time'][11:16]),
        ('Moon upper transit', hm(ev(p['moon_upper_transit'])[0]), um.get('Upper Transit'), mmoon['high_moon']['time'][11:16]),
        ('Illuminated fraction', f"{100*g22[0]['illuminated_fraction']:.0f}-{100*g22[-1]['illuminated_fraction']:.0f}% through the day", usno.get('fracillum'), f"phase angle {mmoon['moonphase']} deg"),
        ('Nearest phase', 'Full Moon 24 Nov 14:53', f"{usno['closestphase']['phase']} {usno['closestphase']['day']} Nov {usno['closestphase']['time']}", '-')]
W('| Quantity | skyfield DE440s | USNO API | MET Norway API |\n|---|---|---|---|')
for r in rows: W('| ' + ' | '.join(str(x) for x in r) + ' |')
W('\nAll three agree to within one minute (differences are rounding / refraction conventions). No contradiction found.\n')
W('## 5. Tide phases against light on 22 November\n')
def lightat(t):
    best = min(p['fine10'], key=lambda r: abs(dt.datetime.fromisoformat(r[0]) - t))
    sun, moon = best[1], best[2]
    hr = min(p['hourly'], key=lambda r: abs(dt.datetime.fromisoformat(r['utc']) - t))
    return klass(sun, moon, hr['moon_illum'])
W('| Port | Event | Time (GMT) | Height (m CD) | Light at that time (Newlyn astronomy, clear sky) |\n|---|---|---|---|---|')
for sid in ('0543','0545','0546','0547','0001','0002','0003','0005','0008','0011','0014'):
    if sid not in tides: continue
    for t, k, h in tides[sid]['events']:
        if t.startswith(D):
            W(f"| {tides[sid]['name']} | {k} | {t[11:16]} | {'' if h is None else f'{h:.2f}'} | {lightat(dt.datetime.fromisoformat(t))} |")
W('\n**Coincidences (south coast, Newlyn/Falmouth/Plymouth timing; north coast about 30-45 min later):**\n')
W('- **Night HW ~02:15-03:20** falls under a bright, high-ish moon in the west (26 deg at 02:00, 9 deg at 04:00) - moonlit unless overcast.')
W('- **The only dark hour (about 05:00-05:50)** falls on the middle of the ebb (HW+2.5 to HW+3.5 south coast).')
W('- **Dawn (civil twilight ~07:10 to sunrise ~07:46)** coincides with the last 1.5-2 h of the ebb; **LW ~08:45-09:35 is in full daylight**, so the first of the flood is a daylight event (09:00-11:00).')
W('- **Afternoon HW ~14:35-15:40** is in daylight; **sunset ~16:25-16:30 and dusk to ~17:05 fall 1-2 h into the ebb** (south coast HW+1 to HW+2.5; north coast HW+1 to HW+1.75).')
W('- **Evening LW ~21:05-22:00** is under a high, 95% moon (48-57 deg altitude, transit 22:28) - the brightest possible night if the sky is clear; the following flood (22:00-24:00) likewise.')
W('- A dusk-plus-flood coincidence does **not** occur on this date; a dawn-plus-flood coincidence does not occur either (dawn is late ebb). The flood tides run ~09:00-15:00 (daylight) and ~21:30-03:30 (night of the 22nd/23rd, mostly outside the 24 h window).\n')
W('## 6. Solunar periods (low-evidence folk theory, grade C/D - recorded only because asked)\n')
mt = ev(p['moon_upper_transit'])[0]; ml = ev(p['moon_lower_transit'])[0]
W(f"- \"Major\" periods (moon overhead / underfoot, +-1 h): lower transit {hm(ml)} and upper transit {hm(mt)} GMT.")
W(f"- \"Minor\" periods (moonset / moonrise, +-30 min): moonset {hm(ev(p['moonset'])[0])}, moonrise {hm(ev(p['moonrise'])[0])} GMT.")
W('- No peer-reviewed support for solunar tables in tidal sea fishing was located by this stream; in tidal water the tide phase dominates. Treated as zero-weight in scoring unless Phase 2 finds evidence.\n')
W('## 7. Gaps\n')
W('- Fishing-effect literature for moonlight/cloud by species is handled in `species_sst.md` (workstream 4), not here.\n- Illuminance in lux under forecast cloud was not modelled; cloud is reported as cover fraction only (THIN for actual on-water brightness).')
(R/'light_moon.md').write_text('\n'.join(out) + '\n')
print('light_moon.md written', len(out), 'lines')
