#!/usr/bin/env python3
"""Workstream 7, step 4: cut the segment table into geographic batches for the qualitative review and
render a labelled map (OS vector data) plus a Sentinel-2 cloudless image for each batch.

Usage: 04_make_batches.py <raw_dir> <out_dir> <repo_root>
Outputs: <repo>/fishing/research/coastline/review/batch_NN.csv, batch_NN.png, batches.json
         <repo>/fishing/research/raw/coastline_review/batch_NN_s2.jpg (local only; EOX s2cloudless-2020, CC BY-NC-SA 4.0)
"""
import sys, glob, json, os, warnings, urllib.request, time
import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.spatial import cKDTree
from scipy.cluster.vq import kmeans2
from pyproj import Transformer
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
RAW, OUT, ROOT = sys.argv[1], sys.argv[2], sys.argv[3]
REV = f"{ROOT}/fishing/research/coastline/review"
IMG = f"{ROOT}/fishing/research/raw/coastline_review"
os.makedirs(REV, exist_ok=True); os.makedirs(IMG, exist_ok=True)
T = Transformer.from_crs(27700, 4326, always_xy=True)
df = pd.read_csv(f"{ROOT}/fishing/research/coastline/segments_scored.csv")
geo = gpd.read_file(f"{OUT}/segments_enriched.gpkg")[["seg_id", "geometry"]]
g = geo.merge(df, on="seg_id")
mid = g.geometry.interpolate(0.5, normalized=True)
g["mx"], g["my"] = mid.x, mid.y

MAIN_PER_BATCH = 25
main = g[g.group == "MAIN"].sort_values("seq")
g["batch"] = -1
g.loc[main.index, "batch"] = (np.arange(len(main)) // MAIN_PER_BATCH)
nmain = int(g.batch.max()) + 1
# Cornish non-mainland segments join the batch of the nearest mainland segment
kt = cKDTree(main[["mx", "my"]].values)
oth = g[g.group.isin(["FRAG", "ISLET", "DRY"])]
g.loc[oth.index, "batch"] = g.loc[main.index, "batch"].values[kt.query(oth[["mx", "my"]].values)[1]]
# Scilly: k-means clusters
sc = g[g.group.isin(["SCILLY", "DRY-SCILLY"])]
K = 12
np.random.seed(7)
cent, lab = kmeans2(sc[["mx", "my"]].values, K, minit="++", seed=7)
order = np.argsort(-cent[:, 1] + 0.0 * cent[:, 0])
remap = {int(o): i for i, o in enumerate(order)}
g.loc[sc.index, "batch"] = [nmain + remap[int(l)] for l in lab]
g["batch"] = g.batch.astype(int)
print("batches", g.batch.nunique(), "sizes min/median/max", g.groupby("batch").size().agg(["min", "median", "max"]).to_dict())

COLS = ["seg_id", "group", "lat", "lon", "length_m", "names_nearby", "nearest_place", "setting", "aspect_open_deg", "intertidal_width_m",
        "maxdepth_150m", "maxdepth_300m", "maxdepth_1000m", "dist_to_5m", "dist_to_10m", "dist_to_20m",
        "eusm_substrate_100m", "eusm_substrate_300m", "eusm_substrate_1000m", "eusm_nearest_substrate", "eusm_nearest_dist_m", "eusm_nearest_biozone", "eusm_nearest_energy",
        "dist_to_mapped_rock_m", "dist_to_mapped_sediment_m", "bedrock", "n_stream_mouths", "n_river_polys", "fetch_max_km", "n_dir_gt10km", "n_dir_gt100km",
        "ref_point", "tide_port", "Hs_near_00", "Hs_near_03", "Hs_near_06", "Hs_near_09", "Hs_near_12", "Hs_near_15", "Hs_near_18", "Hs_near_21",
        "onshore_00", "onshore_12", "onshore_18", "H_score", "H_guild", "P_score", "P_guild", "P_window", "P_tide_at_window", "known_marks_600m", "thin_data"]


def load(layer, areas=("SW", "SX", "SV", "SS")):
    fs = []
    for a in areas:
        p = glob.glob(f"{RAW}/oml_{a}/*/data/{a}_{layer}.shp")
        if p:
            fs.append(gpd.read_file(p[0]))
    return pd.concat(fs, ignore_index=True)


tb = load("TidalBoundary"); fo = load("Foreshore"); tw = load("TidalWater"); sw = load("SurfaceWater_Line"); npl = load("NamedPlace")
npl = npl[npl.CLASSIFICA.isin(["Hydrography", "Landform", "Populated Place"])]
meta = []
for b in sorted(g.batch.unique()):
    sub = g[g.batch == b].sort_values(["group", "seq"])
    sub[COLS].to_csv(f"{REV}/batch_{b:02d}.csv", index=False)
    minx, miny, maxx, maxy = sub.total_bounds
    pad = max(400.0, 0.06 * max(maxx - minx, maxy - miny))
    bx = (minx - pad, miny - pad, maxx + pad, maxy + pad)
    w, h = bx[2] - bx[0], bx[3] - bx[1]
    fig_w = 13.0; fig_h = max(6.0, min(13.0, fig_w * h / w))
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    cx = lambda d: d.cx[bx[0]:bx[2], bx[1]:bx[3]]
    c = cx(tw)
    if len(c): c.plot(ax=ax, color="#d6ecff", linewidth=0)
    c = cx(fo)
    if len(c): c.plot(ax=ax, color="#f1e3b5", linewidth=0)
    c = cx(sw)
    if len(c): c.plot(ax=ax, color="#3b7ddd", linewidth=0.6)
    c = cx(tb[tb.CLASSIFICA == "Low Water Mark"])
    if len(c): c.plot(ax=ax, color="#2f6fb0", linewidth=0.5, linestyle="--")
    c = cx(tb[tb.CLASSIFICA == "High Water Mark"])
    if len(c): c.plot(ax=ax, color="#888888", linewidth=0.5)
    sub.plot(ax=ax, column="P_score", cmap="turbo", vmin=0, vmax=90, linewidth=2.2, legend=True, legend_kwds={"label": "provisional P", "shrink": 0.5})
    for r in sub.itertuples():
        ax.annotate(r.seg_id, (r.mx, r.my), fontsize=5.5, color="black", ha="center", va="center", bbox=dict(fc="white", ec="none", alpha=0.75, pad=0.3))
    c = cx(npl)
    for r in c.itertuples():
        ax.annotate(str(r.DISTNAME), (r.geometry.x, r.geometry.y), fontsize=6 if r.CLASSIFICA != "Populated Place" else 7, color="#7a1fa2" if r.CLASSIFICA != "Populated Place" else "#b33", alpha=0.9)
    ax.set_xlim(bx[0], bx[2]); ax.set_ylim(bx[1], bx[3]); ax.set_aspect("equal")
    ax.set_title(f"Batch {b:02d}: {len(sub)} segments | blue = tidal water, tan = foreshore (dries), dashed = low-water mark, grey = high-water mark | grid = British National Grid (m)", fontsize=8)
    ax.tick_params(labelsize=6); ax.grid(alpha=0.25, linewidth=0.3)
    plt.tight_layout(); plt.savefig(f"{REV}/batch_{b:02d}.png", dpi=110); plt.close(fig)
    lo0, la0 = T.transform(bx[0], bx[1]); lo1, la1 = T.transform(bx[2], bx[3])
    s2 = f"{IMG}/batch_{b:02d}_s2.jpg"
    if not os.path.exists(s2):
        px_w = 1400; px_h = int(max(500, min(1400, px_w * h / w)))
        url = (f"https://tiles.maps.eox.at/wms?service=WMS&version=1.1.1&request=GetMap&layers=s2cloudless-2020&styles=&srs=EPSG:4326"
               f"&bbox={lo0:.5f},{la0:.5f},{lo1:.5f},{la1:.5f}&width={px_w}&height={px_h}&format=image/jpeg")
        for a in range(3):
            try:
                data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "coast-research/1.0"}), timeout=60).read()
                open(s2, "wb").write(data); break
            except Exception as e:
                time.sleep(3)
    names = [x.split(" [")[0] for x in ";".join(sub.names_nearby.dropna().astype(str)).split("; ") if x]
    top = pd.Series(names).value_counts().index[:6].tolist() if names else []
    meta.append(dict(batch=int(b), n=int(len(sub)), groups=sub.group.value_counts().to_dict(), lon=[round(lo0, 4), round(lo1, 4)], lat=[round(la0, 4), round(la1, 4)],
                     first=sub.seg_id.iloc[0], places=top, max_P=float(sub.P_score.max()), s2=os.path.exists(s2)))
g[["seg_id", "batch"]].to_csv(f"{REV}/segment_batches.csv", index=False)
json.dump(meta, open(f"{REV}/batches.json", "w"), indent=1)
print("done", len(meta), "batches; S2 images:", sum(m["s2"] for m in meta))
for m in meta[:3] + meta[-2:]:
    print(m["batch"], m["n"], m["places"][:4])
