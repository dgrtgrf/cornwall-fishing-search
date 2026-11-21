# Workstream 5 - Light and moon, Sunday 22 November 2026

**Method / sources.** Computed with skyfield 1.55 and the JPL de440s.bsp ephemeris (computation saved 2026-11-21 15:18:23 UTC in `raw/light_moon/`; script `raw/light_moon/compute_astro.py`), grade A (direct astronomical computation). Cross-checked against the US Naval Observatory API (aa.usno.navy.mil/api/rstt/oneday, accessed 2026-11-21 15:19 UTC) and MET Norway sunrise API (api.met.no, accessed 15:19 UTC) - section 4. All times GMT (UK clock time). Sunrise/sunset = upper limb on the sea horizon with standard refraction; twilight boundaries at sun altitude -6 / -12 / -18 degrees. Cloud cover: Open-Meteo multi-model forecast pulled 2026-11-21 16:06-16:30 UTC (`data/weather_hourly_multimodel.csv`). Tide times: UKHO EasyTide (see `tides.md`). Table built by `fishing/tools/conditions/build_light_moon.py`.

## 1. Sun and twilight on 22 November

| Point | Astro. twilight begins | Nautical begins | Civil begins | Sunrise (azimuth) | Solar noon (alt) | Sunset (azimuth) | Civil ends | Nautical ends | Astro. ends | Day length |
|---|---|---|---|---|---|---|---|---|---|---|
| Bude | 05:48 | 06:27 | 07:08 | 07:45 (122) | 12:04 (19.0) | 16:23 (238) | 17:00 | 17:41 | 18:20 | 8h37 |
| Stepper Point (Camel mouth) | 05:49 | 06:28 | 07:09 | 07:46 (122) | 12:06 (19.2) | 16:26 (238) | 17:03 | 17:43 | 18:22 | 8h39 |
| Newquay Towan Head | 05:50 | 06:29 | 07:09 | 07:46 (122) | 12:07 (19.4) | 16:27 (238) | 17:04 | 17:44 | 18:23 | 8h41 |
| St Ives Head | 05:51 | 06:30 | 07:10 | 07:46 (121) | 12:08 (19.6) | 16:29 (238) | 17:06 | 17:46 | 18:25 | 8h42 |
| Land's End | 05:52 | 06:30 | 07:10 | 07:47 (121) | 12:09 (19.7) | 16:31 (239) | 17:07 | 17:47 | 18:26 | 8h43 |
| St Mary's Hugh Town (Scilly) | 05:54 | 06:32 | 07:12 | 07:49 (121) | 12:11 (19.9) | 16:34 (239) | 17:10 | 17:50 | 18:28 | 8h44 |
| Newlyn/Penzance | 05:51 | 06:30 | 07:10 | 07:46 (121) | 12:08 (19.7) | 16:30 (239) | 17:06 | 17:46 | 18:25 | 8h43 |
| Lizard Point | 05:50 | 06:28 | 07:08 | 07:44 (121) | 12:07 (19.9) | 16:29 (239) | 17:05 | 17:45 | 18:24 | 8h44 |
| Falmouth Pendennis | 05:49 | 06:28 | 07:08 | 07:44 (121) | 12:06 (19.7) | 16:28 (239) | 17:04 | 17:44 | 18:23 | 8h43 |
| Fowey mouth | 05:48 | 06:27 | 07:07 | 07:44 (121) | 12:05 (19.5) | 16:25 (238) | 17:02 | 17:42 | 18:21 | 8h41 |
| Looe | 05:47 | 06:26 | 07:06 | 07:43 (122) | 12:04 (19.5) | 16:25 (238) | 17:01 | 17:42 | 18:20 | 8h41 |
| Rame Head | 05:46 | 06:25 | 07:05 | 07:42 (121) | 12:03 (19.5) | 16:24 (238) | 17:00 | 17:41 | 18:19 | 8h41 |

## 2. Moon on 22 November

| Point | Moonset (azimuth) | Moonrise (azimuth) | Upper transit (altitude) | Previous transit (21 Nov) |
|---|---|---|---|---|
| Bude | 05:00 (293) | 14:41 (63) | 22:24 (57) | 21:32 (51) |
| Stepper Point (Camel mouth) | 05:01 (293) | 14:44 (63) | 22:26 (57) | 21:33 (52) |
| Newquay Towan Head | 05:01 (293) | 14:45 (63) | 22:26 (58) | 21:34 (52) |
| St Ives Head | 05:02 (293) | 14:47 (63) | 22:28 (58) | 21:35 (52) |
| Land's End | 05:03 (293) | 14:49 (63) | 22:29 (58) | 21:36 (52) |
| St Mary's Hugh Town (Scilly) | 05:05 (293) | 14:52 (64) | 22:31 (58) | 21:39 (52) |
| Newlyn/Penzance | 05:02 (293) | 14:48 (63) | 22:28 (58) | 21:36 (52) |
| Lizard Point | 05:00 (293) | 14:47 (64) | 22:27 (58) | 21:34 (52) |
| Falmouth Pendennis | 05:00 (293) | 14:46 (63) | 22:26 (58) | 21:34 (52) |
| Fowey mouth | 04:59 (293) | 14:43 (63) | 22:24 (58) | 21:32 (52) |
| Looe | 04:58 (293) | 14:43 (63) | 22:24 (58) | 21:31 (52) |
| Rame Head | 04:57 (293) | 14:42 (63) | 22:23 (58) | 21:30 (52) |

Geocentric moon through the day:

| Time (GMT) | Illuminated fraction | Phase | Age (days) | Distance (km) | Declination |
|---|---|---|---|---|---|
| 11-22 00:00 | 90.5% | Waxing Gibbous | 12.71 | 371780 | +13.3 |
| 11-22 06:00 | 92.1% | Waxing Gibbous | 12.96 | 370379 | +14.8 |
| 11-22 12:00 | 93.6% | Waxing Gibbous | 13.21 | 369032 | +16.1 |
| 11-22 18:00 | 94.9% | Waxing Gibbous | 13.46 | 367747 | +17.5 |
| 11-23 00:00 | 96.1% | Waxing Gibbous | 13.71 | 366531 | +18.8 |

Lunar calendar around the date (skyfield):

- Last Quarter: 2026-11-01 20:28:27 GMT
- New Moon: 2026-11-09 07:02:07 GMT
- First Quarter: 2026-11-17 11:47:50 GMT
- Full Moon: 2026-11-24 14:53:34 GMT
- Last Quarter: 2026-12-01 06:08:40 GMT
- New Moon: 2026-12-09 00:51:51 GMT
- Perigee: 2026-10-28 18:13:47 GMT, 364386 km
- Perigee: 2026-11-25 21:08:12 GMT, 359336 km
- Perigee: 2026-12-24 08:37:47 GMT, 356648 km
- Apogee: 2026-11-13 17:57:31 GMT, 405650 km
- Apogee: 2026-12-11 06:58:49 GMT, 406436 km

**Reading:** the session falls 2 days 15 h (at midnight) to 1 day 15 h before the full moon of 24 Nov 14:53 GMT, with lunar perigee on 25 Nov 21:08 (359,336 km). Full moon and perigee nearly coincide, so the spring tides of 25-27 Nov are perigean (large); 22 Nov is on the steep build towards them (see `tides.md`).

## 3. Hour-by-hour light, Newlyn/Penzance (representative of the county; other points differ by <= 5 minutes)

| Hour (GMT) | Sun altitude | Moon altitude | Moon azimuth | Moon lit | Light class (clear sky) | Cloud % Newlyn: median (range) / low-cloud median | Cloud % Bude | Cloud % Looe |
|---|---|---|---|---|---|---|---|---|
| 11-22 00:00 | -59.9 | 42.8 | 230 | 91% | night - MOONLIT (moon 43 deg up, 91% lit) | 100 (92-100) / 100 | 100 (92-100) / 75 | 100 (92-100) / 96 |
| 11-22 01:00 | -58.3 | 35.1 | 246 | 91% | night - MOONLIT (moon 35 deg up, 91% lit) | 100 (92-100) / 100 | 100 (92-100) / 61 | 100 (92-100) / 100 |
| 11-22 02:00 | -52.7 | 26.3 | 259 | 91% | night - MOONLIT (moon 26 deg up, 91% lit) | 100 (92-100) / 100 | 100 (92-100) / 70 | 100 (92-100) / 100 |
| 11-22 03:00 | -44.8 | 17.2 | 270 | 91% | night - MOONLIT (moon 17 deg up, 91% lit) | 100 (92-100) / 100 | 100 (92-100) / 79 | 100 (92-100) / 100 |
| 11-22 04:00 | -35.7 | 8.1 | 281 | 92% | night - low moon (8 deg, 92%) | 100 (92-100) / 96 | 100 (88-100) / 93 | 100 (92-100) / 100 |
| 11-22 05:00 | -26.1 | -0.6 | 292 | 92% | night - DARK (moon down) | 100 (92-100) / 88 | 100 (76-100) / 96 | 100 (92-100) / 100 |
| 11-22 06:00 | -16.6 | -8.5 | 304 | 92% | astronomical twilight - DARK (moon down) | 100 (92-100) / 56 | 100 (88-100) / 100 | 100 (92-100) / 100 |
| 11-22 07:00 | -7.4 | -15.4 | 316 | 92% | nautical twilight | 100 (92-100) / 78 | 100 (88-100) / 98 | 100 (92-100) / 100 |
| 11-22 08:00 | 1.0 | -20.7 | 330 | 93% | DAYLIGHT | 100 (92-100) / 89 | 100 (88-100) / 99 | 100 (92-100) / 100 |
| 11-22 09:00 | 8.4 | -24.1 | 344 | 93% | DAYLIGHT | 100 (92-100) / 76 | 100 (92-100) / 100 | 100 (92-100) / 100 |
| 11-22 10:00 | 14.2 | -25.1 | 360 | 93% | DAYLIGHT | 100 (92-100) / 74 | 100 (92-100) / 100 | 100 (92-100) / 100 |
| 11-22 11:00 | 18.1 | -23.7 | 15 | 93% | DAYLIGHT | 100 (88-100) / 85 | 100 (92-100) / 100 | 100 (92-100) / 99 |
| 11-22 12:00 | 19.7 | -20.0 | 29 | 94% | DAYLIGHT | 100 (92-100) / 54 | 100 (92-100) / 100 | 100 (92-100) / 96 |
| 11-22 13:00 | 18.8 | -14.4 | 42 | 94% | DAYLIGHT | 100 (92-100) / 52 | 100 (92-100) / 100 | 100 (92-100) / 100 |
| 11-22 14:00 | 15.5 | -7.3 | 54 | 94% | DAYLIGHT | 100 (92-100) / 68 | 100 (92-100) / 100 | 100 (92-100) / 98 |
| 11-22 15:00 | 10.1 | 0.9 | 66 | 94% | DAYLIGHT | 100 (88-100) / 69 | 100 (92-100) / 100 | 100 (92-100) / 92 |
| 11-22 16:00 | 3.1 | 9.8 | 76 | 94% | DAYLIGHT | 100 (76-100) / 48 | 100 (92-100) / 99 | 100 (88-100) / 92 |
| 11-22 17:00 | -5.1 | 19.2 | 87 | 95% | civil twilight | 100 (76-100) / 26 | 100 (92-100) / 100 | 100 (92-100) / 84 |
| 11-22 18:00 | -14.1 | 28.7 | 98 | 95% | astronomical twilight - MOONLIT (moon 29 deg up, 95% lit) | 98 (76-100) / 30 | 100 (92-100) / 100 | 100 (88-100) / 77 |
| 11-22 19:00 | -23.6 | 37.9 | 110 | 95% | night - MOONLIT (moon 38 deg up, 95% lit) | 96 (68-100) / 37 | 100 (92-100) / 100 | 100 (88-100) / 90 |
| 11-22 20:00 | -33.2 | 46.4 | 126 | 95% | night - MOONLIT (moon 46 deg up, 95% lit) | 94 (56-100) / 57 | 100 (92-100) / 100 | 100 (92-100) / 86 |
| 11-22 21:00 | -42.5 | 53.3 | 144 | 96% | night - MOONLIT (moon 53 deg up, 96% lit) | 100 (20-100) / 44 | 100 (92-100) / 100 | 100 (92-100) / 88 |
| 11-22 22:00 | -50.9 | 57.3 | 168 | 96% | night - MOONLIT (moon 57 deg up, 96% lit) | 94 (0-100) / 32 | 100 (92-100) / 100 | 100 (88-100) / 92 |
| 11-22 23:00 | -57.2 | 57.4 | 194 | 96% | night - MOONLIT (moon 57 deg up, 96% lit) | 86 (0-100) / 24 | 100 (91-100) / 100 | 100 (39-100) / 90 |
| 11-23 00:00 | -60.1 | 53.5 | 217 | 96% | night - MOONLIT (moon 54 deg up, 96% lit) | n/a | n/a | n/a |

**Summary of the light regime (clear-sky astronomy):** moon up and bright (91-92% lit) from midnight until moonset about 05:00; the only truly dark period of the whole 24 h is about **05:00 to 05:50** (moon down, before astronomical twilight) with deepening twilight to civil dawn about 07:10; sunrise about 07:42-07:49; sunset about 16:22-16:34 (east to west); civil dusk ends about 17:00-17:10; the 94-96% moon has already risen (about 14:45) and is 20+ degrees up by the end of civil twilight, so **the evening has no dark period at all** unless cloud removes the moonlight. Cloud cover therefore decides whether the night of the 22nd fishes as "dark" or "bright" - see the cloud columns above and `weather.md`.

## 4. Cross-check of the computation (Newlyn/Penzance 50.10N 5.54W)

| Quantity | skyfield DE440s | USNO API | MET Norway API |
|---|---|---|---|
| Civil twilight begins | 07:10 | 07:10 | - |
| Sunrise | 07:46 | 07:46 | 07:46 |
| Solar noon | 12:08 | 12:08 | 12:08 |
| Sunset | 16:30 | 16:30 | 16:29 |
| Civil twilight ends | 17:06 | 17:06 | - |
| Moonset | 05:02 | 05:02 | 05:01 |
| Moonrise | 14:48 | 14:48 | 14:47 |
| Moon upper transit | 22:28 | 22:28 | 22:28 |
| Illuminated fraction | 91-95% through the day | 94% | phase angle 144.5 deg |
| Nearest phase | Full Moon 24 Nov 14:53 | Full Moon 24 Nov 14:53 | - |

All three agree to within one minute (differences are rounding / refraction conventions). No contradiction found.

## 5. Tide phases against light on 22 November

| Port | Event | Time (GMT) | Height (m CD) | Light at that time (Newlyn astronomy, clear sky) |
|---|---|---|---|---|
| Bude | HW | 03:10 | 6.74 | night - MOONLIT (moon 16 deg up, 91% lit) |
| Bude | LW | 09:30 |  | DAYLIGHT |
| Bude | HW | 15:31 | 7.15 | DAYLIGHT |
| Bude | LW | 21:55 |  | night - MOONLIT (moon 57 deg up, 96% lit) |
| Padstow | HW | 02:57 | 6.45 | night - MOONLIT (moon 17 deg up, 91% lit) |
| Padstow | LW | 09:25 | 1.75 | DAYLIGHT |
| Padstow | HW | 15:18 | 6.82 | DAYLIGHT |
| Padstow | LW | 21:50 | 1.40 | night - MOONLIT (moon 57 deg up, 96% lit) |
| Newquay | HW | 02:45 | 6.15 | night - MOONLIT (moon 19 deg up, 91% lit) |
| Newquay | LW | 09:12 | 1.60 | DAYLIGHT |
| Newquay | HW | 15:05 | 6.52 | DAYLIGHT |
| Newquay | LW | 21:36 | 1.22 | night - MOONLIT (moon 56 deg up, 96% lit) |
| St Ives | HW | 02:48 | 5.75 | night - MOONLIT (moon 19 deg up, 91% lit) |
| St Ives | LW | 09:16 | 1.66 | DAYLIGHT |
| St Ives | HW | 15:07 | 6.12 | DAYLIGHT |
| St Ives | LW | 21:40 | 1.34 | night - MOONLIT (moon 56 deg up, 96% lit) |
| St Mary's (Scilly) | HW | 02:19 | 5.07 | night - MOONLIT (moon 23 deg up, 91% lit) |
| St Mary's (Scilly) | LW | 08:45 | 1.43 | DAYLIGHT |
| St Mary's (Scilly) | HW | 14:39 | 5.32 | DAYLIGHT |
| St Mary's (Scilly) | LW | 21:06 | 1.20 | night - MOONLIT (moon 54 deg up, 96% lit) |
| Newlyn (Penzance) | HW | 02:17 | 4.97 | night - MOONLIT (moon 23 deg up, 91% lit) |
| Newlyn (Penzance) | LW | 08:55 | 1.48 | DAYLIGHT |
| Newlyn (Penzance) | HW | 14:35 | 5.23 | DAYLIGHT |
| Newlyn (Penzance) | LW | 21:18 | 1.24 | night - MOONLIT (moon 55 deg up, 96% lit) |
| Lizard Point | HW | 02:35 | 4.63 | night - MOONLIT (moon 22 deg up, 91% lit) |
| Lizard Point | LW | 08:59 | 1.34 | DAYLIGHT |
| Lizard Point | HW | 14:54 | 4.92 | DAYLIGHT |
| Lizard Point | LW | 21:23 | 1.03 | night - MOONLIT (moon 55 deg up, 96% lit) |
| Falmouth | HW | 02:49 | 4.63 | night - MOONLIT (moon 19 deg up, 91% lit) |
| Falmouth | LW | 09:23 | 1.17 | DAYLIGHT |
| Falmouth | HW | 15:06 | 4.87 | DAYLIGHT |
| Falmouth | LW | 21:49 | 0.93 | night - MOONLIT (moon 57 deg up, 96% lit) |
| Fowey | HW | 03:08 | 4.86 | night - MOONLIT (moon 16 deg up, 91% lit) |
| Fowey | LW | 09:27 | 1.38 | DAYLIGHT |
| Fowey | HW | 15:27 | 5.05 | DAYLIGHT |
| Fowey | LW | 21:51 | 1.11 | night - MOONLIT (moon 57 deg up, 96% lit) |
| Looe | HW | 03:11 | 4.81 | night - MOONLIT (moon 16 deg up, 91% lit) |
| Looe | LW | 09:30 | 1.38 | DAYLIGHT |
| Looe | HW | 15:31 | 5.01 | DAYLIGHT |
| Looe | LW | 21:55 | 1.11 | night - MOONLIT (moon 57 deg up, 96% lit) |
| Plymouth (Devonport) | HW | 03:21 | 4.96 | night - MOONLIT (moon 14 deg up, 91% lit) |
| Plymouth (Devonport) | LW | 09:35 | 1.58 | DAYLIGHT |
| Plymouth (Devonport) | HW | 15:41 | 5.15 | DAYLIGHT |
| Plymouth (Devonport) | LW | 22:00 | 1.31 | night - MOONLIT (moon 57 deg up, 96% lit) |

**Coincidences (south coast, Newlyn/Falmouth/Plymouth timing; north coast about 30-45 min later):**

- **Night HW ~02:15-03:20** falls under a bright, high-ish moon in the west (26 deg at 02:00, 9 deg at 04:00) - moonlit unless overcast.
- **The only dark hour (about 05:00-05:50)** falls on the middle of the ebb (HW+2.5 to HW+3.5 south coast).
- **Dawn (civil twilight ~07:10 to sunrise ~07:46)** coincides with the last 1.5-2 h of the ebb; **LW ~08:45-09:35 is in full daylight**, so the first of the flood is a daylight event (09:00-11:00).
- **Afternoon HW ~14:35-15:40** is in daylight; **sunset ~16:25-16:30 and dusk to ~17:05 fall 1-2 h into the ebb** (south coast HW+1 to HW+2.5; north coast HW+1 to HW+1.75).
- **Evening LW ~21:05-22:00** is under a high, 95% moon (48-57 deg altitude, transit 22:28) - the brightest possible night if the sky is clear; the following flood (22:00-24:00) likewise.
- A dusk-plus-flood coincidence does **not** occur on this date; a dawn-plus-flood coincidence does not occur either (dawn is late ebb). The flood tides run ~09:00-15:00 (daylight) and ~21:30-03:30 (night of the 22nd/23rd, mostly outside the 24 h window).

## 6. Solunar periods (low-evidence folk theory, grade C/D - recorded only because asked)

- "Major" periods (moon overhead / underfoot, +-1 h): lower transit 10:01 and upper transit 22:28 GMT.
- "Minor" periods (moonset / moonrise, +-30 min): moonset 05:02, moonrise 14:48 GMT.
- No peer-reviewed support for solunar tables in tidal sea fishing was located by this stream; in tidal water the tide phase dominates. Treated as zero-weight in scoring unless Phase 2 finds evidence.

## 7. Gaps

- Fishing-effect literature for moonlight/cloud by species is handled in `species_sst.md` (workstream 4), not here.
- Illuminance in lux under forecast cloud was not modelled; cloud is reported as cover fraction only (THIN for actual on-water brightness).
