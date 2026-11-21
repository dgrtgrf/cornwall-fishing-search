# Workstream 4 - Sea temperature and seasonal fish behaviour (Cornwall + Scilly, session Sun 22 Nov 2026)

STATUS: COMPLETE (first full version 2026-11-21 16:25 UTC). ADVERSARIALLY VERIFIED 16:25-17:00 UTC - inline "[CORRECTED by verifier ...]" / "[UNVERIFIED]" marks; see section 7 and "Verification log" at the end. Stub written 15:18 UTC (run 1, interrupted ~15:25); resumed 16:04 UTC (run 2) re-using the raw downloads in `fishing/research/raw/species_sst/`. Contents: 1 Sea temperature now | 2 Species catalogue (2.0 evidence base, 2.2 catalogue) | 3 Seasonal dynamics | 4 Condition sensitivities | 5 Ranking | 6 Gaps, contradictions, sources.
Source grades: A = official/instrument/primary; B = reputable secondary; C = anecdotal; D = own inference (reasoning shown).
All times UTC (= GMT = local). "Accessed" times are the fetch stamps in the raw filenames.

---------------------------------------------------------------------------------------------------
## 1. SEA TEMPERATURE NOW

### 1.1 Headline (D - synthesis of the A-grade rows below)
- Open-coast SST around mainland Cornwall on 21 Nov 2026 is **13.1-13.5 C by instrument** (CCO Datawell buoys, Sevenstones LV), Scilly **13.2 C** (St Mary's Sound buoy), i.e. practically uniform N coast / S coast / Scilly (spread <= 0.5 C). The only cooler instrument is Bideford Bay (N Devon, estuary-influenced, shallow) at 11.9-13.2 C in the last 48 h.
- **Anomaly sign: POSITIVE (warmer than normal)**. Size depends on baseline: +0.2 to +0.7 C vs MUR 2003-2014 climatology; +0.9 to +1.8 C vs NOAA CRW (1985-2012) and OISST (1971-2000) baselines; +0.5 to +0.7 C on seatemperature.org's "late-November average"; +0.3 to +1.3 C vs the same buoys on the same date last year (22 Nov 2025: 12.3-12.9 C).
- **Trend: falling fast** - about -4 C in the 6 weeks since 10 Oct on the mainland buoys (17.1 -> 13.2 C at Perranporth), about -1.0 C in the last 14 days, and the fall has flattened in the last 5 days (-0.1 to +0.1 C/day; mild SW/S air 11-14 C since 15 Nov).
- **Estuaries: no live in-estuary thermometer found (NOT FOUND - see 1.7)**. Inference (D): upper/mid estuaries are colder than the open coast (air frosts 8 and 12-13 Nov, Tmin -0.6 to -2.8 C at the estuary heads) and since 15-17 Nov carry 4-6x base river flow, with a further 22-48 mm of rain modelled for Sun 22 Nov itself.

### 1.2 Channel Coastal Observatory (CCO) Datawell Waverider buoys - sea temperature at the buoy hull (Grade A, instrument)
Source: https://coastalmonitoring.org/realtimedata/ (station pages 76 Perranporth, 75 Penzance, 107 Porthleven, 113 St Mary's Sound, 98 Looe Bay, 97 Bideford Bay, 82 Start Bay, 102 Port Isaac, 116 Wave Hub). Accessed 2026-11-21 15:18-15:19 UTC. Raw: `cco_*_day_20261121T1518Z.html`, `cco_buoys_halfhourly_sst_year_extracted_20261121T1519Z.json.gz`, derived daily means `cco_buoys_daily_mean_sst_22Nov2025_to_21Nov2026_derived.csv` (D: daily mean = arithmetic mean of the half-hourly values, my derivation).

Latest half-hourly reading and 48 h range:
| Buoy (position) | Coast | Latest reading (UTC) | SST C | 48 h min-max C |
|---|---|---|---|---|
| Perranporth (50.354N 5.174W) | North | 21 Nov 14:30 | 13.2 | 13.0-13.3 |
| Penzance (50.113N 5.501W) | South (Mount's Bay) | 21 Nov 14:30 | 13.5 | 13.3-13.7 |
| Porthleven (50.063N 5.307W) | South (Mount's Bay E) | 21 Nov 14:30 | 13.1 | 12.7-13.4 |
| Looe Bay (50.339N 4.411W) | South-east | 21 Nov 14:00 | 13.3 | 13.1-13.6 |
| St Mary's Sound (49.892N 6.312W) | Scilly | 21 Nov 14:30 | 13.2 | 13.1-13.3 |
| Bideford Bay (51.059N 4.277W) | N Devon (reference for Bude) | 21 Nov 14:00 | 13.2 | 11.9-13.2 |
| Start Bay (50.293N 3.616W) | S Devon (reference) | 21 Nov 14:00 | 13.8 | 13.1-13.9 |
| Port Isaac | North | - | NO SST (temperature column is "-" for the whole year) | - |
| Wave Hub | North (offshore Hayle) | - | NO CURRENT DATA (page serves 2018 data) | - |

Daily-mean trend (C), my derivation from the half-hourly series:
| Date | Bideford Bay | Perranporth | Penzance | Porthleven | St Mary's Sd | Looe Bay | Start Bay |
|---|---|---|---|---|---|---|---|
| 15 Sep 2026 | 18.62 | 18.25 | 17.07 | 17.17 | 15.97 | 17.57 | 17.99 |
| 01 Oct | 17.90 | 17.90 | 16.97 | 16.90 | 15.69 | 17.41 | 17.97 |
| 10 Oct (6 wk ago) | 17.08 | 17.17 | 16.10 | 16.34 | 15.38 | 16.90 | 17.36 |
| 17 Oct | 16.97 | 16.88 | 16.04 | 15.94 | 15.27 | 16.60 | 16.90 |
| 24 Oct (4 wk ago) | 15.30 | 15.42 | 15.09 | 14.73 | 14.52 | 15.50 | 15.70 |
| 31 Oct | 15.19 | 14.27 | 14.48 | 14.46 | 14.10 | 14.92 | 15.16 |
| 07 Nov (2 wk ago) | 14.52 | 14.28 | 13.67 | 14.02 | 13.80 | 14.10 | 14.57 |
| 10 Nov | 14.02 | 14.24 | 13.87 | 14.10 | 13.75 | 13.92 | 14.57 |
| 12 Nov | 13.94 | 13.87 | 13.77 | 14.04 | 13.64 | 13.87 | 14.16 |
| 14 Nov (1 wk ago) | 13.50 | 13.38 | 13.37 | 13.74 | 13.49 | 13.36 | 13.69 |
| 16 Nov | 13.14 | 13.04 | 13.34 | 13.67 | 13.42 | 13.42 | 13.50 |
| 18 Nov | 12.37 | 12.96 | 13.62 | 13.45 | 13.35 | 13.63 | 13.60 |
| 19 Nov | 12.35 | 13.03 | 13.59 | 13.27 | 13.21 | 13.41 | 13.45 |
| 20 Nov | 12.30 | 13.10 | 13.65 | 13.20 | 13.18 | 13.44 | 13.63 |
| 21 Nov (to ~14:30) | 12.75 | 13.19 | 13.54 | 13.07 | 13.18 | 13.35 | 13.60 |
| **Same buoys 22 Nov 2025** | 12.67 | 12.47 | 12.26 | 12.94 | 12.94 | 12.87 | 12.78 |
| 22 Dec 2025 (what +1 month looks like) | 11.25 | 11.61 | 11.41 | 11.82 | 12.02 | 11.59 | n/a |
| 15 Feb 2026 | 9.01 | 10.15 | 9.93 | 10.20 | 11.03 | 10.11 | 9.87 |
Annual extremes in the series (22 Nov 2025-21 Nov 2026): Perranporth max 19.59 (10 Aug 2026) / min 9.34 (8 Jan 2026); Penzance 19.89 (17 Jul) / 9.48 (18 Jan); Porthleven 20.29 (24 Jul) / 9.73 (19 Jan); Looe Bay 20.00 (16 Jul) / 9.32 (17 Jan); St Mary's Sound 18.93 (11 Aug) / 10.89 (29 Mar); Bideford Bay 20.10 (24 Jul) / 8.55 (10 Jan).
Observations (A): (i) 6-week fall 10 Oct -> 21 Nov: Perranporth -3.98, Penzance -2.56, Porthleven -3.27, Looe -3.55, Scilly -2.20, Bideford -4.3 C. (ii) 14-day fall 7 -> 21 Nov: Perranporth -1.09, Penzance -0.13, Porthleven -0.96, Looe -0.75, Scilly -0.62 C. (iii) Year-on-year vs 22 Nov 2025: Perranporth +0.72, Penzance +1.28, Porthleven +0.12, Looe +0.49, Scilly +0.24 C. (iv) Scilly had the coolest summer and has the slowest autumn cooling (deep, well-mixed shelf water) - it is now level with the mainland; by Dec-Feb it is 0.4-1 C WARMER than the mainland (12.0 vs 11.4-11.8 on 22 Dec 2025; 11.0 vs 9.9-10.2 on 15 Feb 2026).
Caveat (D): the Penzance series shows a +0.3 C step up after 16 Nov while Porthleven (15 km away) fell 0.6 C - within-bay differences of that size are real (river plume / mixing) or sensor drift; treat +-0.3 C as the practical uncertainty of any one buoy.

### 1.3 Light vessels / moored buoys via NOAA NDBC (Grade A, instrument; UK Met Office platforms relayed by NDBC)
Source: https://www.ndbc.noaa.gov/data/realtime2/<id>.txt, accessed 2026-11-21 15:20 and 16:05 UTC (files hold only the last ~25 h for these platforms). Raw: `ndbc_*_realtime2_*.txt`.
| Platform | Where | Latest obs (UTC) | Water temp C | Air temp C | Note |
|---|---|---|---|---|---|
| 62107 Sevenstones LV | between Land's End and Scilly (approx 50.1N 6.1W) | 21 Nov 15:00 | **13.1** | 12.8 (14:00) | 20 Nov mean 13.19, 21 Nov mean 13.07; Hs 1.3 m at 14:00, 3.2 m at 14:00 on 20 Nov |
| 62050 (E1, W Channel off Plymouth ~50.0N 4.4W) | S coast offshore | 21 Nov 15:00 | 13.9 | 13.4 | flat 13.9 for 25 h |
| 62103 Channel LV | mid-Channel (49.9N 2.9W) | 21 Nov 15:00 | 14.3 | 11.9 | reference only |
| 62029 K1 | SW Approaches (48.7N 12.4W) | 21 Nov 14:00 | 14.6 | 14.3 | oceanic source water; pressure 995 hPa and falling |
| 62163 Brittany | 47.5N 8.5W | 21 Nov 14:00 | 15.0 | 14.4 | reference only |
Station identities/positions for 62050/62029/62163 are from memory of the NDBC/Met Office station list (D) - not re-verified today. [CORRECTED by verifier: was "not re-verified" - NDBC station pages fetched 2026-11-21 16:25 UTC (raw `species_sst_verify/ndbc_station_*_20261121T1625Z.html`) confirm 62107 = "Sevenstones Lightship" 50.102N 6.100W, 62050 = "E1" 50.000N 4.400W, 62103 = "Channel Lightship" 49.900N 2.900W. 62029/62163 positions still UNVERIFIED.]
[Verifier note: the "20 Nov mean 13.19" for 62107 is the mean of only the 9 hourly obs 15-23Z on 20 Nov that the realtime2 file still held, not a full-day mean.]

### 1.4 Satellite / blended analyses at the STANDARD REFERENCE POINTS (Grade A products; nearest valid sea pixel = my extraction, D)
Sources (all via NOAA CoastWatch ERDDAP https://coastwatch.pfeg.noaa.gov/erddap/griddap/, accessed 2026-11-21 15:21 UTC):
- JPL MUR v4.1 analysed SST, 0.01 deg, data date **20 Nov 2026 09:00Z** (`jplMURSST41`), anomaly product `jplMURSST41anom1day` data date **19 Nov 2026** (baseline: MUR climatology 2003-2014).
- NOAA Coral Reef Watch daily 5 km `NOAA_DHW` CRW_SST and CRW_SSTANOMALY, data date **19 Nov 2026 12:00Z** (baseline 1985-2012).
- NOAA OISST v2.1 NRT 0.25 deg `ncdcOisst21NrtAgg_LonPM180` sst and anom, data date **18 Nov 2026 12:00Z** (baseline 1971-2000).
- Open-Meteo Marine API `sea_surface_temperature` (https://marine-api.open-meteo.com/v1/marine, cell_selection=sea, ~8 km grid; accessed 15:17 UTC; the product is a model/analysis SST, grade A model output). Raw: `openmeteo_marine_sst_refpoints_past92_20261121T1517Z.json`.

| Reference point | MUR 20 Nov | MUR anom 19 Nov | CRW 19 Nov | CRW anom | OISST 18 Nov | OISST anom | Open-Meteo 21 Nov 15Z | OM fcst 22 Nov 12Z | OM 14 Nov | OM 24 Oct | OM 10 Oct |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bude | 13.16 | +0.58 | 13.64 | +1.44 | 14.26 | +1.85 | 13.7 | 13.6 | 14.2 | 15.7 | 17.1 |
| Tintagel Head | 13.45 | +0.48 | 13.78 | +1.56 | 14.20 | +1.81 | 13.7 | 13.6 | 14.3 | 15.5 | 16.9 |
| Port Isaac | 13.31 | +0.44 | 13.87 | +1.65 | 14.20 | +1.81 | 13.3 | 13.4 | 14.4 | 15.3 | 16.7 |
| Stepper Point | 13.12 | +0.74 | 13.95 | +1.75 | 14.20 | +1.81 | 13.2 | 13.3 | 14.4 | 15.1 | 16.6 |
| Trevose Head | 12.93 | +0.60 | 13.91 | +1.75 | 14.15 | +1.82 | 13.3 | 13.2 | 14.2 | 15.1 | 16.3 |
| Newquay Towan Head | 12.86 | +0.22 | 13.74 | +1.61 | 14.02 | +1.64 | 13.2 | 13.1 | 13.9 | 15.1 | 16.2 |
| Perranporth | 12.90 | +0.30 | 13.60 | +1.49 | 14.02 | +1.64 | 13.1 | 13.1 | 13.8 | 15.0 | 16.1 |
| St Agnes Head | 12.97 | +0.28 | 13.50 | +1.38 | 14.02 | +1.64 | 13.1 | 13.0 | 13.7 | 15.0 | 16.1 |
| Godrevy | 13.13 | +0.37 | 13.40 | +1.26 | 14.01 | +1.63 | 13.0 | 12.9 | 13.5 | 14.9 | 16.0 |
| St Ives Head | 13.14 | +0.40 | 13.41 | +1.25 | 14.01 | +1.63 | 13.0 | 13.0 | 13.5 | 14.9 | 16.0 |
| Pendeen Watch | 13.24 | +0.41 | 13.45 | +1.26 | 13.93 | +1.59 | 13.3 | 13.4 | 14.0 | 14.9 | 16.2 |
| Cape Cornwall | 13.24 | +0.41 | 13.50 | +1.30 | 13.93 | +1.59 | 13.3 | 13.4 | 14.0 | 14.9 | 16.2 |
| Land's End | 13.21 | +0.45 | 13.57 | +1.34 | 13.93 | +1.59 | 13.4 | 13.4 | 14.2 | 14.8 | 16.2 |
| Gwennap Head | 13.21 | +0.45 | 13.68 | +1.43 | 13.93 | +1.59 | 13.4 | 13.4 | 14.2 | 14.8 | 16.2 |
| Newlyn/Penzance | 13.10 | +0.45 | 13.59 | +1.31 | 13.93 | +1.59 | 13.4 | 13.3 | 13.6 | 14.8 | 16.4 |
| Marazion | 13.10 | +0.45 | 13.62 | +1.33 | 14.01 | +1.63 | 13.5 | 13.3 | 14.0 | 14.9 | 16.5 |
| Porthleven/Loe Bar | 12.94 | +0.44 | 13.78 | +1.47 | 14.01 | +1.63 | 13.6 | 13.8 | 14.3 | 15.0 | 16.6 |
| Mullion | 12.90 | +0.40 | 13.80 | +1.47 | 14.01 | +1.63 | 13.6 | 13.8 | 14.3 | 15.0 | 16.6 |
| Lizard Point | 13.16 | +0.41 | 13.82 | +1.45 | 14.08 | +1.58 | 13.7 | 13.9 | 14.7 | 15.0 | 16.7 |
| Coverack/Manacles | 13.18 | +0.45 | 13.78 | +1.35 | 14.07 | +1.63 | 14.1 | 14.1 | 14.5 | 15.2 | 17.0 |
| Helford mouth | 13.12 | +0.45 | 13.77 | +1.34 | 14.07 | +1.63 | 13.9 | 14.0 | 14.3 | 15.0 | 16.9 |
| Falmouth Pendennis | 13.12 | +0.45 | 13.76 | +1.34 | 14.07 | +1.63 | 14.1 | 13.9 | 14.1 | 15.3 | 17.0 |
| Carrick Roads | 13.12 | +0.44 | 13.75 | +1.33 | 14.07 | +1.63 | 13.7 | 13.2 | 13.5 | 15.1 | 16.9 |
| Nare Head | 13.15 | +0.44 | 13.77 | +1.33 | 14.15 | +1.66 | 13.7 | 13.2 | 13.5 | 15.1 | 16.9 |
| Dodman Point | 13.24 | +0.46 | 13.81 | +1.35 | 14.15 | +1.66 | 13.9 | 13.9 | 14.4 | 15.3 | 17.0 |
| Mevagissey | 13.16 | +0.50 | 13.81 | +1.36 | 14.15 | +1.66 | 13.9 | 13.9 | 14.4 | 15.3 | 17.0 |
| Par | 13.02 | +0.51 | 13.81 | +1.37 | 14.11 | +1.55 | 13.6 | 13.5 | 13.5 | 15.3 | 17.0 |
| Fowey mouth | 13.13 | +0.52 | 13.83 | +1.39 | 14.11 | +1.55 | 14.0 | 14.0 | 14.3 | 15.6 | 17.0 |
| Polperro | 13.30 | +0.44 | 13.86 | +1.42 | 14.11 | +1.55 | 14.1 | 14.1 | 14.4 | 15.7 | 17.0 |
| Looe | 13.19 | +0.43 | 13.86 | +1.42 | 14.11 | +1.55 | 13.6 | 13.5 | 13.8 | 15.5 | 16.8 |
| Whitsand Bay | 13.08 | +0.28 | 13.87 | +1.41 | 14.11 | +1.55 | 13.6 | 13.5 | 13.9 | 15.3 | 16.9 |
| Rame Head | 13.28 | +0.20 | 13.91 | +1.44 | 14.11 | +1.55 | 14.2 | 14.1 | 14.5 | 15.9 | 17.1 |
| Saltash (Tamar) | 13.11* | +0.25* | 13.90* | +1.45* | 14.11* | +1.55* | 13.4* | 13.5* | 13.8* | 15.0* | 17.0* |
| St Mary's Hugh Town | 12.74 | +0.35 | 13.11 | +1.06 | 13.29 | +0.98 | 13.0 | 13.0 | 13.8 | 14.2 | 16.1 |
| St Agnes/Western Rocks | 12.67 | +0.30 | 12.98 | +0.96 | 13.29 | +0.98 | 12.9 | 13.0 | 13.7 | 14.2 | 16.1 |
| Bishop Rock | 12.75 | +0.20 | 12.93 | +0.93 | 13.29 | +0.98 | 12.9 | 12.9 | 13.6 | 14.0 | 16.1 |
| St Martin's | 12.84 | +0.41 | 13.14 | +1.09 | 13.29 | +0.98 | 13.0 | 13.0 | 13.6 | 14.1 | 16.0 |
| Wolf Rock | 13.06 | +0.43 | 13.59 | +1.38 | 13.67 | +1.29 | 13.3 | 13.3 | 14.3 | 14.5 | 16.1 |
| Longships | 13.19 | +0.43 | 13.57 | +1.34 | 13.93 | +1.59 | 13.4 | 13.4 | 14.2 | 14.8 | 16.2 |
(*) Saltash and Carrick Roads values are the nearest OPEN-SEA pixel (Plymouth Sound approaches / Falmouth Bay), NOT estuary water - none of these products resolves the estuaries. Open-Meteo cell centres used are in the raw JSON (e.g. "Saltash" resolved to 50.292N 4.208W = off Rame Head). [Verifier addition, from the same raw JSON: "Helford mouth" resolved to 49.958N 5.125W (~15 km S, off the Lizard east coast), "Falmouth Pendennis" to 50.125N 4.875W (~12 km ESE, mid Falmouth Bay/offshore), and "Carrick Roads" to 50.208N 4.875W - the SAME cell as "Nare Head". So the Open-Meteo columns for Helford, Falmouth and Carrick Roads are offshore water, not local, and the apparent 13.9-14.1 C "SE-coast warmth" at those rows is partly a cell-placement artefact (D).]

DISAGREEMENTS (recorded, not averaged):
1. Absolute level: MUR (20 Nov) 12.7-13.5 C and Open-Meteo 12.9-14.2 C bracket the buoys (13.1-13.5); CRW (19 Nov) is ~0.4-0.7 C warmer than buoys (13.4-13.9); OISST (18 Nov, coarse 0.25 deg, 3 days old) is ~0.7-1.0 C warmer (13.3-14.3). Part is real cooling between 18 and 21 Nov (buoys fell 0-0.4 C), part is product bias. Buoys are preferred (instrument, same day).
2. Anomaly size: MUR +0.2..+0.7 C; CRW +0.9..+1.75 C; OISST +1.0..+1.85 C. Different baselines (2003-2014 vs 1985-2012 vs 1971-2000) explain most of it: the sea here has warmed, so older baselines give bigger anomalies. All agree on the SIGN (positive everywhere, largest on the N coast Port Isaac-Trevose, smallest at Scilly).
3. South coast vs north coast: Open-Meteo shows the S coast east of the Lizard 0.5-1.0 C warmer (13.6-14.2) than the N coast (13.0-13.7); buoys show only 0.1-0.3 C (Looe 13.3, Penzance 13.5 vs Perranporth 13.2); MUR shows no N/S difference at all. E1 buoy 62050 offshore of Plymouth reads 13.9 (supports Open-Meteo for water a few miles OFF the south-east coast; inshore buoys are cooler).
4. Scilly: satellites say Scilly is 0.3-0.6 C cooler than Land's End (12.7-13.1); St Mary's Sound buoy (13.2) and Sevenstones (13.1) say it is the same as the mainland. Buoy preferred.

### 1.5 Climatology and anomaly (late November)
| Baseline | Implied late-Nov normal (C) | Today minus normal | Grade |
|---|---|---|---|
| OISST 1971-2000 (sst minus anom at the Land's End cell, 18 Nov) | 12.34 | +1.59 (product) ; buoy-based: 13.1-13.4 minus 12.34 = +0.8 to +1.1 | A product / D subtraction |
| CRW 1985-2012 (Land's End pixel, 19 Nov) | 12.23 | +1.34 (product); buoy-based +0.9 to +1.2 | A / D |
| MUR 2003-2014 (Land's End pixel) | ~12.75 (13.2 minus 0.45; MUR SST is 20 Nov, anom 19 Nov, so approximate) | +0.45 (product) | A / D |
| seatemperature.org "average sea temperature in late November" (pages accessed 2026-11-21 16:06 UTC; raw `seatemperature_org_*_20261121T1606Z.html`; the site's data source and baseline period are not stated on the extract I read - not verified) | Bude 12.8; Padstow 12.7; Newquay 12.7; St Ives 12.7; Penzance 12.6; Falmouth 12.7; Looe 12.9; Hugh Town 12.2 | "today's reading" Bude 13.1 (+0.3); Padstow 13.2 (+0.5); Newquay 13.2 (+0.5); St Ives 13.3 (+0.6); Penzance 13.3 (+0.7); Falmouth 13.6 (+0.9); Looe 13.6 (+0.7); Hugh Town 12.8 (+0.6) [Verifier: values re-extracted from the raw pages and confirmed. BUT each page's "Live data from ..." line is simply a relayed CCO buoy (Bude page -> Bideford Bay 12.8; Padstow/Newquay/Falmouth pages -> Perranporth, a NORTH-coast buoy even for Falmouth; St Ives/Penzance -> Penzance; Looe -> Looe Bay; Hugh Town -> St Mary's Sound), so this site is NOT an independent SST observation; its headline "today" numbers are an unstated model/satellite product. Grade C for the headline values.] | B |
| Same CCO buoys, 22 Nov 2025 | 12.26-12.94 | +0.1 to +1.3 (Penzance largest) | A |
Statement: **SST is about 0.5-1 C above the recent (2003-2014-type) late-November normal and ~1-1.5 C above the 1971-2000/1985-2012 normals; sign positive on every product and every coast.** In calendar terms (D): at the last fortnight's cooling rate (about -1.0 C per 14 days at Perranporth/Porthleven, 7 -> 21 Nov) a +0.5 to +1 C anomaly equals 1-2 weeks; at the slower rate the same buoys showed from 22 Nov to 22 Dec 2025 (-0.85 to -1.25 C in 30 days) it equals 2-4 weeks. So the sea is running roughly 1-3 weeks "late" - conditions are those of a typical early-to-mid November. (I have no buoy data from before 22 Nov 2025, so I cannot say on what date last year passed 13.2-13.5 C.)

### 1.6 Recent air temperature, frost, rain and river flow (drivers of estuary cooling)
Air temperature and rain - Open-Meteo forecast API "best match" with past_days=31 (model analysis + forecast, Grade A model output; model run time not stated by the API; https://api.open-meteo.com/v1/forecast; accessed 2026-11-21 16:05 UTC; raw `openmeteo_air_estuary_past31_20261121T1605Z.json`). Daily Tmin / Tmax (C) / precipitation (mm):
| Date | Saltash (Tamar) | Wadebridge (Camel) | Truro (Fal) | Lostwithiel (Fowey) | Gweek (Helford) | St Mary's |
|---|---|---|---|---|---|---|
| 08 Nov | 2.2/12.9/0 | -0.1/12.6/0 | 2.2/12.8/0 | -0.6/12.1/0 | 3.2/13.4/0 | 11.0/13.8/0 |
| 12 Nov | 2.1/9.6/0 | 0.9/8.9/0 | 2.2/9.3/0 | 0.6/8.6/0 | 3.5/10.0/0 | 9.7/12.0/0 |
| 13 Nov | -0.6/9.6/0 | -2.8/9.7/0 | -0.6/9.6/0 | -2.0/9.3/0 | 2.4/9.9/0 | 8.7/11.3/0 |
| 14 Nov | 2.8/11.4/0 | 1.0/11.0/0 | 5.5/10.7/0.1 | 2.2/10.6/0.1 | 5.4/10.5/0.3 | 10.8/11.9/0.3 |
| 15 Nov | 8.5/12.3/6.0 | 7.7/12.2/11.4 | 8.8/12.2/9.1 | 7.5/11.6/14.2 | 8.6/12.1/10.1 | 11.1/13.1/4.6 |
| 16 Nov | 7.7/14.6/10.8 | 6.6/14.6/5.8 | 7.5/14.7/8.5 | 5.8/14.4/13.4 | 7.2/14.6/6.5 | 10.6/14.6/6.3 |
| 17 Nov | 10.4/14.6/11.4 | 10.6/14.4/9.5 | 10.1/14.5/10.1 | 10.1/14.3/6.2 | 9.7/14.4/16.7 | 11.3/14.3/8.7 |
| 18 Nov | 8.4/13.6/4.7 | 8.4/13.0/9.0 | 9.0/13.2/7.5 | 7.6/13.2/6.1 | 9.1/13.3/7.5 | 10.6/13.5/11.9 |
| 19 Nov | 8.5/12.2/7.0 | 9.0/12.1/9.4 | 8.9/12.1/11.7 | 8.0/11.8/7.9 | 9.3/12.5/8.9 | 10.9/13.0/6.4 |
| 20 Nov | 9.2/11.7/8.3 | 4.7/11.5/13.8 | 5.7/12.0/9.1 | 5.1/11.2/16.3 | 5.4/11.7/5.1 | 11.4/13.0/5.4 |
| 21 Nov | 8.2/13.1/0 | 3.9/12.6/0 | 3.2/12.4/2.3 | 2.0/12.3/0.2 | 3.0/12.5/3.3 | 11.8/13.2/9.2 |
| **22 Nov (forecast)** | 10.5/11.9/**47.7** | 10.9/12.2/**21.8** | 11.2/12.6/**23.4** | 10.5/12.0/**43.1** | 10.3/12.6/**26.2** | 11.5/13.0/6.8 |
[Verifier cross-check of the 22 Nov rain, MET Norway locationforecast 2.0 compact (Grade A model output; model run "updated_at" 2026-11-21 13:17 UTC; fetched 16:55 UTC; raw `species_sst_verify/metno_*_20261121T1655Z.json`; hourly amounts summed 00-23 UTC 22 Nov, my arithmetic): Lostwithiel ~28.5 mm, Saltash ~29.3 mm, Truro ~16.2 mm, Wadebridge ~25.4 mm - DISAGREES with the Open-Meteo best-match values above (43.1 / 47.7 / 23.4 / 21.8 mm); recorded, not averaged. Open-Meteo could not be re-fetched (HTTP "Daily API request limit exceeded" at 16:25 UTC). MET Norway puts most of the rain between ~00 and 09 UTC on 22 Nov, little after midday. Both models agree on a wet night/morning; the 22-48 mm figure is the upper end.]
31-day summary (21 Oct-21 Nov): lowest Tmin -2.8 C Wadebridge, -2.0 Lostwithiel, -1.7 Bude, -0.6 Saltash/Truro, all on 13 Nov; air-frost nights (Tmin <= 0): Wadebridge 2, Lostwithiel 2, others 1, Gweek 0, Scilly 0 (Scilly minimum 8.7 C). Rain 31 d: 123-171 mm; last 7 d: 44-64 mm.
River flow - Environment Agency real-time flood-monitoring API (Grade A instrument; https://environment.data.gov.uk/flood-monitoring/id/stations/<id>/readings; accessed 2026-11-21 16:05 UTC; raw `ea_flow_*_20261121T1605Z.json`). Daily mean flow m3/s (my means of 15-min values):
| Station (river) | 8-14 Nov base | 17 Nov | 18 Nov | 19 Nov | 20 Nov | 21 Nov (part) | Latest 15-min | Ratio now/base |
|---|---|---|---|---|---|---|---|---|
| Restormel (Fowey) | 1.87-2.44 | 6.91 | 5.87 | 5.84 | 11.86 | 9.30 | 8.92 @15:45 | ~4.5x (peak 16.0) |
| Gwills (Gannel) | 0.12-0.21 | 1.40 | 0.69 | 1.05 | 1.24 | 0.71 | 0.66 @15:45 | ~5x (peak 3.5) |
| St Erth (Hayle) | 0.26-0.31 | 0.73 | 0.62 | 0.69 | 0.80 | 0.76 | 0.76 @15:30 | ~2.8x |
| Trebrownbridge (Seaton) | 0.46-0.58 | 1.60 | 1.40 | 1.51 | 2.17 | 2.16 | 2.07 @15:45 | ~4x |
| Helston County Bridge (Cober -> Loe Pool) | 0-0.29 | 1.03 | 0.66 | 0.90 | 1.15 | 0.84 | 0.74 @15:30 | - |
| Tamarstone Bridge (upper Tamar) | 0.29-0.45 | 6.41 | 3.68 | 5.92 | 6.84 | 3.55 | 3.06 @15:15 | ~8x (peak 7.3) |
NOT FOUND: live flow for Tamar at Gunnislake, Camel at Denby, Fal at Tregony (not in the EA flood-monitoring "flow" station list returned for a 75 km radius of 50.4N 4.8W; the sea-state stream holds EA level data).
Inference (D): rivers went from late-autumn base flow to a 3-8x spate between 15 and 20 Nov and are only part-way down the recession; the model puts another 22-48 mm on the catchments on 22 Nov. Estuaries on the session day will be: coloured, low-salinity in their upper and middle reaches (strong surface freshwater lens on the ebb), and cooler than the sea. River water temperature is unmeasured here; with mean air 8-12 C over the last week it is probably ~9-11 C (D, THIN DATA) vs 13.1-13.5 C sea - i.e. the freshwater is 2-4 C colder than the salt wedge, so warmth AND salinity both increase toward the mouths. This favours estuary MOUTHS / lower reaches over upper reaches for every species except flounder (which tolerate fresh water) and makes the flood tide (salt wedge pushing in) the better half.

### 1.7 Gaps in section 1
- NOT FOUND: Cefas WaveNet / SmartBuoy SST for Cornwall (not attempted beyond the CCO/NDBC set - CCO buoys are the WaveNet-relayed sites for this coast; no separate Cefas SmartBuoy operates off Cornwall as far as I could establish - D, not verified).
- NOT FOUND: any real-time water temperature inside the Tamar, Fal, Helford, Fowey, Camel, Hayle or Gannel estuaries (EA flood-monitoring API carries level/flow/rain only; Western Channel Observatory L4/E1 pages not fetched; E1 is covered by NDBC 62050).
- NOT FOUND: Met Office OSTIA direct download (requires Copernicus Marine login); MUR, CRW and OISST used instead.
- Port Isaac and Wave Hub CCO buoys carry no usable SST.

---------------------------------------------------------------------------------------------------
## 2. SPECIES CATALOGUE - EVIDENCE BASE FIRST

### 2.0 Cornish club / federation records used as the primary "what is actually caught from the Cornish shore in Nov-Dec" evidence
(Raw files were downloaded by the intel stream at 15:19-15:21 UTC 21 Nov 2026 into `fishing/research/raw/intel_shops_clubs/`; I re-parsed them myself at ~16:08-16:12 UTC. Neither source gives the venue of individual fish - THIN DATA on "where".)

**(a) Mount's Bay Angling Society (Penzance) monthly Fish Recorder sheets** - https://mountsbay.weebly.com/ (uploads/1/2/7/9/12797807/fish_recorders_report_<month>_<year>.xls[x]); Grade B (club recorder, fish photographed/weighed; catch-and-release weights in kg). Senior SHORE returns for the month (date, species, kg); [B] = boat, shown for context only. These are only fish that a member bothered to register (>= roughly 30-40 % of club specimen weight), so they under-count small common fish (whiting, pouting, rockling, dogfish).
- **Nov 2023**: 12 Nov small-eyed ray 3.856; 8 Nov small-eyed ray 3.200; 12 Nov ballan wrasse 2.041; 16 Nov LSD 1.145, 1.029; 22 Nov LSD 0.985; 6 Nov mackerel 0.575; 16 Nov whiting 0.480; 12 Nov whiting 0.360; 8 Nov turbot 0.570. [B 22 Nov bass 2.502, scad 0.539]
- **Nov 2024**: LSD x7 (0.800-1.255; 8, 8, 12, 16, 17, 17, 26 Nov); 11 Nov conger 6.650; bass 26 Nov 1.540, 19 Nov 1.280, 2 Nov 0.840, 20 Nov 0.745; 17 Nov whiting 0.250; 12 Nov tub gurnard 0.110. [B 15 Nov spurdog 8.900]
- **Nov 2025**: sheet not parseable (.numbers) - NOT EXTRACTED (the intel stream took Nov 2025 from the club news log; see `intel/shops_clubs_matches.md` 1c).
- **Dec 2023**: whiting x6 (0.425-0.747; 15 and 29 Dec); LSD 0.997, 0.992; bull huss 4.230 (29 Dec); mackerel 0.375, 0.345 (29 Dec).
- **Dec 2024**: bull huss 5.050 (29 Dec); small-eyed ray 3.540 and 2.940 (29 Dec); thornback ray 2.800 (29 Dec); bass 2.300 (15 Dec), 1.885 (23 Dec); LSD x8 (0.900-1.205); whiting x4 (0.354-0.625); mackerel x4 (0.383-0.515, 29 Dec); flounder 0.475 (23 Dec); thick-lipped mullet 1.545 (29 Dec).
- **Dec 2025**: bull huss 5.975 (29 Dec, 109.8 % of club specimen); small-eyed ray 4.060 (28 Dec); bass 2.720 (6 Dec); LSD x5 (0.830-1.270); whiting x5 (0.370-0.605); flounder 0.625 (7 Dec).
- **Oct 2026 (latest sheet)**: bass 3.120 (31 Oct), 3.026 (20 Oct), 2.150 (21 Oct), 2.140 (31 Oct), 1.850 (18 Oct), 1.700 (31 Oct), 1.420 (30 Oct); ballan wrasse 2.325 (5 Oct), 1.480, 1.390 (18 Oct); corkwing wrasse 0.380 (5 Oct); Couch's bream 0.500 (3 Oct); pollack 1.930 (5 Oct); LSD 0.980; bull huss 4.100 (19 Oct); small-eyed ray 2.360 (19 Oct).
- **Sep 2026 (contrast - what has ALREADY dropped out of the returns by late Oct)**: triggerfish 2.300, 1.520, 0.535; Couch's bream x4; black bream x5; thin-lipped mullet x6; gilthead bream 1.559, 1.021; red mullet 0.510; garfish x3; plaice 0.360; pollack 4.100; cuckoo wrasse; mackerel x3.
- 1-16 Nov 2026 (club news log, via intel stream table 1a): bass 3.060 + 2.110 (16 Nov, night), 2.320 (6 Nov), 1.690 (4 Nov); pollack 3.120 (2 Nov), 2.555 (5 Nov), 1.245 (7 Nov); ballan wrasse 1.255 (5 Nov); three-bearded rockling 0.570 (2 Nov); LSD 1.130 (1 Nov). [Verifier: all weights confirmed in grams in raw `mbas_latest-news-2026_20261121T1520Z.html` ("A good nights fishing ... Will Harvey, Bass 3060g and 2110g 16/11"). Only the 5783g spurdog is explicitly labelled "Boat"; the log does NOT explicitly label the others as shore - shore status of these news-log fish is inferred, UNVERIFIED. "16/11" may be the posting date for a night of 15-16 Nov.]
Observation (B data, my tally by script): across the FIVE parseable sheets (Nov 2023, Nov 2024, Dec 2023, Dec 2024, Dec 2025; 70 senior-shore entries) the species counts are: LSD 24, whiting 17, mackerel 7, bass 7, small-eyed ray 5, bull huss 3, flounder 2, conger 1, thornback 1, ballan wrasse 1, turbot 1, tub gurnard 1 (plus 1 thick-lipped mullet and a few entries in separate 'Returns' blocks). No pollack, coalfish, cod, squid, bream, garfish or triggerfish were registered in those five sheets (pollack DO appear in the 2026 November news log). [Verifier: individual entries spot-checked and confirmed (Nov 2023 small-eyed ray 3.856 kg 12 Nov / 3.200 kg 8 Nov; Dec 2025 bull huss 5.975 kg 109.8 %, bass 2.720 kg 6 Dec, small-eyed ray 4.060 kg 28 Dec; Oct 2026 bass 3.120/3.026/2.150/2.140/1.850/1.700/1.420 kg); the 70-entry species TALLY itself was not re-derived - UNVERIFIED.]

**(b) Cornish Federation of Sea Anglers (CFSA) Annual Recorder's Reports 2023, 2024, 2025 and 2026 shore updates** - https://cornishfed.weebly.com/ ; Grade B (county federation recorder Simon Toms; weighed fish from 5 member clubs; 491 shore specimens from 73 anglers and 31 species in 2025). Weights lb-oz-dr.
Shore "Fish of the Month" - what the best shore fish in Cornwall was in Oct / Nov / Dec:
| Year | October | November | December |
|---|---|---|---|
| 2023 senior | red mullet 2-0-0 (160 %) | small-eyed ray 10-14-4 (108.9 %) | coalfish 2-9-10 (148.6 %) |
| 2024 senior | gilthead bream 7-10-11 (153 %) | scad 1-4-6 (127 %) | coalfish 5-0-0 (285.6 %) |
| 2025 senior | spurdog 11-12-7 (117.8 %) | red mullet 1-8-11 (123.5 %) | coalfish 4-5-0 (246.4 %) |
| Other classes Nov | 2023 U11 pouting 0-13-2; 2024 ladies bass 7-15-0, U11 ballan wrasse 2-12-0; 2025 ladies flounder 1-12-8, U16 tub gurnard 1-3-11, U11 flounder 1-10-0 | | |
| Other classes Dec | 2023 ladies bull huss 8-14-2, U16 mackerel 0-14-0, U11 coalfish 3-9-5; 2024 ladies flounder 1-12-4, U16 mackerel 0-15-6, U11 flounder 1-13-0; 2025 ladies bull huss 10-8-0, U16 thick-lip mullet 4-11-8, U11 thick-lip mullet 2-9-8 | | |
Shore fish over 100 % of CFSA specimen weight with month given (2023 and 2025 reports give the month; the 2024 table does not):
- **November**: bull huss 13-15-0 (2023), 13-10-11 (2025); small-eyed ray 10-14-4 (2023); flounder 3-2-0 (2023); cuckoo wrasse 1-2-0 (2023); red mullet 1-8-11, 1-7-0, 1-6-15 (all 2025); thick-lipped mullet 5-11-11, 5-9-6 (2025).
- **December**: coalfish 2-9-10, 3-9-5 (2023), 4-5-0, 2-2-6 (2025); cod 5-11-13, 6-7-8, 7-3-0 (all 2023); thick-lipped mullet 5-5-13, 5-11-2, 5-6-8 (2023), 7-6-3 (140.7 %), 5-15-4 (2025); bull huss 13-6-9 (2025); whiting 2-5-10 (2025).
- **October**: bass 10-2-13, 8-8-1, 8-0-4 (2023); pollack 8-11-0 (2023); plaice 2-6-10 (2023); red mullet 2-0-0 (2023); scad 1-4-8 (2023), 1-0-15, 1-0-1 (2025); tub gurnard 1-11-0, 1-10-4 (2023); spurdog 11-12-7 (2025).
- For contrast, months of the other 100 % fish in 2025: tope May-Jul only; gilthead bream Jul-Sep; starry smoothhound May-Jun; small-eyed ray Mar, Jul, Aug; scad Jul-Oct; spurdog Feb + Oct; thick-lipped mullet Nov-Mar + Jul; flounder Jan; pouting Jan; golden-grey mullet Jun.
- 2026 so far (shore update to end Sep 2026): Jan pollack **13-2-0** (175 %), Feb spotted ray 5-13-0, Mar spurdog 13-14-4 (138.9 %), May tope 43-0-0, Jun tope 36-14-8, Jul golden-grey mullet 2-8-9, Aug tope 38-12-13, Sep tope 32-10-0. Best-of-species 2026 to end Sep includes conger 31-6-13, bass 9-5-8, small-eyed ray 11-2-8, bull huss 13-2-4, cod 4-2-8, coalfish 2-4-0, thornback 7-6-0, greater weever 1-5-3, Dover sole 0-13-8.
Best shore fish of each species, whole year (specimen scale): 2025 - ballan 5-7-3, bass 9-1-9, black bream 1-2-0, bull huss 13-10-11, coalfish 4-5-0, cod 3-5-9, conger 17-5-10, Couch's bream 1-4-6, dab 0-10-8, flounder 3-2-0, gilthead 9-4-11, golden-grey 2-6-2, LSD 2-14-7, mackerel 1-6-0, plaice 1-8-9, pollack 6-15-7, pouting 2-0-8, red mullet 1-8-11, scad 1-3-12, shore rockling 0-13-0, small-eyed ray 10-11-1, spurdog 11-12-7, starry smoothhound 12-4-13, thick-lip 7-6-3, thin-lip 3-3-4, thornback 7-2-6, 3-bearded rockling 1-9-8, tope 42-12-8, tub gurnard 1-3-11, whiting 2-5-10. 2024 - ballan 5-12-0, bass 9-2-15, bull huss 14-7-10, coalfish 5-0-0, conger 20-2-0, flounder 3-10-1, gilthead 9-1-5, golden-grey 2-14-8, LSD 3-1-8, pollack 6-15-2, small-eyed 11-7-0, thick-lip 6-6-5, thin-lip 3-11-10, thornback 9-8-8, tope 41-14-3, triggerfish 2-4-0, turbot 1-7-8, whiting 2-4-2.
CFSA shore RECORDS (all-time, 2025 list; lb.oz.dr / kg / year) - the upper bound of "specimen potential": bass 16.8.9 (7.5 kg, 2013); pollack 13.4.10 (1995); coalfish 20.6.0 (1982); cod 26.5.0 (1991); whiting 3.9.13 (2012); pouting 2.14.11; poor cod 0.9.8; haddock 3.0.7 (2016); ling 15.8.7 (2010); hake 2.8.8; conger 49.12.0 (1997); bull huss 19.5.0 (2019); LSD 4.2.11; spurdog 12.15.12 (1975; a 13-14-4 was recorded Mar 2026); tope 49.0.0 (1976); smoothhound 10.3.1; starry smoothhound 16.13.13; blonde ray 26.15.2 (2016); small-eyed ray 14.2.11 (1981); thornback 15.4.6 (2015); spotted ray 7.15.2 (2020); cuckoo ray 4.10.0; sting ray 24.2.0; turbot 10.9.12 (1967); brill 3.3.0 (1965); plaice 5.12.8 (1968); flounder 4.1.0 (2007); dab 1.15.3; Dover sole 3.3.14 (1986); thick-lipped mullet 7.6.5 (1995); thin-lipped 7.0.3 (2012); golden-grey 2.14.8 (2024); red mullet 2.5.13 (2019); ballan wrasse 8.4.0 (1976); cuckoo wrasse 1.9.8; corkwing 0.12.4; gilthead bream 10.11.7 (2017); black bream 4.13.0 (1985); Couch's bream 2.10.12 (2019); tub gurnard 5.4.2; red gurnard 2.14.0; grey gurnard 1.10.8; mackerel 3.0.1; scad 2.5.13; garfish 3.4.12; herring 1.1.4 (2001); twaite shad 2.0.6; allis shad 1.11.5; three-bearded rockling 3.12.14; shore rockling 1.9.2; greater weever 1.12.0; triggerfish 4.12.5 (2015); John Dory 2.14.1 (1980); anglerfish 45.0.0; blue shark 25.8.0 (1975); big-eyed tunny 66.12.0 (1985, Mounts Bay AS).

### 2.1 Reading rules for the catalogue
- "Cornish evidence" = dated entries from 2.0 (MBAS, CFSA; grade B), the Newlyn market blog and bird/cetacean logs as compiled by the press stream (`intel/press_social_signals.md`; grade B for what was landed/seen, D for what it implies for the shore), forum/blog items compiled by the forums stream (`intel/forums_blogs_video.md`; grade C/B).
- "Specimen" = CFSA shore specimen weight, back-calculated by me from the published percentages (D arithmetic on B data), e.g. bass 9-1-9 = 113.73 % -> 8 lb; MBAS club specimen weights are read directly from the sheets (bass 2.722-2.772 kg, LSD 1.247 kg, whiting 0.624 kg, bull huss 5.443 kg, small-eyed ray 4.082 kg, conger 9.072 kg, flounder 0.907 kg).
- Biology/threshold statements marked [GEN] are general fisheries/angling literature recalled from memory and NOT re-verified today (grade D for this document); statements with a named source were read today. Web search stopped at ~16:15 UTC when the shared search quota ran out, so several thresholds could not be re-verified - flagged where it matters.
- Session-day context used throughout: open-coast SST 13.1-13.5 C (+0.5 to +1 C, ~1-3 weeks "late"); estuaries in 3-8x spate with 22-48 mm more rain modelled for 22 Nov; pressure falling on 21 Nov (Sevenstones 1010.5 -> 1008.2 hPa 12-14Z; K1 995 hPa) [Verifier: confirmed and still falling - 62107 1007.4 hPa at 15Z, K1 993.6 hPa at 15Z (NDBC re-fetch 16:25/16:40 UTC). BUT for the session day itself MET Norway (run updated 13:17 UTC 21 Nov, A model) has the low passing in the early hours: Truro MSLP 1007.3 (18Z 21st) -> 998.0 (06Z 22nd) -> 1005.8 (12Z) -> 1012.3 (18Z) -> 1017.9 hPa (00Z 23rd), wind backing/veering from ~120 deg (ESE) 11-12 m/s overnight to ~270-285 deg (W-WNW) 11-13 m/s (21-25 kn) from ~09Z. So 22 Nov daytime/evening = RISING pressure, post-frontal W-WNW wind, clearing; NOT a "falling glass" day after ~06Z.]; tide building to springs (22 Nov ~82 % of the 26 Nov peak range; full moon 24 Nov 14:53 - tides stream `tides_numeric.part.md`); moon waxing gibbous, phase angle 144.5 deg (roughly 90 % lit by D calculation), moonset 05:01, moonrise 14:47, sunrise 07:46, sunset 16:29 at Newlyn (MET Norway via light stream raw `raw/light_moon/metno_*_20261121T1519Z.json`). So the only moonless darkness on the day is from moonset 05:01 until morning twilight (sunrise 07:46; twilight times are in the light stream) - unless cloud covers the moon, which the rain forecast makes likely.

### 2.2 Catalogue - predators and main sport species

**BASS (Dicentrarchus labrax)**
- Late-Nov status: PRESENT AND FEEDING - late Oct to early Dec is the big-fish window in the Cornish records. Cornish evidence: MBAS Nov 2026 - 3.060 + 2.110 kg in one night (16 Nov), 2.320 (6 Nov), 1.690 (4 Nov); Oct 2026 - 3.120, 3.026, 2.150, 2.140, 1.850, 1.700, 1.420 kg, four of the six bass-competition placings caught 18-31 Oct; MBAS Nov 2024 - 4 bass (0.745-1.540 kg, 2-26 Nov); Dec 2024 - 2.300 (15 Dec), 1.885 (23 Dec); Dec 2025 - 2.720 (6 Dec). CFSA: Oct 2023 - 10-2-13, 8-8-1, 8-0-4 (all St Columb SAC); Nov 2024 ladies fish of month 7-15-0 (Mevagissey SAC); best 2026 so far 9-5-8. Commercial handliners "busy on the bass again" 9 Nov 2026, "enjoying a few good fish" 14-15 Nov 2026 [CORRECTED by verifier: was 14-15 Nov - "the bass men are enjoying a few good fish" is in the post of Mon 16 Nov 2026], "huge shot of bass" landed by one boat ~5 Nov 2026 (Newlyn blog, B; gear not stated in the extract) [Verifier: in the post "Downs and downs in Newlyn" published 8 Nov 2026 18:13 - the Ygraine, "price on the floor, more than 50% less"; the ~5 Nov catch date is UNVERIFIED]. Estuary: "river was stacked with bass ... nothing big" 30 Oct 2026 (W Cornwall, forum C); ~5 lb estuary fish late Oct 2026 (H. Gilbey, B).
- Size: typical registered fish 0.75-3.1 kg (MBAS); CFSA specimen 8 lb; annual best 9-1-9 to 10-2-13; record 16-8-9 (7.5 kg, 2013).
- Biology: gonad development starts in October, spawning peaks ~April offshore (Pawson & Pickett 1996, JMBA); adults (>42 cm) leave shallow summer grounds in autumn (Oct-Nov) for deeper offshore pre-spawning areas, and warming has lengthened the inshore feeding season and delayed that migration (Lincoln et al., Bangor, spawning-area paper); tagged mature bass averaged 8.5 C water during the offshore/spawning phase (Wright et al., Movement Ecology 2024). All three as summarised by WebSearch at ~16:13 UTC - abstracts, papers not opened (treat as B). [Verifier: Wright, Griffiths, Bendall, Righton, Hyder & Hunter 2024 CONFIRMED from the Europe PMC abstract (PMC11167799; fetched 16:52 UTC, raw `species_sst_verify/epmc_wright_20261121T1652Z.json`; grade A): 171 mature bass >42 cm tagged; "Seasonal movements between shallow areas (Q2-Q3) and deeper spawning areas (Q4-Q1) were accompanied by ... average water temperatures of 8.5 C in the English Channel and Irish Sea". Note Q4 = Oct-Dec, i.e. the tagging places the move to deeper spawning areas IN the current quarter - counter-evidence to "adults still inshore in strength", reconciled only by the Cornish catch data. Pawson & Pickett 1996 and Lincoln et al. remain UNVERIFIED (the saved "bangor_bass_spawning" PDF is an HTML challenge page, not the paper).] School bass and many adults overwinter inshore in the SW [GEN].
- Temperature: 13.1-13.5 C is well above anything that suppresses bass feeding; the anomaly (+0.5-1 C) argues the autumn inshore feed is running late/extended, i.e. MORE adult bass inshore than in a normal 22 Nov (D, consistent with Lincoln et al. and with the Nov 2026 catches).
- Habitat/depth: surf beaches (1-3 m), reef edges and gullies, estuary mouths and channels, harbour mouths; at night within metres of the edge (Gilbey fish "less than two yards from the edge").
- Conditions: Atlantic swell producing "an even surf with deep water tables" is the key on beaches; N coast best with W/NW wind, S coast with SW; best period ~2 h either side of low water on surf beaches but can run to high water; sandeel the best surf bait, lugworm "especially good at night", also razor, mackerel strip, soft crab; weed in the gullies after blows can kill a beach (UKBASS, N. Hester, "Surf Angling for Bass in Cornwall", 1984 article re-published on ukbass.com; B, old but Cornwall-specific).
- Methods: surf bait (sandeel, lug, squid, razor, crab; big mackerel/squid/whole-fish baits for big fish at night); soft plastics, surface and shallow-diving plugs in fizzed-up but not filthy water; weedless soft plastics in estuaries (Gilbey Oct 2026).
- Where documented in Nov: Mount's Bay / West Penwith (MBAS, venue-less); St Austell Bay area (Mevagissey SAC lady's 7-15-0, Nov 2024); N coast surf beaches (UKBASS; St Columb SAC Oct 2023 doubles); SE and W Cornwall estuaries (Gilbey, forum). THIN on exact marks.

**POLLACK (Pollachius pollachius)**
- Status: PRESENT; the bigger fish show on deep rock marks from late autumn into winter. Evidence: MBAS Nov 2026 - 3.120 kg (2 Nov), 2.555 (5 Nov), 1.245 (7 Nov); Oct 2026 1.930; Sep 2026 4.100. CFSA: Oct 2023 8-11-0 (St Columb SAC); best 2024 6-15-2, 2025 6-15-7; **Jan 2026 13-2-0 (175 %, Camborne AA)** - within ~2.6 oz of the 13-4-10 county shore record (1995). None registered in the five MBAS Nov/Dec sheets 2023-25 (so not an every-year November fish in Mount's Bay).
- Size: typical 1-3 kg from rock; specimen 7 lb 8 oz (derived); record 13-4-10.
- Biology: spawns Jan-Apr; moves deeper with size (Cornwall Good Seafood Guide, B). "Larger pollock will generally move into deeper water in the colder winter months ... some stay in shallow water all year" (britishseafishing.co.uk, B). The Jan 2026 13-pounder contradicts "only small ones in winter" for Cornwall - big pre-spawn fish are within shore range on the right deep marks.
- Temperature: no constraint at 13 C. Habitat: deep kelp-fringed rock, headlands with tide run, harbour walls at night; 5-25 m.
- Conditions [GEN + C]: dusk and dawn strongly best, clear to lightly coloured water, moderate swell tolerable, fish rise at dusk. Methods: weedless soft plastics / paddle-tails, metals, float-fished or free-lined sandeel/mackerel strip, big fish baits at night.
- Where: West Penwith and Lizard rock marks (MBAS, Camborne AA - venue-less); THIN on named marks.

**COALFISH (Pollachius virens)**
- Status: MARGINAL in late Nov, ARRIVES IN DECEMBER. Evidence: CFSA senior shore Fish of the Month for DECEMBER three years running - 2023 2-9-10 (also U11 3-9-5), 2024 5-0-0 (285 %), 2025 4-5-0 (246 %) plus 2-2-6; all Camborne AA / Truro City / St Columb SAC. No November coalfish in any sheet read. Best 2026 to Sep 2-4-0.
- Size: small - CFSA specimen is only ~1 lb 12 oz (derived); 2-5 lb fish are exceptional; record 20-6-0 dates from 1982.
- Biology: cold-water gadoid, "in the south classed as an autumn and winter fish" [CORRECTED by verifier: was presented as a quote; that phrase is NOT on the saved talkseafishing page. What the page says: "the season for shore caught coalfish is typically from late October to late March along the open coastline. Their numbers build inshore from that mid-October period, but you see the best numbers in the southern section from Christmas through to mid-March"; south of a N Wales-NE line coalfish "can be more localised ... mainly near rocky coastal areas, especially in the west"]; juveniles in harbours, estuaries, surf beaches, deep water off rock ledges; spawn Jan-Apr (talkseafishing coalfish guide, 2021, B). The guide therefore puts late November inside the shore season but before the southern peak - consistent with the CFSA December pattern. Temperature: the +0.5-1 C anomaly argues AGAINST an early arrival this year (D).
- Methods [GEN]: small lures / baited feathers / worm and fish baits after dark around lit harbours and surf; dusk. Where: THIN DATA - club base suggests north-coast / west Cornwall marks; no venue published.

**COD / CODLING (Gadus morhua)**
- Status: RARE. "Becoming increasingly rare in Cornish waters ... a cold water species" (Cornwall Good Seafood Guide, B). Evidence: CFSA Dec 2023 three specimens 5-11-13 (Looe SAA), 6-7-8 and 7-3-0 (Truro City SAC); best cod 2025 only 3-5-9, 2026 to Sep 4-2-8 (both Padstow SAC). No cod in any MBAS Nov/Dec sheet. N Devon estuary note (ndan blog, C): codling "now seldom caught during the autumn or winter months".
- Size: specimen 5 lb 8 oz (derived); record 26-5-0 (1991). Temperature: warm anomaly is unfavourable. Methods [GEN]: big lug/squid/crab baits at night into coloured water after a blow; estuary mouths and deep rock marks. Where: Fal (Truro City), Looe, Camel (Padstow) by club proxy - THIN.

**WHITING (Merlangius merlangus)**
- Status: PRESENT, numbers build from mid-Nov to a late-Dec peak. Evidence: MBAS - 16 Nov 2023 (0.480 kg), 12 Nov 2023 (0.360), 17 Nov 2024 (0.250); Dec 2023 x6 (to 0.747 kg), Dec 2024 x4 (to 0.625), Dec 2025 x6 (to 0.605). CFSA: Dec 2025 2-5-10 (104.7 %, Padstow SAC), Jan 2025 U11 1-14-0; best 2024 2-4-2.
- Stock caveat: "not doing well ... ICES advising zero catch since 2023 ... cold water species that has poor recruitment in warmer years" (Cornwall Good Seafood Guide, B) - so expect fewer than the "winter staple" reputation suggests; the registered MBAS November whiting are few and small.
- Size: typical under 0.5 kg; MBAS specimen 0.624 kg; CFSA specimen 2 lb 4 oz; record 3-9-13.
- Conditions [GEN]: darkness essential in clear water; clean sand/shingle beaches and deep water off piers/rocks; flood tide to high water; calm frosty nights classic. Methods: small fish/squid/worm baits on 1-2/0 hooks, 2-3 hook flappers. Where: Mount's Bay beaches (MBAS), Camel/north-coast (Padstow SAC) - THIN on marks.

**POUTING, POOR COD, ROCKLINGS, HADDOCK, LING, HAKE**
- Pouting: present all winter at night over mixed ground/harbour walls; CFSA Nov 2023 U11 0-13-2, Jan 2025 2-0-8 (135 %, Looe SAA), best 2024 1-14-8; specimen ~1 lb 8 oz; record 2-14-11. High catch probability after dark on worm/fish baits [GEN].
- Poor cod: ubiquitous small night fish on rock/harbour marks; record 0-9-8 (Looe SAA 2001). LRF/scratching target [GEN].
- Three-bearded rockling: MBAS 2 Nov 2026 0.570 kg; CFSA Oct 2024 U11 1-0-0, Mar 2025 1-3-4, best 2025 1-9-8, 2026 1-5-8; specimen 2 lb; record 3-12-14. Rough ground at night, fish/worm/crab baits [GEN]. Shore rockling: CFSA best 0-13-0/0-14-0; record 1-9-2; gullies and rough ground at night.
- Haddock: exceptional (record 3-0-7, 2016); no recent autumn evidence - THIN. Ling: exceptional from shore (record 15-8-7, 2010); deep rough ground at night [GEN]. Hake: record 2-8-8 (1981) - not a realistic target.

**CONGER (Conger conger)**
- Status: PRESENT, active at night until inshore water drops well below 10 C [GEN]. Evidence: MBAS 11 Nov 2024 6.650 kg; CFSA best 2024 20-2-0, 2025 17-5-10, 2026 to Sep **31-6-13** (Camborne AA); record 49-12-0 (Looe SAA 1997). Specimen 20 lb (derived).
- Habitat: harbour walls, breakwaters, deep rough ground and wrecks/reefs within casting range, kelp gullies. Conditions [GEN]: darkness, slack-ish water around high or low, mild humid nights, coloured water helps in daylight; severe cold snaps push them out/kill them - none this year. Methods: large mackerel/squid/cuttle/pouting baits, heavy mono/wire trace. Where: THIN on dated venues; club proxy = Camborne AA, Truro City, Looe.

**BULL HUSS (Scyliorhinus stellaris)**
- Status: PRIME - November/December are the specimen months in the county records. Evidence: CFSA 100 % fish - Nov 2023 13-15-0, Nov 2025 13-10-11 (both Sean Haley, ECC Ports/Padstow SAC), Dec 2025 13-6-9 (Camborne AA); Dec 2023 ladies 8-14-2, Dec 2025 ladies 10-8-0; best 2024 14-7-10. MBAS: 29 Dec 2023 4.230 kg, 29 Dec 2024 5.050, 29 Dec 2025 5.975 (109.8 %), 19 Oct 2026 4.100.
- Size: typical 3-6 kg; CFSA specimen 13 lb; record 19-5-0 (2019).
- Habitat/conditions [GEN]: rough/mixed ground and kelp close in, 3-15 m, night, any tide with some run, will feed in coloured and rough water. Methods: big fish/squid/crab baits on pulley rigs. Where: N coast rough ground (Padstow SAC proxy), West Penwith/Mount's Bay (MBAS) - THIN on marks.

**LESSER SPOTTED DOGFISH (Scyliorhinus canicula)**
- Status: the single most frequently registered shore fish in MBAS Nov/Dec sheets (24 of 70 senior-shore entries; 7 of 14 in Nov 2024); won the 1 Nov 2026 rover at 1.130 kg. Present everywhere over sand/mixed ground, day or night, any sea state. Typical 0.8-1.25 kg; MBAS specimen 1.247 kg; CFSA specimen 3 lb, record 4-2-11. Highest catch probability of any species; low sport value.

**SPURDOG (Squalus acanthias)**
- Status: PRESENT offshore now, shore-catchable from deep-water marks; county specimens fall Oct-Mar. Evidence: CFSA Oct 2025 11-12-7 (Looe SAA), Feb 2025 11-10-4 and 11-0-6 (Padstow SAC), **Mar 2026 13-14-4** (Camborne AA; exceeds the listed 12-15-12 record of 1975). MBAS boat: 15 Nov 2024 8.900 kg, 1 Nov 2026 5.783 kg (in Mount's Bay now).
- "Highly migratory" (CGSG); "will move into relatively shallow water to feed" (BSF). Specimen 10 lb. Methods [GEN]: fish baits (mackerel, herring, squid) at night from deep rock ledges/steep beaches, wire or heavy mono. Where: THIN - club proxy only (Looe, Padstow, Camborne).

**TOPE, SMOOTHHOUNDS** - OUT OF SEASON from the shore. CFSA 100 % tope are all May-Sep (2025: May-Jul; 2026: May, Jun, Aug, Sep 32-10-0); starry smoothhound May-Jul. MBAS BOAT tope 25.6 and 19.3 kg on 18 Oct 2026 shows tope were still in Mount's Bay five weeks ago, so a late shore tope from a deep ledge is "exceptional but not impossible" (D). Tope must be released (rules stream).

**RAYS**
- Small-eyed ray (Raja microocellata): PRESENT ALL WINTER. MBAS: 12 Nov 2023 3.856 kg, 8 Nov 2023 3.200, 29 Dec 2024 3.540 + 2.940, 28 Dec 2025 4.060 (99.5 %), 19 Oct 2026 2.360. CFSA: Nov 2023 Fish of the Month 10-14-4 (108.9 %, ECC Ports SAC); other 100 % fish Mar, Jul, Aug; best 2026 11-2-8. Specimen 10 lb; record 14-2-11. Surf/clean sand beaches adjacent to rock, night, sandeel (the classic) / squid / mackerel-sandeel wraps; "casts of around 100 yards can be needed" (BSF). Best after a settling sea with slight colour [GEN].
- Thornback: MBAS 29 Dec 2024 2.800 kg; CFSA best 2024 9-8-8, 2025 7-2-6, 2026 7-6-0 (Mevagissey SAC) - present but minor in Cornwall. Record 15-4-6.
- Spotted ray: CFSA Feb 2026 5-13-0 (116 %, Padstow SAC) - winter fish on the N coast by club proxy; record 7-15-2 (2020). Blonde ray: record 26-15-2 (2016, St Columb SAC) but no entry in any 2023-26 list read - big-fish potential, very low probability, THIN. Undulate ray: NOT in the CFSA shore record list at all - treat as not a Cornish shore species. Cuckoo ray record 4-10-0 (1981). Sting ray: summer only.

**FLATFISH**
- Flounder (Platichthys flesus): PRIME SEASON in estuaries. CFSA: Nov 2023 3-2-0 (104 %, Looe SAA); Nov 2025 ladies 1-12-8, U11 1-10-0; Dec 2024 ladies 1-12-4, U11 1-13-0; Jan 2025 3-2-0 (ladies record, Camborne AA); best 2024 3-10-1 (Looe SAA); MBAS 23 Dec 2024 0.475, 7 Dec 2025 0.625 kg. "Late October/early November through February is the peak"; "big fish begin moving from the outer estuaries onto beaches ahead of spawning" (December column); "neaps often beat springs"; Fowey and Looe "hold very large flounder"; Tamar (Maristow) winter fish average ~1 lb 8 oz, 2 lb good; baits peeler/soft crab and ragworm (Sea Angler pieces as summarised by WebSearch ~16:14 UTC; pages themselves returned HTTP 403 to direct fetch - B, not opened) [UNVERIFIED - verifier could not open these either; the BSF flounder page (opened) supports only "near an influx of freshwater ... can travel up rivers far into freshwater territory" and the late-winter/early-spring move to deeper water to spawn]. BSF: moves to deeper water to spawn in late winter/early spring; lives "near an influx of freshwater ... can travel far into freshwater".
  Specimen 3 lb; record 4-1-0 (2007). Current conditions: flounder are the most spate-tolerant estuary fish, but a 4-8x spate with more rain pushes feeding fish seaward to the lower/middle estuary and the mouths (D + [GEN]).
- Dab: winter beach fish, small - CFSA best 0-10-8 (2025), 0-12-6 (2026, Padstow SAC); record 1-15-3. "Feed in most sea conditions, daylight and darkness" (BSF).
- Plaice: tailing off - "most commonly caught March to September ... colder months in deeper water" (BSF); CFSA Oct 2023 2-6-10; MBAS Sep 2026 0.360. Low probability in late Nov.
- Dover sole: MBAS annual list has Dover sole entries (month not shown); CFSA best 2026 0-13-8 (Mevagissey SAC). Night fish on clean sand, calm warm nights, small worm baits [GEN]; late Nov is the tail end - low probability.
- Turbot: MBAS 8 Nov 2023 0.570 kg; CFSA best 2024 1-7-8. Surf beaches with sandeel/mackerel strip; "only the coldest few months see turbot very difficult from the shore" (BSF). Small fish only; record 10-9-12 dates from 1967. Brill: record 1965, no recent entries - exceptional.

**GREY MULLETS**
- Thick-lipped (Chelon labrosus): **CONTRADICTS the "winter slow-down" expectation - the county's biggest thick-lips are WINTER fish.** CFSA 100 % specimens by month, 2025: Jan 1, Feb 4, Mar 2, Jul 1, Nov 2 (5-11-11, 5-9-6), Dec 2 (7-6-3 = 140.7 %, 2 dr under the 7-6-5 record of 1995; 5-15-4); 2023: Dec x3 (5-5-13, 5-11-2, 5-6-8). Dec 2025 U16 4-11-8; MBAS 29 Dec 2024 1.545 kg. Generic sources say feeding effort falls in winter (NW IFCA, K&E IFCA) but that thick-lips "can be caught year round in Cornwall" (Angling Trust) - WebSearch summaries, B. Interpretation (D): big adults concentrate in harbours/lower estuaries in winter and remain catchable on bread/fish-flesh in settled spells; numbers of bites fall, average size rises.
  Specimen 5 lb 4 oz (derived). Methods [GEN]: float or quiver-tip, bread flake/mashed-bread groundbait, small hooks, fine line; harbours with fish-waste/sardine landings also fish with mackerel/sardine flesh. Conditions: calm, clear, low flow; spate and colour are BAD (D) - which hurts estuary mullet on 22 Nov and favours enclosed harbours.
- Thin-lipped: summer/autumn estuary fish on baited spinners (MBAS Sep 2026 x6 on 6 Sep); CFSA best 3-3-4 (2025); record 7-0-3. Low probability in a late-Nov spate. Golden-grey: surf-beach fish, CFSA specimens Jun-Jul (2-6-2, 2-8-9); record 2-14-8 (2024). Low probability now.

**WRASSES**
- Ballan (Labrus bergylta): **still feeding - also contradicts a blanket "slow-down" at this SST.** MBAS: 12 Nov 2023 2.041 kg; 5 Nov 2026 1.255; Oct 2026 2.325, 1.480, 1.390. CFSA Nov 2024 U11 2-12-0. West Cornwall lure specialist (forum, C): 15 Nov 2024 32 wrasse to 5 lb 5 oz; 15 Dec 2023 5 fish to 5-1; 22 Dec 2023 6 lb 5 oz; 20 Dec 2024 12 fish; 6 Nov 2026 7 wrasse on a bass lure in heavy swell; 20 Nov 2026 "5, all on lures" in a river because swell kept him off the rocks "for nearly 6 weeks". Specimen 5 lb 8 oz; record 8-4-0.
  Temperature [GEN, not re-verified] [UNVERIFIED - no source found by verifier either]: activity falls sharply below ~9-10 C; at 13 C they are fully active. Limiting factor is swell/colour (need to hold bottom in kelp gullies and for fish to see a lure), not temperature. Methods: Texas/weedless soft plastics, crab, rag, limpet on float or leger; daylight, flood tide.
- Cuckoo wrasse: CFSA Nov 2023 1-2-0 (100 %); deeper rock marks. Corkwing: MBAS 5 Oct 2026 0.380 kg club record. Goldsinny/rock cook: LRF targets [GEN].

**SEA BREAMS, RED MULLET, GURNARDS, JOHN DORY, TRIGGERFISH**
- Gilthead bream: summer-autumn (CFSA 100 % fish Jul-Sep; Oct 2024 7-10-11); "spawning occurs between November and December" (CGSG, B) -> adults leave estuaries for the sea; commercial "cracking gilt-head bream" at Newlyn ~5 Nov 2026 (boat). Late-Nov shore probability LOW, lower still in spate estuaries; specimen potential high if one is met (record 10-11-7).
- Black bream / Couch's bream: MBAS Sep 2026 (black x5, Couch's x4), Couch's 3 Oct 2026; boat Couch's 4.082 kg on 7 Nov 2026 (so still on reefs in Mount's Bay). Shore probability in late Nov low; THIN.
- Red mullet (Mullus surmuletus): **a genuine November shore species in Cornwall**: CFSA Nov 2025 Fish of the Month 1-8-11 (123 %) plus 1-7-0 and 1-6-15 (Padstow SAC, Truro City SAC); Oct 2023 2-0-0 (160 %); MBAS Sep 2026 0.510 kg. Commercial: "inshore red mullet" 9 Nov 2026, "a good few red mullet" 14-15 Nov 2026 (Newlyn blog, B). Warm-water species (CGSG) favoured by the positive anomaly. Specimen 1 lb 4 oz; record 2-5-13. Methods [GEN]: small worm/fish baits on fine traces over clean sand next to reef, at night, calm clear conditions. Where: THIN (club proxy only).
- Gurnards: tub gurnard CFSA Nov 2025 U16 1-3-11, Oct 2023 1-11-0, 1-10-4; MBAS 12 Nov 2024 0.110 kg; red gurnard best 2024 0-10-9. Present on clean ground through November; minor.
- John Dory: shore record 2-14-1 (1980); "a few late season John Dory" from inshore boats 9 Oct 2026 - exceptional from shore, effectively nil by late Nov.
- Triggerfish: MBAS Sep 2026 x3 (to 2.300 kg); CFSA best 2024 2-4-0; none after September in any sheet. Warm-water vagrant that dies or leaves as the sea cools [GEN]; at 13 C the season is over - very low probability.

**PELAGICS AND BAIT-FISH**
- Mackerel: STILL PRESENT - MBAS 6 Nov 2023 0.575 kg; 29 Dec 2023 x2; 29 Dec 2024 x4 (0.383-0.515 kg); CFSA Dec 2023 U16 0-14-0, Dec 2024 U16 0-15-6. "Gill nets are used during winter months on the south coast to target mackerel" (CGSG); Newlyn 9 Nov 2026 "the size of these mackerel is encouraging", 23 Oct "a good shot of mackerel". Patchy, shoal-dependent, mostly dusk/dark from deep-water piers/rocks and under harbour lights [GEN]. Specimen 1 lb 12 oz.
- Scad: CFSA Nov 2024 Fish of the Month 1-4-6 (127 %, Mevagissey SAC); 100 % fish run Jul-Oct; MBAS boat 22 Nov 2023. Night fish around lit harbours/piers, small lures/sabikis/float [GEN]. Specimen 1 lb.
- Garfish: MBAS Sep 2026; "move away into deeper water in the winter months" (BSF) - low probability.
- Herring: Celtic Sea stock "currently very low" (ICES June 2025 per CGSG); landed "mainly from the south coast"; shore record 1-1-4 (Mevagissey SAC 2001); boat sonar report of "small herring" shoals in the Helford (forum, undated in extract, C). Occasional on sabikis in harbours in winter - THIN.
- Sardine (pilchard) / sprat / anchovy: the Cornish ring-net sardine fleet works Mount's Bay and the south coast at night; Nov 2026: boats "drawing a blank on more nights than not" except on marks "not being chased hard by bluefin and dolphins" (post 8 Nov on the 5 Nov market), one good landing despite "marauding bluefin and dolphins" (9 Nov) - press stream, B. Analogues: sardines scarce in Mount's Bay for weeks to 2 Dec 2024; 5-week drought to 7 Nov 2025, "finding fish in the Bay again" 24-25 Nov 2025. Not angling targets but THE driver of bass/mackerel/pollack/tuna/squid location.
- Sandeel / launce: lesser sandeels spend most of the winter buried in sand and are far less available than in summer; greater sandeel (launce) remain over offshore banks [GEN]. Still the reference surf bait (frozen) for bass, ray, turbot.

**CEPHALOPODS**
- Squid (Loligo vulgaris / L. forbesii): **PEAK INSHORE SEASON.** Commercial jig/handline evidence (press stream, B): 2026 - "a good weekend on the squid" 17-18 Oct, punts "nabbed a few squid" 22-23 Oct, "a few canny men went after squid with the jigs ... really got in amongst them" ~6-9 Nov; 2025 - "bumper landings of squid" 17 Nov attributed to "warmer seas than normal", jigged squid 172 kg in the week to 6 Dec; 2024 - "plenty on the grounds" through November; 2023 - "inshore jigged squid" 13 and 20 Nov. Biology (CGSG, B): squid return to the warmer western Channel/Celtic Sea in winter; UK landings far higher in autumn-winter (167 t Feb vs 23 t Apr 2022); L. vulgaris eggs die below 10 C, L. forbesii below 8 C; "more likely over sand in rougher sea and rock in calmer sea". Shore (Plymouth guide, planetseafishing 2013, B): the long inshore run is "towards the end of summer, right through autumn", fish "prefer marks that have some form of artificial light, move in around dusk and stay throughout the hours of darkness"; a 2.6 kg Falmouth Bay squid in late Nov 2013 and 3 kg+ "not rare" in far-west Cornwall (WebSearch summary of a Fishing News column, B/C).
  Conditions [GEN + above]: clear water, light swell, dusk and night, lit piers/harbour mouths and deep rock ledges, flooding tide to HW; coloured water and heavy swell kill it. Methods: egi jigs 2.5-3.5, baited squid jigs under a float. Current implication: SST 13 C is ideal (well above egg-lethal limits) and three consecutive years of strong November squid make this a real target - IF a clear-water venue exists after the swell and rain (sea-clarity stream decides).
- Cuttlefish: adults overwinter in deep water offshore (CGSG: trawlers "target deep water aggregations of overwintering cuttles"); market "stacked with cuttles" 19 Oct 2026 (boat). Occasional on squid jigs in autumn; low probability late Nov.
- Common octopus (Octopus vulgaris): see 3.6. Realistic incidental catch on crab/fish baits and squid jigs at night over rough ground in 2026.

**APEX / EXOTICS**
- Bluefin tuna: PRESENT close inshore this month - "10 Blue-fin Tuna" off Kilgerran Head (Roseland) 7 Nov; "Bluefin Tuna breaking surface in Mounts Bay" from Trenow 8 Nov; "Tuna and Harbour Porpoises" off East Pentire, Newquay 11 Nov; sardine skippers report shoals "chased hard by bluefin and dolphins" 5-9 Nov (press stream, B). No record after 13 Nov (absence of reports in poor weather, not proof of absence). Shore capture: no modern Cornish shore-caught bluefin found (NOT FOUND); the CFSA shore list does carry a "Tunny (Big Eyed) 66-12-0" (Mounts Bay AS, 1985) and a shore blue shark 25-8-0 (1975), so exceptional pelagic captures from the Cornish shore have happened. For a superhuman angler on an offshore rock (Wolf Rock, Longships, Runnel Stone area, Scilly outer rocks) a bluefin within casting range is conceivable (D) but there is NO evidence base for catch probability, and targeting is licence-controlled (rules stream). Atlantic bonito/skipjack were landed to 26 Oct 2026 (boat).
- Sharks: blue shark season is Jun-Oct offshore; porbeagle are taken by boats off the north coast in winter-spring [GEN, not verified today]. Shore probability effectively nil - THIN/none.

**ESTUARY / MIGRATORY**
- Sea trout and salmon: adults are in the rivers on these spates (late-running fish on Camel/Fowey [GEN]); estuary rod fishing for them is governed by EA byelaws and close seasons (rules stream) - not assessed here as an angling target. Sea trout do get taken by bass/mullet anglers in estuary mouths. THIN.
- Shad (twaite/allis): spring-summer captures (records 1982, 1988); not a November fish. European eel: silver eels run seaward on autumn spates and dark nights [GEN] - exactly these conditions - but must be returned; feeding falls with temperature. Smelt/sand smelt: LRF targets in harbours [GEN].
- Mini-species / LRF (gobies, blennies, long-spined sea scorpion, tompot, shanny, clingfish, topknot, juvenile pollack/coalfish/pouting/poor cod, sand smelt): available all winter in harbours and rock pools, best on calm clear nights under lights with isome/ragworm scraps on size 14-20 hooks [GEN]. No dated Cornish November evidence found today (LRF search returned nothing local) - THIN DATA.
- Weevers: greater weever CFSA 2026 1-5-3 (month not given); lesser weever "in winter found in slightly deeper water away from the shore" (BSF) - incidental only.

---------------------------------------------------------------------------------------------------
## 3. SEASONAL DYNAMICS SPECIFIC TO LATE NOVEMBER (and to THIS late November)

### 3.1 Where the season stands (D synthesis of sections 1-2)
The sea is at 13.1-13.5 C, about what a normal early-to-mid November looks like, after the first storm of the season on 22-23 Oct 2026 ("Storm Austen" per the Newlyn blog; "first of this season's storms ... howling north westerly" - Gilbey 23 Oct), roughly six weeks of swell that kept rock anglers off exposed marks (W Cornwall forum poster, 21 Nov: not properly on the rocks "for nearly 6 weeks"), a short cold snap with air frost on 13 Nov (Tmin -0.6 to -2.8 C at the estuary heads) and a wet, mild SW spell since 15 Nov that put the rivers into spate. Summer visitors (triggerfish, black/Couch's bream, thin-lipped and golden-grey mullet, garfish, tope, smoothhound, gilthead in estuaries) have dropped out of the club returns since September/early October; the winter set (whiting, small-eyed ray, bull huss, conger, dogfish, flounder, big thick-lipped mullet, then coalfish in December) is in; bass, pollack, wrasse, mackerel, scad, red mullet and squid are in their late-autumn overlap and - because the sea is warm - that overlap is probably wider than usual this year.

### 3.2 Bass: pre-spawning feed and offshore movement
- Science (B, abstracts via search): gonads develop from October; adults leave the shallows Oct-Nov for offshore pre-spawning/wintering areas in the western Channel/Celtic Sea; spawning peaks ~April; a warmer sea extends the inshore feeding season and delays departure.
- Cornish shore evidence (B): the best MBAS bass of each autumn come 18 Oct-16 Nov in 2026 (3.12, 3.06, 3.03 kg), and bass keep appearing to late December (23 Dec 2024 1.885 kg; 15 Dec 2024 2.300; 6 Dec 2025 2.720). CFSA doubles/near-doubles are October fish (10-2-13 in 2023), with a 7-15-0 in November 2024.
- Commercial evidence (B): Newlyn handliners on bass 9 and 14-15 Nov 2026; a "huge shot of bass" landed by one boat ~5 Nov 2026; analogues - weekly Newlyn bass 518.58 kg in the week to 6 Dec 2025, bass from "a dozen or so inshore boats ... on some good marks" 8 Dec 2023. So in Mount's Bay/West Cornwall the adult bass aggregate close inshore through November into early December before leaving.
- Reading for 22 Nov 2026 (D): adult bass are still inshore in strength, feeding hard before departure, keyed on sardine/sprat/mackerel and on surf-dislodged food; the estuaries hold mostly school fish (and are in spate - fish drop to the mouths).

### 3.3 Bait-fish and what follows them
- Sardine: fleet struggling in early Nov 2026 because shoals were scattered/harried by "marauding bluefin and dolphins" (5-9 Nov); no fleet activity mid-week 18-19 Nov (weather). In 2025 the sardines were back "in the Bay" (Mount's Bay) by 24-25 Nov; in 2024 they were scarce in Mount's Bay until 2 Dec. Grounds = Mount's Bay and the south coast bays (ring-netters land to Newlyn/Mevagissey) - current precise marks NOT FOUND.
- Seabird/cetacean feeding events (press stream, B): very large gannet/kittiwake/auk flock off Levant-Pendeen 15 Oct; 500 gannets + fin whale off Porthkerris 12 Oct; common dolphins on the Scillonian crossing 7 Nov; bluefin off the Roseland 7 Nov, Mount's Bay 8 Nov, Newquay 11 Nov. Nothing remarkable logged 20 Nov. So bait and predators were on BOTH coasts in the first half of November; the most recent fix is 9-10 days old.
- Mackerel "of encouraging size" landed 9 Nov 2026; club records show shore mackerel to 29 Dec in 2023 and 2024.
- Sandeel availability falls in winter [GEN]; sprat/herring presence inshore is plausible (winter gill-net/ring-net herring "mainly from the south coast" - CGSG) but undated for 2026 - THIN.

### 3.4 Squid inshore peak
Four consecutive Novembers (2023-2026) of inshore jigged squid at Newlyn/St Ives, with 2025 called "bumper" and tied to "warmer seas than normal"; 2026 jig boats "really got in amongst them" ~6-9 Nov. Biology supports a late-autumn/winter concentration in the warm western Channel. This is the peak of the shore squid season; the practical constraint is water clarity and swell at lit piers/deep rock (see clarity stream), not temperature.

### 3.5 Whiting / codling arrival; coalfish
Whiting: first registered MBAS fish 12-17 Nov in both 2023 and 2024, numbers peaking late December. With the sea ~1 C warm and the Celtic Sea stock depressed, expect a thin, small-fish showing on 22 Nov (D). Codling: effectively absent in most years (three specimens in Dec 2023 are the exception). Coalfish: a December fish in all three CFSA years; not yet expected in strength.

### 3.6 Flounder
Pre-spawning feed in estuaries is the classic Nov-Jan fishery (CFSA Nov 2023 3-2-0; Nov 2025 ladies/U11 fish; Jan 2025 3-2-0). Largest fish move toward outer estuaries/adjacent beaches in December before leaving to spawn (Sea Angler via search, B). Frost on 13 Nov will have started that movement [GEN]; the current spate reinforces it (D).

### 3.7 Mullet and wrasse "slow-down" - not yet, and for mullet the reverse
See 2.2: Cornish records show winter (Nov-Mar) as the specimen season for thick-lipped mullet and Nov-Dec lure-caught wrasse to 6 lb 5 oz. At 13 C neither is temperature-limited; wrasse are swell-limited, mullet are colour/flow-limited.

### 3.8 Rays, huss, conger
Small-eyed ray remain on the surf/sand marks all winter (Nov 2023 x2, Dec 2024 x2, Dec 2025, Oct 2026 in MBAS; county Fish of the Month Nov 2023 at 10-14-4). Bull huss peak in size in Nov-Dec (three 13 lb+ county fish in Nov 2023, Nov 2025, Dec 2025). Conger feed through the winter nights while inshore water stays above ~10 C [GEN] - it is 13 C. Spurdog packs are in Mount's Bay now (boat fish 1 Nov 2026).

### 3.9 Effect of the first winter storms
(i) Swell and colour end the clear-water summer species close in and strip/redistribute weed - MBAS match at Perranuthnoe 3 Oct 2026 was a blank "in tough weedy conditions"; UKBASS notes weed collecting in low-water gullies after blows. (ii) Surf dislodges worm, razor, sandeel and crab - the classic bass/ray/whiting/huss feed in the days AFTER a blow as the sea fines down with colour still in it [GEN]. (iii) Rain spates colour and freshen estuaries, pushing bass/mullet/bream seaward and silver eels and salmonids on the move. (iv) Storms scatter bait-fish shoals (sardine fleet "found fish after the mid-week blow" 9 Oct 2026 - so shoals re-form quickly).

### 3.10 The common octopus bloom, 2025-2026
- Scale (A, MMO "Octopus and Shellfish Landings Data Summary - August 2026", data 1 Jan 2021-31 Aug 2026, provisional; fetched 16:11 UTC, raw `mmo_octopus_landings_aug2026_20261121T1611Z.pdf`): octopus landed by UK vessels - Newlyn 47 t/yr (2021-24 average) -> 977 t (2025) -> **1,522 t in Jan-Aug 2026 alone**; Mevagissey 1 -> 90 -> 279 t; Plymouth 11 -> 147 -> 224 t; Brixham 126 -> 770 -> 788 t; Salcombe 0 -> 286 -> 348 t; Dartmouth 1 -> 187 -> 296 t. ICES area 7e has "consistently the most landings". MMO guidance page "MMO updates on the octopus bloom" published 9 Jul 2026, last updated 9 Nov 2026 (https://www.gov.uk/guidance/mmo-updates-on-the-octopus-bloom): "During 2025 and into 2026, fishermen in South West England reported a surge in sightings and landings of common octopus (Octopus vulgaris)".
- Causes/consequences (A/B, MBA-led "2025 Octopus Bloom Non-Technical Summary", https://www.mba.ac.uk/wp-content/uploads/2026/01/2025-Octopus-Bloom-Non-Technical-Summary.pdf, fetched 16:11 UTC): driven by unusually warm sea temperatures and altered currents; in 2025 catches "spread westward, peaking in May, June, and July before declining in late summer"; brown crab and scallop catches fell "by over 50 %", lobster by 30 %; 2025 deficits brown crab -1,206 t (-GBP 3.19 M), lobster -87.6 t (-GBP 1.41 M), king scallop -3,165 t (-GBP 6.04 M); 57.6 % of surveyed crab/lobster fishers reported negative effects; chance of another bloom "appears to be high".
- Now (B, Newlyn blog via press stream): 33,150.8 kg of octopus on Newlyn market on Mon 19 Oct 2026 alone [CORRECTED by verifier: was "on Newlyn market" - the source is the "Weekly Cornish Market Report" post of 22 Oct 2026, which gives "Pot Caught Mediterranean Octopus ... 33,150.8 kg across 833 boxes" for Monday 19 Oct across "Cornish auctions"/"local markets", not Newlyn alone]; "octopus are on the march again" 23 Oct; "octopus filling pots" 14-15 Nov 2026 [CORRECTED by verifier: was 14-15 Nov - the words are "the octopus that are currently filling their pots" in the post published Mon 16 Nov 2026 14:13]. So unlike 2025 (decline after August) octopus are still abundant inshore in mid-November 2026.
- DISAGREEMENT: Cornwall Good Seafood Guide (page "updated October 2026") says "In 2025 1087 tonnes of Octopus vulgaris were landed to SW fishing ports"; the MMO table gives 977 + 770 + 286 + 187 + 90 + 147 = 2,457 t for the top six ports in 2025. Different scope/time-cut presumably; MMO (A) preferred.
- Effect on angling (D - NO angling-specific study or report found; NOT FOUND): (1) octopus are now a realistic incidental shore catch at night over rough ground on crab, fish and squid-jig presentations, especially west of the Lizard and around Mevagissey; (2) heavy predation on crabs (and on potted lobster/scallops) plausibly reduces the edible/velvet/shore-crab forage that wrasse, bull huss, smoothhound, bass and cod use and makes peeler crab scarcer as bait - no data; (3) octopus compete with conger/huss for the same holes and will take legered baits intended for them - no data; (4) for squid/cuttle jigging, octopus by-catch is likely. Evidence for any of (2)-(4): THIN/none.

---------------------------------------------------------------------------------------------------
## 4. HOW CONDITIONS CHANGE CATCHABILITY - main candidate species
Evidence key: [S] = source read today (named); [R] = Cornish records pattern (section 2.0); [GEN] = general angling/fisheries knowledge, not re-verified today (grade D here); "none" = no evidence found.
Barometric pressure, general finding: WebSearch (16:14 UTC) for scientific evidence returned only angling journalism; no controlled study for sea bass, cod or any UK shore species was found. The swim-bladder mechanism is "plausible but unproven for feeding"; several writers attribute the apparent effect to the weather that accompanies pressure change (wind, swell, light, rain). So for EVERY species below the pressure column is angler lore (C) and is best read as a proxy for sea state and light. NOT FOUND: peer-reviewed pressure-catchability evidence.

| Species | Pressure & trend | Wind direction | Swell / surf | Water colour | Tide size & phase | Moon / brightness | Time of day | Temperature drop | Freshwater run-off |
|---|---|---|---|---|---|---|---|---|---|
| Bass | Lore: feeds on falling glass ahead of a front and in the first settled day after (C). Real driver = surf. | Onshore/alongshore wind that builds surf: N coast W/NW, S coast SW [S: UKBASS]; a strong offshore S/SE wind can "lift" a small N-coast swell into ideal surf [S: UKBASS]. Easterlies flatten/clear the S coast and are disliked [C: forum 30 Oct 2026 "hoping these easterly winds give up"]. | Moderate even surf with "deep water tables" is the single most important factor [S: UKBASS]; huge storm surf with weed = unfishable/empty; calm clear = night/lure only [GEN]. | Fizz to light colour ideal for lures; coloured water = bait; chocolate + weed poor [GEN]. | Surf beaches: 2 h either side of LW, can run to HW [S: UKBASS]; bigger tides move more food and open low-water gullies; estuaries: first of flood and last of ebb at mouths [GEN]. | Dark nights favour close-in bait fishing; bright moon + clear calm = harder [C/GEN]. | Dawn, dusk and darkness; "early mornings in Oct-Nov" in Mount's Bay [B via search]. Biggest MBAS fish of Nov 2026 came at night (16 Nov). | Gradual autumn cooling to 12-13 C = peak feed [R]; sharp frost-driven drops put estuary fish off for days [GEN]; adults leave as inshore water heads below ~10 C [GEN, cf. 8.5 C in tagging]. | Tolerant; "the attraction of fresh water to bass" on beaches (streams crossing the sand are features) [S: UKBASS]; but a heavy cold spate empties upper estuaries toward the mouths [GEN]. |
| Pollack | none/lore | Lee shore not needed; any wind that leaves the mark fishable; clear water preferred | Light-moderate swell fine; heavy swell colours kelp edges and scatters fish [GEN] | Clear to slightly coloured best for lures; bait in colour [GEN] | Tide run essential on headlands; flood into dusk classic [GEN] | Rise in the water column at dusk regardless; moonlit clear nights can keep them feeding high [C/GEN] | Dusk >> dawn > night > day [GEN] | None at 13 C; larger fish drift deeper only in mid-winter [S: BSF] - contradicted for Cornwall by the 13-2-0 in Jan 2026 [R] | Avoids low salinity; open-coast fish unaffected |
| Ballan wrasse | none | Offshore/light winds give the calm they need | STRONGLY negative above a moderate swell (forum: six weeks lost to swell; still caught 7 in "large swells" 6 Nov 2026) [C] | Clear best; "murky water" still produced a 4 lb 3 oz fish 29 Dec 2023 [C] | Flood over kelp gullies; bigger tides expose/cover more ground [GEN] | Daylight feeder - moon irrelevant [GEN] | Daylight only, best mid-flood [GEN] | Fully active at 13 C; slows below ~9-10 C [GEN]; a -2 C air frost on 21 Nov 2025 coincided with "nothing of any size" [C] | Negative - but wrasse were caught "in the river" 20 Nov 2026 during swell [C] |
| Squid | none | Offshore or light wind for clear calm water | Negative: need calm-to-light swell; "over sand in rougher sea, rock in calmer sea" [S: CGSG] | Clear water essential (sight hunters) [GEN] | Flood to HW at piers; moving water but not fierce [GEN/B] | Attracted to artificial light; bright moon spreads them out, dark nights concentrate them under lights [C/GEN] | "Move in around dusk and stay throughout the hours of darkness" [S: planetseafishing]; dusk + first hours best | Positive association with warm autumn seas ("bumper ... warmer seas" Nov 2025) [B]; eggs die <10 C (L. vulgaris) / <8 C (L. forbesii) [S: CGSG] | Strongly negative - avoid estuary plumes |
| Whiting | Lore: calm, cold, high-pressure nights (C) | Offshore/light | Slight sea best; fish move in after dark even in calm [GEN] | Feed in clear water at night; colour allows daytime catches [GEN] | Flood to HW; springs bring them closer [GEN] | Dark nights better than bright [GEN] | Night | Positive - arrive as the sea cools [S: BSF, CGSG "cold water species"] | Neutral to negative |
| Conger / bull huss / dogfish | none | Any | Tolerant; huss and dogfish feed in rough coloured seas; conger prefer a settled sea at the mark [GEN] | Colour helps daytime; irrelevant at night [GEN] | Conger best at slack water (HW/LW) on tide-swept marks; huss on the run of tide [GEN] | Dark, overcast nights best for conger [GEN] | Night; huss also dusk | None at 13 C; conger retreat/die in severe cold only [GEN] | Conger tolerate harbour/estuary-mouth salinities; huss and dogfish do not enter fresh plumes [GEN] |
| Small-eyed ray | Lore: settled spells (C) | Offshore/light after a blow | Best as a surf fines down; heavy surf moves them off [GEN] | Slight colour fine; they hunt sandeels by smell at night [GEN] | Bigger tides, LW up and the top of the flood on surf beaches [GEN]; December MBAS fish were all on 28-29 Dec club dates (no tide inference possible) | Night species; moon effect unknown (none) | Night | Present Oct-Mar at 10-14 C [R] | Avoids fresh water |
| Flounder | Lore: mild, overcast | Sheltered estuaries - wind matters little | n/a (estuary); on open beaches a slight surf | Feed well in colour; bright clear frosty water = slow [GEN] | "Neaps often beat springs"; neap-to-middle tides in outer channels; flood over the mud margins [B: Sea Angler via search] | Day feeder; moon irrelevant [GEN] | Daylight flood tides | First frosts trigger the pre-spawn feed and seaward drift [GEN]; move deep late winter [S: BSF] | Most tolerant species ("can travel far into freshwater" [S: BSF]) but big cold spates push feeding fish down-estuary [GEN] |
| Thick-lipped mullet | Lore: settled high pressure | Calm/sheltered | Negative (need calm harbour water) | Clear to light colour; turbid spate water = hard [GEN/D] | Flood into harbours; neaps keep water in drying harbours longer [GEN] | none | Daylight, dawn and dusk best | Specimens peak Nov-Mar in Cornwall [R] despite reduced feeding effort in winter [B: IFCAs via search] | Tolerant of brackish water but spate colour/flow puts them down [GEN/D] |
| Mackerel / scad / herring | none | Offshore/light, clear water | Negative in heavy swell at shore marks | Clear water needed for lures [GEN] | Flood to HW at piers/rock; tide run [GEN] | Scad/herring gather under lights after dark; moon effect unknown | Mackerel dusk; scad and herring dusk and night [GEN] | Mackerel thin out below ~11-12 C inshore [GEN]; still present to late Dec in 2023 and 2024 [R] | Negative |
| Coalfish | none | Any; surf beaches and harbours | Tolerant of surf ("run sandy surf beaches in a couple of feet of water" [S: talkseafishing]) | Either | Flood, HW at night [GEN] | Under harbour lights at night [GEN] | Dusk and night | Positive - a December arrival [R] | Tolerant of estuary mouths ("juveniles live inshore in harbours, estuaries" [S: talkseafishing]) |
| Spurdog | none | Any that leaves deep-water ledges fishable | Tolerant | Either | Tide run, deep water close in [GEN] | Night | Night | Winter fish (Oct-Mar specimens) [R] | Avoids |
| Red mullet | Lore: settled | Offshore/light | Negative above slight | Clear | Neap-to-middle, flood [GEN] | none | Night | Warm-water species; Nov is late-season - the +ve anomaly helps (D) | Avoids |

[CORRECTED by verifier: the next sentence was written as if the whole of 22 Nov were "a deepening low, falling pressure ... under (probably) thick cloud". MET Norway (run updated 13:17 UTC 21 Nov; see 2.1 note) has the low's trough over Cornwall ~03-06 UTC with the rain mostly 00-09 UTC, then RISING pressure (998 -> 1012 hPa by 18Z), wind W-WNW 11-13 m/s (21-25 kn) and clearing in the afternoon/evening. Consequences (D): (i) a dusk-into-night session on 22 Nov is under rising pressure and probably a partly clear sky with a 91-95 % moon up from 14:47 (ephem: illumination 90.5 % at 00Z, 94.9 % at 18Z) - brighter than the text assumes; (ii) a strong onshore W-WNW wind after a SE blow builds surf on the NORTH coast (UKBASS: "on the north coast, west and northwesterly winds tend to be best") and flattens/shelters the south coast after its overnight SE chop; (iii) the post-frontal wind is itself an obstacle to squid/LRF and lure presentation on exposed W/N-facing marks. Pre-dawn (the moonless 05:01-07:09 civil dawn window) coincides with the trough, heaviest rain and the SE-to-W wind shift.]
Applying this to 22 Nov 2026 (D): a deepening low, falling pressure, heavy rain and a building tide two days before a full moon under (probably) thick cloud favour, in order: (1) surf/reef bass on bait or lure wherever the swell is fishable and the water is not chocolate - away from estuary plumes on the ebb, or AT estuary mouths on the flood; (2) night-time rough-ground predators (huss, conger, dogfish) and small-eyed ray on adjacent sand; (3) pollack at dusk on any deep headland with clear enough water. They count against: squid, mullet, red mullet, mackerel/scad sight-feeders (need clear calm water), wrasse on exposed rock (swell), and upper-estuary anything. Flounder are the least-harmed estuary option. Which coast actually offers the right swell/clarity window is for the sea-state and clarity streams.

---------------------------------------------------------------------------------------------------
## 5. FIRST RANKING - which species offer the BEST Cornish shore fishing in late November
Scores are my judgement (D) on a 1-5 scale from the evidence above; "evidence" rates how well the Cornish record supports the row (strong / moderate / thin). (a) = probability of catching the species in one well-chosen session; (b) = numbers; (c) = size / specimen potential relative to the species and in absolute weight; (d) = sport quality.

| Rank | Species | (a) probability | (b) numbers | (c) size / specimen | (d) sport | Evidence | Why / caveats |
|---|---|---|---|---|---|---|---|
| 1 | **Bass** | 4 | 3 (5 for school fish in estuaries) | 5 (2-3 kg+ fish in Nov 2026; 7-15-0 in Nov 2024; doubles in Oct 2023; record 16-8-9) | 5 | STRONG and current (MBAS 4-16 Nov 2026; Newlyn handliners 9-15 Nov 2026; warm anomaly; science on delayed departure) | Best overall. Needs fishable surf/fizz and not-filthy water; venue-level evidence thin because clubs withhold marks. |
| 2 | **Bull huss** | 3-4 at night on rough ground | 2 | 5 (Nov-Dec is THE specimen window: 13-15-0, 13-10-11, 13-6-9) | 3 | STRONG (CFSA 2023, 2025; MBAS every December) | Night, big baits; marks not published. |
| 3 | **Pollack** | 3-4 at dusk on deep rock | 3 | 4 (3.1 kg on 2 Nov 2026; 8-11-0 Oct 2023; 13-2-0 Jan 2026) | 5 on lures | MODERATE (present in Nov 2026 log, absent from Nov/Dec 2023-25 sheets) | Needs clear-ish water and manageable swell; pollack retention rules - see rules stream. |
| 4 | **Conger** | 3 | 2 | 5 in absolute weight (31-6-13 in 2026; record 49-12-0) | 3 | MODERATE (few dated Nov fish: 6.65 kg 11 Nov 2024) | Night, harbour walls/deep rough ground; octopus competition (D). |
| 5 | **Small-eyed ray** | 3 | 2 | 4 (10-14-4 Nov 2023; 3.2-4.1 kg MBAS fish every Nov/Dec) | 3 | STRONG for presence | Night surf beaches with sandeel; best as surf fines down. |
| 6 | **Ballan wrasse** | 4 if the mark is fishable, else 1 | 4 (32 in a session 15 Nov 2024) | 4 (5-6 lb fish Nov-Dec 2023-24) | 4 on lures | MODERATE (one prolific W Cornwall poster, grade C, plus MBAS) | Daylight; swell is the limiter - six weeks of lost sessions this autumn. |
| 7 | **Squid** | 3 in clear calm water at dusk/night, 1 otherwise | 4 | 3 (to 2.6-3 kg) | 4 | MODERATE-THIN for the shore (strong commercial jig signal 2023-26; no Cornish shore catch log found) | Entirely clarity/swell dependent. |
| 8 | **Whiting / dogfish / pouting / rockling** ("scratching") | 5 (dogfish), 4 (whiting at night) | 5 | 1-2 | 1-2 | STRONG (most frequent MBAS entries) | Highest certainty, lowest quality; whiting fewer/smaller than reputation (stock). |
| 9 | **Flounder** | 3-4 in a normal week, 2-3 in this spate | 3 | 3 (3 lb+ fish Nov 2023, Jan 2025) | 3 on light gear | MODERATE | Lower/outer estuaries on the flood; spate caveat. |
| 10 | **Thick-lipped mullet** | 2 (3 in a settled harbour) | 2 | 5 relative (5-9 to 5-11 in Nov 2025; 7-6-3 Dec 2025) | 5 | STRONG for specimen size, THIN for catch rate | Spate/colour hurts; enclosed harbours. |
| 11 | Mackerel / scad / herring | 2-3 | 4 when found | 2 (scad 1-4-6 Nov 2024 = 127 %) | 2-3 (LRF) | MODERATE | Shoal-dependent, lit harbours at night. |
| 12 | Red mullet | 2 | 2 | 4 relative (three 100 % fish Nov 2025) | 2 | MODERATE (one year) | Calm clear nights, clean sand by reef. |
| 13 | Spurdog | 2 | 2-3 if a pack arrives | 4 (10-13 lb) | 3 | THIN for November shore (Oct/Feb/Mar specimens; boat fish 1 Nov 2026) | Deep-water ledges at night. |
| 14 | Coalfish | 1-2 (December fish) | 2 | 2 absolute, 5 relative | 3 | STRONG for December, none for November | Probably a week or three early, more so in a warm year. |
| 15 | Cod, gilthead, turbot, blonde/spotted ray, tope, triggerfish, bream, garfish, John Dory, octopus | 1 (octopus 2) | 1 | variable | variable | THIN | Bonus fish only. |
| - | Bluefin tuna (offshore rocks) | unknown | - | extreme | extreme | NONE for shore capture | Present inshore 7-11 Nov 2026; licence-controlled; no catch-rate basis. |

By criterion: (a) probability - dogfish > whiting/pouting/rockling > bass ~ wrasse (if fishable) > huss ~ pollack > conger ~ small-eyed ray ~ flounder > squid > mullet. (b) numbers - whiting/dogfish/pouting > school bass (estuary) ~ wrasse ~ squid ~ mackerel/scad (when found) > pollack > flounder. (c) specimen potential - conger (absolute) > bass ~ bull huss > pollack ~ small-eyed ray ~ thick-lipped mullet > spurdog > flounder/red mullet. (d) sport - bass ~ pollack on lures ~ mullet > wrasse ~ squid > huss/conger/ray > flounder > scratching.
Combined reading (D): the highest-value single session is a bass-first session that can roll into night predators - i.e. surf or reef-adjacent-to-sand ground fished from late afternoon through dusk into darkness (pollack/bass at dusk -> bass, huss, conger, small-eyed ray, whiting, dogfish after dark), with squid as the alternative only where water stays clear. The pre-dawn dark window (moonset 05:01 to first light, sunrise 07:46) is the other candidate bass slot; tide state then is for the tides stream (N coast HW ~03:00, LW ~09:10-09:25 on 22 Nov, i.e. an ebbing tide pre-dawn on the north coast).

Where the evidence is thin or conflicting: (1) no Cornish source read today gives the VENUE of individual fish - "where" rests on club base and commercial landings; (2) the wrasse/mullet "slow-down" expected from generic guides is contradicted by Cornish dated records; (3) whiting abundance conflicts between reputation and stock advice/club returns; (4) pollack absent from Nov/Dec 2023-25 MBAS sheets but prominent in Nov 2026; (5) squid evidence is commercial, not shore; (6) all pressure/moon effects are lore; (7) bluefin are demonstrably inshore but un-assessable as a shore target.

---------------------------------------------------------------------------------------------------
## 6. GAPS, NOT FOUND, CONTRADICTIONS, SOURCES

### 6.1 NOT FOUND / not done (with what was tried)
- In-estuary water temperature (any Cornish estuary): EA flood-monitoring API (level/flow/rain only); no other real-time source tried successfully.
- Year-on-year satellite analogues for 21 Nov 2020-2025: ERDDAP griddap `ncdcOisst21Agg_LonPM180` and `NOAA_DHW` returned HTTP 404 "Currently unknown datasetID" at 16:16 UTC (the same server answered at 15:21 UTC). Only the buoy series back to 22 Nov 2025 is available.
- Cefas WaveNet/SmartBuoy, Met Office OSTIA direct, WCO L4 buoy: not fetched (see 1.7).
- River flow for Tamar (Gunnislake), Camel (Denby), Fal (Tregony): not in the EA flow-station list returned.
- MBAS November 2025 sheet (.numbers format) not parsed.
- Venue-level November catch data for coalfish, spurdog, red mullet, small-eyed ray, bull huss, conger: none of the club/federation documents give venues.
- Cornish LRF/mini-species and shore-squid catch logs for November: one WebSearch each returned nothing local.
- Peer-reviewed evidence on barometric pressure, moon phase or wind direction vs catch rate for any target species: not found (one search); bass temperature thresholds could not be re-verified because the shared WebSearch quota (200 calls per turn across all agents) was exhausted at ~16:15 UTC. Sea Angler and Angling Trust pages returned HTTP 403 to direct fetch; Bangor bass-spawning PDF did not download.
- Current sardine-fleet fishing marks; any tuna/dolphin/bird-feeding record after 13 Nov 2026 (press stream).
- Angling-specific effects of the octopus bloom: none documented.

### 6.2 Contradictions noted
1. SST level and anomaly differ by product (section 1.4): buoys 13.1-13.5; MUR 12.7-13.5; CRW 12.9-13.9; OISST 13.3-14.3; Open-Meteo 12.9-14.2; anomaly +0.2..+0.7 (MUR) vs +0.9..+1.85 (CRW/OISST).
2. N vs S coast temperature difference: Open-Meteo +0.5-1.0 C for the SE coast; buoys +0.1-0.3 C; MUR nil.
3. Scilly: satellites cooler than mainland by 0.3-0.6 C; buoy/lightship equal to mainland.
4. Mullet and wrasse "winter slow-down" (generic guides, IFCA pages) vs Cornish records (winter specimen mullet; Nov-Dec wrasse hauls).
5. "Only small pollack inshore in winter" (BSF) vs CFSA 13-2-0 shore pollack in Jan 2026.
6. Whiting "widespread ... most common in autumn and winter" (BSF) vs "not doing well ... zero catch advice since 2023" (CGSG) and few/small registered fish.
7. Bass science says adults leave Oct-Nov; Cornish shore and handline data show the best adult fishing 18 Oct-early Dec. Reconciled (D) as the pre-departure aggregation plus a warm-sea delay, but it remains an inference.
8. Octopus 2025 tonnage: CGSG 1,087 t "SW ports" vs MMO 2,457 t for six ports; and MBA "declining in late summer" (2025) vs pots still filling mid-Nov 2026.
9. MMO-vs-MBA on shellfish impact (search summary): press reports of MMO data say lobster/crawfish/scallop "stable" while MBA reports -30 % lobster and >-50 % scallop. Not resolved.
10. Inside MBAS's own records, dates/weights of some Oct 2026 fish differ by a day / 42 g between news log and sheet (noted by the intel stream).

### 6.3 Sources (accessed 21 Nov 2026 UTC; grade)
- CCO real-time buoys https://coastalmonitoring.org/realtimedata/ - 15:18-15:19 - A.
- NOAA NDBC realtime2 (62107 Sevenstones, 62050, 62103, 62029, 62163) https://www.ndbc.noaa.gov/data/realtime2/ - 15:20 and 16:05 - A.
- NOAA CoastWatch ERDDAP (MUR 20 Nov, MUR anomaly 19 Nov, CRW 19 Nov, OISST NRT 18 Nov) https://coastwatch.pfeg.noaa.gov/erddap/griddap/ - 15:21 - A.
- Open-Meteo Marine API (SST, past 92 d + forecast) - 15:17 - A (model); Open-Meteo forecast API (air temp/rain, past 31 d + 3 d) - 16:05 - A (model).
- Environment Agency flood-monitoring API (flow at Restormel, Gwills, St Erth, Trebrownbridge, Helston, Tamarstone Bridge) - 16:05 - A.
- seatemperature.org town pages (Bude, Padstow, Newquay, St Ives, Penzance, Falmouth, Looe, Hugh Town) - 16:06 - B.
- Mount's Bay AS recorder sheets and news log https://mountsbay.weebly.com/ - files fetched 15:20-15:21 by intel stream, parsed ~16:08-16:12 - B.
- CFSA Annual Recorder's Reports 2023, 2024, 2025; shore updates Oct 2024, Oct 2025, Jul 2026, Sep 2026 https://cornishfed.weebly.com/ - fetched 15:19 by intel stream, parsed ~16:09-16:12 - B.
- MMO Octopus & Shellfish Landings Data Summary Aug 2026 (assets.publishing.service.gov.uk) and MMO guidance page (updated 9 Nov 2026) - 16:11 - A. MBA 2025 Octopus Bloom Non-Technical Summary (Jan 2026) - 16:11 - A/B.
- Cornwall Good Seafood Guide species pages (herring, cuttlefish, red mullet, grey mullet, mackerel, gilthead bream, octopus, pollack, whiting, cod, spurdog, small-eyed ray) https://cornwallgoodseafoodguide.org.uk/fish-guide/ and "The dark and inky art of squid fishing" (13 Dec 2022) - 16:13-16:15 - B. (sardine, sprat, bass, squid, flounder, black-bream, scad, garfish pages returned HTTP 500.)
- britishseafishing.co.uk species pages (38 pages; raw `web/bsf_*`) and "Lure fishing for squid" (2021) - 16:12-16:13 - B. planetseafishing.com "Hunting the Jet Propelled Squid" (J. F. Costello, 11 Nov 2013) - 16:13 - B. talkseafishing.co.uk coalfish guide (2021) - 16:15 - B. UKBASS "Surf Angling for Bass in Cornwall" (N. Hester, BASS 31/32, 1984) https://www.ukbass.com/surf-angling-for-bass-in-cornwall/ - 16:14 - B.
- WebSearch result summaries (16:11-16:15), papers/pages NOT opened: Pawson & Pickett 1996 (JMBA); Pawson et al. 2007 (ICES JMS); Lincoln et al. (Bangor, bass spawning areas); Wright et al. 2024 (Movement Ecology) https://movementecologyjournal.biomedcentral.com/articles/10.1186/s40462-024-00482-w ; Sea Angler flounder pieces (pressreader/everand); NW IFCA and K&E IFCA mullet pages; Angling Trust mullet introduction - B at best (second-hand).
- Other streams' compiled files (read, not modified): `intel/press_social_signals.md` (Newlyn "Through the Gaps" blog, CBWPS sightings), `intel/shops_clubs_matches.md`, `intel/forums_blogs_video.md`, `tides_numeric.part.md`, `raw/light_moon/metno_*.json`, `rules.md`.

---------------------------------------------------------------------------------------------------
## 7. Verifier additions (adversarial verification, 2026-11-21 16:25-17:00 UTC)

### 7.1 Counter-evidence to the ranking (D unless stated)
- **Bull huss at #2 rests on specimen SIZE, not catch probability.** Of the three 13 lb+ county fish, two (Nov 2023 13-15-0, Nov 2025 13-10-11) are by the same angler (CFSA, confirmed); the MBAS Nov 2023 and Nov 2024 sheets contain NO bull huss - every MBAS huss is a late-Dec (29 Dec) or October fish. The specimen window is real, but probability (a) of 3-4 is generous for a single 22 Nov session; 2-3 is better supported by the MBAS November sheets.
- **Bass #1 survives**, but the strongest current evidence (MBAS 2-16 Nov 2026; Newlyn handliners posts 8, 9, 16 Nov) is Mount's Bay/West Cornwall; Wright et al. 2024 (A) put the move to deeper spawning areas in Q4. The forecast W-WNW 21-25 kn wind after a SE blow (MET Norway) builds N-coast surf (UKBASS: N coast best on W/NW) - so the bass case is plausibly stronger for the north coast on 22 Nov afternoon/evening than the text implies; the S coast gets an offshore/cross-shore W wind after an overnight SE chop.
- **Moon**: the session-day evening is under clearing skies with a 91-95 % moon up from 14:47 (ephem). The ranking text assumes "probably clouded"; that is less likely after the front (D). Bright moon + clear water is the classic negative for close-in bass/whiting/squid under lights (lore, C).
- **Coalfish**: talkseafishing (B) puts late October-March inside the shore season with numbers building from mid-October, so "none in November" is a Cornish-records statement (CFSA/MBAS), not a biological one; the warm anomaly still argues for a late showing.

### 7.2 Species the catalogue omitted or under-recorded (sourced; all CFSA, B)
- Chub mackerel (Scomber colias): CFSA shore record 1-4-6 (0.578 kg, Sid Pender, Mounts Bay AS, 2011); a 100 % shore fish (1-4-0, Mevagissey SAC) in AUGUST - a late-summer visitor; not a realistic late-Nov target, but it should be in the "every species" list.
- Atlantic bonito: CFSA shore record 0-12-1 (0.342 kg, Camborne AA, 2014) - confirms shore capture is possible; MBAS 2026 bonito were BOAT fish (20-25 Sep, 2.2-3.4 kg). Nil probability by late Nov.
- Anglerfish: CFSA senior SHORE record 45-0-0 (Camborne AA, 1968) (a 61-0-0 in another CFSA list is a 2015 St Columb SAC fish in a different (boat) table). Exceptional only.
- Red gurnard: CFSA entries 0-14-0 (ECC Ports), 1-3-0 (Truro City) in addition to the 0-10-9 cited.

### 7.3 Remaining gaps after verification
- Independent (non-CCO) inshore SST: none found. seatemperature.org relays the same CCO buoys; Western Channel Observatory L4 not fetched; Cefas SmartBuoy/OSTIA not accessed. The three genuinely independent families used are CCO buoys, NDBC/Met Office platforms (62107, 62050) and satellite/model (MUR re-fetch, Open-Meteo re-fetch) - all agree on 13.0-13.9 C and a positive anomaly.
- CRW baseline period (1985-2012) not stated in the ERDDAP metadata - UNVERIFIED.
- Open-Meteo forecast re-fetch blocked (daily request limit, 16:25 UTC); rain amounts for 22 Nov disagree between Open-Meteo (22-48 mm) and MET Norway (16-29 mm).
- Air-frost of 13 Nov rests on one model analysis (Open-Meteo); no Met Office station obs checked - UNVERIFIED independently.
- Pawson & Pickett 1996, Lincoln et al. (Bangor), Sea Angler flounder pieces, IFCA/Angling Trust mullet pages: not opened by verifier either.

## Verification log
| # | Claim (as written) | Source used by verifier | Accessed (UTC) | Result |
|---|---|---|---|---|
| 1 | Perranporth CCO buoy 13.2 C (14:30) | coastalmonitoring.org chart=76 re-fetch, latest row 15:30 = 13.2 | 16:26 | confirmed |
| 2 | Penzance buoy 13.5 C | CCO chart=75, 15:30 = 13.5 | 16:26 | confirmed |
| 3 | Porthleven buoy 13.1 C | CCO chart=107, 15:30 = 13.1 | 16:26 | confirmed |
| 4 | St Mary's Sound buoy 13.2 C | CCO chart=113, 15:30 = 13.2 | 16:26 | confirmed |
| 5 | Looe Bay buoy 13.3 C (14:00) | CCO chart=98, 15:00 = 13.4 | 16:26 | confirmed (within 0.1) |
| 6 | Sevenstones 62107 13.1 C; identity/position | NDBC realtime2 + station page (50.102N 6.100W) | 16:25 | confirmed |
| 7 | 62050 = E1, 13.9 C ("from memory") | NDBC station page "E1" 50.000N 4.400W; 15Z WTMP 13.9 | 16:25 | corrected (caveat removed, identity verified) |
| 8 | 62103 Channel LV 14.3 C | NDBC station page 49.900N 2.900W | 16:25 | confirmed |
| 9 | Pressure falling 21 Nov: 62107 1010.5->1008.2 (12-14Z); K1 995 | NDBC re-fetch: 1010.5/1009.2/1008.2/1007.4 (12-15Z); K1 995.0 (14Z), 993.6 (15Z) | 16:25, 16:40 | confirmed |
| 10 | 62107 Hs 3.2 m at 14:00 20 Nov; 20 Nov mean SST 13.19 | researcher raw 15:20 file (Hs 3.2 confirmed); mean is from 9 obs only | 16:40 | confirmed / annotated |
| 11 | Open-Meteo SST Bude 13.7, Land's End 13.4, Looe 13.6, St Mary's 13.0 (21 Nov 15Z) | marine-api.open-meteo.com re-fetch | 16:25 | confirmed |
| 12 | Open-Meteo values at Helford / Falmouth / Carrick Roads are local | resolved cell centres in researcher raw JSON | 16:45 | corrected (cells offshore; Carrick = Nare cell) |
| 13 | MUR 20 Nov ~13.2 C near Land's End | ERDDAP jplMURSST41 re-fetch 50.10N 5.70W = 13.198 (data 20 Nov 09Z) | 16:32 | confirmed |
| 14 | MUR anomaly baseline 2003-2014 | ERDDAP info jplMURSST41anom1day | 16:32 | confirmed |
| 15 | OISST anomaly baseline 1971-2000 | ERDDAP info ncdcOisst21NrtAgg ("Climatology is based on 1971-2000 OI.v2 SST") | 16:32 | confirmed |
| 16 | CRW anomaly baseline 1985-2012 | ERDDAP info NOAA_DHW (period not stated) | 16:32 | unverifiable |
| 17 | seatemperature.org late-Nov averages and "today" values | researcher raw pages re-parsed | 16:35 | confirmed values; corrected independence (relays CCO buoys) |
| 18 | CCO daily means (22 Nov 2025, 10 Oct, 7 Nov, 21 Nov) | researcher derived CSV | 16:35 | confirmed (internal consistency only) |
| 19 | Restormel (Fowey) 8.92 m3/s @15:45, peak 16.0 | EA flood-monitoring E45746 (label RESTORMEL) live: 8.915 @15:45, 8.819 @16:00; raw peak 16.032 | 16:30 | confirmed |
| 20 | Helston County Bridge 0.74 @15:30 | EA 48198 live 0.739 @15:30 | 16:25 | confirmed |
| 21 | Tamarstone Bridge 3.06 @15:15, peak 7.3 | researcher raw 47174 (3.063; 7.272) | 16:30 | confirmed (same source) |
| 22 | 22-48 mm rain on 22 Nov | MET Norway locationforecast (run 13:17Z): 16-29 mm; Open-Meteo re-fetch refused | 16:55 | disagreement recorded (upper end) |
| 23 | 22 Nov = falling pressure / deepening low all day | MET Norway: trough 03-06Z (998 hPa), rising to 1012 by 18Z, W-WNW 11-13 m/s | 16:57 | corrected |
| 24 | Sunrise 07:46, sunset 16:29, moonset 05:01, moonrise 14:47, full moon 24 Nov 14:53, ~90 % lit | PyEphem at 50.10N 5.54W | 16:42 | confirmed (illum 90.5 % 00Z, 94.9 % 18Z) |
| 25 | N coast HW ~03:00, LW ~09:10-09:25 on 22 Nov | EasyTide 0546 Newquay re-fetch: HW 02:45 6.15 m, LW 09:12 1.60 m, HW 15:06, LW 21:36 | 16:40 | confirmed |
| 26 | CFSA Fish of Month: SER 10-14-4 Nov 2023; coalfish Dec 2023/24/25 (2-9-10, 5-0-0 285.6 %, 4-5-0 246.4 %); red mullet 1-8-11 Nov 2025; scad 1-4-6 Nov 2024; ladies bass 7-15-0 Nov 2024 | CFSA report PDFs (pdftotext) | 16:36 | confirmed |
| 27 | Bull huss 13-15-0 (Nov 2023), 13-10-11 (Nov 2025), 13-6-9 (Dec 2025) | CFSA PDFs | 16:36 | confirmed (two by same angler) |
| 28 | Pollack 13-2-0 Jan 2026 (175 %); spurdog 13-14-4 Mar 2026; conger 31-6-13; cod Dec 2023 x3; whiting 2-5-10; thick-lip 7-6-3 (140.7 %), 5-11-11, 5-9-6 | CFSA PDFs | 16:36 | confirmed |
| 29 | CFSA records: bass 16.8.9 (2013), pollack 13.4.10 (1995), conger 49.12.0 (1997), spurdog 12.15.12 (1975), tunny 66.12.0 (1985) | CFSA 2025 report, senior shore records table | 16:36 | confirmed |
| 30 | MBAS sheet entries Nov 2023 / Dec 2025 / Oct 2026 | MBAS .xls/.xlsx (pandas) | 16:38 | confirmed |
| 31 | MBAS 70-entry species tally | not re-derived | - | unverifiable |
| 32 | MBAS Nov 2026 news-log weights (3060 g + 2110 g "16/11" etc.) | MBAS latest-news-2026 raw | 16:39 | confirmed weights; shore status unverifiable |
| 33 | Couch's bream 4.082 kg boat, 7 Nov 2026 | MBAS news ("4082g ... aboard Bite Adventures on the 7th November") | 16:39 | confirmed |
| 34 | MMO octopus: Newlyn 47 -> 977 -> 1,522 t; other ports; 7e most landings | MMO PDF (pdftotext) | 16:37 | confirmed |
| 35 | MBA: crab/scallop >50 %, lobster 30 %, -1,206 t / -87.6 t / -3,165 t, 57.6 %, "appears to be high", decline late summer 2025 | MBA PDF | 16:37 | confirmed |
| 36 | CGSG octopus 1,087 t (2025) | CGSG octopus page raw | 16:34 | confirmed |
| 37 | 33,150.8 kg octopus "on Newlyn market" Mon 19 Oct | Newlyn blog Oct feed (Weekly Cornish Market Report, 22 Oct) | 16:44 | corrected (Cornish auctions, not Newlyn alone) |
| 38 | "busy on the bass again" 9 Nov; squid "really got in amongst them"; "marauding bluefin and dolphins" | Newlyn blog Nov feed, post 9 Nov 12:20 | 16:44 | confirmed |
| 39 | "enjoying a few good fish" and "octopus filling pots" 14-15 Nov | Newlyn blog post 16 Nov 14:13 | 16:44 | corrected (post date 16 Nov) |
| 40 | "huge shot of bass" ~5 Nov | Newlyn blog post 8 Nov 18:13 | 16:44 | confirmed text; catch date unverifiable |
| 41 | "bumper landings of squid ... warmer seas" 17 Nov 2025 | Newlyn blog 2025 analogue feed, post 17 Nov 2025 ("late summer and warner [sic] seas than normal") | 16:44 | confirmed |
| 42 | Bluefin: 10 off Kilgerran Head 7 Nov; Mounts Bay/Trenow 8 Nov; tuna off East Pentire 11 Nov | CBWPS daily sightings raw | 16:46 | confirmed (plus a 2nd 8 Nov report "several Bluefin Tuna heading west") |
| 43 | BSF pollock (larger fish deeper in winter; some stay shallow) | BSF pollock page | 16:33 | confirmed (page adds "usually smaller specimens") |
| 44 | BSF flounder, plaice (Mar-Sep), turbot (coldest months), garfish, dab, small-eyed ray (~100 yd), spurdog, lesser weever, whiting | BSF pages | 16:33 | confirmed (paraphrases faithful) |
| 45 | CGSG cod "increasingly rare ... cold water"; whiting ICES zero catch since 2023, poor recruitment in warm years | CGSG pages | 16:33 | confirmed |
| 46 | CGSG gilthead spawning Nov-Dec; mackerel winter gill nets S coast; herring ICES June 2025 "very low", mainly S coast; cuttlefish overwintering; spurdog "highly migratory"; pollack spawns Jan-Apr, deeper with growth; red mullet warm-water | CGSG pages | 16:33 | confirmed |
| 47 | CGSG squid: eggs die <10 C / <8 C; sand in rough, rock in calm; 167 t Feb vs 23 t Apr 2022 | CGSG "dark and inky art of squid fishing" raw (the other cgsg_squid file is empty) | 16:34 | confirmed |
| 48 | talkseafishing coalfish quote "in the south classed as an autumn and winter fish" | talkseafishing raw | 16:35 | corrected (quote not present; real wording inserted) |
| 49 | planetseafishing squid: lights, move in at dusk, stay through darkness | PSF raw | 16:33 | confirmed |
| 50 | UKBASS: deep-water tables; 2 h either side of LW; sandeel best bait; lugworm good at night; N coast W/NW, S coast SW; offshore S/SE lift; weed in gullies; fresh water | UKBASS raw | 16:35 | confirmed |
| 51 | Wright et al. 2024: mature bass 8.5 C during movement to deeper spawning areas | Europe PMC abstract PMC11167799 | 16:52 | confirmed (upgraded to A; Q4-Q1 timing noted) |
| 52 | Pawson & Pickett 1996; Lincoln et al. (Bangor) | not opened (Bangor file is an HTML challenge page) | 16:50 | unverifiable |
| 53 | Forum: 32 wrasse to 5-5 on 15 Nov 2024; 6-5 wrasse 22 Dec 2023; "river stacked with bass" 30 Oct 2026; 5 wrasse on lures in a river 20 Nov 2026; "nearly 6 weeks" | talkseafishing threads raw | 16:47 | confirmed |
| 54 | Sea Angler flounder claims (neaps beat springs; Fowey/Looe big flounder; Tamar averages) | not openable (403) | - | unverifiable |
| 55 | Ballan wrasse activity falls below ~9-10 C; mackerel thin below 11-12 C; conger above ~10 C | no source found | - | unverifiable |
| 56 | Air frost 13 Nov (Tmin -0.6 to -2.8 C) | researcher raw Open-Meteo (transcription confirmed); no independent obs | 16:50 | unverifiable independently |

Tally: 56 checks - confirmed 41 (row 10 with an annotation, row 40 text only), corrected 7 (rows 7, 12, 17, 23, 37, 39, 48), source disagreement recorded 1 (row 22), partly confirmed/partly unverifiable 1 (row 32), unverifiable 6 (rows 16, 31, 52, 54, 55, 56).
Verifier raw files: `fishing/research/raw/species_sst_verify/` (CCO pages, NDBC, Open-Meteo marine, MUR/ERDDAP info, EA, EasyTide 0546, MET Norway, Europe PMC, CFSA/MMO/MBA text extractions).
