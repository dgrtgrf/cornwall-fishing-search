#!/usr/bin/env python3
"""Workstream 6: merge the per-sector / per-theme mark sweeps (fishing/research/marks/*.jsonl) into one
de-duplicated list: fishing/research/marks_merged.jsonl and fishing/research/marks.md.
Duplicates = same normalised name, or names sharing a key token AND coordinates within 600 m.
Usage: merge_marks.py <repo_root>"""
import sys, json, glob, re, math, pathlib, collections
ROOT = pathlib.Path(sys.argv[1]); R = ROOT/'fishing/research'
def norm(s):
    s = re.sub(r"\(.*?\)", " ", (s or '').lower()); s = re.sub(r"[^a-z0-9 ]", " ", s.replace("'", ""))
    stop = {'the','beach','cove','bay','point','head','harbour','pier','quay','rocks','rock','sands','sand','and','of','at','near','st','mark','marks','area','estuary','river','mouth'}
    toks = [t for t in s.split() if t not in stop]
    return ' '.join(toks) or ' '.join(s.split())
def dist(a, b):
    if None in (a[0], a[1], b[0], b[1]): return None
    k = 111320.0; return math.hypot((a[0]-b[0])*k, (a[1]-b[1])*k*math.cos(math.radians(a[0])))
recs = []; bad = 0
for fp in sorted(glob.glob(str(R/'marks/*.jsonl'))):
    key = pathlib.Path(fp).stem
    for ln in open(fp):
        ln = ln.strip()
        if not ln: continue
        try: d = json.loads(ln)
        except Exception: bad += 1; continue
        d['_src_file'] = key
        for k in ('lat', 'lon'):
            try: d[k] = float(d[k]) if d.get(k) not in (None, '', 'NOT FOUND') else None
            except Exception: d[k] = None
        if d['lat'] is not None and not (49.7 <= d['lat'] <= 51.0 and -6.7 <= (d['lon'] or 0) <= -4.0): d['_coord_flag'] = 'outside Cornwall bbox - check'
        recs.append(d)
print('records', len(recs), 'unparseable lines', bad)
groups = []
for d in recs:
    nm = norm(d.get('name')); al = {norm(a) for a in (d.get('aliases') or []) if isinstance(a, str)} | {nm}
    hit = None
    for g in groups:
        if nm and nm in g['names']: 
            dd = dist((d['lat'], d['lon']), (g['lat'], g['lon']))
            if dd is None or dd < 3000: hit = g; break
        dd = dist((d['lat'], d['lon']), (g['lat'], g['lon']))
        if dd is not None and dd < 600 and (al & g['names'] or set(nm.split()) & set(' '.join(g['names']).split())): hit = g; break
    if hit is None:
        groups.append(dict(names=set(al), lat=d['lat'], lon=d['lon'], recs=[d]))
    else:
        hit['names'] |= al; hit['recs'].append(d)
        if hit['lat'] is None: hit['lat'], hit['lon'] = d['lat'], d['lon']
order = {'N1':1,'N2':2,'N3':3,'W1':4,'S1':5,'S2':6,'S3':7,'S4':8,'S5':9,'SC':10,'T1':11,'T2':12,'T3':13,'T4':14}
Q = {'good': 3, 'moderate': 2, 'thin': 1}
merged = []
for g in groups:
    rs = sorted(g['recs'], key=lambda r: (-Q.get(str(r.get('data_quality')).lower(), 0), order.get(r['_src_file'], 99)))
    p = rs[0]
    def uni(k):
        seen = []; 
        for r in rs:
            v = r.get(k)
            if v in (None, '', 'NOT FOUND', []): continue
            v = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
            if v not in seen: seen.append(v)
        return seen
    sp = collections.OrderedDict()
    for r in rs:
        for s in (r.get('late_nov_species') or []):
            if isinstance(s, str): sp.setdefault(s.strip().lower(), None)
    allsp = collections.OrderedDict()
    for r in rs:
        for s in (r.get('species') or []):
            nmv = s.get('name') if isinstance(s, dict) else s
            if isinstance(nmv, str): allsp.setdefault(nmv.strip().lower(), None)
    srcs = []
    for r in rs:
        for s in (r.get('sources') or []):
            if isinstance(s, dict) and s.get('url') and s['url'] not in [x['url'] for x in srcs]: srcs.append({k: s.get(k) for k in ('url', 'title', 'pub_date', 'accessed', 'grade')})
    grades = sorted({str(s.get('grade')) for s in srcs if s.get('grade')})
    merged.append(dict(name=p.get('name'), aliases=sorted({a for r in rs for a in ([r.get('name')] + list(r.get('aliases') or [])) if isinstance(a, str) and a != p.get('name')}),
        sector_files=sorted({r['_src_file'] for r in rs}, key=lambda k: order.get(k, 99)), nearest_town=p.get('nearest_town'), lat=g['lat'], lon=g['lon'],
        coord_confidence=p.get('coord_confidence'), type=p.get('type'), aspect_deg=p.get('aspect_deg'), ground=uni('ground'), depth=uni('depth'), features=uni('features'),
        fishes_well_in=uni('fishes_well_in'), fishes_badly_in=uni('fishes_badly_in'), best_tide=uni('best_tide'), best_light=uni('best_light'),
        species=list(allsp), late_nov_species=list(sp), methods_baits=uni('methods_baits'), size_potential=uni('size_potential'), notes=uni('notes'),
        sources=srcs, source_grades=grades, n_sources=len(srcs), n_records=len(rs), data_quality=max((str(r.get('data_quality')).lower() for r in rs), key=lambda q: Q.get(q, 0)),
        coord_flag=next((r['_coord_flag'] for r in rs if r.get('_coord_flag')), None)))
merged.sort(key=lambda m: (order.get(m['sector_files'][0], 99), -(m['lat'] or 0)))
for i, m in enumerate(merged, 1): m['mark_id'] = f'K{i:03d}'
with open(R/'marks_merged.jsonl', 'w') as fh:
    for m in merged: fh.write(json.dumps(m, ensure_ascii=False) + '\n')
SECT = {'N1':'North coast: Devon border to Camel mouth','N2':'Camel estuary to Newquay','N3':'Crantock to St Ives','W1':'West Penwith (St Ives to Mousehole)','S1':"Mount's Bay (Newlyn to Mullion)",'S2':'The Lizard and Helford','S3':'Falmouth Bay and the Fal','S4':'Roseland to Fowey','S5':'Polruan to the Tamar','SC':'Isles of Scilly','T1':'Thematic: estuaries','T2':'Thematic: harbours and piers','T3':'Thematic: deep-water rock / islands / obscure','T4':'Thematic: surf and open beaches'}
o = []; A = o.append
A('# Workstream 6 - Known shore marks (merged list)\n')
cnt = collections.Counter(m['data_quality'] for m in merged)
A(f"Merged from 14 sweeps (`fishing/research/marks/*.md` + `.jsonl`, 10 geographic sectors + 4 thematic sweeps, run 2026-11-21 16:06-16:27 UTC). **{len(recs)} raw mark records -> {len(merged)} distinct marks** after de-duplication (`fishing/tools/marks/merge_marks.py`; full merged records with every field and source URL in `marks_merged.jsonl`). Evidence quality as graded by the sweep agents: {dict(cnt)}.\n")
A('**Read this first - limits of the list.** (1) Most per-mark descriptions come from one aggregator site (wheresthefish.uk, grade C; its text is templated and its species scores are modelled, not catch records). (2) Sea Angler, World Sea Fishing forum, Planet Sea Fishing, PressReader and most Facebook sources were blocked to automated access, so the best venue literature was NOT read. (3) Very few marks have a dated late-November catch attached. (4) Aspect, depth and wind/swell preferences are frequently the sweep agent\'s inference (grade D) - the per-sector files say which. The physical assessment of every kilometre of shore is in `coastline.md`; this list is the documentary layer only.\n')
A('Columns: id, name, type, lat/lon (confidence), late-November species named by sources, evidence quality, number of source URLs (grades), sweeps that reported it.\n')
cur = None
for m in merged:
    s = m['sector_files'][0]
    if s != cur:
        cur = s; A(f'\n## {SECT.get(s, s)}\n'); A('| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |\n|---|---|---|---|---|---|---|---|')
    ll = f"{m['lat']:.4f}, {m['lon']:.4f} ({m['coord_confidence']})" if m['lat'] is not None and m['lon'] is not None else 'no coordinate'
    A(f"| {m['mark_id']} | {m['name']} | {m['type']} | {ll} | {', '.join(m['late_nov_species'][:10]) or '-'} | {m['data_quality']} | {m['n_sources']} ({'/'.join(m['source_grades']) or '-'}) | {', '.join(m['sector_files'])} |")
A('\n## Documentation gaps reported by the sweeps (stretches with NO angling documentation found)\n')
A('These are listed in each sweep file under "gaps" / "NOT FOUND"; consolidated list to be completed at the Phase 1 gap-fill round. The 1 km coastline assessment covers them physically regardless.\n')
(R/'marks.md').write_text('\n'.join(o) + '\n')
by = collections.Counter(m['sector_files'][0] for m in merged)
print('merged marks', len(merged), dict(by)); print('quality', dict(cnt), '| no coords', sum(1 for m in merged if m['lat'] is None), '| coord flags', sum(1 for m in merged if m['coord_flag']))
sp = collections.Counter(s for m in merged for s in m['late_nov_species']); print('top late-Nov species:', sp.most_common(22))
