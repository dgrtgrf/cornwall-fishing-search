
## 6. Storm surge / residual (what the real water level will do relative to the predictions)

- **NTSLF / NOC surge model, latest surge forecast for Newlyn** (https://ntslf.org/storm-surges/surge-model/latest-surge-forecast?port=Newlyn, page and forecast graphic saved 2026-11-21 15:21-15:22 UTC, grade A; values read off the graphic by eye, +-0.03 m): residual about **+0.10 to +0.15 m** through 20-21 Nov, rising from the evening of the 21st to a **peak of about +0.42 m around midnight 21/22 Nov**, still about **+0.40 m at the 02:17 HW**, falling to about **+0.25 m at the 08:55 LW**, about **+0.12 m at the 14:35 HW** and about **-0.05 m by the 21:18 LW**. The four overlapping model runs (00/06/12/18 GMT) agree within about 0.03 m.
- Cause: the passing low (MSLP ~997-1000 hPa, i.e. ~15 hPa below standard = ~+0.15 m inverse-barometer) plus the south-easterly gale piling water into the western Channel; residual collapses as pressure rises and the wind veers west (`weather.md`).
- **Observed check (Environment Agency tide gauge, St Mary's, 15-min data 20 Nov 23:00 - 21 Nov 14:30 UTC, n = 32, against the EasyTide half-hourly prediction):** mean observed-minus-predicted **+0.15 m**, standard deviation 0.07 m, last 6 h +0.10 m - consistent with the surge model's +0.10 to +0.15 m for the same period, and the small scatter shows the predicted timing is good. (The same comparison for Newlyn and Devonport was not completed - station files were mismatched in the quick check; NOT DONE.)
- **Effect on 22 Nov:** the early-morning HW will stand roughly 0.4 m higher than the tables (Newlyn ~5.4 m instead of 4.97 m - i.e. spring-tide height although the astronomical tide is only ~75-85 % of springs); the morning LW will not fall as far (Newlyn ~1.7 m instead of 1.48 m), so low-water ledges, bars and gutters uncover ~0.25 m less than predicted; the afternoon HW ~0.1 m high (~5.35 m); the evening LW close to prediction. Times of HW/LW shift by only minutes. Surge forecasts for Padstow/north coast were not retrieved (NOT FOUND) - a SE wind is offshore there so the residual should be smaller.

## 7. Standard-port tidal levels and the size of the tide

| Port | MHWS | MHWN | MLWN | MLWS | Mean spring range | Mean neap range | 22 Nov ranges (am, pm) | pm range as % of mean spring range | Position neap(0 %) -> spring(100 %) |
|---|---|---|---|---|---|---|---|---|---|
| Newlyn | 5.5 | 4.4 | 2.1 | 0.9 | 4.6 | 2.3 | 3.49, 3.75 / 3.99 | 87 % | 73 % |
| Plymouth (Devonport) | 5.7 | 4.5 | 2.3 | 1.1 | 4.6 | 2.2 | 3.38, 3.57 / 3.84 | 83 % | 68 % |
| St Mary's | 5.6 | 4.3 | 2.0 | 0.8 | 4.8 | 2.3 | 3.64, 3.89 / 4.12 | 86 % | 73 % |

Source for the levels (grade A): NTSLF "Highest & lowest predicted tides" pages for each port (https://ntslf.org/tides/uk-network/predictions-hilo?port=Newlyn etc., saved 2026-11-21 15:21 UTC). Ranges are from the EasyTide events in section 1 (am = first HW to first LW; the two pm figures are LW1 to HW2 and HW2 to LW2).

**French tidal coefficient (SHOM via maree.info, Brest, https://maree.info/82?d=20261122, accessed 2026-11-21 ~16:55 UTC, grade A/B):** 22 Nov **70 (morning tide) and 76 (afternoon tide)**; 23 Nov 81 / 86; 24 Nov 90 / 93. (Coefficient 70 = mean tide, 95 = mean spring, 45 = mean neap.) So the session falls on a medium-to-large, fast-building tide, two to three days before large perigean springs (full moon 24 Nov 14:53, perigee 25 Nov 21:08).

Cycle: neaps were about 19-20 Nov (Newlyn range 2.3-2.5 m on the 20th); every tide is larger than the last through the session; the 7-day EasyTide window maximum (Newlyn 4.87 m, Padstow 6.68 m) falls on 25-26 Nov.

## 8. Cross-checks

| Check | Result |
|---|---|
| tidetimes.org.uk, Padstow and Falmouth, 22 Nov (accessed ~16:55 UTC) | Identical to EasyTide to the minute and centimetre (Padstow HW 02:57 6.45, LW 09:25 1.75, HW 15:18 6.82, LW 21:50 1.40; Falmouth HW 02:49 4.64, LW 09:23 1.17, HW 15:06 4.87, LW 21:49 0.93). NOTE: that site republishes UKHO data, so this confirms transcription only - it is **not** an independent prediction. |
| St Mary's EA gauge vs EasyTide (section 6) | Mean residual +0.15 m, sd 0.07 m - prediction timing and shape confirmed by observation. |
| SHOM (Brest) coefficient trend | Independent hydrographic office; coefficient rising 70 -> 76 -> 81 -> 86 matches the building ranges in the UKHO data. |
| NOC/NTSLF own harmonic predictions for Newlyn / Plymouth / St Mary's | NOT RETRIEVED - the prediction tables are JavaScript-rendered; carry to Phase 3. |
| BBC / tide-forecast.com / tides4fishing | Not compared (BBC republishes UKHO; the others use their own harmonics) - carry to Phase 3. |

GMT/BST: UK clocks are on GMT in November; EasyTide event times carry no zone suffix and were confirmed as GMT by the match with the half-hourly series (stamped Z) and by the St Mary's gauge comparison.

## 9. Which reference port applies to which stretch of shore

| Coast sector | Reference port (EasyTide id) | Notes |
|---|---|---|
| Marsland Mouth - Bude - Widemouth - Crackington | Bude (0543) HW only; curve from Boscastle (0544) | Bude has no LW prediction (dries); HW about 13 min after Padstow |
| Boscastle - Tintagel - Trebarwith | Boscastle (0544) | |
| Port Isaac - Port Quin - Pentire | Port Isaac (0544A) | |
| Camel estuary: Stepper Point - Padstow - Rock | Padstow (0545) | |
| Camel above Padstow to Wadebridge | Wadebridge (0545A) | HW within minutes of Padstow; LW delayed ~3 h 20 min (river level persists) - upper estuary is a flood-only venue |
| Trevose - Constantine - Porthcothan - Mawgan Porth - Watergate - Newquay - Gannel | Newquay (0546) | |
| Holywell - Perranporth - St Agnes - Porthtowan - Portreath | Perranporth (0546A) | |
| Godrevy - Hayle - St Ives Bay - St Ives | St Ives (0547) | Hayle estuary lags; no secondary port |
| Zennor - Gurnard's Head - Pendeen - Cape Cornwall | Cape Cornwall (0547A) | |
| Sennen - Land's End | Sennen Cove (0548) HW only; curve from Cape Cornwall / Newlyn | |
| Isles of Scilly (all islands) | St Mary's (0001) | |
| Porthgwarra - Porthcurno - Lamorna - Mousehole - Newlyn - Penzance - Marazion - Prussia Cove - Praa | Newlyn (0002) | |
| Porthleven - Loe Bar - Gunwalloe - Mullion | Porthleven (0002A) | |
| Kynance - Lizard Point - Cadgwith | Lizard Point (0003) | |
| Kennack - Coverack - Manacles - Porthoustock - Porthallow | Coverack (0004) | |
| Gillan - Helford River | Helford River entrance (0004A) | creeks lag slightly; no secondary ports |
| Falmouth Bay - Falmouth - Carrick Roads - St Mawes - Percuil - St Anthony | Falmouth (0005) | |
| Truro / Tresillian / upper Fal | Truro (0005A) HW only | dries at LW |
| Portscatho - Nare Head - Portloe - Dodman - Gorran Haven - Mevagissey - Pentewan | Mevagissey (0007) | |
| St Austell Bay: Porthpean - Charlestown - Carlyon - Par - Polkerris | Par (0007A) | |
| Gribbin - Fowey - Polruan - lower estuary | Fowey (0008) | |
| Fowey above Golant to Lostwithiel | Lostwithiel (0008A) HW only | dries at LW |
| Lantic - Polperro - Talland - Looe - Seaton - Downderry | Looe (0011) | |
| Portwrinkle - Whitsand Bay - Rame Head | Whitsand Bay (0012) | |
| Penlee - Cawsand - Kingsand - Mount Edgcumbe - Cremyll - Torpoint | Plymouth Devonport (0014) | |
| Lynher: Jupiter Point - St Germans | Jupiter Point (0014E), St Germans (0014F) | |
| Tamar: Saltash - Cargreen - Cotehele - Calstock - Gunnislake | Saltash (0014A), Cargreen (0014B), Cotehele Quay (0014C) | LW progressively later upstream (+20 min Cargreen, +45 min Cotehele) |

## 10. Gaps

- Independent (non-UKHO) predictions for Cornish ports not obtained (section 8).
- Surge forecast only read for Newlyn; no north-coast surge figure.
- Estuary-head lags beyond the listed secondary ports (Gannel, Hayle, Helford creeks, Looe rivers, Lerryn, Tresillian) NOT FOUND - see `tidal_streams.md`.
- Tidal streams: literature is thin (Admiralty atlas tables are behind a paywall); the only hour-by-hour series is coarse ocean-model output - see `tidal_streams.md` and `sea_state.md` section 6.
