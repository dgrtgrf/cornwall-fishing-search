#!/usr/bin/env python3
"""Workstream 7, step 2: attach first-principles physical descriptors to every shoreline segment.

Per segment: place names (OS Open Names), seaward aspect, low-water shore position and intertidal width
(OS low water mark), wave fetch in 36 directions (ray casting against OS high-water lines + Natural Earth
far-field land), bathymetry statistics (EMODnet DTM, ~115 m), seabed substrate (EMODnet Geology) and
habitat class (EUSeaMap 2025: substrate / biozone / energy), bedrock (BGS 625k), stream outflows (OS
OpenMap Local surface water), and a setting class.

Usage: 02_enrich.py <raw_dir> <out_dir>
"""
import sys, glob, json, math, warnings, csv, os
os.environ["OGR_GEOJSON_MAX_OBJ_SIZE"] = "0"
import numpy as np
import pandas as pd
import geopandas as gpd
import shapely
from shapely.geometry import LineString, Point, box
from shapely import STRtree
from scipy.spatial import cKDTree
from pyproj import Transformer
import rasterio

warnings.filterwarnings("ignore")
RAW, OUT = sys.argv[1], sys.argv[2]
T = Transformer.from_crs(27700, 4326, always_xy=True)
F = Transformer.from_crs(4326, 27700, always_xy=True)


def load(layer, areas=("SW", "SX", "SV", "SS")):
    fs = []
    for a in areas:
        p = glob.glob(f"{RAW}/oml_{a}/*/data/{a}_{layer}.shp")
        if p:
            fs.append(gpd.read_file(p[0]))
    return pd.concat(fs, ignore_index=True)


seg = gpd.read_file(f"{OUT}/segments_raw.gpkg")
n = len(seg)
print("segments", n)
geoms = seg.geometry.values
mid = shapely.line_interpolate_point(geoms, 0.5, normalized=True)
mx, my = shapely.get_x(mid), shapely.get_y(mid)

# ---------------------------------------------------------------- seaward side / aspect
tb = load("TidalBoundary")
hw_lines = tb[tb.CLASSIFICA == "High Water Mark"].geometry.values
lw_lines = tb[tb.CLASSIFICA == "Low Water Mark"].geometry.values
tw = load("TidalWater").geometry.values
fo = load("Foreshore").geometry.values
water_all = np.concatenate([tw, fo])
tree_all = STRtree(water_all)
tree_tw = STRtree(tw)

# local tangent: chord between points at 35 % and 65 % of the segment (robust to wiggles), and whole-segment chord
p_a = shapely.line_interpolate_point(geoms, 0.35, normalized=True)
p_b = shapely.line_interpolate_point(geoms, 0.65, normalized=True)
tx, ty = shapely.get_x(p_b) - shapely.get_x(p_a), shapely.get_y(p_b) - shapely.get_y(p_a)
nrm = np.hypot(tx, ty)
nrm[nrm == 0] = 1.0
tx, ty = tx / nrm, ty / nrm
nx, ny = ty, -tx          # right-hand normal


def in_water(px, py, tree):
    pts = shapely.points(px, py)
    hit = np.zeros(len(pts), bool)
    idx = tree.query(pts, predicate="within")
    hit[np.unique(idx[0])] = True
    return hit


is_dry = seg.group.str.startswith("DRY").values
side = np.zeros(n)        # +1 = right-hand normal is seaward, -1 = left
conf = np.array(["ok"] * n, dtype=object)
for off in (12.0, 30.0, 70.0, 150.0):
    todo = side == 0
    if not todo.any():
        break
    for tree, mask in ((tree_all, todo & ~is_dry), (tree_tw, todo & is_dry)):
        if not mask.any():
            continue
        r = in_water(mx[mask] + nx[mask] * off, my[mask] + ny[mask] * off, tree)
        l = in_water(mx[mask] - nx[mask] * off, my[mask] - ny[mask] * off, tree)
        s = np.where(r & ~l, 1.0, np.where(l & ~r, -1.0, 0.0))
        ids = np.where(mask)[0]
        side[ids] = s
        both = ids[(r & l)]
        conf[both] = "water both sides (spit/pier/rock) at %dm" % off
unres = side == 0
conf[unres] = "seaward side unresolved - larger-fetch side used"
print("seaward side unresolved after offsets:", int(unres.sum()))

# ---------------------------------------------------------------- obstacles for ray casting
hw_all = hw_lines
# cut the high-water lines into short pieces for a tight spatial index
pieces = []
for g in hw_all:
    g = g.simplify(3.0)
    c = np.asarray(g.coords)
    for i in range(0, len(c) - 1, 25):
        pieces.append(LineString(c[i:i + 26]))
ne = gpd.read_file(f"{RAW}/../ne_10m_land.geojson").clip(box(-13, 45.5, 3.5, 56.5)).to_crs(27700)
ne_geom = ne.geometry.unary_union
os_cover = box(0, 0, 300000, 100000).union(box(200000, 100000, 300000, 200000))
ne_far = ne_geom.difference(os_cover.buffer(0))
far_lines = []
for poly in (ne_far.geoms if hasattr(ne_far, "geoms") else [ne_far]):
    c = np.asarray(poly.exterior.coords)
    for i in range(0, len(c) - 1, 40):
        far_lines.append(LineString(c[i:i + 41]))
obst = np.array(pieces + far_lines, dtype=object)
otree = STRtree(obst)
print("obstacle pieces", len(pieces), "+ far-field", len(far_lines))

NDIR = 36
RMAX = 500000.0
az = np.arange(NDIR) * 10.0
dxs, dys = np.sin(np.radians(az)), np.cos(np.radians(az))


def fetch_from(ox, oy):
    """fetch (m) for each origin x 36 directions"""
    m = len(ox)
    res = np.full((m, NDIR), RMAX)
    for k in range(NDIR):
        ex, ey = ox + dxs[k] * RMAX, oy + dys[k] * RMAX
        rays = shapely.linestrings(np.stack([np.stack([ox, oy], 1), np.stack([ex, ey], 1)], 1))
        qi, oi = otree.query(rays, predicate="intersects")
        if len(qi) == 0:
            continue
        inter = shapely.intersection(rays[qi], obst[oi])
        d = shapely.distance(shapely.points(ox[qi], oy[qi]), inter)
        np.minimum.at(res[:, k], qi, d)
    return res


OFF = 15.0
if unres.any():
    fr = fetch_from(mx[unres] + nx[unres] * OFF, my[unres] + ny[unres] * OFF).mean(1)
    fl = fetch_from(mx[unres] - nx[unres] * OFF, my[unres] - ny[unres] * OFF).mean(1)
    side[unres] = np.where(fr >= fl, 1.0, -1.0)
sx, sy = nx * side, ny * side                       # unit seaward normal
ox, oy = mx + sx * OFF, my + sy * OFF
fetch = fetch_from(ox, oy)
print("fetch done; median of max fetch km", round(float(np.median(fetch.max(1))) / 1000, 1))
aspect_local = (np.degrees(np.arctan2(sx, sy)) + 360) % 360
# open-water aspect: fetch-weighted mean direction (capped at 50 km so the ocean does not swamp local geometry)
w = np.minimum(fetch, 50000.0)
ax_, ay_ = (w * dxs).sum(1), (w * dys).sum(1)
aspect_open = (np.degrees(np.arctan2(ax_, ay_)) + 360) % 360
open_strength = np.hypot(ax_, ay_) / np.maximum(w.sum(1), 1)

# ---------------------------------------------------------------- low-water shore point, intertidal width
lw_tree = STRtree(lw_lines)
near = lw_tree.nearest(mid)
lw_near_pt = shapely.line_interpolate_point(lw_lines[near], shapely.line_locate_point(lw_lines[near], mid))
inter_w = shapely.distance(mid, lw_near_pt)
inter_w = np.where(is_dry, 0.0, inter_w)
lwx = np.where(is_dry, mx, shapely.get_x(lw_near_pt))
lwy = np.where(is_dry, my, shapely.get_y(lw_near_pt))
far_lw = inter_w > 3000
lwx[far_lw], lwy[far_lw] = mx[far_lw], my[far_lw]

# ---------------------------------------------------------------- bathymetry (EMODnet DTM)
with rasterio.open(f"{RAW}/emodnet_mean.tif") as r:
    z = r.read(1).astype("float32")
    tr = r.transform
    nod = r.nodata
print("bathy raw stats min/max", float(np.nanmin(z)), float(np.nanmax(z)), "nodata", nod)
rows, cols = np.indices(z.shape)
lon = tr.c + (cols + 0.5) * tr.a
lat = tr.f + (rows + 0.5) * tr.e
valid = np.isfinite(z)
if nod is not None:
    valid &= z != nod
# EMODnet mean depth: negative below datum (LAT) at sea, positive on land -> depth = -z for sea cells
sea = valid & (z < 0)
bx, by = F.transform(lon[sea], lat[sea])
depth = -z[sea]
# keep cells within 6 km of any segment
ktmp = cKDTree(np.stack([mx, my], 1))
dmin, _ = ktmp.query(np.stack([bx, by], 1), distance_upper_bound=6000)
keepc = np.isfinite(dmin)
bx, by, depth = bx[keepc], by[keepc], depth[keepc]
bt = cKDTree(np.stack([bx, by], 1))
print("sea cells kept", len(depth))
# reference shore point for depth statistics = low-water shore point (where the water's edge is at LW)
ref = np.stack([lwx, lwy], 1)
B = {}
for rad in (150, 300, 500, 1000, 2000):
    idx = bt.query_ball_point(ref, rad)
    B[f"maxdepth_{rad}m"] = np.array([depth[i].max() if len(i) else np.nan for i in idx])
    if rad in (300, 1000):
        B[f"meandepth_{rad}m"] = np.array([depth[i].mean() if len(i) else np.nan for i in idx])
        B[f"ncells_{rad}m"] = np.array([len(i) for i in idx])
for thr in (2, 5, 10, 20, 30, 50):
    sel = depth >= thr
    tt = cKDTree(np.stack([bx[sel], by[sel]], 1))
    d, _ = tt.query(ref)
    B[f"dist_to_{thr}m"] = d
dn, _ = bt.query(ref)
B["dist_to_nearest_bathy_cell"] = dn

# ---------------------------------------------------------------- seabed substrate + EUSeaMap at offsets seaward of LW
def load_poly(path):
    g = gpd.read_file(path)
    return g.to_crs(27700)


subs = []
for nm in ("50k_multiscale", "250k", "1m"):
    try:
        g = load_poly(f"{RAW}/substrate_{nm}.geojson")
        col = "folk_16cl_txt" if "folk_16cl_txt" in g else None
        g["cls"] = np.where(g["folk_16cl_txt"].astype(str).str.contains("No data"), g["folk_7cl_txt"], g["folk_16cl_txt"]) if col else g["folk_7cl_txt"]
        subs.append((nm, g))
    except Exception as e:
        print("substrate", nm, "failed", e)
eus = load_poly(f"{RAW}/eusm2025_eunis2019_full.geojson")
print("EUSeaMap polys", len(eus))


def pip(gdf, px, py, col):
    pts = shapely.points(px, py)
    tree = STRtree(gdf.geometry.values)
    qi, gi = tree.query(pts, predicate="within")
    out = np.array([None] * len(pts), dtype=object)
    vals = gdf[col].values
    out[qi] = vals[gi]
    return out


S = {}
for off in (100, 300, 1000):
    px, py = lwx + sx * off, lwy + sy * off
    best = np.array([None] * n, dtype=object)
    src = np.array([None] * n, dtype=object)
    for nm, g in subs:
        v = pip(g, px, py, "cls")
        take = (best == None) & (v != None)          # noqa: E711
        best[take] = v[take]
        src[take] = nm
    S[f"substrate_{off}m"] = best
    S[f"substrate_src_{off}m"] = src
    for col in ("substrate", "biozone", "energy"):
        S[f"eusm_{col}_{off}m"] = pip(eus, px, py, col)

# ---------------------------------------------------------------- bedrock geology
bgs = load_poly(f"{RAW}/bgs625_bedrock.geojson")
btree = STRtree(bgs.geometry.values)
ni = btree.nearest(shapely.points(mx - sx * 30, my - sy * 30))
G = {"bedrock": bgs["rcs_d"].values[ni], "bedrock_unit": bgs["lex_d"].values[ni],
     "bedrock_dist_m": shapely.distance(shapely.points(mx - sx * 30, my - sy * 30), bgs.geometry.values[ni])}

# ---------------------------------------------------------------- stream outflows (OS surface water reaching the shore)
swl = load("SurfaceWater_Line").geometry.values
swa = load("SurfaceWater_Area").geometry.values
stree = STRtree(geoms)
ends = shapely.points(np.concatenate([np.asarray([g.coords[0] for g in swl]), np.asarray([g.coords[-1] for g in swl])]))
qi, si = stree.query(ends, predicate="dwithin", distance=25.0)
n_streams = np.bincount(si, minlength=n)
qa, sa = stree.query(swa, predicate="dwithin", distance=10.0)
n_riverpoly = np.bincount(sa, minlength=n)

# ---------------------------------------------------------------- names (OS Open Names)
rows_ = []
for fpath in glob.glob(f"{RAW}/opname/Data/S[VWXS]*.csv"):
    with open(fpath, newline="", encoding="utf-8") as fh:
        for r in csv.reader(fh):
            if r[6] in ("landform", "hydrography", "populatedPlace", "landcover"):
                rows_.append((r[2], r[6], r[7], float(r[8]), float(r[9])))
names = pd.DataFrame(rows_, columns=["name", "type", "local", "x", "y"])
print("names loaded", len(names), names.local.value_counts().head(25).to_dict())
coastal = names[names.type.isin(["landform", "hydrography", "landcover"]) & ~names.local.isin(["Hill Or Mountain", "Valley", "Woodland Or Forest", "Inland Water", "Spring", "Waterfall", "Hill Or Mountain Ranges", "Other Landcover", "Wetland", "Other Landform"])]
kt = cKDTree(coastal[["x", "y"]].values)
d1, i1 = kt.query(np.stack([mx, my], 1), k=3)
pop = names[names.type == "populatedPlace"]
kp = cKDTree(pop[["x", "y"]].values)
d2, i2 = kp.query(np.stack([mx, my], 1))
cn, cl = coastal.name.values, coastal.local.values
feat_names = []
for a in range(n):
    L = [f"{cn[i1[a, k]]} [{cl[i1[a, k]]}, {d1[a, k]:.0f} m]" for k in range(3) if d1[a, k] <= 1500]
    feat_names.append("; ".join(L))
place = [f"{pop.name.values[i2[a]]} ({pop.local.values[i2[a]]}, {d2[a] / 1000:.1f} km)" for a in range(n)]

# ---------------------------------------------------------------- assemble
out = seg.drop(columns="geometry").copy()
lonlat = np.array([T.transform(x, y) for x, y in zip(mx, my)])
out["lon"], out["lat"] = lonlat[:, 0].round(5), lonlat[:, 1].round(5)
ll2 = np.array([T.transform(x, y) for x, y in zip(lwx, lwy)])
out["lw_lon"], out["lw_lat"] = ll2[:, 0].round(5), ll2[:, 1].round(5)
out["aspect_local_deg"] = aspect_local.round(0)
out["aspect_open_deg"] = aspect_open.round(0)
out["open_strength"] = open_strength.round(2)
out["side_note"] = conf
out["intertidal_width_m"] = np.round(inter_w, 0)
for k in range(NDIR):
    out[f"fetch_{int(az[k]):03d}"] = (fetch[:, k] / 1000).round(2)
out["fetch_max_km"] = (fetch.max(1) / 1000).round(1)
out["n_dir_gt10km"] = (fetch > 10000).sum(1)
out["n_dir_gt100km"] = (fetch > 100000).sum(1)
out["n_dir_gt300km"] = (fetch > 300000).sum(1)
out["fetch_normal_km"] = np.array([fetch[a, int(round(aspect_local[a] / 10.0)) % NDIR] for a in range(n)]).round(2) / 1000
for k, v in B.items():
    out[k] = np.round(v, 1)
for k, v in S.items():
    out[k] = v
for k, v in G.items():
    out[k] = v
out["n_stream_mouths"] = n_streams
out["n_river_polys"] = n_riverpoly
out["names_nearby"] = feat_names
out["nearest_place"] = place
# setting class
ng10 = out["n_dir_gt10km"].values
fmax = out["fetch_max_km"].values
setting = np.where(ng10 >= 6, "open coast", np.where(fmax >= 10, "semi-enclosed bay / estuary mouth", np.where(fmax >= 1.5, "estuary / ria / harbour", "tidal river / creek")))
out["setting"] = setting
out.to_csv(f"{OUT}/segments_enriched.csv", index=False)
g2 = gpd.GeoDataFrame(out, geometry=seg.geometry.values, crs=27700)
g2.to_file(f"{OUT}/segments_enriched.gpkg", driver="GPKG")
print(out.setting.value_counts().to_dict())
print("depth data missing within 300 m:", int(np.isnan(B["maxdepth_300m"]).sum()), "| substrate missing at 300 m:", int((S["substrate_300m"] == None).sum()), "| EUSeaMap missing at 300 m:", int((S["eusm_substrate_300m"] == None).sum()))  # noqa: E711
print(out[["maxdepth_150m", "maxdepth_300m", "maxdepth_1000m", "intertidal_width_m", "fetch_max_km"]].describe().round(1).to_string())
