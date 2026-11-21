# Sea-state observations and water-clarity evidence (workstream 3, observational part)

Target: Sunday 22 Nov 2026 (UTC). Compiled 2026-11-21 ~16:15 UTC. Raw: `raw/sea_state/` (parsed CSVs `parsed_cco_*_month.csv`).
Grades: A instrument/model, B secondary, C anecdotal, D own inference.

## 1. Observations (Channel Coastal Observatory buoys, grade A)
Source: https://coastalmonitoring.org/realtimedata/ (pages `cco_*_waves_month_20261121T152xZ.html`, fetched 15:20-15:22 UTC, data to 21-11 14:30 UTC). Records ~hourly from 25 Oct. Daily maximum Hs (m) / mean Hs (m) / Tp(s)/dir(deg) at the maximum. Computed by me (D arithmetic on A data).

| Day | Bideford Bay (N) | Perranporth (N) | St Mary's Sound (Scilly) | Penzance (Mount's Bay) | Porthleven | Looe Bay | Start Bay |
|---|---|---|---|---|---|---|---|
| 08 Nov | .3/.2 | .4/.3 | 1.9/.9 (6.5s,219) | .9/.4 | .8/.4 | .8/.3 | .7/.2 |
| 09 | .7/.4 | .8/.4 | 3.2/2.6 (7.4s,104 E) | 1.4/1.2 | 1.5/1.0 | 1.7/1.3 | 2.5/1.8 |
| 10 | .9/.6 | 1.1/.8 | 2.9/2.4 | 1.4/1.2 | 2.5/1.9 (10.5s,222) | 1.9/1.6 | 2.6/2.1 |
| 11 | 1.3/.7 | 1.3/1.0 | 2.1/1.8 | 1.2/1.0 | 2.4/1.8 | 1.9/1.3 | 1.4/1.1 |
| 12 | .8/.5 | 1.5/1.0 | 1.7/1.5 | .8/.5 | 1.2/.8 | 1.0/.8 | 1.4/1.2 |
| 13 | .3/.2 | .8/.5 | 1.5/1.0 | .5/.4 | .7/.5 | .6/.5 | 1.1/.7 |
| 14 | .5/.4 | .5/.4 | 1.9/1.3 | 1.1/.9 | 1.2/1.0 | 1.2/.9 | .9/.6 |
| 15 | 1.8/.9 | 2.3/1.2 | 2.3/1.8 | 1.7/1.1 | 2.9/1.7 | 2.0/1.4 | 1.2/.9 |
| 16 | 1.5/1.0 | 2.2/1.4 | 2.0/1.5 | 1.7/1.0 | 2.0/1.5 | 1.8/1.2 | 1.8/.9 |
| 17 | 3.5/2.2 (10.5s,274) | 3.5/2.5 (11.8s,260) | 3.8/2.9 (11.1s,200) | 2.3/1.8 | 4.0/3.2 (11.1s,228) | 2.6/2.1 | 1.8/1.4 |
| 18 | 4.2/3.5 (15.4s,276) | 4.7/4.0 (18.2s,288) | 3.0/2.6 | 1.8/1.5 | 3.9/3.5 | 2.3/2.1 | 1.9/1.5 |
| 19 | 3.2/2.8 (14.3s) | 4.4/3.6 (16.7s,283) | 2.6/2.3 | 1.3/1.2 | 3.5/3.1 (16.7s,241) | 1.9/1.7 | 1.6/1.2 |
| 20 | 3.0/2.3 | 4.2/3.0 (12.5s,277) | 2.6/1.9 | 1.3/1.0 | 3.8/2.5 | 2.2/1.5 | 1.7/1.1 |
| 21 (to 14:30) | 1.6/1.3 | 2.2/1.6 (11.1s,273) | 1.6/1.4 | 1.1/.8 | 1.8/1.4 | 1.2/1.0 | .9/.7 |

(Days 1-7 Nov: mostly <1.5 m N coast; Scilly/Start Bay 1-2.8 m with E-NE short-period sea 3-5 Nov, e.g. Start Bay Hs 2.8 on 4 Nov.)
Key events:
- Biggest event of the whole 25 Oct-21 Nov record: Perranporth Hs 5.2 m, Hmax 7.32 m, Tp 13.3 s, from 286 deg at 06:00 on 25 Oct (the CCO page also lists "highest Hs 2026: 23-10, 5.7 m"; storm alert threshold 5.40 m, swell threshold Te 15 s).
- Most recent big-swell event 17-20 Nov: W/WNW groundswell, Tp up to 18.2 s at Perranporth 18 Nov (Hs ~4.7, Hmax up to 8.74 m at the 18 Nov peak per the pages' own rows), Porthleven Hs 4.0 m 17 Nov 20:30 (228 deg SW). North coast ~3-4.7 m for 3 days; sheltered Mount's Bay/Looe/Start Bay only 1.3-2.6 m (WNW swell shadowed). Already decaying 21 Nov: Perranporth 14:30 Hs 1.02 m, Hmax 1.54, Tp 10.5 s, 274 deg, Te 8.8 s.
- Sea temperature 21 Nov: Perranporth 13.2, St Mary's 13.2, Penzance 13.5, Porthleven 13.1, Looe 13.3, Start Bay 13.6, Bideford 12.7 C (A). Sevenstones NDBC 62107 (https://www.ndbc.noaa.gov/data/realtime2/62107.txt, fetched 16:04 UTC): 15:00 WVHT 1.5 m, APD 8 s, SST 13.1 C, pressure 1007.4 hPa falling (1009.2 at 13:00) - A.
- Named storms since 1 Nov 2026: NOT FOUND (did not locate a Met Office/Irish storm-name list; the 17-20 Nov swell is consistent with a deep Atlantic low but I cannot name it).
- Data caveats: Port Isaac buoy columns misparse / short record (only ~1 m Hs, no direction) - treat as THIN DATA; Wave Hub page returned 2018 data (stale); Bideford Bay record contains one odd 11.1 m value on 25 Oct (likely spike/different column) - ignore. Cefas WaveNet, 62103 Channel LV, 62050 E1, 62029 K1: NOT FETCHED (budget; only Sevenstones tried).

## 2. Direct clarity evidence - what was actually found
- NASA Worldview snapshot API (wvs.earthdata.nasa.gov) for 19/20/21 Nov: returned identical all-black 1040x600 images (tiles unavailable via proxy). NO satellite colour evidence. Sentinel/Copernicus, EUMETSAT, PML NEODAAS: not attempted successfully. NOT FOUND.
- SWL WaterFit Live: connection failed (000). Surfers Against Sewage alerts page: HTTP 403. NOT FOUND (CSO status unknown).
- WebSearch for surf/dive visibility reports Nov 2026: nothing on clarity. Only surf-forecast.com (B) pages with SST (Caerhays 14.9 C on 2 Nov, Newlyn Harbour Wall 14.3 C on 5 Nov) - older than buoy data, not clarity. Webcams, dive-centre visibility, china-clay St Austell Bay, plankton notes: NOT FOUND/not reached.
- So all clarity figures below are INFERRED (D) from wave history and rain (EA rain tables belong to the orchestrator).

## 3. Per-sector clarity estimate for 22 Nov (all D, inferred; no observation)
Forecast context (Open-Meteo best_match hourly, `raw/sea_state/derived_wave_forecast_all_models_20261120-24_hourly.csv`, run 15:18 UTC, A model output): 22 Nov Hs ranges: Bude 1.1-3.9, Perranporth 1.1-3.9, Port Isaac 1.1-3.7, Trevose 1.0-3.6, Godrevy 1.0-3.0, St Ives 1.1-2.1, Pendeen/Cape Cornwall 1.8-4.0, Land's End/Longships 2.2-4.1, Newlyn 1.6-2.9, Marazion 1.7-2.7, Porthleven/Mullion 2.1-3.8, Lizard 2.2-4.2, Coverack/Helford 2.2-4.0, Falmouth 1.7-2.4, Carrick Roads 1.2-2.2, Dodman-Fowey-Par 1.5-2.4, Looe/Polperro 1.7-2.3, Rame/Whitsand/Saltash 1.7-2.4, Scilly (St Mary's/Western Rocks/Bishop) 2.4-4.7, Wolf Rock 2.2-4.2. Wind-wave share 1.9-2.7 m in the west vs swell ~1-1.9 m: a rising SW'ly blow through the day (mean dir 215-250 deg), i.e. a fresh wind sea replacing the decayed groundswell. Compare 21 Nov daily mean modelled Hs 1.1-2.3 m.
Inference: the 17-20 Nov 4 m+ swells churned sand/suspended sediment on all open N and W beaches; by 21 Nov Hs fell to ~1-2 m but a renewed SW sea of 2-4 m on 22 Nov re-suspends it. Clarity ranking (poor to better), D:
- Poor/brown-milky: all open north-coast surf beaches (Bude-Perranporth-St Agnes-Godrevy) on the flood and with 3-4 m late; Porthleven/Loe Bar and Mullion-Lizard west side (SW sea onshore, plus Loe/Cober outflow); Penzance-Marazion front (sandy bay, but sheltered from W swell, moderate).
- Moderate: St Ives Head/Pendeen/Cape Cornwall/Land's End (rocky, deep water close in; white water but little sand), Scilly Hugh Town side, Wolf Rock/Longships/Bishop (offshore, clear blue-green water but heavy surf).
- Better (relative): Falmouth/Carrick Roads-Fowey-Looe-Whitsand (lee of SW, Hs ~1.5-2.4 m but wind-driven chop; estuaries carry river-flow colour - rain data needed; THIN DATA). Estuaries (Camel, Hayle, Fal, Fowey, Looe, Tamar): clarity governed by river flow after the 17-21 Nov period; not assessed here (EA tables are the orchestrator's). THIN DATA.
Everything in this section is UNOBSERVED.

## 4. Weed and drift (D, general)
The 17-20 Nov W/NW swell (Tp 12-18 s) will have torn kelp/wrack onto open beaches; expect loose weed in the surf on N and W beaches on 22 Nov with new SW sea lifting more; weed less on the sheltered south-east coast. No observation of weed found. Lateral drift: with SW wind the current/longshore drift runs to the north-east on south-facing beaches (D, no measurement).

## 5. Species rules of thumb (grade B/C - literature recall, NOT verified live this session)
I did not retrieve citable fishing-literature pages in this run; the following are general-knowledge claims from memory and carry NO URL (so by hard rule 1 treat as D / unverified): bass favour surf-coloured water with some turbidity after swell and a lull; rays, turbot, whiting, codling, flounder are less clarity-dependent and feed in coloured water on sandy surf beaches; pollack/wrasse prefer clearer water over rough ground and go off in heavy brown water; conger/huss are insensitive to clarity; mullet prefer calm sheltered harbours/estuaries and are poor in heavy surf; squid need clear water. NOT FOUND: cited sources.

## Gaps
Satellite imagery, webcams, dive visibility, CSO alerts, Cefas WaveNet, other Met Office buoys, storm names, cited fishing literature.
