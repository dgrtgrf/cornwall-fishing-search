#!/usr/bin/env python3
"""Workstreams 2 + 3 (numeric part): multi-model weather and wave forecasts for every reference point.
Fetches Open-Meteo forecast / marine / ensemble APIs, saves raw JSON with the fetch time, writes tidy CSVs
to fishing/research/data/.  Usage: fetch_conditions.py <repo_root> [tag]"""
import sys, json, time, csv, datetime as dt, pathlib, urllib.request, urllib.parse
ROOT = pathlib.Path(sys.argv[1]); TAG = sys.argv[2] if len(sys.argv) > 2 else ''
RAW = ROOT/'fishing/research/raw/conditions'; RAW.mkdir(parents=True, exist_ok=True)
DATA = ROOT/'fishing/research/data'; DATA.mkdir(parents=True, exist_ok=True)
stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%MZ')
# name, lat, lon (land/coast point for weather), sea point for waves (lat, lon)
PTS = [
 ('Bude',50.832,-4.556,50.835,-4.60),('Tintagel Head',50.668,-4.763,50.675,-4.80),('Port Isaac',50.595,-4.832,50.61,-4.85),
 ('Stepper Point',50.570,-4.945,50.585,-4.96),('Trevose Head',50.549,-5.037,50.56,-5.07),('Newquay Towan Head',50.425,-5.100,50.44,-5.12),
 ('Perranporth',50.350,-5.160,50.36,-5.19),('St Agnes Head',50.320,-5.235,50.335,-5.26),('Godrevy',50.240,-5.395,50.26,-5.41),
 ('St Ives Head',50.220,-5.478,50.235,-5.48),('Pendeen Watch',50.165,-5.672,50.18,-5.70),('Cape Cornwall',50.127,-5.709,50.13,-5.74),
 ("Land's End",50.066,-5.716,50.065,-5.75),('Gwennap Head',50.036,-5.680,50.02,-5.69),('Newlyn/Penzance',50.100,-5.540,50.09,-5.51),
 ('Marazion',50.118,-5.477,50.105,-5.47),('Porthleven/Loe Bar',50.070,-5.300,50.055,-5.32),('Mullion',50.015,-5.260,50.01,-5.29),
 ('Lizard Point',49.958,-5.205,49.94,-5.21),('Coverack/Manacles',50.045,-5.060,50.045,-5.03),('Helford mouth',50.095,-5.095,50.095,-5.06),
 ('Falmouth Pendennis',50.145,-5.045,50.13,-5.03),('Carrick Roads',50.21,-5.03,50.19,-5.035),('Nare Head',50.195,-4.925,50.18,-4.92),
 ('Dodman Point',50.218,-4.802,50.20,-4.80),('Mevagissey',50.270,-4.780,50.27,-4.75),('Par',50.340,-4.705,50.32,-4.70),
 ('Fowey mouth',50.325,-4.645,50.31,-4.64),('Polperro',50.328,-4.515,50.31,-4.51),('Looe',50.350,-4.450,50.335,-4.44),
 ('Whitsand Bay',50.355,-4.290,50.335,-4.29),('Rame Head',50.312,-4.223,50.30,-4.22),('Saltash (Tamar)',50.405,-4.205,50.36,-4.16),
 ("St Mary's (Scilly)",49.915,-6.315,49.90,-6.30),('St Agnes/Western Rocks',49.885,-6.370,49.87,-6.39),('Bishop Rock',49.873,-6.445,49.87,-6.47),
 ("St Martin's (Scilly)",49.967,-6.270,49.985,-6.26),('Wolf Rock',49.945,-5.808,49.945,-5.82),('Longships',50.067,-5.747,50.067,-5.77)]
WX_MODELS = ['ukmo_uk_deterministic_2km','ukmo_global_deterministic_10km','ecmwf_ifs025','ecmwf_ifs','ecmwf_aifs025_single','gfs_seamless',
             'icon_eu','icon_seamless','meteofrance_arpege_europe','meteofrance_arome_france','knmi_harmonie_arome_europe','dmi_harmonie_arome_europe','gem_global']
WX_VARS = ['wind_speed_10m','wind_direction_10m','wind_gusts_10m','pressure_msl','precipitation','cloud_cover','cloud_cover_low','temperature_2m','visibility']
MAR_MODELS = ['meteofrance_wave','ecmwf_wam025','ncep_gfswave025','ncep_gfswave016','ewam','gwam']
MAR_VARS = ['wave_height','wave_direction','wave_period','wave_peak_period','wind_wave_height','wind_wave_direction','wind_wave_period',
            'swell_wave_height','swell_wave_direction','swell_wave_period','swell_wave_peak_period']
def get(url, params, name):
    q = url + '?' + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            raw = urllib.request.urlopen(urllib.request.Request(q, headers={'User-Agent': 'research-script'}), timeout=90).read()
            (RAW/f'{name}_{stamp}.json').write_bytes(raw)
            return json.loads(raw)
        except Exception as e:
            err = str(e)[:150]; time.sleep(3 + 3*attempt)
    print('FAILED', name, err); return None
lat = ','.join(str(p[1]) for p in PTS); lon = ','.join(str(p[2]) for p in PTS)
slat = ','.join(str(p[3]) for p in PTS); slon = ','.join(str(p[4]) for p in PTS)
rows = []
ok = []
for m in WX_MODELS:
    d = get('https://api.open-meteo.com/v1/forecast', dict(latitude=lat, longitude=lon, hourly=','.join(WX_VARS), models=m,
            wind_speed_unit='kn', start_date='2026-11-19', end_date='2026-11-24', timezone='GMT'), f'wx_{m}')
    if not d: continue
    d = d if isinstance(d, list) else [d]
    n = 0
    for p, loc in zip(PTS, d):
        h = loc.get('hourly', {})
        for i, t in enumerate(h.get('time', [])):
            vals = {v: (h.get(v) or [None]*len(h['time']))[i] for v in WX_VARS}
            if all(x is None for x in vals.values()): continue
            rows.append(dict(point=p[0], model=m, time=t, grid_lat=loc.get('latitude'), grid_lon=loc.get('longitude'), **vals)); n += 1
    ok.append((m, n))
with open(DATA/f'weather_hourly_multimodel{TAG}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['point','model','time','grid_lat','grid_lon']+WX_VARS); w.writeheader(); w.writerows(rows)
print('weather rows', len(rows), ok)
mrows = []; mok = []
for m in MAR_MODELS:
    d = get('https://marine-api.open-meteo.com/v1/marine', dict(latitude=slat, longitude=slon, hourly=','.join(MAR_VARS), models=m,
            start_date='2026-11-19', end_date='2026-11-24', timezone='GMT', cell_selection='sea'), f'marine_{m}')
    if not d: continue
    d = d if isinstance(d, list) else [d]
    n = 0
    for p, loc in zip(PTS, d):
        h = loc.get('hourly', {})
        for i, t in enumerate(h.get('time', [])):
            vals = {v: (h.get(v) or [None]*len(h['time']))[i] for v in MAR_VARS}
            if all(x is None for x in vals.values()): continue
            mrows.append(dict(point=p[0], model=m, time=t, grid_lat=loc.get('latitude'), grid_lon=loc.get('longitude'), **vals)); n += 1
    mok.append((m, n))
with open(DATA/f'waves_hourly_multimodel{TAG}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['point','model','time','grid_lat','grid_lon']+MAR_VARS); w.writeheader(); w.writerows(mrows)
print('marine rows', len(mrows), mok)
# SST + currents + sea level (best match marine model)
d = get('https://marine-api.open-meteo.com/v1/marine', dict(latitude=slat, longitude=slon, hourly='sea_surface_temperature,ocean_current_velocity,ocean_current_direction,sea_level_height_msl',
        start_date='2026-11-19', end_date='2026-11-24', timezone='GMT', cell_selection='sea'), 'marine_sst_currents')
srows = []
if d:
    for p, loc in zip(PTS, d if isinstance(d, list) else [d]):
        h = loc.get('hourly', {})
        for i, t in enumerate(h.get('time', [])):
            srows.append(dict(point=p[0], time=t, grid_lat=loc.get('latitude'), grid_lon=loc.get('longitude'), sst=h['sea_surface_temperature'][i],
                              cur_kmh=h['ocean_current_velocity'][i], cur_dir=h['ocean_current_direction'][i], sea_level=h['sea_level_height_msl'][i]))
with open(DATA/f'sst_currents_hourly{TAG}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['point','time','grid_lat','grid_lon','sst','cur_kmh','cur_dir','sea_level']); w.writeheader(); w.writerows(srows)
print('sst/current rows', len(srows))
# preceding weeks: analysis history at 8 points (best match, past 21 days)
H = [p for p in PTS if p[0] in ('Bude','Newquay Towan Head',"Land's End",'Newlyn/Penzance','Lizard Point','Falmouth Pendennis','Looe',"St Mary's (Scilly)")]
d = get('https://api.open-meteo.com/v1/forecast', dict(latitude=','.join(str(p[1]) for p in H), longitude=','.join(str(p[2]) for p in H),
        hourly='pressure_msl,wind_speed_10m,wind_direction_10m,wind_gusts_10m,precipitation,temperature_2m', wind_speed_unit='kn', past_days=21, forecast_days=3, timezone='GMT'), 'wx_history_bestmatch')
hrows = []
if d:
    for p, loc in zip(H, d):
        h = loc['hourly']
        for i, t in enumerate(h['time']):
            hrows.append(dict(point=p[0], time=t, **{k: h[k][i] for k in h if k != 'time'}))
with open(DATA/f'weather_history_21d{TAG}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(hrows[0].keys())); w.writeheader(); w.writerows(hrows)
print('history rows', len(hrows))
# ensembles at 6 points
E = [p for p in PTS if p[0] in ('Bude','Newquay Towan Head',"Land's End",'Porthleven/Loe Bar','Falmouth Pendennis','Looe')]
erows = []
for m in ['ecmwf_ifs025','gfs025','icon_seamless','ukmo_global_ensemble_20km','ukmo_uk_ensemble_2km']:
    d = get('https://ensemble-api.open-meteo.com/v1/ensemble', dict(latitude=','.join(str(p[1]) for p in E), longitude=','.join(str(p[2]) for p in E),
            hourly='wind_speed_10m,wind_direction_10m,wind_gusts_10m,pressure_msl', models=m, wind_speed_unit='kn', start_date='2026-11-22', end_date='2026-11-22', timezone='GMT'), f'ens_{m}')
    if not d: continue
    for p, loc in zip(E, d if isinstance(d, list) else [d]):
        h = loc.get('hourly', {})
        for var in ('wind_speed_10m','wind_direction_10m','wind_gusts_10m','pressure_msl'):
            mem = [k for k in h if k.startswith(var)]
            for i, t in enumerate(h.get('time', [])):
                vals = [h[k][i] for k in mem if h[k][i] is not None]
                if vals:
                    vals.sort(); erows.append(dict(point=p[0], model=m, time=t, var=var, n=len(vals), min=vals[0], p10=vals[int(0.1*(len(vals)-1))], median=vals[len(vals)//2], p90=vals[int(0.9*(len(vals)-1))], max=vals[-1]))
with open(DATA/f'ensemble_spread_22nov{TAG}.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['point','model','time','var','n','min','p10','median','p90','max']); w.writeheader(); w.writerows(erows)
print('ensemble rows', len(erows), 'stamp', stamp)
