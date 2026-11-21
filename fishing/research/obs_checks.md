# Observation and independent-source checks (stream obs_checks)

Compiled 21 Nov 2026, from about 16:58 UTC. All times UTC (= GMT = local).

## 1. Station observations 12-21 Nov 2026 (Ogimet raw SYNOP)

Source: Ogimet getsynop, https://www.ogimet.com/cgi-bin/getsynop?block=NNNNN&begin=202611120000&end=202611211800 . Grade A (primary WMO SYNOP messages relayed by Ogimet). Accessed 2026-11-21 ~16:58 UTC; data run to the 16:30 UTC observation (Culdrose, Scilly 10-minute reports) or 16:00 (others). Raw files: raw/obs/synop_<block>_1658.txt.

Decoding (D = my own decoding, shown so it can be checked): groups after "AAXX DDGGi" - iw digit (last char of the date/time group): 4 = wind in knots, 1 = m/s (Culdrose's 10-minute reports use iw=1, converted x1.944). Nddff: dd tens of degrees, ff speed. 1sTTT air temp, 2sTTT dew point, 3PPPP station pressure (ignored), 4PPPP = MSLP in hPa (value +1000 when <500). In section 333: 911ff = highest gust in the past hour (kt, iw=4), 6RRR5 = rain in the past hour, mm (RRR 990 = trace 0.0, 991-999 = 0.1-0.9). Only the on-the-hour report of each station is used for tables; the 10-minute Culdrose and Scilly reports exist but were not tabulated. Daily rows are UTC days; "mean wind" is the mean of 24 hourly 10-minute-mean speeds. Rain = sum of hourly 6RRR5 groups (may be slightly low if an hour is missing; daily n is shown).

Stations obtained: Culdrose 03809, Camborne 03808, St Mary's Airport (Scilly) 03803, Cardinham 03823, Plymouth Mount Batten 03827.
NOT FOUND on Ogimet: Newquay/St Mawgan (03817 returned empty; also tried 03815, 03816, 03813, 03814, 03818, 03820, 03821, 03822, 03826, 03829, 03830 - empty). Bude / Chivenor: no SYNOP block located via Ogimet. Met Office observation pages not tried for these (JS site). THIN DATA for the north-coast mainland (only Camborne is near the north coast).

Note: Cardinham (03823) is an inland upland site (station pressure ~979 hPa; MSLP reduced); Camborne and St Mary's are close to the coast. Winds at inland sites read lower than at exposed headlands.

### Headline (observations)

(see tables below)

## 1a. Daily summaries

### Culdrose (03809) daily summary from on-the-hour SYNOP (UTC day)

| Date | n obs | MSLP min/mean/max hPa | Mean wind kt (max) | Max gust kt | Dominant dir (circ. mean) | T min/max C | Rain mm (sum of hourly 6RRR5 groups in SYNOP sect.3) |
|---|---|---|---|---|---|---|---|
| 11-12 | 24 | 1002.1/1006.7/1013.8 | 12 (17) | 24 | 47 | 2.3/10.2 | 0.0 (24 hourly grp) |
| 11-13 | 24 | 1014.6/1017.4/1018.9 | 6 (10) | 12 | 61 | 0.7/9.7 | 0.0 (24 hourly grp) |
| 11-14 | 24 | 1004.2/1012.1/1018.2 | 7 (12) | 21 | 154 | 5.8/10.4 | 0.0 (24 hourly grp) |
| 11-15 | 24 | 995.8/999.2/1004.9 | 11 (17) | 29 | 252 | 9.5/12.6 | 8.8 (24 hourly grp) |
| 11-16 | 24 | 985.8/1000.5/1006.8 | 8 (16) | 31 | 141 | 7.4/14.3 | 9.4 (24 hourly grp) |
| 11-17 | 24 | 982.1/983.6/985.1 | 19 (25) | 50 | 251 | 10.9/14.2 | 14.8 (24 hourly grp) |
| 11-18 | 24 | 983.1/986.3/989.4 | 16 (24) | 42 | 241 | 9.3/13.3 | 8.0 (24 hourly grp) |
| 11-19 | 24 | 982.7/988.5/994.0 | 19 (23) | 39 | 256 | 10.0/12.7 | 8.6 (24 hourly grp) |
| 11-20 | 24 | 993.9/1004.9/1014.6 | 12 (29) | 43 | 272 | 8.5/12.4 | 4.0 (24 hourly grp) |
| 11-21 | 17 | 1008.5/1013.1/1015.3 | 8 (16) | 23 | 105 | 2.9/12.3 | 0.2 (17 hourly grp) |

### Camborne (03808) daily summary from on-the-hour SYNOP (UTC day)

| Date | n obs | MSLP min/mean/max hPa | Mean wind kt (max) | Max gust kt | Dominant dir (circ. mean) | T min/max C | Rain mm (sum of hourly 6RRR5 groups in SYNOP sect.3) |
|---|---|---|---|---|---|---|---|
| 11-12 | 24 | 1003.0/1007.4/1014.2 | 10 (15) | 24 | 51 | 3.3/9.1 | 0.0 (24 hourly grp) |
| 11-13 | 24 | 1014.9/1017.8/1019.2 | 5 (7) | 12 | 94 | 1.9/9.5 | 0.0 (24 hourly grp) |
| 11-14 | 24 | 1004.2/1012.3/1018.4 | 8 (14) | 22 | 154 | 6.5/10.2 | 0.0 (24 hourly grp) |
| 11-15 | 24 | 996.0/999.4/1005.3 | 10 (15) | 28 | 261 | 8.3/12.4 | 17.8 (24 hourly grp) |
| 11-16 | 24 | 985.9/1000.6/1007.0 | 10 (22) | 35 | 143 | 7.2/14.2 | 6.8 (24 hourly grp) |
| 11-17 | 24 | 982.3/983.7/985.1 | 15 (22) | 38 | 241 | 10.4/14.2 | 14.6 (24 hourly grp) |
| 11-18 | 24 | 983.3/986.3/989.4 | 12 (18) | 37 | 223 | 7.8/12.9 | 4.2 (24 hourly grp) |
| 11-19 | 24 | 983.1/988.7/994.3 | 14 (20) | 35 | 251 | 9.2/12.5 | 17.8 (24 hourly grp) |
| 11-20 | 24 | 994.0/1005.1/1014.8 | 10 (24) | 40 | 274 | 7.9/12.0 | 2.4 (24 hourly grp) |
| 11-21 | 17 | 1008.6/1013.2/1015.5 | 8 (15) | 23 | 137 | 7.1/12.2 | 0.2 (17 hourly grp) |

### St Mary's Airport (03803) daily summary from on-the-hour SYNOP (UTC day)

| Date | n obs | MSLP min/mean/max hPa | Mean wind kt (max) | Max gust kt | Dominant dir (circ. mean) | T min/max C | Rain mm (sum of hourly 6RRR5 groups in SYNOP sect.3) |
|---|---|---|---|---|---|---|---|
| 11-12 | 24 | 1002.3/1006.8/1013.7 | 17 (22) | 31 | 51 | 8.9/11.5 | 0.0 (24 hourly grp) |
| 11-13 | 24 | 1014.3/1017.1/1018.8 | 10 (17) | 23 | 101 | 7.6/10.8 | 0.0 (24 hourly grp) |
| 11-14 | 24 | 1002.8/1011.4/1017.5 | 17 (24) | 30 | 165 | 9.2/11.5 | 0.0 (24 hourly grp) |
| 11-15 | 24 | 996.2/999.7/1005.9 | 15 (26) | 33 | 259 | 9.8/13.0 | 8.0 (24 hourly grp) |
| 11-16 | 24 | 985.7/999.8/1007.1 | 14 (26) | 37 | 153 | 9.2/14.3 | 6.8 (24 hourly grp) |
| 11-17 | 24 | 982.8/984.0/985.6 | 22 (26) | 46 | 245 | 11.5/14.2 | 11.0 (24 hourly grp) |
| 11-18 | 24 | 982.9/986.1/989.1 | 21 (27) | 45 | 235 | 10.2/14.8 | 11.2 (24 hourly grp) |
| 11-19 | 24 | 983.0/989.1/994.6 | 20 (28) | 45 | 257 | 11.0/13.3 | 12.6 (24 hourly grp) |
| 11-20 | 24 | 994.7/1005.9/1014.6 | 17 (30) | 47 | 276 | 11.1/13.9 | 4.6 (24 hourly grp) |
| 11-21 | 17 | 1006.7/1012.1/1014.9 | 14 (22) | 28 | 142 | 12.0/14.5 | 0.0 (17 hourly grp) |

### Cardinham (03823) daily summary from on-the-hour SYNOP (UTC day)

| Date | n obs | MSLP min/mean/max hPa | Mean wind kt (max) | Max gust kt | Dominant dir (circ. mean) | T min/max C | Rain mm (sum of hourly 6RRR5 groups in SYNOP sect.3) |
|---|---|---|---|---|---|---|---|
| 11-12 | 24 | 1003.3/1007.5/1013.9 | 9 (13) | 22 | 42 | 1.2/7.2 | 0.0 (24 hourly grp) |
| 11-13 | 24 | 1014.7/1017.9/1019.4 | 4 (7) | 14 | 115 | 0.1/9.3 | 0.0 (24 hourly grp) |
| 11-14 | 24 | 1004.8/1012.5/1018.9 | 9 (13) | 23 | 151 | 3.7/9.5 | 0.0 (24 hourly grp) |
| 11-15 | 24 | 995.5/998.8/1004.4 | 10 (17) | 28 | 265 | 6.6/11.1 | 21.4 (24 hourly grp) |
| 11-16 | 24 | 985.6/1000.9/1006.8 | 8 (20) | 33 | 132 | 5.5/13.3 | 8.8 (24 hourly grp) |
| 11-17 | 24 | 981.1/982.8/984.8 | 14 (21) | 34 | 257 | 8.6/13.5 | 27.8 (24 hourly grp) |
| 11-18 | 24 | 983.3/985.8/988.7 | 12 (18) | 35 | 238 | 6.3/12.7 | 5.0 (24 hourly grp) |
| 11-19 | 24 | 982.5/987.9/993.9 | 10 (16) | 31 | 258 | 6.9/11.1 | 14.4 (24 hourly grp) |
| 11-20 | 24 | 992.2/1004.2/1014.7 | 7 (16) | 30 | 275 | 7.5/12.0 | 19.6 (24 hourly grp) |
| 11-21 | 17 | 1009.8/1013.7/1015.4 | 8 (15) | 24 | 131 | 6.3/11.0 | 0.2 (17 hourly grp) |

### Plymouth Mount Batten (03827) daily summary from on-the-hour SYNOP (UTC day)

| Date | n obs | MSLP min/mean/max hPa | Mean wind kt (max) | Max gust kt | Dominant dir (circ. mean) | T min/max C | Rain mm (sum of hourly 6RRR5 groups in SYNOP sect.3) |
|---|---|---|---|---|---|---|---|
| 11-12 | 24 | 1002.9/1007.0/1013.9 | 8 (15) | 24 | 40 | 2.9/9.2 | 0.0 (24 hourly grp) |
| 11-13 | 24 | 1014.6/1018.0/1019.6 | 3 (6) | 8 | 77 | -0.4/10.5 | 0.0 (24 hourly grp) |
| 11-14 | 24 | 1005.1/1013.1/1019.1 | 7 (13) | 17 | 126 | 3.0/10.7 | 0.0 (24 hourly grp) |
| 11-15 | 24 | 995.9/999.1/1004.6 | 12 (17) | 26 | 240 | 9.3/12.6 | 6.2 (24 hourly grp) |
| 11-16 | 24 | 986.2/1001.5/1007.0 | 7 (25) | 33 | 112 | 7.2/14.3 | 12.2 (24 hourly grp) |
| 11-17 | 24 | 981.6/983.3/985.5 | 18 (26) | 41 | 247 | 10.5/14.2 | 12.6 (24 hourly grp) |
| 11-18 | 24 | 983.5/986.4/989.6 | 18 (25) | 45 | 237 | 9.2/13.0 | 5.0 (24 hourly grp) |
| 11-19 | 24 | 983.2/988.3/994.6 | 13 (18) | 30 | 257 | 8.7/12.8 | 13.2 (24 hourly grp) |
| 11-20 | 24 | 993.3/1004.4/1014.9 | 7 (24) | 36 | 256 | 8.8/12.2 | 6.2 (24 hourly grp) |
| 11-21 | 17 | 1010.9/1014.2/1015.4 | 7 (12) | 20 | 113 | 7.4/13.2 | 0.2 (17 hourly grp) |

## 1b. 20-21 Nov trace

### Culdrose (03809) trace, every 3 h (UTC), 20-21 Nov, plus last hourly

| Time | MSLP hPa | Wind dir/kt | Gust kt | Temp C | Dew C | 1h rain mm |
|---|---|---|---|---|---|---|
| 11-20T00:00 | 993.9 | 250/26 | 39 | 12.0 | 9.7 | 0.0 |
| 11-20T03:00 | 995.6 | 280/21 | 34 | 11.2 | 9.6 | 0.4 |
| 11-20T06:00 | 999.5 | 280/12 | 26 | 10.6 | 9.4 | 0.4 |
| 11-20T09:00 | 1003.4 | 280/10 | 15 | 10.3 | 9.3 | 0.0 |
| 11-20T12:00 | 1006.9 | 290/15 | 23 | 11.0 | 9.3 | 0.6 |
| 11-20T15:00 | 1008.5 | 280/10 | 19 | 11.4 | 9.7 | 0.0 |
| 11-20T18:00 | 1011.2 | 260/5 | 8 | 10.0 | 9.1 | 0.0 |
| 11-20T21:00 | 1013.6 | 310/2 | 8 | 8.5 | 7.8 | 0.0 |
| 11-21T00:00 | 1014.8 | 270/4 | 5 | 7.3 | 6.9 | 0.0 |
| 11-21T03:00 | 1014.8 | 90/4 | 4 | 4.4 | 4.4 | 0.0 |
| 11-21T06:00 | 1014.6 | 90/5 | 7 | 4.6 | 4.5 | 0.0 |
| 11-21T09:00 | 1013.8 | 100/7 | 9 | 6.3 | 6.3 | 0.0 |
| 11-21T12:00 | 1012.1 | 120/13 | 21 | 12.1 | 9.4 | 0.0 |
| 11-21T15:00 | 1009.1 | 110/15 | 21 | 12.3 | 10.9 | 0.0 |
| 11-21T16:00 | 1008.5 | 120/16 | 23 | 12.2 | 10.9 | 0.0 |

### Camborne (03808) trace, every 3 h (UTC), 20-21 Nov, plus last hourly

| Time | MSLP hPa | Wind dir/kt | Gust kt | Temp C | Dew C | 1h rain mm |
|---|---|---|---|---|---|---|
| 11-20T00:00 | 994.0 | 240/17 | 29 | 11.0 | 9.5 | 0.2 |
| 11-20T03:00 | 995.9 | 280/18 | 32 | 10.3 | 9.5 | 1.0 |
| 11-20T06:00 | 999.7 | 290/13 | 24 | 11.2 | 9.4 | 0.0 |
| 11-20T09:00 | 1003.6 | 280/10 | 16 | 11.0 | 9.1 | 0.2 |
| 11-20T12:00 | 1007.0 | 280/11 | 20 | 12.0 | 9.6 | 0.0 |
| 11-20T15:00 | 1008.7 | 280/9 | 14 | 11.9 | 9.6 | 0.0 |
| 11-20T18:00 | 1011.5 | 240/2 | 6 | 10.1 | 8.8 | 0.2 |
| 11-20T21:00 | 1013.8 | 220/3 | 6 | 9.3 | 8.3 | 0.0 |
| 11-21T00:00 | 1015.0 | 210/4 | 6 | 7.9 | 7.4 | 0.0 |
| 11-21T03:00 | 1014.9 | 160/5 | 6 | 8.4 | 8.0 | 0.2 |
| 11-21T06:00 | 1014.7 | 140/6 | 8 | 7.4 | 7.1 | 0.0 |
| 11-21T09:00 | 1013.8 | 130/8 | 12 | 9.9 | 8.3 | 0.0 |
| 11-21T12:00 | 1012.2 | 140/12 | 22 | 12.1 | 9.2 | 0.0 |
| 11-21T15:00 | 1009.4 | 120/13 | 22 | 12.1 | 10.0 | 0.0 |
| 11-21T16:00 | 1008.6 | 120/15 | 22 | 12.0 | 10.2 | 0.0 |

### St Mary's Airport (03803) trace, every 3 h (UTC), 20-21 Nov, plus last hourly

| Time | MSLP hPa | Wind dir/kt | Gust kt | Temp C | Dew C | 1h rain mm |
|---|---|---|---|---|---|---|
| 11-20T00:00 | 994.7 | 260/30 | 47 | 12.1 | 10.4 | 0.2 |
| 11-20T03:00 | 997.5 | 270/25 | 39 | 12.4 | 10.4 | 0.0 |
| 11-20T06:00 | 1001.0 | 280/17 | 29 | 12.0 | 10.4 | 0.8 |
| 11-20T09:00 | 1004.8 | 280/19 | 32 | 11.9 | 10.8 | 0.8 |
| 11-20T12:00 | 1007.8 | 260/15 | 28 | 12.6 | 10.5 | 0.0 |
| 11-20T15:00 | 1009.3 | 280/16 | 24 | 13.4 | 11.0 | 0.0 |
| 11-20T18:00 | 1011.8 | 280/11 | 19 | 13.7 | 11.0 | 0.0 |
| 11-20T21:00 | 1013.7 | 280/7 | 12 | 12.9 | 10.8 | 0.0 |
| 11-21T00:00 | 1014.9 | 240/4 | 7 | 12.0 | 10.7 | 0.0 |
| 11-21T03:00 | 1014.3 | 170/7 | 8 | 12.6 | 11.8 | 0.0 |
| 11-21T06:00 | 1013.5 | 150/12 | 15 | 13.6 | 12.4 | 0.0 |
| 11-21T09:00 | 1012.7 | 140/17 | 21 | 14.5 | 13.0 | 0.0 |
| 11-21T12:00 | 1010.9 | 150/20 | 25 | 13.0 | 12.0 | 0.0 |
| 11-21T15:00 | 1007.6 | 130/20 | 24 | 13.4 | 12.2 | 0.0 |
| 11-21T16:00 | 1006.7 | 120/22 | 28 | 13.6 | 12.3 | 0.0 |

### Cardinham (03823) trace, every 3 h (UTC), 20-21 Nov, plus last hourly

| Time | MSLP hPa | Wind dir/kt | Gust kt | Temp C | Dew C | 1h rain mm |
|---|---|---|---|---|---|---|
| 11-20T00:00 | 993.5 | 250/10 | 15 | 8.9 | 8.9 | 3.0 |
| 11-20T03:00 | 993.4 | 280/16 | 27 | 9.3 | 9.3 | 2.0 |
| 11-20T06:00 | 998.1 | 310/11 | 19 | 9.0 | 9.0 | 0.8 |
| 11-20T09:00 | 1002.7 | 250/3 | 10 | 8.5 | 8.5 | 1.0 |
| 11-20T12:00 | 1006.2 | 270/2 | 4 | 8.9 | 8.6 | 1.0 |
| 11-20T15:00 | 1008.1 | 310/3 | 7 | 10.9 | 9.3 | 0.0 |
| 11-20T18:00 | 1011.1 | 50/1 | 3 | 8.2 | 7.9 | 0.0 |
| 11-20T21:00 | 1013.7 | 130/7 | 10 | 8.0 | 8.0 | 0.0 |
| 11-21T00:00 | 1015.0 | 130/6 | 9 | 7.4 | 7.1 | 0.2 |
| 11-21T03:00 | 1014.9 | 120/3 | 6 | 6.9 | 6.8 | 0.0 |
| 11-21T06:00 | 1015.0 | 130/6 | 9 | 6.4 | 6.4 | 0.0 |
| 11-21T09:00 | 1014.5 | 130/7 | 10 | 7.9 | 7.9 | 0.0 |
| 11-21T12:00 | 1012.9 | 130/9 | 16 | 10.2 | 9.3 | 0.0 |
| 11-21T15:00 | 1010.1 | 130/15 | 24 | 10.2 | 8.5 | 0.0 |
| 11-21T16:00 | 1009.8 | 120/13 | 21 | 10.1 | 9.0 | 0.0 |

### Plymouth Mount Batten (03827) trace, every 3 h (UTC), 20-21 Nov, plus last hourly

| Time | MSLP hPa | Wind dir/kt | Gust kt | Temp C | Dew C | 1h rain mm |
|---|---|---|---|---|---|---|
| 11-20T00:00 | 994.6 | 270/7 | 19 | 10.1 | 9.1 | 0.2 |
| 11-20T03:00 | 993.3 | 250/24 | 36 | 11.0 | 9.0 | 0.0 |
| 11-20T06:00 | 997.8 | 290/5 | 14 | 9.8 | 9.2 | 1.0 |
| 11-20T09:00 | 1002.7 | 30/3 | 7 | 9.4 | 8.9 | 0.4 |
| 11-20T12:00 | 1006.2 | 240/2 | 4 | 10.9 | 10.2 | 0.6 |
| 11-20T15:00 | 1008.5 | 110/5 | 7 | 10.9 | 8.7 | 0.0 |
| 11-20T18:00 | 1011.4 | 100/5 | 8 | 9.3 | 7.9 | 0.0 |
| 11-20T21:00 | 1013.9 | 90/6 | 9 | 8.9 | 7.0 | 0.0 |
| 11-21T00:00 | 1015.2 | 110/6 | 11 | 8.7 | 7.4 | 0.2 |
| 11-21T03:00 | 1015.2 | 100/4 | 8 | 7.7 | 6.8 | 0.0 |
| 11-21T06:00 | 1015.2 | 100/6 | 9 | 7.7 | 6.9 | 0.0 |
| 11-21T09:00 | 1015.1 | 100/6 | 9 | 8.7 | 8.1 | 0.0 |
| 11-21T12:00 | 1013.7 | 130/8 | 15 | 12.7 | 8.8 | 0.0 |
| 11-21T15:00 | 1011.1 | 120/10 | 20 | 11.9 | 8.5 | 0.0 |
| 11-21T16:00 | 1010.9 | 120/9 | 18 | 11.4 | 8.8 | 0.0 |

### Interpretation (D)
Daily mean MSLP at Culdrose: 983.6 hPa on 17 Nov (low 982.1) -> 1013.1 on 21 Nov. Winds were W/WSW and gusty 17-20 Nov (Culdrose max gust 50 kt on 17 Nov; 43 kt on 20 Nov, 250-280 deg), eased through 20 Nov evening, calm and clear overnight 20/21 Nov (Culdrose 4.4 C at 03:00), then veered ESE-E and freshened from about 09:00 on 21 Nov with pressure beginning to fall from the 1014.8 hPa peak (1008.5 at 16:00, falling about 3.5 hPa/3 h). That is the leading edge of the next system arriving from the west/southwest.

## 1c. Model verification

#### Verification window: 21 today (on-the-hour obs, stations 03809,03808,03803,03827 vs nearest model points)

| Model | n | MSLP bias hPa | MSLP MAE | Wind bias kt | Wind MAE kt | Wind dir MAE deg (obs>=5kt) |
|---|---|---|---|---|---|---|
| ecmwf_ifs | 136 | -0.1 | 0.2 | -0.2 | 1.5 | 12 |
| meteofrance_arpege_europe | 136 | -0.1 | 0.2 | +1.1 | 2.1 | 13 |
| ecmwf_ifs025 | 136 | -0.0 | 0.2 | -0.7 | 1.3 | 14 |
| ukmo_global_deterministic_10km | 136 | -0.1 | 0.2 | +0.6 | 1.7 | 14 |
| gem_global | 136 | -0.1 | 0.2 | +0.8 | 1.9 | 17 |
| ukmo_uk_deterministic_2km | 136 | -0.1 | 0.2 | +0.4 | 1.7 | 13 |
| gfs_seamless | 136 | -0.1 | 0.3 | +0.5 | 1.6 | 16 |
| ecmwf_aifs025_single | 136 | +0.1 | 0.3 | -0.1 | 1.5 | 14 |
| meteofrance_arome_france | 136 | -0.2 | 0.4 | +1.5 | 2.5 | 16 |
| icon_eu | 136 | -0.3 | 0.4 | -1.1 | 2.3 | 18 |
| dmi_harmonie_arome_europe | 136 | -0.3 | 0.4 | +0.5 | 1.9 | 15 |

#### Verification window: 19-21 (on-the-hour obs, stations 03809,03808,03803,03827 vs nearest model points)

| Model | n | MSLP bias hPa | MSLP MAE | Wind bias kt | Wind MAE kt | Wind dir MAE deg (obs>=5kt) |
|---|---|---|---|---|---|---|
| ecmwf_ifs | 520 | -0.1 | 0.2 | +0.4 | 2.6 | 10 |
| ecmwf_ifs025 | 520 | -0.1 | 0.2 | -1.6 | 3.3 | 13 |
| ukmo_uk_deterministic_2km | 520 | -0.0 | 0.3 | +0.6 | 2.8 | 10 |
| meteofrance_arpege_europe | 520 | -0.1 | 0.3 | +1.6 | 3.1 | 11 |
| gem_global | 520 | +0.0 | 0.3 | +1.7 | 3.1 | 13 |
| gfs_seamless | 520 | -0.1 | 0.3 | +2.5 | 3.3 | 11 |
| ukmo_global_deterministic_10km | 520 | -0.3 | 0.3 | +0.1 | 2.5 | 10 |
| icon_eu | 520 | -0.2 | 0.3 | -1.0 | 2.7 | 13 |
| ecmwf_aifs025_single | 520 | -0.1 | 0.4 | -0.3 | 3.1 | 12 |
| meteofrance_arome_france | 520 | +0.1 | 0.4 | +4.2 | 5.0 | 13 |
| dmi_harmonie_arome_europe | 520 | -0.3 | 0.4 | +1.1 | 2.8 | 11 |
