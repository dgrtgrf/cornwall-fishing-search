# Tidal streams and estuary tide behaviour (workstream 1, literature part)
Target session: Sun 22 Nov 2026 (GMT=UTC). Written Sat 21 Nov 2026 ~16:30 UTC. Raw files: raw/tidal_streams/ (and raw/tides/ for EasyTide JSON).

**Headline honesty note.** Published Admiralty stream-atlas (NP250/NP255) hourly tables are paywalled/members-only at visitmyharbour (fetched 16:0x UTC: "Please become a member to read the description"), and several searches (kayak guides, pilot extracts, PBO, eoceanic, Wikipedia) yielded only fragments of diamond-by-diamond data. So section 2 (literature) is THIN for most headlands; section 3 (Open-Meteo marine model currents for 22 Nov, grade A model output but coarse ~8 km grid, offshore of the stated points) is the only hour-by-hour stream series obtained and is the working basis for clock times. Where the two disagree this is recorded, not averaged.

## 1. Reference tide times 22 Nov 2026 (EasyTide / UKHO, grade A; times GMT; accessed 21 Nov ~15:17-16:04 UTC; raw/tides/ and raw/tidal_streams/easytide_0089_1604Z.json, easytide_0496_1604Z.json)
| Port | HW | LW | HW | LW |
|---|---|---|---|---|
| Dover 0089 | 08:38 (6.30) | 16:01 (1.37) | 21:06 (6.30) | (03:35 1.73 prior LW) |
| Milford Haven 0496 | 03:50 (6.31) | 10:10 (1.76) | 16:11 (6.65) | 22:35 (1.44) |
| Devonport 0014 | 03:21 (4.96) | 09:35 (1.58) | 15:41 (5.15) | 22:00 (1.31) |
| Newlyn 0002 | 02:17 (4.97) | 08:55 (1.48) | 14:35 (5.23) | 21:18 (1.24) |
| St Mary's 0001 | 02:19 (5.07) | 08:45 (1.43) | 14:39 (5.32) | 21:06 (1.20) |
| Padstow 0545 | 02:57 (6.45) | 09:25 (1.75) | 15:18 (6.82) | 21:50 (1.40) |
| Falmouth 0005 | 02:49 (4.63) | 09:23 (1.17) | 15:06 (4.87) | 21:49 (0.93) |
Conversion keys used below: HW Devonport = 03:21 and 15:41 (next 04:10 on 23rd; previous 14:46 and 02:27 on 21st). HW Dover = 08:38 and 21:06. Dover HW is ~5h17-5h25 after Devonport HW.
EasyTide lunar-phase field in the same JSON: type 3 at 2026-11-24T14:53 (consistent with full moon 24 Nov, i.e. session ~2 d 22 h before full moon).

## 2. Spring/neap scaling for 22 Nov (D = inference from A data)
Devonport daily range (mean of HWs minus mean of LWs, from EasyTide 0014 JSON): 20 Nov 2.50 | 21 Nov 3.06 | **22 Nov 3.61** | 23 Nov 4.08 | 24 Nov 4.42 | 25 Nov 4.61 | 26 Nov 4.64 (max in data) | 27 Nov 4.52 m. Tide is building fast toward springs (about +0.5 m range per day).
Mean ranges: MHWS 5.5, MHWN 4.4, MLWN 2.2, MLWS 0.8 m for Devonport (grade B: MDL Queen Anne's Battery marina page via search, accessed 21 Nov; marked there "accurate to ~1 h", datum not stated; I could not retrieve NTSLF/Admiralty constants - NOT FOUND from a grade-A source). => mean spring range 4.7, mean neap range 2.2.
Method (standard atlas interpolation): rate = neap + f x (spring - neap), f = (R - Rn)/(Rs - Rn).
- f = (3.61 - 2.2)/(4.7 - 2.2) = **0.56** (using in-window extremes 2.50/4.64: 0.52). So the stream is a bit over half way from neap to spring figures.
- Worked example (kayak-guide Plymouth figure 1.7 kn springs/0.8 kn neaps): 0.8 + 0.56 x 0.9 = **1.3 kn**.
- Crude proportional alternative (rate ~ range): 3.61/4.7 = 0.77 of the spring rate. Real behaviour lies between; use 0.56 for atlas springs/neaps pairs, 0.77 if only a spring rate is known. Day-to-day: each later day adds ~10%, so Monday-Tuesday are noticeably faster than Sunday.
- The Open-Meteo model series below already carries the actual 22 Nov forcing; do NOT rescale it.

## 3. Hour-by-hour modelled stream, 22 Nov 2026 (grade A model output, tide-resolving ocean model)
Source: https://marine-api.open-meteo.com/v1/marine ?hourly=ocean_current_velocity,ocean_current_direction (22 Nov 00-23 UTC). Accessed 21 Nov ~16:05 UTC; model run/publication date NOT stated in the response (THIN DATA on run time). File: raw/tidal_streams/openmeteo_marine_currents_20261122_1605Z.json. NB: the API returned velocity in km/h (my kn request was ignored); values below are converted /1.852. Grid snaps to nearest sea cell (~0.04-0.08 deg off the requested point, offshore of it: lat/lon shown), so inshore eddies, races, bay-head slack and close-in streams (which turn 30-45 min earlier than offshore per pilot text) are NOT resolved. Direction convention (towards vs from) is not documented in the response; I list it as the direction the water moves TOWARD (pattern is physically plausible: NE-going N-coast stream before HW Devonport, SW after). Hartland fetch failed (connection reset); not retried.
Hourly values are in the JSON; below are peaks and near-slack hours (UTC) with offset from HW Devonport.
| Point (grid cell) | Peaks (hour UTC, rate, towards, offset from nearest HW Devonport) | Near-slack hours (<55% of day max) |
|---|---|---|
| Hartland | fetch failed (<urlopen error [Errno 104] Connection re) |||||
| Bude (50.88,-4.62) | 01h 0.6kn to NE (HWDev-2h21); 07h 0.8kn to SW (HWDev+3h39); 14h 0.8kn to NE (HWDev-1h41); 19h 0.6kn to SW (HWDev+3h19) | 04h (HWDev+0h39); 10h (HWDev-5h41); 16h (HWDev+0h19); 22h (HWDev-6h06) |
| Tintagel (50.71,-4.87) | 01h 0.6kn to NE (HWDev-2h21); 07h 0.9kn to SW (HWDev+3h39); 14h 1.0kn to NE (HWDev-1h41); 19h 0.5kn to SW (HWDev+3h19) | 04h (HWDev+0h39); 10h (HWDev-5h41); 17h (HWDev+1h19); 22h (HWDev-6h06) |
| Stepper (50.54,-4.96) | 01h 0.6kn to NE (HWDev-2h21); 06h 1.5kn to W (HWDev+2h39); 13h 1.7kn to NE (HWDev-2h41); 19h 0.4kn to SW (HWDev+3h19) | 03h (HWDev-0h21); 10h (HWDev-5h41); 17h (HWDev+1h19); 20h (HWDev+4h19) |
| Trevose (50.54,-5.12) | 01h 0.8kn to N (HWDev-2h21); 06h 0.9kn to SW (HWDev+2h39); 13h 1.6kn to NE (HWDev-2h41); 20h 0.5kn to S (HWDev+4h19) | 04h (HWDev+0h39); 09h (HWDev+5h39); 17h (HWDev+1h19); 21h (HWDev+5h19) |
| Towan (50.46,-5.12) | 01h 0.9kn to N (HWDev-2h21); 06h 0.8kn to SW (HWDev+2h39); 14h 1.5kn to NE (HWDev-1h41); 19h 0.6kn to S (HWDev+3h19) | 04h (HWDev+0h39); 09h (HWDev+5h39); 17h (HWDev+1h19); 21h (HWDev+5h19) |
| StAgnes (50.38,-5.29) | 01h 0.7kn to N (HWDev-2h21); 06h 0.8kn to SW (HWDev+2h39); 13h 1.5kn to NE (HWDev-2h41); 19h 0.4kn to S (HWDev+3h19) | 03h (HWDev-0h21); 09h (HWDev+5h39); 17h (HWDev+1h19); 21h (HWDev+5h19) |
| Godrevy (50.29,-5.46) | 05h 1.4kn to W (HWDev+1h39); 12h 2.4kn to E (HWDev-3h41); 18h 1.1kn to SW (HWDev+2h19) | 03h (HWDev-0h21); 08h (HWDev+4h39); 16h (HWDev+0h19); 21h (HWDev+5h19) |
| StIves (50.21,-5.54) | 06h 1.2kn to SW (HWDev+2h39); 13h 2.6kn to E (HWDev-2h41); 18h 1.1kn to SW (HWDev+2h19) | 03h (HWDev-0h21); 08h (HWDev+4h39); 16h (HWDev+0h19); 21h (HWDev+5h19) |
| Pendeen (50.21,-5.71) | 05h 1.2kn to SW (HWDev+1h39); 12h 2.8kn to NE (HWDev-3h41); 18h 1.8kn to S (HWDev+2h19) | 03h (HWDev-0h21); 08h (HWDev+4h39); 16h (HWDev+0h19); 21h (HWDev+5h19) |
| CapeCornwall (50.13,-5.79) | 06h 0.6kn to SW (HWDev+2h39); 12h 1.9kn to N (HWDev-3h41); 17h 1.4kn to S (HWDev+1h19) | 03h (HWDev-0h21); 07h (HWDev+3h39); 15h (HWDev-0h41); 21h (HWDev+5h19) |
| Longships (50.04,-5.79) | 05h 0.6kn to S (HWDev+1h39); 12h 1.3kn to N (HWDev-3h41); 17h 1.4kn to SE (HWDev+1h19) | 03h (HWDev-0h21); 07h (HWDev+3h39); 21h (HWDev+5h19) |
| Runnel (50.04,-5.71) | 05h 0.7kn to SE (HWDev+1h39); 11h 1.5kn to NW (HWDev-4h41); 17h 1.9kn to SE (HWDev+1h19) | 03h (HWDev-0h21); 07h (HWDev+3h39); 14h (HWDev-1h41); 20h (HWDev+4h19) |
| MountsBay (50.04,-5.54) | 03h 0.2kn to NE (HWDev-0h21); 08h 1.1kn to W (HWDev+4h39); 16h 1.3kn to E (HWDev+0h19); 20h 0.8kn to SW (HWDev+4h19) | 04h (HWDev+0h39); 12h (HWDev-3h41); 19h (HWDev+3h19) |
| Lizard (49.96,-5.21) | 02h 0.7kn to E (HWDev-1h21); 08h 1.6kn to W (HWDev+4h39); 15h 1.6kn to E (HWDev-0h41); 21h 1.7kn to W (HWDev+5h19) | 04h (HWDev+0h39); 11h (HWDev-4h41); 17h (HWDev+1h19) |
| Manacles (49.96,-5.04) | 02h 0.6kn to NE (HWDev-1h21); 08h 1.5kn to SW (HWDev+4h39); 14h 0.5kn to E (HWDev-1h41); 20h 1.8kn to SW (HWDev+4h19) | 04h (HWDev+0h39); 12h (HWDev-3h41); 16h (HWDev+0h19) |
| Falmouth (50.13,-4.87) | 02h 0.5kn to NW (HWDev-1h21); 08h 1.2kn to S (HWDev+4h39); 14h 0.4kn to NW (HWDev-1h41); 20h 1.2kn to S (HWDev+4h19) | 04h (HWDev+0h39); 12h (HWDev-3h41); 16h (HWDev+0h19) |
| Dodman (50.21,-4.79) | 09h 1.0kn to SW (HWDev+5h39); 20h 1.3kn to SW (HWDev+4h19) | 03h (HWDev-0h21); 13h (HWDev-2h41); 15h (HWDev-0h41) |
| Fowey (50.29,-4.62) | 02h 0.5kn to NW (HWDev-1h21); 09h 0.9kn to W (HWDev+5h39); 21h 1.0kn to SW (HWDev+5h19) | 03h (HWDev-0h21); 15h (HWDev-0h41) |
| Rame (50.29,-4.21) | 03h 0.3kn to N (HWDev-0h21); 09h 1.2kn to W (HWDev+5h39); 15h 0.2kn to NE (HWDev-0h41); 21h 1.1kn to W (HWDev+5h19) | 04h (HWDev+0h39); 16h (HWDev+0h19) |
| StMarysSound (49.88,-6.29) | 07h 0.5kn to SW (HWDev+3h39); 14h 1.3kn to E (HWDev-1h41) | 04h (HWDev+0h39); 09h (HWDev+5h39); 22h (HWDev-6h06) |
| Wolf (49.96,-5.87) | 06h 0.6kn to S (HWDev+2h39); 16h 1.3kn to SE (HWDev+0h19) | 03h (HWDev-0h21); 09h (HWDev+5h39); 21h (HWDev+5h19) |
| Bishop (49.88,-6.54) | 06h 0.8kn to S (HWDev+2h39); 14h 1.2kn to E (HWDev-1h41); 16h 1.1kn to SE (HWDev+0h19) | 03h (HWDev-0h21); 09h (HWDev+5h39); 21h (HWDev+5h19) |

Reading of the model (D): north coast (Bude-St Agnes) has a clear semi-diurnal reversing pattern: NE/ENE-going stream peaking ~HWDev -1h40 to -2h40 (13-14h and ~01h), SW/W-going peaking ~HWDev +2h40 to +3h40, slack ~HWDev +0h30..+1h20 (turn to NE ... slack at 04h, 16-17h) and ~HWDev -5h40..-6h (09-10h, 22h). Strongest north-coast rates: Stepper 1.7 kn, Trevose 1.6, Towan 1.5, St Agnes 1.5 (offshore cells; the model's rates inshore of Stepper/Trevose/Pentire will differ; headland races are not represented). The big rates start at Godrevy-Pendeen (2.4-2.8 kn NE-going peak 12h) where the model's stream is E/NE-going 3.5-4 h before HW Devonport. West of Land's End (Cape Cornwall/Longships/Runnel Stone) the streams rotate (peaks N/S/SE/NW rather than reversing along one axis) - matches pilot text "rotatory near Land's End and Runnel Stone". Lizard/Manacles/Falmouth/Dodman/Fowey/Rame: south coast is E-going peak ~HWDev -0h40 to -1h40 (14-15h model for Lizard) and W/SW-going peaks ~HWDev +4h20 to +5h40, with weak rates (Falmouth 1.2, Fowey 1.0, Rame 1.2 kn peaks; Lizard 1.6-1.7). Mount's Bay offshore cell is weak (0.2-1.3 kn) with near-slack at 04h and 12h.
Scilly cells (St Mary's Sound, Wolf, Bishop): SE/E-going peak 14-16h (1.2-1.3 kn), S/SW-going peak ~06h (0.5-0.8 kn); the model's grid is too coarse to resolve the sounds (Crow Sound, Smith Sound, New Grimsby), so those are NOT FOUND/THIN.

## 4. Literature stream data found (with conversion to clock time on 22 Nov)
| Location | Statement | Source (grade) / access | Clock times 22 Nov (GMT) |
|---|---|---|---|
| 5 mi S of Lizard Head | E-going stream (065 deg, slightly rotatory clockwise) begins HW Devonport -0330 (= +0315 Dover); W-going (245 deg) begins +0250 Devonport. Rates not in snippet. | Admiralty pilot text as quoted via web-search summary of visitmyharbour NP250 text, accessed 21 Nov ~16:10 UTC (B, secondary quote of A) | E-going begins ~12:11 (from HW 15:41) and ~23:51 on the 21st (from HW 03:21 less 3h30 = 23:51); W-going begins ~06:11 and ~18:31 |
| Lizard-Land's End coastal widget (reference point not stated) | SW and W-going HW Dover -0145 to +0330; NE and E-going +0330 to -0245 | eoceanic.com route 48 page, accessed 21 Nov 16:05 UTC (B) | SW/W 06:53-12:08 and 19:21-00:36; NE/E 12:08-18:21 and 00:36-06:36 |
| Runnel Stone | "west-going" HW Dover -0200 to +0100 (only a 3 h window - widget wording unclear) | eoceanic route 49 (B; unclear, flagged) | 06:38-09:38 and 19:06-22:06 |
| Scilly (offshore, to depart) | "Scillies east-going HW Dover +0500 to -0500" and prose "a window of 6 hours of eastward stream" - internally inconsistent; THIN | eoceanic route 49 (B) | not reliably convertible |
| Land's End / Runnel Stone | streams rotatory near Land's End and Runnel Stone; direction past Runnel Stone depends on offshore stream; rates increase off salient points and rocks with overfalls; timing variable with wind | Admiralty pilot text via visitmyharbour/search summary (B) | no clock times |
| Land's End inshore | Reeds/PBO plan is a close-inshore rounding needing ~9 h favourable tide | PBO via search (B/C) | - |
| Lizard Head | irregular soundings give heavy overfalls to 1 mile S in bad weather; "extensive race" SE of Head from confluence of streams either side, up to ~2 mi S; stream off point up to 3 kn, strong race on flood and ebb when blowing fresh; short heavy sea in SW gales; very close inshore passage: tide turns 30-45 min earlier than offshore | eoceanic route 47/48 (B) | race times not given |
| Kynance/Lizard W side (eoceanic harbour 562) | E-going stream starts HW Dover +0315; an early eddy running SE starts a couple of hours earlier; substantial race S of Lizard | eoceanic (B) | E-going starts ~11:53 (08:38+3:15) and 00:21; eddy ~09:50 |
| Dodman | "recognised tidal race off Dodman Point"; heavy overfalls to the S in bad weather | eoceanic route 47 and harbour page (B) | no times |
| Greeb Point (Roseland) | races/overfalls "The Bizzies" over ledge least depth 3.8 m | eoceanic harbour 554 (B) | no times |
| Carrick Roads | ebb begins 6 h 05 min before HW Dover; peak ~3 kn in upper basin, 1.5-2 kn lower reaches | Wikipedia 'Carrick Roads' via search summary (C/B) | ebb begins 02:33 and 15:01 (vs Falmouth HW 02:49/15:06 - ebb starts about at local HW) |
| Fal narrows/bends (eoceanic 556) | "narrows and river bend increase the velocity ... 2-3 knots at springs and rips" (place within the Fal not extracted) | eoceanic (B) | - |
| Helford mouth | east winds cause heavy sea Mawnan Shear to Bosahan Point esp. on the ebb; short seas break on the bar at ebb | eoceanic harbour 558 (B) | - |
| Plymouth Sound/Drake Channel | max flow at HW Plymouth and +4 h, 1.7 kn springs / 0.8 kn neaps (open waters near Plymouth); in Drake Channel ("The Bridge") spring stream up to 3 kn | kayak guide (bookdown 'sea_kayak_navigation', C/B) and eoceanic 544 (B) | max flow ~03:21 and ~07:21; ~15:41 and ~19:41; with f=0.56: 1.7/0.8 -> ~1.3 kn |
| Tamar moorings (eoceanic 545) | rates up to 3.5 kn at springs at quays; "big spring tide will run as much as 2.5 knots" at moorings | eoceanic (B) | scale by 0.56-0.77 |
| Tamar upper | river dries almost completely at LW; above Dandy Hole (St Germans arm) dries completely; above Weir Quay river contracts and partly dries; channel to Cotehele has 0.1 to >2.5 m in pools; outer wall dries to shingle ~6 h each tide | eoceanic 545 (B) | LW Devonport 09:35 / 22:00 |
| Scilly sound entrance (eoceanic 573) | streams >2 kn at springs set across entrance, running east at HW Dover +0115 and west at HW Dover -0510 (place unverified; Tresco/New Grimsby area) | eoceanic (B) | east 09:53 and 22:21; west 03:28 and 15:56 |
| Scilly overfalls (573/574) | overfalls 3-4 h after HW Dover off Kettle Bottom Ledge and across entrance between Kettle Bottom and Golden Ball Brow; strong rotary streams around the islands, unpredictable localised streams between them; overfall SE/S of St Agnes between 4 h flood and 2 h ebb (reference not stated) | eoceanic (B) | Kettle Bottom 11:38-12:38 and 00:06-01:06 |
| New Grimsby Channel | up to 2 kn at springs | eoceanic 576 (B) | - |
| River Avon / Kingsbridge area | not Cornwall - ignore | - | - |

## 5. Estuary behaviour on 22 Nov (EasyTide secondary-port predictions, grade A for predictions but secondary-port values are derived; times GMT)
Heights are as published by each station's own datum. Truro/Lostwithiel print only HWs (no LW row), i.e. the predictor gives no low-water value - consistent with those reaches draining/drying at low water (D inference; also eoceanic: Truro river and creeks above entrance "dries entirely").
| Estuary | Station: HW times (heights) / LW times (heights) 22 Nov | Lag vs mouth station and height change (D) |
|---|---|---|
| Fal | Falmouth H02:49 (4.63) H15:06 (4.87); L09:23 (1.17) L21:49 (0.93). Truro H02:58 (2.96) H15:17 (3.15), no LW given | HW lag +9 to +11 min; height listed 1.7 m lower (datum differs; LW not predicted) |
| Helford | Entrance H02:48 (4.76) H15:07 (4.95) L09:22 L21:46 | ~in step with Falmouth; no upstream station |
| Fowey | Fowey H03:08 (4.86) H15:27 (5.05); L09:27 (1.38) L21:51 (1.11). Lostwithiel H03:17 (0.86) H15:36 (1.05), no LW | HW lag +9 min to Lostwithiel; no LW predicted (tidal limit dries) |
| Looe | Looe H03:11 (4.81) H15:31 (5.01); L09:30 (1.38) L21:55 (1.11) | no upstream station (East/West Looe rivers: NOT FOUND) |
| Tamar | Devonport H03:21/H15:41; Saltash H03:26 (5.06)/H15:47 (5.25), L09:32 (1.68)/L21:58 (1.41); Cargreen H03:26/H15:47, L09:55 (1.52)/L22:20 (1.27); Cotehele H03:32 (4.06)/H15:53 (4.25), L10:20 (0.96)/L22:45 (0.76); St Germans (Lynher) H03:21/H15:41, L09:55 (1.67)/L22:20 (1.44) | HW lag Saltash +5, Cargreen +5, Cotehele +11 min; LW lag Saltash -3, Cargreen +20, Cotehele +45 min, St Germans +20 min: ebb lasts longer upstream (flood shortens - LW delayed 45 min vs HW 11 min at Cotehele); Cotehele heights are on a different datum so read lag not height |
| Camel | Padstow H02:57 (6.45) H15:18 (6.82), L09:25 (1.75) L21:50 (1.40). Wadebridge H02:58 (2.30) H15:19 (2.68), L00:28 (0.25) L12:49 (0.26) | HW lag +1 min; Wadebridge LW +3 h 24 min after Padstow LW (12:49 vs 09:25) with LW height ~0.25 (stays at a floor): upper estuary drains very late - flood duration at Wadebridge about 2.2 h of rise vs 10 h of fall; heights again different datum |
| Other north coast | Port Isaac H02:50 (6.65)/H15:11 (7.02); Newquay H02:45 (6.15)/H15:05 (6.52); Perranporth H02:45 (6.05); St Ives H02:48 (5.75)/H15:07 (6.12); Cape Cornwall H02:12 (5.15)/H14:33 (5.52); Sennen not printed | - |
NOT FOUND: Gannel, Hayle, Helford creeks, Tresillian, Percuil, Restronguet, Penryn, Lerryn, Looe rivers, Lynher to St Germans channel depth, Calstock/Gunnislake weir; no EasyTide stations for them and several searches returned no pilot detail. Camel: tidal limit Wadebridge (Sladesbridge/Egloshayle also named); three persistent bars Doom Bar, Town Bar (~1 mile above Padstow), Halwyn Bank; coastal study says estuary slightly flood-dominant in peak speeds (Defra/EA SMP via search, B). Fal estuary tidal limit Tresillian (Tresillian River) / Truro; "The Tresillian River dries 200 metres above the pontoon", Restronguet Creek "dries entirely" above entrance, St Just Creek dries 300 m within entrance, Gillan Creek dries ~300 m above Car Croc, Helford Creek entrance dries at LWS, "Above Percuil, about midway, it quickly dries" (eoceanic harbour pages 556/558/559/557, B). Fowey and Looe pages: Polperro/ Looe harbours dry (eoceanic 546).

## 6. Table of headlands requested: status
Hartland-Bude, Tintagel, Pentire/Rumps, Stepper/Doom Bar, Trevose, Towan, St Agnes, Godrevy, St Ives, Pendeen, Cape Cornwall, Land's End/Longships, Runnel Stone, Scilly sounds, Wolf, Western Rocks/Bishop, Mount's Bay, Lizard, Black Head, Manacles, Helford, Falmouth entrance/Carrick Roads/King Harry, St Anthony, Dodman, Gribbin, Fowey, Looe Island, Rame, Tamar narrows:
- Modelled hourly stream (section 3): Bude, Tintagel, Stepper, Trevose, Towan, St Agnes, Godrevy, St Ives, Pendeen, Cape Cornwall, Longships, Runnel, Mount's Bay, Lizard, Manacles, Falmouth offshore, Dodman, Fowey, Rame, St Mary's Sound offshore, Wolf, Bishop.
- Literature only (section 4): Lizard, Land's End/Runnel (qualitative), Dodman (race, no times), Carrick Roads, Fal narrows, Plymouth/Tamar, Scilly (partial).
- NOT FOUND (no source data retrieved): Pentire/The Rumps, Black Head, Gribbin, Looe Island, St Anthony Head stream, King Harry exact rates, Cremyll/Torpoint/Saltash rates, Smith Sound, Crow Sound, Wolf Rock race timing, spring/neap rates for any north-coast headland, Admiralty NP255 diamond rates. Tried: visitmyharbour NP250/NP255 (members only), eoceanic route and harbour pages, kayak-navigation bookdown, Pesda Press sample (issuu, not extractable), Wikipedia, several web searches.

## 7. Contradictions and caveats
- Runnel Stone widget window (3 h) and Scillies "+0500 to -0500" are inconsistent with each other and with the "6 hour window" prose; flagged THIN.
- Model: Lizard-area model shows E-going peak ~15h (HWDev -0h41), pilot text says E-going begins HWDev -3h30 (12:11); peak would be ~3 h later ~15:10: consistent. Lizard W-going begins HWDev +2h50 = 06:11, model W peak 08h and slack 04h: consistent within about an hour (model slack 04h vs pilot slack ~06:11: ~2 h offset, inshore vs 5 mi offshore, unreconciled).
- Open-Meteo marine currents are model output on coarse grid: treat rates as indicative; inshore races and eddies not captured.
- Mean-range constants are grade B and quoted with a stated ~1 h accuracy caveat.
