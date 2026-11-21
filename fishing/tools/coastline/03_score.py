#!/usr/bin/env python3
"""Workstream 7, step 3: first-principles provisional score for every shoreline segment and the
coastline log (fishing/research/coastline.md + coastline/segments_scored.csv).

The score has two parts, both 0-100:
  H = habitat potential (static): best of five habitat guilds, from substrate, depth close in, setting,
      openness, outflows.
  P = provisional score for 22 Nov 2026: H combined with an hour-by-hour conditions model (nearshore
      wave height from offshore model waves x geometric exposure, tide phase, light), best 3-hour window.
Weights are provisional (Phase 2 revisits them with the species workstream); everything is reproducible.

Usage: 03_score.py <raw_dir> <out_dir> <repo_root>
"""
import sys, os, json, csv, math, glob, collections, statistics as st, datetime as dt, warnings
os.environ["OGR_GEOJSON_MAX_OBJ_SIZE"] = "0"
import numpy as np
import pandas as pd
import geopandas as gpd
import shapely
from shapely import STRtree
from pyproj import Transformer

warnings.filterwarnings("ignore")
RAW, OUT, ROOT = sys.argv[1], sys.argv[2], sys.argv[3]
R = f"{ROOT}/fishing/research"
F = Transformer.from_crs(4326, 27700, always_xy=True)
df = pd.read_csv(f"{OUT}/segments_enriched.csv")
n = len(df)
fcols = [f"fetch_{a:03d}" for a in range(0, 360, 10)]
fetch = df[fcols].values            # km
az = np.arange(36) * 10.0

# ---------------------------------------------------------------- nearest EUSeaMap class where the point-in-polygon lookup missed
eus = gpd.read_file(f"{RAW}/eusm2025_eunis2019_full.geojson").to_crs(27700)
eus = eus[eus["substrate"].notna() & (eus["substrate"] != "Seabed")].reset_index(drop=True)
lwx, lwy = F.transform(df.lw_lon.values, df.lw_lat.values)
tree = STRtree(eus.geometry.values)
pts = shapely.points(lwx, lwy)
ni = tree.nearest(pts)
nd = shapely.distance(pts, eus.geometry.values[ni])
df["eusm_nearest_substrate"] = eus["substrate"].values[ni]
df["eusm_nearest_biozone"] = eus["biozone"].values[ni]
df["eusm_nearest_energy"] = eus["energy"].values[ni]
df["eusm_nearest_dist_m"] = nd.round(0)
rock_polys = eus[eus["substrate"].str.contains("Rock", na=False)]
rtree = STRtree(rock_polys.geometry.values)
ri = rtree.nearest(pts)
df["dist_to_mapped_rock_m"] = shapely.distance(pts, rock_polys.geometry.values[ri]).round(0)
sed_polys = eus[~eus["substrate"].str.contains("Rock", na=False)]
stree = STRtree(sed_polys.geometry.values)
si = stree.nearest(pts)
df["dist_to_mapped_sediment_m"] = shapely.distance(pts, sed_polys.geometry.values[si]).round(0)
df["nearest_sediment_class"] = sed_polys["substrate"].values[si]

# ---------------------------------------------------------------- documentary overlay: merged known marks within 600 m
marks = [json.loads(l) for l in open(f"{R}/marks_merged.jsonl")]
mk = [(m["mark_id"], m["name"], *F.transform(m["lon"], m["lat"])) for m in marks if m.get("lat") is not None and m.get("lon") is not None]
from scipy.spatial import cKDTree
mx, my = F.transform(df.lon.values, df.lat.values)
kt = cKDTree(np.array([[a[2], a[3]] for a in mk]))
near = kt.query_ball_point(np.stack([mx, my], 1), 600.0)
df["known_marks_600m"] = ["; ".join(f"{mk[j][0]} {mk[j][1]}" for j in L[:4]) for L in near]

# ---------------------------------------------------------------- conditions for 22 Nov: nearest reference point / tide port
src = open(f"{ROOT}/fishing/tools/conditions/fetch_conditions.py").read()
ns = {}
exec(src.split("WX_MODELS")[0].split("PTS = ")[1].join(["PTS = ", ""]), ns)   # reference point list only
PTS = ns["PTS"]
pname = [p[0] for p in PTS]
px, py = F.transform([p[2] for p in PTS], [p[1] for p in PTS])
ref_i = cKDTree(np.stack([px, py], 1)).query(np.stack([mx, my], 1))[1]
df["ref_point"] = [pname[i] for i in ref_i]
f = lambda x: float(x) if x not in ("", None) else None


def cmean(ds):
    s = sum(math.sin(math.radians(d)) for d in ds); c = sum(math.cos(math.radians(d)) for d in ds)
    return (math.degrees(math.atan2(s, c)) + 360) % 360


HOURS = [f"2026-11-22T{h:02d}:00" for h in range(24)]
wind = {p: np.zeros((24, 2)) for p in pname}      # dir, speed kn
wave = {p: np.zeros((24, 3)) for p in pname}      # Hs, dir, Tp
acc = collections.defaultdict(lambda: collections.defaultdict(list))
for r in csv.DictReader(open(f"{R}/data/weather_hourly_multimodel.csv")):
    if r["time"] in HOURS and f(r["wind_speed_10m"]) is not None and f(r["wind_direction_10m"]) is not None:
        acc[("w", r["point"])][r["time"]].append((f(r["wind_direction_10m"]), f(r["wind_speed_10m"])))
for r in csv.DictReader(open(f"{R}/data/waves_hourly_multimodel.csv")):
    if r["time"] in HOURS and f(r["wave_height"]) not in (None, 0.0) and f(r["wave_direction"]) is not None:
        acc[("v", r["point"])][r["time"]].append((f(r["wave_height"]), f(r["wave_direction"]), f(r["wave_peak_period"]) or f(r["wave_period"]) or 8.0))
for p in pname:
    for h, t in enumerate(HOURS):
        L = acc[("w", p)][t]
        wind[p][h] = (cmean([x[0] for x in L]), st.median([x[1] for x in L]))
        L = acc[("v", p)][t]
        wave[p][h] = (st.median([x[0] for x in L]), cmean([x[1] for x in L]), st.median([x[2] for x in L])) if L else (np.nan, np.nan, np.nan)
# points whose every wave model is land-masked inherit the nearest point with data
for i, p in enumerate(pname):
    if np.isnan(wave[p]).any():
        order = np.argsort(np.hypot(np.array(px) - px[i], np.array(py) - py[i]))
        for j in order[1:]:
            if not np.isnan(wave[pname[j]]).any():
                wave[p] = wave[pname[j]].copy(); break

tides = json.load(open(sorted(glob.glob(f"{R}/data/tides/easytide_all_*.json"))[-1]))
st_meta = json.load(open(glob.glob(f"{R}/raw/tides/easytide_GetStations_*.json")[0]))["features"]
pos = {s["properties"]["Id"]: s["geometry"]["coordinates"] for s in st_meta}
ports = [sid for sid in tides if sid in pos and sid not in ("0089", "0496") and len([e for e in tides[sid]["events"] if e[0].startswith("2026-11-22") and e[2] is not None]) >= 3]
tx, ty = F.transform([pos[s][0] for s in ports], [pos[s][1] for s in ports])
port_i = cKDTree(np.stack([tx, ty], 1)).query(np.stack([mx, my], 1))[1]
df["tide_port"] = [tides[ports[i]]["name"] for i in port_i]


def tide_phase(sid):
    ev = [(dt.datetime.fromisoformat(t), k) for t, k, h in tides[sid]["events"]]
    out = []
    for h in range(24):
        t = dt.datetime(2026, 11, 22, h, 30)
        prev = [e for e in ev if e[0] <= t][-1]; nxt = [e for e in ev if e[0] > t][0]
        out.append((prev[1], (t - prev[0]).total_seconds() / 3600, (nxt[0] - t).total_seconds() / 3600))
    return out


phase = {sid: tide_phase(sid) for sid in ports}

# ---------------------------------------------------------------- nearshore wave estimate (geometric exposure)
openk = np.clip(fetch / 25.0, 0, 1)                 # a direction counts as open to offshore waves once fetch >= 25 km
aspect = df.aspect_open_deg.values
Hs_near = np.zeros((n, 24)); onshore = np.zeros((n, 24)); wspd = np.zeros((n, 24)); Hs_off = np.zeros((n, 24)); wdir = np.zeros((n, 24))
for i in range(n):
    p = pname[ref_i[i]]
    for h in range(24):
        hs0, th, tp = wave[p][h]; wd, ws = wind[p][h]
        nexp = 8 if tp >= 9 else 4
        d = np.abs((az - th + 180) % 360 - 180)
        D = np.where(d < 90, np.cos(np.radians(d)) ** nexp, 0.0)
        E = max(float((D * openk[i]).sum() / D.sum()), 0.01)
        hs = hs0 * math.sqrt(E)
        # local wind sea across short fetches (estuaries, bays in the lee): Hs = 0.0016 U sqrt(F/g), only where the upwind fetch < 25 km
        k = int(round(wd / 10.0)) % 36
        Fw = fetch[i, k] * 1000.0
        if Fw < 25000:
            hs = math.hypot(hs, 0.0016 * (ws * 0.5144) * math.sqrt(Fw / 9.81))
        Hs_near[i, h] = hs; Hs_off[i, h] = hs0; wspd[i, h] = ws; wdir[i, h] = wd
        onshore[i, h] = math.cos(math.radians((wd - aspect[i] + 180) % 360 - 180))

# ---------------------------------------------------------------- habitat guilds
txt = lambda c: df[c].fillna("").astype(str)
rock_at = lambda off: txt(f"eusm_substrate_{off}m").str.contains("Rock") | txt(f"substrate_{off}m").str.contains("Rock")
sed_re = "Sand|Coarse|Mixed|mud|Mud|Gravel|gravel|sand"
sed_at = lambda off: (txt(f"eusm_substrate_{off}m").str.contains(sed_re) | txt(f"substrate_{off}m").str.contains(sed_re)) & ~rock_at(off)
beach_name = txt("names_nearby").str.contains(r"\[Beach, (?:[0-9]{1,2}|[1-4][0-9]{2}) m\]")
setting = df.setting.values
is_open = setting == "open coast"; is_semi = setting == "semi-enclosed bay / estuary mouth"; is_est = np.isin(setting, ["estuary / ria / harbour", "tidal river / creek"])
iw = df.intertidal_width_m.values
d150 = df.maxdepth_150m.values; d300 = df.maxdepth_300m.values; d1000 = df.maxdepth_1000m.values
d300f = np.where(np.isnan(d300), np.where(np.isnan(d1000), 0.0, d1000 * 0.3), d300)
d150f = np.where(np.isnan(d150), d300f * 0.5, d150)
rock_near = (rock_at(100) | rock_at(300)).values
rock_far = rock_at(1000).values | (df.dist_to_mapped_rock_m.values <= 500)
inferred_rock = is_open & (iw < 40) & ~beach_name.values
rockness = np.where(rock_near, 1.0, np.where(rock_far, 0.7, np.where(inferred_rock, 0.5, 0.1)))
sed_near = (sed_at(100) | sed_at(300)).values
sandness = np.where(sed_near & beach_name.values, 1.0, np.where(sed_near, 0.8, np.where(beach_name.values, 0.7, np.where(sed_at(1000).values | (df.dist_to_mapped_sediment_m.values <= 400), 0.3, 0.0))))
openf = np.where(is_open, 1.0, np.where(is_semi, 0.6, 0.0))
headland = np.clip((df.n_dir_gt10km.values - 14) / 10.0, 0, 1)
streams = np.minimum(df.n_stream_mouths.values + df.n_river_polys.values, 2)
H = {}
sed_far = sed_at(1000).values | (df.dist_to_mapped_sediment_m.values <= 400)
beachness = np.where(beach_name.values | (sed_at(100).values & (iw >= 60)), np.clip(iw / 150.0, 0.3, 1.0), 0.25)
H["ROUGH"] = rockness * (0.15 + 0.85 * np.clip(d300f / 25.0, 0, 1) ** 0.7) * (0.7 + 0.3 * headland) * np.where(is_est, 0.6, 1.0)
H["SURF"] = np.minimum(1.0, sandness * beachness * np.clip(1 - d300f / 15.0, 0.2, 1) * openf * (0.85 + 0.075 * streams))
H["STEEP"] = sandness * np.clip(d150f / 8.0, 0, 1) * openf
# reef-meets-sand: strongest where rock AND sediment are both mapped inside 300 m of the low-water line
edge = np.where(rock_near & sed_near, 1.0, np.where(rock_near & sed_far, 0.7, np.where(sed_near & rock_far, 0.6, np.where(rock_far & sed_far, 0.35, 0.0))))
H["EDGE"] = edge * (0.3 + 0.7 * np.clip(d300f / 12.0, 0, 1)) * openf * (0.85 + 0.075 * streams)
estbase = np.where(is_est, 1.0, np.where(is_semi, 0.5, 0.0))
H["EST"] = np.minimum(1.0, estbase * (0.45 + 0.25 * (d300f >= 3) + 0.15 * ((iw >= 50) & (iw <= 800)) + 0.15 * (streams > 0) + 0.10 * (d300f >= 10)))
V = {"SURF": 1.0, "EDGE": 1.0, "ROUGH": 0.9, "STEEP": 0.8, "EST": 0.7}
LABEL = {"SURF": "surf / open sandy beach (bass, rays, turbot, flounder, whiting)", "EDGE": "reef-meets-sand mixed ground (bass, huss, rays, pollack)",
         "ROUGH": "rough ground / deep-water rock (pollack, wrasse, conger, huss)", "STEEP": "steep-to beach with depth close in (whiting, rays, bass, codling)",
         "EST": "estuary / creek (flounder, bass, mullet)"}


def trap(x, pts):
    xs, ys = zip(*pts)
    return np.interp(x, xs, ys)


WAVE = {"SURF": [(0.2, 0.0), (0.8, 1.0), (1.6, 1.0), (2.5, 0.55), (3.5, 0.2), (4.5, 0.05)], "EDGE": [(0.1, 0.4), (0.6, 1.0), (1.8, 1.0), (2.8, 0.45), (4.0, 0.1)],
        "ROUGH": [(0.0, 1.0), (1.2, 1.0), (2.2, 0.55), (3.5, 0.15)], "STEEP": [(0.2, 0.6), (0.5, 1.0), (1.8, 1.0), (3.0, 0.45), (4.0, 0.15)],
        "EST": [(0.0, 1.0), (0.6, 1.0), (1.5, 0.5)]}
night = np.array([1.0 if (h <= 6 or h >= 18) else (1.0 if h in (7, 16, 17) else 0.6) for h in range(24)])
LIGHT = {g: night for g in ("SURF", "EDGE", "ROUGH", "STEEP")}
LIGHT["EST"] = np.array([1.0 if (h <= 7 or h >= 16) else 0.9 for h in range(24)])
spate = np.where(setting == "tidal river / creek", 0.7, 1.0)
tidef = np.zeros((n, 24)); tidef_est = np.zeros((n, 24)); tlabel = np.empty((n, 24), dtype=object)
for i in range(n):
    ph = phase[ports[port_i[i]]]
    for h, (k, since, to) in enumerate(ph):
        if k == "LW":
            tidef[i, h] = 1.0 if since >= 1 else 0.85; tidef_est[i, h] = 1.0 if since >= 1 else 0.6
        else:
            tidef[i, h] = 0.9 if since < 1 else (0.75 if since < 3 else 0.65); tidef_est[i, h] = 0.8 if since < 2 else 0.5
        tlabel[i, h] = f"{k}+{since:.1f}"
C3 = {}; best_start = {}
for g in H:
    C = trap(Hs_near, WAVE[g]) * LIGHT[g][None, :] * (tidef_est if g == "EST" else tidef)
    if g in ("SURF", "STEEP"):                      # an onshore gale fills a beach with weed and side-drift: mild penalty
        C = C * np.where((onshore > 0.5) & (wspd > 25), 0.85, 1.0)
    roll = np.stack([C[:, s:s + 3].mean(1) for s in range(22)], 1)
    best_start[g] = roll.argmax(1); C3[g] = roll.max(1)
    if g == "EST":
        C3[g] = C3[g] * spate
P_g = np.stack([V[g] * H[g] * C3[g] for g in H], 1); H_g = np.stack([V[g] * H[g] for g in H], 1)
G = list(H)
bi = P_g.argmax(1)
df["H_score"] = (100 * H_g.max(1)).round(0)
df["H_guild"] = [G[i] for i in H_g.argmax(1)]
df["P_score"] = (100 * P_g.max(1)).round(0)
df["P_guild"] = [G[i] for i in bi]
df["P_window"] = [f"{best_start[G[b]][i]:02d}-{best_start[G[b]][i] + 3:02d}h" for i, b in enumerate(bi)]
df["P_tide_at_window"] = [tlabel[i, best_start[G[b]][i] + 1] for i, b in enumerate(bi)]
for g in G:
    df[f"H_{g}"] = (100 * H[g]).round(0)
for h in (0, 3, 6, 9, 12, 15, 18, 21):
    df[f"Hs_near_{h:02d}"] = Hs_near[:, h].round(1)
df["onshore_00"] = onshore[:, 0].round(2); df["onshore_12"] = onshore[:, 12].round(2); df["onshore_18"] = onshore[:, 18].round(2)
thin = []
for i in range(n):
    t = []
    if np.isnan(d300[i]): t.append("no bathymetry cell within 300 m")
    if not (rock_near[i] or sed_near[i]): t.append("no mapped seabed within 300 m (nearest %d m)" % df.eusm_nearest_dist_m.values[i])
    if isinstance(df.side_note.values[i], str) and "unresolved" in df.side_note.values[i]: t.append("seaward side inferred from fetch")
    if iw[i] > 3000: t.append("no low-water line within 3 km")
    thin.append("; ".join(t))
df["thin_data"] = thin
df["rockness"] = rockness; df["sandness"] = sandness
df.to_csv(f"{R}/coastline/segments_scored.csv", index=False)
df.to_csv(f"{OUT}/segments_scored.csv", index=False)

# ---------------------------------------------------------------- coastline.md
GROUPN = {"MAIN": "Mainland backbone (Marsland Mouth to the Tamar tidal limit, consecutive)", "FRAG": "Mainland side pieces (harbour interiors, branches, river islands - open lines)",
          "ISLET": "Cornish islands, islets and rocks standing above high water (closed rings)", "SCILLY": "Isles of Scilly (all islands and rocks above high water)",
          "DRY": "Detached drying reefs, ledges and banks (land only below high water) - Cornwall", "DRY-SCILLY": "Detached drying reefs and ledges - Isles of Scilly"}
o = []; A = o.append
A("# Workstream 7 - Systematic coastline coverage: every segment of the Cornish and Scilly shoreline\n")
A(f"Built {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC by `fishing/tools/coastline/01_build_segments.py`, `02_enrich.py`, `03_score.py`. Full table (all {len(df.columns)} columns, including the 36-direction fetch) in `coastline/segments_scored.csv`.\n")
A("## 1. How the shoreline was divided\n")
g = df.groupby("group").agg(nseg=("seg_id", "count"), km=("length_m", lambda s: s.sum() / 1000), pieces=("piece", "nunique"), maxlen=("length_m", "max"))
A("- **Base line:** Ordnance Survey OS OpenMap Local (Open Government Licence), `TidalBoundary` *High Water Mark* lines, tiles SW, SX, SV, SS (downloaded 2026-11-21 ~15:18 UTC from api.os.uk). The high-water line runs up every estuary and creek to the Normal Tidal Limit. The *Low Water Mark* lines give the low-water shore position and intertidal width; `Foreshore` polygons give drying ground.")
A("- **County membership:** ONS Counties and Unitary Authorities (December 2024) full-extent (BFE) polygons for Cornwall and the Isles of Scilly; Devon and Plymouth shores are excluded (Tamar east bank, Plymouth Sound east, Eddystone - administratively Plymouth). Offshore rocks outside every polygon were assigned to the nearest authority (list in the tool output `offshore_pieces_assignment.json`).")
A("- **Consecutive order:** the mainland high-water line was chained into one continuous line from **Marsland Mouth (Devon border, north coast) clockwise round Land's End to the tidal limit of the Tamar**; small breaks in the OS line work (median 3 m; stream mouths, bridges, structures) were bridged with straight connectors. It was then cut into equal pieces of **no more than 1,000 m** (IDs `M0001`-`M%04d`). Side pieces, islands and rocks are listed after the mainland in order of the adjacent mainland chainage; Scilly follows; then detached drying reefs and banks (land that meets water only below high water)." % (df.group == "MAIN").sum())
A(f"- **Totals: {n} segments, {df.length_m.sum()/1000:.0f} km of shoreline; longest segment {df.length_m.max():.0f} m.**\n")
A("| Group | Segments | Shoreline km | Separate pieces | Longest segment m |\n|---|---|---|---|---|")
for k, r in g.iterrows():
    A(f"| {GROUPN.get(k, k)} | {int(r.nseg)} | {r.km:.1f} | {int(r.pieces)} | {r.maxlen:.0f} |")
A("\n## 2. What was computed for every segment (first principles) and from what\n")
A("| Descriptor | Method | Source | Quality |\n|---|---|---|---|")
A("| Aspect | seaward normal of the segment (local) and fetch-weighted open-water direction (`aspect_open`) | geometry | good |")
A("| Wave fetch, 36 directions | ray casting from a point 15 m seaward to the first land (OS high-water lines within the tiles; Natural Earth 1:10m land beyond: Ireland, Wales, France), capped at 500 km | OS + Natural Earth | good; no refraction/diffraction |")
A("| Setting | open coast (>= 6 directions with fetch > 10 km) / semi-enclosed bay or estuary mouth / estuary-ria-harbour / tidal river-creek (max fetch < 1.5 km) | derived | good |")
A("| Intertidal width | distance from the segment midpoint to the OS low-water line | OS | good (OS low water = mean low water, not LAT) |")
A("| Depth close in | EMODnet Digital Bathymetry (DTM, 1/16 arc-minute = ~115 m x 74 m cells, depths below LAT), max depth within 150 / 300 / 500 / 1000 / 2000 m of the low-water shore point; distance to the 2 / 5 / 10 / 20 / 30 / 50 m depth | EMODnet Bathymetry WCS `emodnet:mean`, downloaded 2026-11-21 15:20 UTC | **coarse**: gullies, ledges and drop-offs narrower than ~100 m are invisible; many estuaries have no cells |")
A("| Seabed type | point-in-polygon at 100 / 300 / 1000 m seaward of low water, plus nearest mapped polygon: EMODnet Geology seabed substrate (1:50k multiscale, 1:250k, 1:1M Folk classes) and EUSeaMap 2025 (substrate, biozone, energy) | EMODnet Geology WFS, EMODnet Seabed Habitats WFS, downloaded 15:20-15:25 UTC | **thin inshore**: broad-scale modelled map; no mapped seabed within 300 m for most segments (see section 5) |")
A("| Kelp | not mapped anywhere at this scale. Proxy only: rock substrate in the infralittoral biozone (kelp zone) | EUSeaMap | THIN (inference) |")
A("| Bedrock | BGS Geology 625k bedrock polygon just landward of the segment | BGS OGC API, downloaded 15:20 UTC | good at 1:625k |")
A("| Outflows | OS OpenMap Local stream line ends within 25 m and river polygons within 10 m of the segment | OS | good for mapped streams; outfalls/pipes not included |")
A("| Names | three nearest coastal features within 1.5 km and nearest settlement | OS Open Names | good |")
A("| Tidal flow | NOT computed per segment. Only proxies: headland index (number of directions with > 10 km fetch) and the coarse ocean-model currents at the reference points (`sea_state.md` section 6); literature in `tidal_streams.md` | - | **THIN for every segment** |")
A("| Reefs / gullies / sandbanks | detached drying reefs and banks are themselves segments (groups DRY); mapped rock within 500 m is recorded; gullies are below the resolution of every dataset used | OS Foreshore, EUSeaMap | THIN for gullies |")
A("| Charts | Admiralty / Navionics charts could not be accessed programmatically - NOT USED | - | gap |")
A("| Man-made structure (piers, harbour walls) | OpenStreetMap could not be reached (Overpass servers refused/timed out); structures appear only through the documented-marks overlay | - | gap |")
A("| Conditions on 22 Nov | wind and offshore waves: multi-model median at the nearest of 39 reference points (`weather.md`, `sea_state.md`); nearshore wave height = offshore Hs x sqrt(directional energy fraction reaching the segment through its open fetch directions, cos^4 or cos^8 spreading) plus fetch-limited local wind sea where the upwind fetch is < 25 km; tide phase from the nearest EasyTide port | this study | indicative only |")
A("| Documentary overlay | merged known marks within 600 m of the segment midpoint (`marks.md`) | workstream 6 | - |")
A("\n## 3. The provisional score\n")
A("**H (habitat potential, 0-100)** = the best of five habitat guilds, each 0-1, times a provisional species-value weight:\n")
A("| Guild | Meaning | Formula (rockness, sandness in [0,1]; d150/d300 = max depth within 150/300 m; open = 1 open coast, 0.6 semi-enclosed, 0 estuary) | Value weight |\n|---|---|---|---|")
A("| SURF | surf / open sandy beach (bass, rays, turbot, flounder, whiting) | sandness x beachness x clip(1 - d300/15, 0.2, 1) x open x (0.85 + 0.075 x outflows[max 2]); beachness = clip(intertidal width/150, 0.3, 1) where a beach is named or sediment is mapped at 100 m with >= 60 m of foreshore, else 0.25 | 1.0 |")
A("| EDGE | reef-meets-sand mixed ground (bass, huss, rays, pollack) | edge x (0.3 + 0.7 x clip(d300/12)) x open x (0.85 + 0.075 x outflows); edge = 1.0 rock and sediment both mapped within 300 m, 0.7 rock within 300 m and sediment within 1 km, 0.6 sediment within 300 m and rock within 500 m-1 km, 0.35 both only at distance | 1.0 |")
A("| ROUGH | rough ground / deep-water rock (pollack, wrasse, conger, huss) | rockness x (0.15 + 0.85 x clip(d300/25)^0.7) x (0.7 + 0.3 x headland index) x (0.6 inside estuaries) | 0.9 |")
A("| STEEP | steep-to beach with depth close in (whiting, rays, bass, codling) | sandness x clip(d150/8) x open | 0.8 |")
A("| EST | estuary / creek (flounder, bass, mullet) | [estuary 1, semi-enclosed 0.5] x (0.45 + 0.25[channel >= 3 m within 300 m] + 0.15[flats 50-800 m] + 0.15[stream/river] + 0.10[>= 10 m]) | 0.7 |")
A("\nrockness = 1.0 rock mapped at 100 or 300 m; 0.7 rock within 500 m or at 1000 m; 0.5 inferred (open coast, intertidal < 40 m, no beach name); else 0.1. sandness = 1.0 sediment mapped at 100/300 m and an OS-named beach within 500 m; 0.8 sediment mapped; 0.7 named beach only; 0.3 sediment only at >= 400-1000 m; else 0.\n")
A("**P (provisional score for 22 Nov, 0-100)** = max over guilds of value x H_guild x best 3-hour mean of [wave suitability(nearshore Hs) x light factor x tide factor], with a 0.7 spate factor on tidal rivers/creeks (heavy rain forecast, rivers already above normal). Wave suitability: SURF ideal 0.8-1.6 m (0 below 0.2 m, 0.55 at 2.5 m, 0.2 at 3.5 m); EDGE ideal 0.6-1.8 m (0.45 at 2.8 m); ROUGH ideal <= 1.2 m (0.55 at 2.2 m, 0.15 at 3.5 m); STEEP ideal 0.5-1.8 m; EST ideal < 0.6 m; SURF and STEEP x 0.85 under an onshore wind > 25 kn. Light: darkness and dusk/dawn 1.0, daylight 0.6 (EST 0.9). Tide: flood from LW+1 1.0; first hour of flood 0.85; HW to HW+1 0.9; to HW+3 0.75; later ebb 0.65 (EST: flood 1.0, early ebb 0.8, later ebb 0.5).\n")
A("**These weights are provisional and deliberately simple.** They exist so that every segment has a comparable, reproducible number in Phase 1; Phase 2 must re-derive the weights from `species_sst.md`, add water clarity, and re-score. The score knows nothing about fish records - the documentary evidence is the separate overlay column.\n")
q = df.P_score.quantile([0.5, 0.75, 0.9, 0.95, 0.99]).round(0).to_dict()
A(f"Distribution of P over all {n} segments: median {q[0.5]:.0f}, 75th pct {q[0.75]:.0f}, 90th {q[0.9]:.0f}, 95th {q[0.95]:.0f}, 99th {q[0.99]:.0f}, max {df.P_score.max():.0f}. Segments with P >= the 90th percentile are carried into Phase 2 as candidates whether or not anyone has documented fishing there.\n")
A("| Best guild on the day | Segments | Mean P | Max P |\n|---|---|---|---|")
for k, r in df.groupby("P_guild").P_score.agg(["count", "mean", "max"]).iterrows():
    A(f"| {k} - {LABEL[k]} | {int(r['count'])} | {r['mean']:.0f} | {r['max']:.0f} |")
thr = df.P_score.quantile(0.9)
cand = df[df.P_score >= thr]
A(f"\n## 4. High-scoring segments (P >= {thr:.0f}; {len(cand)} segments) - candidates for Phase 2\n")
A(f"Of these, {int((cand.known_marks_600m == '').sum())} have **no documented mark within 600 m** (first-principles-only candidates).\n")
cols = "| Seg | Lat, Lon | Nearest names | Setting | Faces | d150 / d300 / d1000 m | Seabed near (100 / 300 / 1000 m; nearest) | Hs near 00/06/12/18h | H | P | Guild | Window (tide) | Known marks within 600 m | Thin data |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"


def row(r):
    sb = "/".join((str(r[f"eusm_substrate_{o_}m"]) if isinstance(r[f"eusm_substrate_{o_}m"], str) else "-").replace(" or other hard substrata", "").replace(" substrate", "").replace(" sediment", "") for o_ in (100, 300, 1000)) + f"; {str(r.eusm_nearest_substrate).replace(' or other hard substrata','').replace(' substrate','')} @{r.eusm_nearest_dist_m:.0f} m"
    dep = "/".join("-" if pd.isna(r[c]) else f"{r[c]:.0f}" for c in ("maxdepth_150m", "maxdepth_300m", "maxdepth_1000m"))
    nm = str(r.names_nearby) if isinstance(r.names_nearby, str) and r.names_nearby else f"near {r.nearest_place}"
    nm = "; ".join(x.split(" [")[0] for x in nm.split("; "))[:70]
    return f"| {r.seg_id} | {r.lat:.4f}, {r.lon:.4f} | {nm} | {r.setting.split(' / ')[0]} | {r.aspect_open_deg:.0f} | {dep} | {sb} | {r.Hs_near_00}/{r.Hs_near_06}/{r.Hs_near_12}/{r.Hs_near_18} | {r.H_score:.0f} | {r.P_score:.0f} | {r.P_guild} | {r.P_window} ({r.P_tide_at_window}) | {r.known_marks_600m or '-'} | {r.thin_data or '-'} |"


A(cols)
for r in cand.sort_values("P_score", ascending=False).itertuples(index=False):
    A(row(pd.Series(r._asdict())))
A("\n## 5. Thin data - where the assessment is weak\n")
tcount = collections.Counter(t.split(" (")[0] for T_ in thin for t in T_.split("; ") if t)
A("| Limitation | Segments affected |\n|---|---|")
for k, v in tcount.most_common():
    A(f"| {k} | {v} |")
A(f"| tidal flow not assessed per segment | {n} (all) |")
A(f"| gullies / ledges / kelp below data resolution | {n} (all) |")
A(f"| no seabed map AND no bathymetry within 300 m (score rests on geometry only) | {int(sum(1 for T_ in thin if 'no bathymetry' in T_ and 'no mapped seabed' in T_))} |")
by = df.assign(t=[bool(x) for x in thin]).groupby("setting").t.agg(["sum", "count"])
A("\nBy setting: " + "; ".join(f"{k}: {int(r['sum'])} of {int(r['count'])} segments carry at least one thin-data flag" for k, r in by.iterrows()) + ".\n")
A("## 6. The log - every segment, in order\n")
for grp in ("MAIN", "FRAG", "ISLET", "SCILLY", "DRY", "DRY-SCILLY"):
    sub = df[df.group == grp]
    if not len(sub): continue
    A(f"\n### {GROUPN[grp]} - {len(sub)} segments\n")
    A(cols)
    for r in sub.itertuples(index=False):
        A(row(pd.Series(r._asdict())))
open(f"{R}/coastline.md", "w").write("\n".join(o) + "\n")
print("coastline.md written:", len(o), "lines; P quantiles", q, "max", df.P_score.max())
print(df.groupby("P_guild").P_score.agg(["count", "mean", "max"]).round(0).to_string())
top = df.sort_values("P_score", ascending=False).head(25)
for r in top.itertuples():
    print(r.seg_id, r.lat, r.lon, (r.names_nearby if isinstance(r.names_nearby, str) else "")[:45], "|", r.setting[:10], "| H", r.H_score, "P", r.P_score, r.P_guild, r.P_window, "| marks:", (r.known_marks_600m or "-")[:40])
