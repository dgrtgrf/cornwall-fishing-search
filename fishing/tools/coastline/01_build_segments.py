#!/usr/bin/env python3
"""Workstream 7, step 1: cut the entire Cornwall + Isles of Scilly shoreline into consecutive
segments of <= 1 km.

Source geometry: Ordnance Survey OS OpenMap Local (OGL v3), layers TidalBoundary (High Water Mark,
Low Water Mark), Foreshore and TidalWater, tiles SW, SX, SV, SS.  The Mean High Water line is the
base line that is segmented; it runs up every estuary to the Normal Tidal Limit.
County membership: ONS Counties & Unitary Authorities (Dec 2024) "BFE" polygons (extent of the realm).

Usage: 01_build_segments.py <raw_dir> <out_dir>
"""
import sys, glob, json, math, warnings
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString, MultiLineString, Point, Polygon
from shapely.ops import linemerge, unary_union, substring
from shapely import STRtree
from pyproj import Transformer

warnings.filterwarnings("ignore")
RAW, OUT = sys.argv[1], sys.argv[2]
MAXLEN = 1000.0
T = Transformer.from_crs(27700, 4326, always_xy=True)


def load(layer, areas=("SW", "SX", "SV", "SS")):
    fs = []
    for a in areas:
        p = glob.glob(f"{RAW}/oml_{a}/*/data/{a}_{layer}.shp")
        if p:
            fs.append(gpd.read_file(p[0]))
    return pd.concat(fs, ignore_index=True)


tb = load("TidalBoundary")
hwm = tb[tb.CLASSIFICA == "High Water Mark"].geometry.tolist()
lwm = tb[tb.CLASSIFICA == "Low Water Mark"].geometry.tolist()
fore = load("Foreshore")
print("HWM lines", len(hwm), "LWM lines", len(lwm), "foreshore polys", len(fore))

ua = gpd.read_file(f"{RAW}/ctyua_BFE.geojson").set_index("CTYUA24NM").geometry
corn, scil, devon, plym = ua["Cornwall"], ua["Isles of Scilly"], ua["Devon"], ua["Plymouth"]
other = unary_union([devon, plym])


def merge(lines):
    m = linemerge(unary_union(lines))
    return list(m.geoms) if hasattr(m, "geoms") else [m]


hw_chains = merge(hwm)
print("merged HWM chains (all tiles):", len(hw_chains), "total km", round(sum(c.length for c in hw_chains) / 1000, 1))

# --- county assignment -------------------------------------------------------------------------
# Region claimed by Cornwall: its BFE polygon (to low water / mid-river) with a 25 m tolerance, minus
# Devon and Plymouth.  Scilly likewise.  Chains wholly outside every polygon (offshore rocks) go to
# the nearest authority.
corn_reg = corn.buffer(25).difference(other)
scil_reg = scil.buffer(25)
other_reg = other.buffer(25)


def parts(g):
    if g.is_empty:
        return []
    if g.geom_type == "LineString":
        return [g]
    if g.geom_type in ("MultiLineString", "GeometryCollection"):
        return [p for p in g.geoms if p.geom_type == "LineString" and p.length > 0]
    return []


keep = {"Cornwall": [], "Isles of Scilly": []}
dropped_other_km = 0.0
unassigned = []
for c in hw_chains:
    inC = parts(c.intersection(corn_reg))
    inS = parts(c.intersection(scil_reg))
    keep["Cornwall"] += inC
    keep["Isles of Scilly"] += inS
    rest = c.difference(corn_reg).difference(scil_reg)
    for p in parts(rest):
        if p.intersects(other_reg) and p.intersection(other_reg).length > 0.5 * p.length:
            dropped_other_km += p.length / 1000
        else:
            unassigned.append(p)

# offshore rocks / islets not inside any authority polygon -> nearest authority
EDDYSTONE = Point(238300, 33600)  # Eddystone Rocks: administratively City of Plymouth (Devon)
log_unassigned = []
for p in unassigned:
    d = {"Cornwall": p.distance(corn), "Isles of Scilly": p.distance(scil), "Devon/Plymouth": p.distance(other)}
    who = min(d, key=d.get)
    if p.distance(EDDYSTONE) < 1500:
        who = "Devon/Plymouth"
    lon, lat = T.transform(p.centroid.x, p.centroid.y)
    log_unassigned.append(dict(lat=round(lat, 5), lon=round(lon, 5), length_m=round(p.length, 1), assigned=who,
                               dist_km={k: round(v / 1000, 2) for k, v in d.items()}))
    if who in keep:
        keep[who].append(p)
    else:
        dropped_other_km += p.length / 1000
print("Devon/Plymouth/other HWM dropped km:", round(dropped_other_km, 1), "| offshore pieces assigned by distance:", len(unassigned))

for k in keep:
    keep[k] = merge(keep[k]) if keep[k] else []
    print(k, "chains", len(keep[k]), "km", round(sum(c.length for c in keep[k]) / 1000, 1))

# --- order the Cornish mainland shoreline ---------------------------------------------------------
# The OS high-water line work has small breaks (stream mouths, bridges, structures; median gap ~3 m).
# Build a graph of the open chains (endpoints within TOL metres are joined), find the path from the
# Devon border on the north coast (Marsland Mouth) to the tidal limit of the Tamar, and bridge the
# gaps with straight connectors so the mainland becomes ONE consecutive line.  Chains not on that
# path are side pieces (harbour interiors, branches at structures, river islands) or closed rings
# (islands, islets, rocks) and are logged next to the nearest mainland chainage.
import heapq
from scipy.spatial import cKDTree
from pyproj import Transformer as _Tr
TOL = 150.0
cchains = keep["Cornwall"]
is_closed = lambda c: c.is_ring or Point(c.coords[0]).distance(Point(c.coords[-1])) < 1.0
open_ch = [c for c in cchains if not is_closed(c)]
ring_ch = [c for c in cchains if is_closed(c)]
E = np.array([pt for c in open_ch for pt in (c.coords[0], c.coords[-1])])   # endpoint 2*i = start, 2*i+1 = end
kd = cKDTree(E)
F = _Tr.from_crs(4326, 27700, always_xy=True)
p_start = F.transform(-4.546, 50.9284)    # Marsland Mouth (Devon border, north coast)
p_end = F.transform(-4.2071, 50.5172)     # upstream end of the Tamar high-water line (tidal limit)
n_start = int(kd.query(p_start)[1]); n_end = int(kd.query(p_end)[1])
print("start endpoint offset m", round(float(kd.query(p_start)[0]), 1), "end endpoint offset m", round(float(kd.query(p_end)[0]), 1))
# Dijkstra over endpoints: traversing chain i costs 0, jumping a gap costs the gap length (prefers true continuations)
dist = {n_start: 0.0}; prev = {}; pq = [(0.0, n_start)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist.get(u, 1e18): continue
    if u == n_end: break
    v = u ^ 1                                   # other end of the same chain
    if d < dist.get(v, 1e18) and prev.get(u, (None, None))[1] != "chain":
        dist[v] = d; prev[v] = (u, "chain"); heapq.heappush(pq, (d, v))
    if prev.get(u, (None, "x"))[1] == "chain" or u == n_start:
        pass
    for w in kd.query_ball_point(E[u], TOL):
        if w // 2 == u // 2: continue
        g = float(np.hypot(*(E[u] - E[w]))) + 0.01
        if d + g < dist.get(w, 1e18):
            dist[w] = d + g; prev[w] = (u, "gap"); heapq.heappush(pq, (d + g, w))
assert n_end in dist, "no continuous path from Marsland Mouth to the Tamar tidal limit within TOL"
path = [n_end]
while path[-1] != n_start:
    path.append(prev[path[-1]][0])
path = path[::-1]
coords = []; used = set(); bridged = 0.0; nbridge = 0
k = 0
while k < len(path) - 1:
    u, v = path[k], path[k + 1]
    if u // 2 == v // 2:                        # traverse the chain from endpoint u to endpoint v
        c = list(open_ch[u // 2].coords)
        if u % 2 == 1: c = c[::-1]
        if coords and np.hypot(coords[-1][0] - c[0][0], coords[-1][1] - c[0][1]) > 0.01:
            bridged += np.hypot(coords[-1][0] - c[0][0], coords[-1][1] - c[0][1]); nbridge += 1
        coords += c; used.add(u // 2)
    k += 1
main = LineString([(x, y) for x, y in ((c[0], c[1]) for c in coords)])
print("mainland backbone km", round(main.length / 1000, 1), "chains on path", len(used), "of", len(open_ch), "| gaps bridged", nbridge, "total bridged m", round(bridged, 1))

segments = []


def cut(chain, group, piece_id, closed):
    n = max(1, math.ceil(chain.length / MAXLEN))
    step = chain.length / n
    for i in range(n):
        seg = substring(chain, i * step, (i + 1) * step)
        if seg.geom_type != "LineString" or seg.length == 0:
            continue
        segments.append(dict(group=group, piece=piece_id, piece_len_m=chain.length, closed=closed, idx_in_piece=i,
                             n_in_piece=n, chain_start_m=i * step, geometry=seg))


cut(main, "MAIN", 0, False)
pieces = []
for i, c in enumerate(open_ch):
    if i not in used:
        pieces.append((main.project(c.centroid), c, False))
for c in ring_ch:
    pieces.append((main.project(c.centroid), c, True))
pieces.sort(key=lambda t: t[0])
for j, (ch, c, closed) in enumerate(pieces, start=1):
    cut(c, "ISLET" if closed else "FRAG", j, closed)
    for sgm in segments[-max(1, math.ceil(c.length / MAXLEN)):]:
        sgm["attach_chain_m"] = ch
        sgm["dist_to_main_m"] = c.distance(main)

# --- Scilly --------------------------------------------------------------------------------------
schains = sorted(keep["Isles of Scilly"], key=lambda c: -c.length)
for j, c in enumerate(schains, start=1):
    closed = c.is_ring or Point(c.coords[0]).distance(Point(c.coords[-1])) < 1.0
    cut(c, "SCILLY", j, closed)

# --- detached drying areas (land meets water only below high water): foreshore polygons that do not
#     touch any HWM line, e.g. drying reefs, ledges and sandbanks.  Segment their outline (the LWM).
fo = unary_union(fore.geometry.buffer(0.5).tolist())
fo_polys = list(fo.geoms) if hasattr(fo, "geoms") else [fo]
hw_all = keep["Cornwall"] + keep["Isles of Scilly"]
hw_tree = STRtree(hw_chains)
dry_km = 0.0
dj = 0
for poly in fo_polys:
    cands = hw_tree.query(poly, predicate="dwithin", distance=3.0)
    if len(cands):
        continue  # attached to a high-water shore
    c = poly.centroid
    inC = corn_reg.buffer(0).contains(c) or (not other_reg.contains(c) and not scil_reg.contains(c) and c.distance(corn) < min(c.distance(other), c.distance(scil)))
    inS = scil_reg.contains(c) or (not inC and c.distance(scil) < min(c.distance(other), c.distance(corn)))
    if other_reg.contains(c) and not inC:
        continue
    if not (inC or inS):
        continue
    if c.distance(EDDYSTONE) < 1500:
        continue
    ring = LineString(poly.buffer(-0.5).exterior.coords) if not poly.buffer(-0.5).is_empty and poly.buffer(-0.5).geom_type == "Polygon" else LineString(poly.exterior.coords)
    dj += 1
    cut(ring, "DRY-SCILLY" if (inS and not inC) else "DRY", dj, True)
    dry_km += ring.length / 1000
print("detached drying (LW-only) outlines:", dj, "km", round(dry_km, 1))

# --- ids + basic geometry ------------------------------------------------------------------------
gdf = gpd.GeoDataFrame(segments, geometry="geometry", crs=27700)
gdf["length_m"] = gdf.length.round(1)
ids = []
counters = {}
for r in gdf.itertuples():
    if r.group == "MAIN":
        counters["M"] = counters.get("M", 0) + 1
        ids.append(f"M{counters['M']:04d}")
    else:
        pre = {"ISLET": "I", "FRAG": "F", "SCILLY": "S", "DRY": "D", "DRY-SCILLY": "DS"}[r.group]
        ids.append(f"{pre}{int(r.piece):03d}-{int(r.idx_in_piece) + 1:02d}")
gdf["seg_id"] = ids
mid = gdf.geometry.interpolate(0.5, normalized=True)
gdf["mid_e"], gdf["mid_n"] = mid.x.round(1), mid.y.round(1)
lonlat = [T.transform(x, y) for x, y in zip(mid.x, mid.y)]
gdf["lon"] = [round(l[0], 5) for l in lonlat]
gdf["lat"] = [round(l[1], 5) for l in lonlat]
gdf["seq"] = range(1, len(gdf) + 1)

gdf.to_file(f"{OUT}/segments_raw.gpkg", driver="GPKG")
json.dump(log_unassigned, open(f"{OUT}/offshore_pieces_assignment.json", "w"), indent=1)
summ = gdf.groupby("group").agg(n=("seg_id", "count"), km=("length_m", lambda s: round(s.sum() / 1000, 1)), maxlen=("length_m", "max"), pieces=("piece", "nunique"))
print(summ)
print("TOTAL segments", len(gdf), "km", round(gdf.length_m.sum() / 1000, 1), "max seg len", gdf.length_m.max())
