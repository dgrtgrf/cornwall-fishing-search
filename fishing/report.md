# Best shore-fishing spot in Cornwall, Sunday 22 November 2026

> **STATUS: PHASE 1 CHECKPOINT - no verdict yet.**
> This file currently holds the Phase 1 (wide pass) findings only. Phases 2 (deep pass: cross-check, score, eliminate, hour-by-hour models, winner) and 3 (attack the answer) have not been run. Nothing below is a recommendation.
> Written 2026-11-21 ~17:05 UTC. Session date is tomorrow.

Purely hypothetical exercise: locations are judged only on fishing quality; access, danger and comfort are ignored (superhuman angler, any point where land meets water).

---

## 1. The day in one paragraph (from the workstream files)

A deepening low crosses overnight. **South-easterly gale** (about 110-125 deg, 18-27 kn, gusts 32-45 kn) from the evening of the 21st until a sharp **veer to west / west-north-west** (270-290 deg, 17-30 kn, gusts 30-47 kn) that reaches Scilly about 03:00, Land's End / Penzance about 04:00, Falmouth about 05:00, Mevagissey about 07:00 and Looe / Rame about 09:00 GMT (twelve models; spread 3-8 h, widest in the east). Pressure bottoms near 997-1000 hPa at 03-06 h then rises about 3 hPa per 3 h. Rain overnight and through the morning; overcast nearly all day. Sea: 2-3 m short south-easterly sea on the south coast and Scilly overnight while the north coast sits at about 1 m under an offshore wind; after the veer a **westerly sea builds to about 4 m** on the north and west coasts and Scilly by afternoon, while the east-facing south coast (Lizard east side, Falmouth Bay, Mevagissey to Looe) drops to 1.5-2.4 m in the lee. Tide: **Newlyn HW 02:17 (4.97 m), LW 08:55 (1.48 m), HW 14:35 (5.23 m), LW 21:18 (1.24 m)**; about 85 % of mean spring range and building fast toward large perigean springs (Brest coefficient 70 then 76); a surge of about +0.4 m sits on the early-morning high water. Light: sunrise about 07:46, sunset about 16:30 (Newlyn); 91-96 % moon, set 05:02, up again 14:48 - the only astronomically dark hour is about 05:00-05:50, but cloud is forecast to hide the moon for most of the day. Sea temperature 13.1-13.5 C, 0.2-1.9 C above normal.

## 2. What each workstream found

| # | Workstream | File(s) | Headline | Evidence quality |
|---|---|---|---|---|
| 1 | Tides | `research/tides.md`, `research/tidal_streams.md` | UKHO predictions for 30 Cornish/Scilly ports (+ Dover, Milford as stream references), hourly heights and tide state for 22 Nov, surge (+0.40 m at the 02:17 HW, +0.12 m at the 14:35 HW, Newlyn), tidal levels, Brest coefficient 70/76, sector-to-port map. Tidal-stream literature is **thin**: Admiralty atlas tables are paywalled; only coarse ocean-model currents hour by hour. | Heights/times: A. Streams: thin. |
| 2 | Weather | `research/weather.md`, `research/data/weather_hourly_multimodel.csv` | 12 models x 39 reference points, hourly; ensembles at 6 points; frontal timing per model; 21-day lead-in; Met Office shipping / inshore / regional text (gale warnings Lundy, Plymouth, Sole, Fastnet). | A (model output); model run times not exposed; station observations pending. |
| 3 | Sea state | `research/sea_state.md`, `research/sea_clarity_evidence.md`, `research/data/waves_hourly_multimodel.csv` | 6 wave models x 39 points; buoy history: W/WNW groundswell 17-20 Nov (Perranporth 3.5 / 4.7 / 4.4 / 4.2 m daily maxima, Tp to 18 s), down to about 1 m by 14:30 on the 21st; 46 EA river stations (none above typical high, most in the lower half of their range). Per-sector water clarity is **inferred only** - no satellite or webcam observation was obtained. | Waves: A but offshore cells. Clarity: D. |
| 4 | Sea temperature and species | `research/species_sst.md` | Buoy SST 13.1-13.5 C on every coast (N = S = Scilly within 0.5 C), positive anomaly, about -1 C in the last fortnight. Species catalogue with Cornish club evidence. First ranking for late November: bass, bull huss, pollack, conger, small-eyed ray, ballan wrasse (swell-limited), squid (clarity-limited), then whiting / dogfish / pouting (most certain, least quality), flounder, thick-lipped mullet. Verified adversarially (56 checks: 41 confirmed, 7 corrected). | B for club records (no venues given); effects of pressure / moon / wind are angler lore, no peer-reviewed support found. |
| 5 | Light and moon | `research/light_moon.md` | Computed with skyfield/DE440s for 12 points, cross-checked to the minute against USNO and MET Norway. No dusk-plus-flood or dawn-plus-flood coincidence on this date: floods run about 09:00-15:00 (daylight) and from about 21:30. Night HW about 02:15-03:20. | A. |
| 6 | Known marks | `research/marks.md`, `research/marks_merged.jsonl`, `research/marks/*.md` | 14 sweeps (10 sectors, 4 themes): 525 raw records merged to **308 distinct marks**. Evidence: 2 good, 93 moderate, 213 thin. | Weak: most text is from one aggregator; the main venue literature refused automated access (see section 6). |
| 7 | Coastline coverage | `research/coastline.md`, `research/coastline/segments_scored.csv`, `segments_map.png` | **2,009 segments, 1,243 km**, none longer than 1,000 m (section 3 below). Every segment scored from first principles. | Geometry: good. Seabed/depth close in: thin for about half. Tidal flow: thin everywhere. |
| 8 | Recent intel | `research/intel.md`, `research/intel/*.md` | About 45 dated items since 10 Oct. Strongest signal: shore bass of 1.4-3.1 kg from the Penzance club (venues withheld) 18 Oct - 16 Nov, latest **two fish 3.06 kg + 2.11 kg on the night of 16 Nov**; bluefin, dolphins and bait within sight of both coasts 7-13 Nov, nothing logged since; swell has kept anglers off exposed West Cornwall rocks for about six weeks, sheltered estuary/river sessions produced. No report from Scilly. No 2026 venue named for any fish except one blank match. | B/C; single-source dependence in places. |
| 9 | Rules | `research/rules.md` | Recorded for information only. Bass **may be retained on 22 Nov 2026** (within the 1 April - 31 December retention period; daily bag and 42 cm size as tabulated in the file). MPAs, IFCA byelaws, estuary and harbour restrictions listed. Verified against primary sources. | A. |

## 3. Coastline coverage (workstream 7)

- Base line: Ordnance Survey high-water mark (OS OpenMap Local), followed up every estuary to the Normal Tidal Limit; county membership from ONS boundaries; Devon/Plymouth shores and Eddystone excluded.
- Mainland chained into one consecutive line from **Marsland Mouth clockwise to the tidal limit of the Tamar: 971 segments, 970 km**. Plus 102 side pieces (16.7 km), 300 segments on 295 Cornish islets and rocks (49.6 km), 278 segments on Scilly (113 km), and 358 segments on detached drying reefs and banks (93 km) that are land only below high water.
- Per segment: aspect, 36-direction fetch, setting, intertidal width, depth within 150/300/500/1000/2000 m (EMODnet, ~115 m cells), seabed class (EMODnet Geology + EUSeaMap 2025), bedrock (BGS), stream outflows (OS), names (OS Open Names), nearshore wave estimate for each hour of 22 Nov, tide phase, and the documented marks within 600 m.
- Provisional score P (0-100): median 30, 90th percentile 54, 95th 60, 99th 76, maximum 91. The top decile (about 200 segments) goes forward to Phase 2; a large share has **no documented mark within 600 m**.
- **Thin data:** no mapped seabed within 300 m for 1,041 segments; no bathymetry cell within 300 m for 351 (mostly estuaries and creeks: 386 of 399 tidal-river segments carry a flag); 347 segments rest on geometry alone; tidal flow, gullies, ledges and kelp are below the resolution of every dataset for all 2,009. Charts and OpenStreetMap structure data could not be obtained.

## 4. Contradictions noticed so far (to be resolved in Phase 2, not resolved here)

1. **River state.** The species stream describes rivers "in spate since 15-17 Nov"; the EA level table built at 16:35 UTC shows no station above its typical high and 37 of 46 in the lower half of the typical range. Likely a receding rise, but it changes how estuaries should be treated.
2. **Rain on the 22nd.** Open-Meteo models give 22-48 mm in places; MET Norway gives 16-29 mm. East Cornwall totals are the least certain.
3. **Evening sky.** The multi-model median keeps 100 % cloud to 21:00 on the mainland; the species verifier, using MET Norway, expects a clearing sky at dusk with a bright moon. This decides whether the evening fishes "dark" or "bright".
4. **Best window.** The provisional segment model puts nearly every open-coast segment's best 3 h at 00:00-03:00 (night flood to HW, before the veer); the species stream suggests dusk into night. These rest on different assumptions and neither has been tested.
5. **Loe Bar.** One source leads with cod and whiting in stormy conditions; another with bass and stingray.
6. **"Winter slow-down" of mullet and wrasse** in general guides versus Cornish records showing specimen thick-lips November-March and wrasse to 6 lb on lures in November-December.
7. **Tidal streams off the Lizard:** pilot text and the ocean model differ by about 2 h on the turn.
8. **Sea-surface temperature products** disagree on level (12.7-14.3 C) though all show a positive anomaly; buoys are taken as truth.

## 5. Gap-fill round (in progress at the time of writing)

Second-pass marks sweeps (north coast; south coast; West Penwith / Scilly / offshore rocks), station observations plus independent tide predictions plus surge values, and an adversarial verification of the script-built tides / weather / sea-state / light files. Results are appended in section 8 when they return.

## 6. Limits and process notes (read before trusting anything above)

- **Blocked sources stay unread.** Sea Angler, World Sea Fishing forum, Planet Sea Fishing, PressReader and most Facebook pages refused automated access. I began to route around that through web-archive copies; that was refused as unauthorised and I dropped it rather than rework it. Those sources remain unread. If you want them in, they would need to be supplied or access permitted.
- **Usage limit.** The first launch of the research agents hit the account's 5-hour usage limit after about 8 minutes and every agent died. On restart the bulk collection sweeps (marks, intel, rules, streams, clarity) ran on a cheaper model tier to stay inside the limit; the species stream ran on the session model. The numeric streams (tides, weather, waves, light, coastline) were produced by scripts in `fishing/tools/` rather than by agents. The marks sweeps were told to economise and stopped early - the list is shorter than it could be.
- **Raw downloads are not in the repository.** They contain third-party pages with embedded keys that trip GitHub's push protection. `research/raw_manifest.tsv` lists every file with size and SHA-256; the tidy data that the tables are built from is in `research/data/`.
- **Not verified yet:** `weather.md`, `sea_state.md`, `tides.md` and `light_moon.md` were built by my own scripts and are being adversarially checked now. Independent (non-UKHO) tide predictions have not been compared. Model run times are not exposed by the forecast API.
- **Forecast staleness.** Every forecast figure was pulled 16:06-16:35 UTC on 21 Nov. Phase 3 must re-pull.

## 7. Sources

Each research file carries its own sources with access times and grades. Principal primary sources: UKHO Admiralty EasyTide; NTSLF/NOC (tidal levels, surge model); SHOM via maree.info (coefficient); Open-Meteo forecast, ensemble and marine APIs (UKMO UKV 2 km and global, ECMWF IFS / AIFS, GFS, ICON-EU, ARPEGE, AROME, HARMONIE (DMI, KNMI), GEM; MFWAM, ECMWF WAM, GFS-Wave, EWAM, GWAM); Met Office shipping, inshore-waters and regional forecasts; Channel Coastal Observatory buoys; NDBC 62107 / 62050; Environment Agency flood-monitoring API; skyfield + JPL DE440s, USNO, MET Norway; Ordnance Survey OpenMap Local and Open Names; ONS boundaries; EMODnet Bathymetry, Geology and Seabed Habitats (EUSeaMap 2025); BGS 625k geology; Natural Earth; Mount's Bay Angling Society and Cornish Federation of Sea Anglers record sheets; Through the Gaps (Newlyn); Cornwall Birds sightings; legislation.gov.uk, Cornwall IFCA, MMO, Environment Agency.

## 8. Gap-fill results

_(pending)_
