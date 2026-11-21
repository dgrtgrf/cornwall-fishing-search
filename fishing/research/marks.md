# Workstream 6 - Known shore marks (merged list)

Merged from 14 sweeps (`fishing/research/marks/*.md` + `.jsonl`, 10 geographic sectors + 4 thematic sweeps, run 2026-11-21 16:06-16:27 UTC). **530 raw mark records -> 308 distinct marks** after de-duplication (`fishing/tools/marks/merge_marks.py`; full merged records with every field and source URL in `marks_merged.jsonl`). Evidence quality as graded by the sweep agents: {'thin': 213, 'moderate': 93, 'good': 2}.

**Read this first - limits of the list.** (1) Most per-mark descriptions come from one aggregator site (wheresthefish.uk, grade C; its text is templated and its species scores are modelled, not catch records). (2) Sea Angler, World Sea Fishing forum, Planet Sea Fishing, PressReader and most Facebook sources were blocked to automated access, so the best venue literature was NOT read. (3) Very few marks have a dated late-November catch attached. (4) Aspect, depth and wind/swell preferences are frequently the sweep agent's inference (grade D) - the per-sector files say which. The physical assessment of every kilometre of shore is in `coastline.md`; this list is the documentary layer only.

Columns: id, name, type, lat/lon (confidence), late-November species named by sources, evidence quality, number of source URLs (grades), sweeps that reported it.


## North coast: Devon border to Camel mouth

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K001 | Marsland Mouth | rock mark | 50.9297, -4.5497 (medium) | pouting, whiting | thin | 1 (C) | N1 |
| K002 | Higher Sharpnose Point | headland | 50.9035, -4.5698 (medium) | conger, bull huss, pollack | thin | 2 (B/C) | N1 |
| K003 | Stanbury Mouth | rock mark | 50.8918, -4.5621 (medium) | pouting, conger | thin | 1 (C) | N1 |
| K004 | Lower Sharpnose Point | deep-water rock mark | 50.8859, -4.5666 (medium) | bull huss, conger, pouting | thin | 1 (C) | N1 |
| K005 | Duckpool | rock mark | 50.8757, -4.5585 (medium) | conger, bull huss, pouting | thin | 1 (C) | N1 |
| K006 | Sandymouth | surf beach | 50.8630, -4.5578 (medium) | whiting, bass | moderate | 4 (B/C) | N1, T4 |
| K007 | Northcott Mouth | surf beach | 50.8487, -4.5552 (medium) | whiting, bass, dogfish | moderate | 3 (B/C) | N1, T4 |
| K008 | Flexbury | surf beach | 50.8385, -4.5563 (low) | - | thin | 2 (B) | N1 |
| K009 | Crooklets | surf beach | 50.8357, -4.5537 (medium) | dogfish, bull huss, whiting, flounder, dab, bass | moderate | 4 (B/C) | N1, T4 |
| K010 | Bude Breakwater | pier/breakwater/quay | 50.8310, -4.5512 (medium) | whiting, lesser spotted dogfish, conger, flounder, bass, flounder (d, low), codling, dogfish | moderate | 9 (B/C) | N1, T1, T2, T4 |
| K011 | Compass Point (Bude) | headland | 50.8286, -4.5579 (medium) | - | thin | 1 (B) | N1 |
| K012 | Widemouth Bay | surf beach | 50.7940, -4.5586 (medium) | whiting, dogfish, bass | moderate | 6 (B/C) | N1, T4 |
| K013 | Black Rock (Widemouth) | rock mark | 50.7861, -4.5602 (medium) | pouting, conger | thin | 2 (C) | N1, S3 |
| K014 | Crackington Haven | rock mark | 50.7420, -4.6359 (medium) | pouting, conger | thin | 2 (B/C) | N1 |
| K015 | The Strangles | other | 50.7270, -4.6492 (low) | - | thin | 1 (B) | N1 |
| K016 | High Cliff | headland | 50.7177, -4.6504 (low) | - | thin | 1 (B) | N1 |
| K017 | Boscastle Harbour | harbour | 50.6923, -4.6989 (medium) | flounder | thin | 2 (C) | N1, T2 |
| K018 | Penally Point / Pentargon | headland | 50.6919, -4.7011 (low) | - | thin | 1 (B) | N1 |
| K019 | Rocky Valley | other | 50.6733, -4.7294 (low) | - | thin | 1 (B) | N1 |
| K020 | Bossiney Haven | rock mark | 50.6718, -4.7379 (medium) | conger, rockling | thin | 1 (C) | N1 |
| K021 | Tintagel Head / Barras Nose | deep-water rock mark | 50.6690, -4.7640 (medium) | conger, bull huss, pouting, pollack | thin | 3 (B/C) | N1 |
| K022 | Trebarwith Strand | surf beach | 50.6438, -4.7633 (medium) | whiting, bass | thin | 2 (C) | N1, T4 |
| K023 | Backways Cove | other | 50.6405, -4.7692 (low) | - | thin | 1 (B) | N1 |
| K024 | Tregardock | other | 50.6241, -4.7706 (low) | - | thin | 1 (B) | N1 |
| K025 | The Mouls | island/offshore rock | 50.5939, -4.9230 (medium) | conger, bull huss | thin | 1 (C) | N1 |
| K026 | Port Isaac Harbour | harbour | 50.5938, -4.8332 (medium) | - | thin | 2 (C) | N1, T2 |
| K027 | Port Gaverne | sheltered beach | 50.5927, -4.8227 (low) | - | thin | 1 (B) | N1 |
| K028 | Port Quin | sheltered beach | 50.5888, -4.8672 (low) | - | thin | 1 (B) | N1 |
| K029 | Pentire Point / The Rumps | deep-water rock mark | 50.5869, -4.9348 (medium) | cod, bull huss, conger, dogfish, pollack, pouting, conger eel, lesser spotted dogfish, squid | moderate | 8 (A/B/C) | N1, N2, T3 |
| K030 | Lundy Bay | rock mark | 50.5835, -4.8872 (medium) | pollack, wrasse, conger, pouting | thin | 1 (C) | N1 |
| K031 | Pentireglaze Haven | sheltered beach | 50.5802, -4.9175 (medium) | whiting, pouting, pollack, bass | thin | 2 (C) | N1, N2, T4 |
| K032 | Polzeath | surf beach | 50.5748, -4.9160 (medium) | whiting, lesser spotted dogfish, flounder, small-eyed ray, bass, dab | thin | 4 (B/C) | N1, N2, T4 |
| K033 | Greenaway | rock mark | 50.5679, -4.9272 (medium) | pouting, dogfish, pollack, lesser spotted dogfish, bull huss, conger eel, poor cod, squid, whiting, bass | thin | 2 (C) | N1, N2, T4 |

## Camel estuary to Newquay

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K034 | Stepper Point | deep-water rock mark | 50.5685, -4.9457 (medium) | pollack, pouting, bull huss, conger eel, lesser spotted dogfish, squid | thin | 1 (C) | N2 |
| K035 | Hawker's Cove | estuary | 50.5602, -4.9489 (medium) | flounder, bass, mullet, whiting | thin | 1 (C) | N2 |
| K036 | Daymer Bay | sheltered beach | 50.5602, -4.9281 (medium) | whiting, lesser spotted dogfish, flounder, bass | thin | 2 (C) | N2, T4 |
| K037 | Doom Bar | estuary | 50.5582, -4.9443 (medium) | flounder, bass, mullet, whiting | thin | 1 (C) | N2 |
| K038 | Rock Beach (Camel, Rock shore) | estuary | 50.5534, -4.9280 (medium) | flounder, bass, mullet, whiting | thin | 1 (C) | N2, T4 |
| K039 | Trevose Head | deep-water rock mark | 50.5492, -5.0364 (medium) | pollack, pouting, bull huss, conger eel, lesser spotted dogfish, squid | thin | 2 (C) | N2 |
| K040 | Trevone Bay | sheltered beach | 50.5460, -4.9804 (medium) | whiting, lesser spotted dogfish, flounder, bass | thin | 1 (C) | N2, T4 |
| K041 | Mother Ivey's Bay | sheltered beach | 50.5454, -5.0182 (medium) | whiting, lesser spotted dogfish, flounder, bass | thin | 1 (C) | N2, T4 |
| K042 | Padstow Harbour (outer harbour wall) | harbour | 50.5429, -4.9363 (medium) | pouting, poor cod, whiting, squid, conger eel, flounder | thin | 2 (C) | N2, T2 |
| K043 | Harlyn Bay | surf beach | 50.5399, -4.9975 (medium) | whiting, lesser spotted dogfish, flounder, small-eyed ray, bass, dab | thin | 1 (C) | N2, T4 |
| K044 | Booby's Bay | surf beach | 50.5387, -5.0259 (medium) | whiting, lesser spotted dogfish, flounder, small-eyed ray, bass | thin | 1 (C) | N2 |
| K045 | Constantine Bay | surf beach | 50.5347, -5.0227 (medium) | whiting, lesser spotted dogfish, flounder, small-eyed ray, bass | moderate | 3 (B/C) | N2, T4 |
| K046 | Treyarnon Bay | surf beach | 50.5262, -5.0246 (medium) | whiting, lesser spotted dogfish, flounder, small-eyed ray, bass | thin | 2 (C) | N2, T4 |
| K047 | Wadebridge Quay / tidal Camel at Wadebridge | tidal river | 50.5189, -4.8378 (medium) | flounder, mullet, sea trout (closed season rules apply) | thin | 2 (C) | N2, T2 |
| K048 | Little Petherick Creek | tidal river | 50.5124, -4.9374 (low) | flounder, mullet | thin | 0 (-) | N2 |
| K049 | Porthcothan Bay | sheltered beach | 50.5109, -5.0303 (medium) | whiting, lesser spotted dogfish, flounder, bass | thin | 1 (C) | N2, T4 |
| K050 | Park Head | deep-water rock mark | 50.4975, -5.0459 (medium) | pollack, pouting, bull huss, conger eel, lesser spotted dogfish, squid | thin | 2 (C) | N2 |
| K051 | Pentire Steps (Bedruthan) | rock mark | 50.4909, -5.0359 (medium) | pollack, pouting, lesser spotted dogfish, bull huss, conger eel, poor cod, squid | thin | 1 (C) | N2 |
| K052 | Mawgan Porth | surf beach | 50.4678, -5.0349 (medium) | whiting, lesser spotted dogfish, flounder, small-eyed ray, bass | thin | 2 (C) | N2, T4 |
| K053 | Beacon Cove | sheltered beach | 50.4601, -5.0395 (medium) | - | thin | 0 (-) | N2 |
| K054 | Watergate Bay | surf beach | 50.4455, -5.0438 (medium) | whiting, lesser spotted dogfish, flounder, small-eyed ray, bass | moderate | 5 (B/C) | N2, T4 |
| K055 | Whipsiderry Beach | sheltered beach | 50.4318, -5.0551 (medium) | whiting, lesser spotted dogfish, flounder, bass | thin | 1 (C) | N2, T4 |
| K056 | Towan Head | headland | 50.4255, -5.0999 (medium) | pollack, pouting, conger eel, squid | thin | 1 (C) | N2 |
| K057 | Porth Beach | surf beach | 50.4252, -5.0606 (medium) | flounder, bass, whiting, lesser spotted dogfish, small-eyed ray | moderate | 2 (B/C) | N2, T4 |
| K058 | Lusty Glaze Beach | sheltered beach | 50.4232, -5.0676 (medium) | whiting, dab, bass, lesser spotted dogfish, flounder | moderate | 2 (B/C) | N2, T4 |
| K059 | The Gazzle | rock mark | 50.4211, -5.0942 (medium) | pollack, pouting, lesser spotted dogfish, bull huss, conger eel, poor cod, squid | thin | 1 (C) | N2 |
| K060 | Fly Cellars (Newquay) | rock mark | 50.4191, -5.0871 (medium) | whiting, codling, flounder, lesser spotted dogfish | moderate | 2 (B/C) | N2 |
| K061 | Tolcarne Beach | sheltered beach | 50.4176, -5.0739 (medium) | whiting, flounder, bass, lesser spotted dogfish, small-eyed ray | moderate | 2 (B/C) | N2, T4 |
| K062 | Fistral Beach | surf beach | 50.4163, -5.0996 (medium) | whiting, dab, bass, lesser spotted dogfish, flounder, small-eyed ray | moderate | 2 (B/C) | N2, T4 |
| K063 | Great Western Beach | surf beach | 50.4160, -5.0769 (medium) | whiting, bass, lesser spotted dogfish, flounder | moderate | 2 (B/C) | N2, T4 |
| K064 | Newquay North Quay | harbour | 50.4158, -5.0850 (medium) | pouting, pollack, squid(site-ranked only), whiting, dab, bass, lesser spotted dogfish, flounder, poor cod, squid | moderate | 5 (B/C) | N2, T2, T4 |
| K065 | Pentire Headland (Newquay) | headland | 50.4113, -5.1234 (medium) | pollack, pouting, conger eel, squid, conger/pouting after dark (aggregator, thin) | thin | 1 (C) | N2, N3 |
| K066 | Crantock Beach / Gannel mouth | estuary | 50.4058, -5.1207 (medium) | flounder, bass, mullet, whiting, dab, school bass (coloured water, thin data) | thin | 3 (C) | N2, N3, T1, T4 |
| K067 | Gannel estuary (Crantock/Penpol reaches) | estuary | 50.4036, -5.0730 (low) | flounder, whiting | thin | 1 (C) | N2 |

## Crantock to St Ives

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K068 | Kelsey Head | headland | 50.4046, -5.1466 (high) | conger, bull huss, pouting (d) | thin | 2 (A/C) | N3 |
| K069 | Porth Joke (Polly Joke) | sheltered beach | 50.4013, -5.1362 (high) | dogfish (night), school bass if coloured (thin), whiting, dab, bass | thin | 2 (A/C) | N3, T4 |
| K070 | Holywell Bay | surf beach | 50.3925, -5.1456 (high) | dogfish, flounder (thin), whiting, flounder, bass | thin | 3 (B/C) | N3, T4 |
| K071 | Penhale Sands (Perran Sands, Ligger Point end) | surf beach | 50.3650, -5.1491 (medium) | whiting, dogfish, flounder/dab (thin), dab, bass | moderate | 2 (B/C) | N3, T4 |
| K072 | Perranporth Beach (incl. Droskyn Point, Chapel Rock, river mouth) | surf beach | 50.3485, -5.1545 (medium) | whiting, dogfish, flounder, dab, bass, pollack | moderate | 6 (A/B/C) | N3, T3, T4 |
| K073 | Cligga Head | headland | 50.3398, -5.1818 (medium) | conger, pouting, whiting (aggregator), pollack | thin | 2 (C) | N3, T3 |
| K074 | Trevellas Porth | rock mark | 50.3235, -5.1962 (medium) | pollack, pouting | thin | 3 (A/C) | N3, T3 |
| K075 | Trevaunance Cove (St Agnes) | rock mark | 50.3200, -5.2019 (medium) | pollack, pouting (thin), conger, pouting, pollack (thin) | thin | 5 (A/B/C) | N3 |
| K076 | Chapel Porth | surf beach | 50.3003, -5.2346 (medium) | dab, flounder (thin), whiting, bass | thin | 3 (B/C) | N3, T4 |
| K077 | Porthtowan | surf beach | 50.2872, -5.2418 (medium) | whiting, bass | thin | 2 (C) | N3, T4 |
| K078 | Portreath Beach | surf beach | 50.2611, -5.2942 (medium) | whiting, dogfish, pouting, conger, poor cod, whiting(site-ranked only), bass | thin | 4 (B/C) | N3, T2, T4 |
| K079 | Basset's Cove | deep-water rock mark | 50.2498, -5.3156 (medium) | pollack (thin) | thin | 2 (A/C) | N3 |
| K080 | Navax Point | deep-water rock mark | 50.2437, -5.3788 (medium) | unspecified predators (thin) | thin | 2 (B/C) | N3 |
| K081 | Godrevy Point and Island | headland | 50.2399, -5.3941 (medium) | flounder, conger (thin), pollack | moderate | 5 (A/B/C) | N3, T3 |
| K082 | Gwithian Beach | surf beach | 50.2234, -5.3966 (medium) | whiting, bass, dab, flatfish, plaice | moderate | 4 (B/C) | N3, T4 |
| K083 | Porthgwidden Beach | sheltered beach | 50.2171, -5.4765 (medium) | unspecified (thin), whiting, bass | thin | 1 (C) | N3, T4 |
| K084 | Man's Head / Carrick Du / Clodgy Point | rock mark | 50.2168, -5.4887 (low) | pollack | thin | 4 (A/B/C) | N3, W1 |
| K085 | Porthmeor Beach | surf beach | 50.2156, -5.4816 (medium) | flounder, plaice, dogfish, whiting, cod (possible, unverified), dab, bass | moderate | 4 (B/C) | N3, T4 |
| K086 | The Island (St Ives Head) | rock mark | 50.2135, -5.4767 (medium) | whiting, dogfish, dab, wrasse (reduced), pouting, flounder, school pollack (thin), bass | moderate | 11 (A/B/C) | N3, W1, T2, T4 |
| K087 | Porthminster Beach | sheltered beach | 50.2085, -5.4760 (medium) | whiting, dab, bass, dogfish | moderate | 2 (B/C) | N3, T4 |
| K088 | Mexico Towans | surf beach | 50.2085, -5.4113 (medium) | whiting, flounder, dab, bass, flatfish | moderate | 3 (B/C) | N3, T4 |
| K089 | Carbis Bay Beach | sheltered beach | 50.1982, -5.4647 (medium) | whiting, dab, bass, plaice | moderate | 5 (B/C) | N3, T4 |
| K090 | Hawke's Point | rock mark | 50.1974, -5.4550 (medium) | conger (thin) | thin | 1 (C) | N3 |
| K091 | Hayle Harbour | estuary | 50.1940, -5.4319 (medium) | flounder, mullet(if present), whiting, dab, bass, flatfish, school bass (thin), flounder (d) | moderate | 10 (A/B/C) | N3, T1, T2, T4 |
| K092 | Porth Kidney Sands | surf beach | 50.1938, -5.4399 (medium) | whiting, flounder, bass, dab, flatfish | moderate | 4 (B/C) | N3, T4 |

## West Penwith (St Ives to Mousehole)

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K093 | Penlee Point (lifeboat slip, Mousehole side) | rock mark | 50.3182, -4.1897 (low) | whiting, pouting, coalfish, codling, dogfish, conger | moderate | 4 (B/C) | W1, S5 |
| K094 | Hor Point | rock mark | 50.2176, -5.5088 (medium) | - | thin | 1 (A) | W1 |
| K095 | Pen Enys Point | rock mark | 50.2161, -5.5193 (medium) | - | thin | 1 (A) | W1 |
| K096 | The Carracks | rock mark | 50.2142, -5.5517 (medium) | - | thin | 1 (A) | W1 |
| K097 | Zennor Head | headland | 50.1999, -5.5756 (medium) | pouting, conger, pollack | thin | 1 (C) | W1 |
| K098 | Gurnard's Head | headland | 50.1927, -5.5991 (medium) | pollack, conger, coalfish, pouting | thin | 3 (A/C) | W1, T3 |
| K099 | Porthmeor Cove (Zennor) | rock mark | 50.1850, -5.6000 (medium) | pollack, coalfish, whiting | thin | 2 (C) | W1, T3 |
| K100 | Bosigran / Porthmoina | rock mark | 50.1751, -5.6208 (low) | - | thin | 1 (A) | W1 |
| K101 | Pendeen Watch | headland | 50.1652, -5.6722 (medium) | conger, bull huss, whiting, codling | thin | 1 (C) | W1 |
| K102 | Boat Cove (Pendeen) | rock mark | 50.1649, -5.6623 (medium) | conger | thin | 1 (C) | W1 |
| K103 | Portheras Cove | surf beach | 50.1639, -5.6573 (medium) | bass, flatfish, whiting | thin | 2 (C) | W1, T4 |
| K104 | Levant | rock mark | 50.1526, -5.6841 (low) | - | thin | 1 (A) | W1 |
| K105 | Botallack | rock mark | 50.1375, -5.6841 (low) | - | thin | 1 (A) | W1 |
| K106 | Cape Cornwall | headland | 50.1270, -5.7090 (medium) | pouting, poor cod, conger, pollack | thin | 4 (B/C) | W1, T3 |
| K107 | Priest's Cove | rock mark | 50.1261, -5.7063 (medium) | conger, bull huss | thin | 2 (B/C) | W1 |
| K108 | The Brisons | island/offshore rock | 50.1209, -5.7220 (low) | - | thin | 1 (A) | W1 |
| K109 | Porth Nanven (Cot Valley) | steep shingle beach | 50.1194, -5.7006 (medium) | - | thin | 1 (A) | W1 |
| K110 | Gwynver | surf beach | 50.0897, -5.6893 (medium) | bass | thin | 1 (C) | W1, T4 |
| K111 | Mousehole Harbour | harbour | 50.0823, -5.5381 (medium) | pollack, mullet(if present), flounder | moderate | 4 (B/C) | W1, T2 |
| K112 | St Clement's Isle | island/offshore rock | 50.0815, -5.5322 (medium) | - | thin | 1 (A) | W1 |
| K113 | Sennen Cove breakwater | pier/breakwater/quay | 50.0784, -5.7045 (low) | dogfish | thin | 4 (A/B/C) | W1, T2 |
| K114 | Longships | island/offshore rock | 50.0670, -5.7470 (medium) | - | thin | 2 (A/B) | W1, T3 |
| K115 | Land's End (Dr Syntax's Head, Dr Johnson's Head) | headland | 50.0663, -5.7149 (medium) | conger | thin | 2 (B/C) | W1 |
| K116 | Kemyel / Penzer Point | headland | 50.0649, -5.5490 (medium) | pollack, whiting, conger, bull huss | thin | 3 (B/C) | W1 |
| K117 | Lamorna Cove (quay and point) | harbour | 50.0621, -5.5629 (medium) | conger | thin | 3 (B/C) | W1 |
| K118 | Carn Du (Lamorna) | rock mark | 50.0600, -5.5700 (low) | conger, bull huss, pollack | moderate | 4 (B/C) | W1, T3 |
| K119 | Pordenack Point / Enys Dodnan | rock mark | 50.0584, -5.7097 (low) | - | thin | 1 (A) | W1 |
| K120 | Nanjizal (Mill Bay) | rock mark | 50.0536, -5.6924 (medium) | pollack, conger, pouting, bull huss | thin | 2 (B/C) | W1 |
| K121 | Tater-du | headland | 50.0524, -5.5774 (medium) | - | thin | 1 (A) | W1 |
| K122 | St Loy Cove | steep shingle beach | 50.0514, -5.6015 (medium) | - | thin | 1 (C) | W1 |
| K123 | Boscawen Point | headland | 50.0502, -5.5905 (medium) | - | thin | 1 (C) | W1 |
| K124 | Penberth Cove | rock mark | 50.0473, -5.6292 (medium) | ling, pollack | good | 9 (A/B/C) | W1, T3, G2 |
| K125 | Pedn Vounder | surf beach | 50.0436, -5.6409 (medium) | bass | thin | 1 (C) | W1, T4 |
| K126 | Porthcurno beach | surf beach | 50.0430, -5.6510 (medium) | whiting, dogfish, bass | moderate | 3 (A/B/C) | W1, T4 |
| K127 | Logan Rock (Treryn Dinas) | headland | 50.0409, -5.6369 (medium) | pollack, conger, bull huss | thin | 5 (A/B/C) | W1, T3 |
| K128 | Porth Chapel | rock mark | 50.0395, -5.6580 (medium) | conger, bull huss, bass | thin | 2 (B/C) | W1, T4 |
| K129 | Porthgwarra | rock mark | 50.0378, -5.6722 (medium) | whiting, pollack | thin | 5 (A/B/C) | W1, T3 |
| K130 | Gwennap Head (Tol-Pedn-Penwith) | headland | 50.0360, -5.6800 (medium) | conger, dogfish | thin | 2 (B/C) | W1, T3 |
| K131 | Runnel Stone | island/offshore rock | 50.0228, -5.6734 (medium) | - | thin | 2 (A) | W1 |
| K132 | Wolf Rock | island/offshore rock | 49.9450, -5.8080 (medium) | - | thin | 1 (B) | W1, T3 |
| K133 | Pendour Cove | other | no coordinate | - | thin | 0 (-) | W1 |
| K134 | Penpol (Zennor coast) | rock mark | no coordinate | - | thin | 1 (C) | W1 |
| K135 | Kenidjack (Castle) | rock mark | no coordinate | - | thin | 0 (-) | W1 |
| K136 | Porth Ledden | rock mark | no coordinate | - | thin | 0 (-) | W1 |
| K137 | Aire Point | rock mark | no coordinate | - | thin | 2 (B) | W1 |
| K138 | Carn Les Boel | rock mark | no coordinate | - | thin | 0 (-) | W1 |
| K139 | Pedn-men-an-mere | rock mark | no coordinate | - | thin | 2 (B) | W1 |
| K140 | Porthguarnon | rock mark | no coordinate | - | thin | 0 (-) | W1 |
| K141 | The Merlin | rock mark | no coordinate | conger, pollack | thin | 1 (B) | W1 |

## Mount's Bay (Newlyn to Mullion)

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K142 | Long Rock / Eastern Green beach | surf beach | 50.1283, -5.4999 (medium) | whiting, dab, flounder, plaice, squid, bass, plaice (first pass) | moderate | 4 (B/C) | S1, T4, G2 |
| K143 | Marazion beach | surf beach | 50.1246, -5.4776 (medium) | whiting, plaice, dab, bass | thin | 1 (C) | S1, T4 |
| K144 | St Michael's Mount Causeway | other | 50.1199, -5.4760 (medium) | bass, flounder | thin | 1 (C) | S1, T2 |
| K145 | Albert Pier, Penzance | pier/breakwater/quay | 50.1183, -5.5297 (medium) | flounder, whiting, herring, cod, gobies, rockling, pouting, conger | moderate | 6 (B/C) | S1, T2 |
| K146 | Battery Rocks | rock mark | 50.1144, -5.5312 (medium) | pouting, conger, pollack, whiting, plaice | thin | 3 (B/C) | S1 |
| K147 | Perranuthnoe beach | surf beach | 50.1120, -5.4417 (medium) | whiting, dogfish, whiting (first pass), dogfish (first pass), squid, bass | moderate | 5 (B/C) | S1, T4, G2 |
| K148 | Kenneggy Sands (Keneggy) | surf beach | 50.1042, -5.4117 (medium) | dogfish, dab, bass | thin | 1 (C) | S1, T4 |
| K149 | Newlyn South Pier | pier/breakwater/quay | 50.1029, -5.5430 (medium) | conger, pouting, pollack, rockling, red gurnard | moderate | 5 (B/C) | S1, T2 |
| K150 | Praa Sands | surf beach | 50.1009, -5.3850 (medium) | whiting, dab, plaice, sole/flounder (oct 2024 evidence only), whiting (first pass), bass | moderate | 2 (B/C) | S1, T4, G2 |
| K151 | Prussia Cove (Bessy's Cove) | rock mark | 50.1005, -5.4173 (medium) | pollack, conger, pouting | moderate | 3 (B/C) | S1 |
| K152 | Cudden Point | deep-water rock mark | 50.0992, -5.4269 (medium) | conger, pouting, pollack | moderate | 5 (A/B/C) | S1, T3 |
| K153 | Piskies Cove | rock mark | 50.0990, -5.4223 (medium) | pollack | thin | 1 (C) | S1 |
| K154 | Rinsey Cove | rock mark | 50.0934, -5.3666 (medium) | pouting, rockling, conger | thin | 1 (C) | S1 |
| K155 | Trewavas Head | headland | 50.0895, -5.3622 (medium) | conger, pouting | moderate | 2 (B/C) | S1 |
| K156 | Porthleven Pier & harbour | pier/breakwater | 50.0818, -5.3181 (medium) | rockling, poor cod, pouting, pollack, whiting, dogfish, dab, plaice, flounder, conger(occasional) | moderate | 6 (B/C) | S1, T2, T4 |
| K157 | Loe Bar | steep shingle beach | 50.0687, -5.2945 (medium) | whiting, cod, dogfish, lesser spotted dogfish, small-eyed ray (one nov 2025 fish), bass, cod (b snippet; d for 22 nov) | moderate | 8 (A/B/C) | S1, T4, G2 |
| K158 | Gunwalloe Fishing Cove | sheltered beach | 50.0544, -5.2792 (medium) | whiting, conger, bass | thin | 1 (C) | S1, T4 |
| K159 | Dollar Cove | rock mark | 50.0400, -5.2714 (medium) | rockling, dogfish, bass | thin | 1 (C) | S1, T4 |
| K160 | Church Cove, Gunwalloe | sheltered beach | 50.0383, -5.2675 (medium) | dogfish, pouting, bass | thin | 1 (C) | S1, T4 |
| K161 | Polurrian Cove | rock mark | 50.0225, -5.2568 (medium) | conger, bull huss, bass | thin | 1 (C) | S1, T4 |
| K162 | Mullion Cove harbour wall | pier/breakwater | 50.0150, -5.2593 (high) | pouting, wrasse (small), rockling, pollack, wrasse (small, weed-dependent), dogfish, conger, wrasse | moderate | 4 (A/B/C) | S1, S2, T2, T3 |
| K163 | Mullion Island | island/offshore rock | 50.0125, -5.2692 (low) | - | thin | 1 (C) | S1 |

## The Lizard and Helford

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K164 | Mawnan shore / Rosemullion Head | headland | 50.1099, -5.0823 (medium) | conger, pouting, pollack, ballan wrasse (reduced) | thin | 2 (C) | S2, S3 |
| K165 | Durgan | estuary | 50.1036, -5.1158 (medium) | dogfish, whiting, pouting | thin | 1 (C) | S2 |
| K166 | Helford River (Helford Passage, Port Navas, Gweek) | estuary | 50.1000, -5.1293 (medium) | flounder, whiting, gilthead bream (unlikely, d), pouting, conger (d) | moderate | 3 (B/C) | S2, T1 |
| K167 | Gweek Quay | tidal river | 50.0960, -5.2079 (medium) | flounder, eel (d) | thin | 1 (C) | S2, T2 |
| K168 | Nare Point | headland | 50.0859, -5.0762 (medium) | pouting, whiting | thin | 1 (C) | S2 |
| K169 | Gillan Creek and mouth | tidal river | 50.0855, -5.0956 (medium) | - | moderate | 3 (C) | S2 |
| K170 | Porthallow | steep shingle beach | 50.0684, -5.0793 (medium) | whiting, pouting, conger, dogfish, coalfish, bass | moderate | 5 (A/B/C) | S2, T3, T4 |
| K171 | Porthkerris quarry ledges | rock mark | 50.0646, -5.0679 (medium) | - | thin | 2 (A/C) | S2 |
| K172 | Porthoustock (beach, silo ledge, quarry) | steep shingle beach | 50.0559, -5.0646 (medium) | pollack (d), pouting/scad after dark (wtf), pouting, squid, bass | moderate | 5 (A/C) | S2, T2, T4 |
| K173 | Godrevy Cove (Lizard) | steep shingle beach | 50.0477, -5.0668 (medium) | bass | thin | 1 (C) | S2, T4 |
| K174 | Lowland Point | headland | 50.0359, -5.0688 (medium) | - | thin | 1 (C) | S2 |
| K175 | Coverack harbour and breakwater | pier/breakwater/quay | 50.0230, -5.0941 (medium) | conger, bull huss, dogfish, pouting, bass (after easterly) | moderate | 6 (A/B/C) | S2, T2, T3 |
| K176 | Kennack Sands | surf beach | 50.0065, -5.1587 (medium) | dogfish, ray (d), bass (d), bass | thin | 1 (C) | S2, T4 |
| K177 | Predannack Head | deep-water rock mark | 50.0005, -5.2676 (medium) | pollack, bass (d: swell-dependent) | thin | 2 (A/C) | S2 |
| K178 | Cadgwith Cove (The Todden / Devil's Frying Pan) | rock mark | 49.9868, -5.1793 (medium) | pouting, conger, bull huss | thin | 2 (B/C) | S2 |
| K179 | Kynance Cove / Asparagus Island | rock mark | 49.9743, -5.2299 (medium) | conger, pollack, bass (d) | thin | 3 (A/B/C) | S2, T3 |
| K180 | Church Cove (Landewednack) | rock mark | 49.9711, -5.1875 (medium) | conger, pouting, bull huss, pollack, bass | thin | 1 (C) | S2, T4 |
| K181 | Bass Point | rock mark | 49.9630, -5.1860 (medium) | pouting, conger, bull huss, pollack, bass | thin | 1 (C) | S2 |
| K182 | Housel Bay | rock mark | 49.9623, -5.1959 (medium) | pollack, lesser spotted dogfish, rockling | thin | 1 (C) | S2 |
| K183 | Lizard Point (Polpeor) | deep-water rock mark | 49.9593, -5.2065 (medium) | pollack, conger | thin | 3 (A/B/C) | S2, T3 |

## Falmouth Bay and the Fal

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K184 | Malpas (Truro River / Tresillian confluence) | tidal river | 50.2439, -5.0256 (medium) | flounder, eels | thin | 1 (C) | S3 |
| K185 | Loe Beach, Feock | estuary | 50.2027, -5.0487 (medium) | - | thin | 1 (C) | S3 |
| K186 | Mylor Creek | estuary | 50.1780, -5.0539 (medium) | flounder, bass(late-year, stone quay), mullet (cold-water, reduced) | moderate | 5 (C) | S3, T2 |
| K187 | Kiln Quay / Trefusis Point, Flushing | rock mark | 50.1623, -5.0599 (low) | pollack, ray (occasional) | thin | 3 (B/B (geography only, no fishing)/C) | S3 |
| K188 | Towan Beach, Roseland | sheltered beach | 50.1584, -4.9832 (medium) | whiting, dogfish, small-eyed ray (chance), lesser spotted dogfish, bass | thin | 1 (C) | S3, S4, T4 |
| K189 | St Mawes Harbour | harbour | 50.1581, -5.0145 (medium) | conger | thin | 2 (C) | S3, T2 |
| K190 | Prince of Wales Pier | pier/breakwater/quay | 50.1567, -5.0691 (medium) | flounder, pouting, whiting, conger, pollack | moderate | 4 (B/C) | S3 |
| K191 | St Mawes Castle Rocks | deep-water rock mark | 50.1549, -5.0242 (medium) | conger, pouting, pollack | thin | 3 (C) | S3 |
| K192 | Prince of Wales Pier, Falmouth | pier/breakwater/quay | 50.1530, -5.0656 (medium) | whiting, pouting, pollack, flounder, thornback ray, conger, squid(site-ranked), flatfish, squid (autumn log) | moderate | 8 (B/C) | S3, T2 |
| K193 | Porthbeor Beach | sheltered beach | 50.1489, -4.9945 (medium) | flounder, dogfish | thin | 2 (A (coordinate only)/C) | S3 |
| K194 | Castle Beach, Falmouth | rock mark | 50.1482, -5.0555 (medium) | pollack, wrasse (reduced), mini-species via lrf, conger, squid, bass | thin | 3 (C) | S3, T2, T4 |
| K195 | Great Molunan | sheltered beach | 50.1458, -5.0157 (medium) | flatfish, pouting, small cod family, dogfish, pollack, wrasse (reduced), bass | thin | 3 (C) | S3, T4 |
| K196 | Gyllyngvase Beach | sheltered beach | 50.1443, -5.0683 (medium) | flatfish, small species, whiting, bass | thin | 1 (C) | S3, T4 |
| K197 | Pendennis Point | deep-water rock mark | 50.1443, -5.0426 (medium) | whiting, conger, garfish (one 8 nov 2026 log), pollack, black bream | moderate | 7 (A/B/C) | S3, T3 |
| K198 | St Anthony Head | deep-water rock mark | 50.1409, -5.0151 (medium) | pollack, black bream (autumn night - tail end) | moderate | 3 (B/C) | S3 |
| K199 | Swanpool Beach | sheltered beach | 50.1407, -5.0765 (medium) | whiting, pouting/small cod family, dogfish, bass | thin | 1 (C) | S3, T4 |
| K200 | Maenporth Beach | sheltered beach | 50.1251, -5.0936 (medium) | whiting, bass, dogfish | moderate | 2 (B/C) | S3, T4 |
| K201 | Porthcuel / 'Porthcawl' river by St Mawes | tidal river | no coordinate | - | thin | 1 (C) | S3 |

## Roseland to Fowey

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K202 | Lerryn / St Winnow / Lostwithiel tidal limit | tidal river | 50.4046, -4.6688 (medium) | not found | thin | 2 (C) | S4 |
| K203 | Fowey estuary upper reaches: Golant, Penpoll, Mixtow Pill, Wiseman's Reach | tidal river | 50.3638, -4.6396 (medium) | flounder (d), eels (inactive, d) | thin | 1 (C) | S4 |
| K204 | Par Beach (Par Sands) | surf beach | 50.3448, -4.7023 (medium) | whiting, flatfish, bass (d), flounder, bass, bass (d, oct 2026 evidence) | moderate | 6 (B/C) | S4, T4 |
| K205 | Shorthorn Beach / Spit Point (Par west) | rock mark | 50.3406, -4.7063 (medium) | - | thin | 1 (C) | S4 |
| K206 | Caffa Mill / Bodinnick | estuary | 50.3402, -4.6341 (medium) | flounder, whiting, cod | thin | 1 (C) | S4 |
| K207 | Polkerris harbour wall (quay) | pier/breakwater/quay | 50.3372, -4.6825 (medium) | flatfish (d), dogfish, whiting(site-ranked) | thin | 2 (C) | S4, T2 |
| K208 | Carlyon Bay / Crinnis Beach | surf beach | 50.3364, -4.7329 (medium) | flounder, dab, whiting, plaice, sole (odd), bass | moderate | 4 (B/C) | S4, T4 |
| K209 | Pont Pill and Pont Creek | tidal river | 50.3353, -4.6204 (medium) | flounder (d) | thin | 2 (A/C) | S4 |
| K210 | Fowey Town Quay / Albert Quay / Whitehouse | estuary | 50.3351, -4.6338 (medium) | flounder, whiting, cod (occasional), pouting (d), codling, coalfish, conger, school bass (d) | moderate | 16 (A/B/C) | S4, T1, T2 |
| K211 | Charlestown harbour (inner, outer wall, beach) | harbour | 50.3306, -4.7563 (medium) | not found - no winter data (d: pouting/whiting plausible) | thin | 3 (C) | S4, T2 |
| K212 | Little Hell (Polkerris) | rock mark | 50.3305, -4.6775 (low) | - | thin | 0 (-) | S4 |
| K213 | Polruan castle, blockhouse and quay | rock mark | 50.3297, -4.6381 (medium) | not found, pollack, flounder | thin | 5 (B/C) | S4, T2 |
| K214 | Readymoney Cove | sheltered beach | 50.3292, -4.6453 (medium) | not found, whiting, flounder, bass | thin | 1 (C) | S4, T4 |
| K215 | Duporth / Silvermine / Ropehaven (St Austell Bay west cliffs) | rock mark | 50.3276, -4.7615 (low) | - | thin | 0 (-) | S4 |
| K216 | St Catherine's Point and Castle rocks (Fowey mouth) | deep-water rock mark | 50.3270, -4.6469 (medium) | conger (bsf), pouting/whiting at night (wtf d), pollack, conger | moderate | 4 (A/B/C) | S4, T3 |
| K217 | Coombe Haven | sheltered beach | 50.3268, -4.6521 (medium) | - | thin | 0 (-) | S4 |
| K218 | Menabilly Beach / Polridmouth | sheltered beach | 50.3235, -4.6659 (medium) | dogfish, flatfish, whiting, bass | thin | 1 (C) | S4, T4 |
| K219 | Porthpean Beach | sheltered beach | 50.3231, -4.7664 (medium) | whiting, bass, flatfish (d), rock gobies, lrf | moderate | 2 (B/C) | S4, T4 |
| K220 | Gribbin Head | deep-water rock mark | 50.3146, -4.6729 (medium) | conger, (d) pollack/bass fade, pollack | moderate | 5 (A/B/C) | S4, T3 |
| K221 | Black Head (Trenarren) | rock mark | 50.2996, -4.7546 (medium) | conger, pouting, rockling | thin | 1 (C) | S4 |
| K222 | Pentewan old harbour | harbour | 50.2913, -4.7822 (medium) | flounder | thin | 1 (B) | S4, T1 |
| K223 | Pentewan Sands (beach and river mouth) | surf beach | 50.2856, -4.7833 (medium) | whiting, flounder (bsf), bass (d), flounder, bass | moderate | 5 (B/C) | S4, T4 |
| K224 | Mevagissey outer harbour wall and lighthouse | pier/breakwater/quay | 50.2697, -4.7827 (medium) | dogfish, whiting, pouting, conger, squid (stormy), flounder, flounder (d) | good | 10 (A/B/C) | S4, T2 |
| K225 | Portmellon Beach | sheltered beach | 50.2621, -4.7848 (medium) | bass (d), whiting, dab, bass | thin | 1 (C) | S4, T4 |
| K226 | Chapel Point / Colona area (Portmellon) | rock mark | 50.2566, -4.7692 (medium) | - | thin | 1 (C) | S4 |
| K227 | Great Perhaver Beach | sheltered beach | 50.2462, -4.7844 (medium) | flatfish (d), whiting, bass | thin | 1 (C) | S4, T4 |
| K228 | Gorran Haven pier and harbour wall | pier/breakwater/quay | 50.2408, -4.7864 (medium) | pouting, whiting, conger (d) | moderate | 5 (B/C) | S4, T2 |
| K229 | Porthluney Cove (Caerhays) | sheltered beach | 50.2370, -4.8425 (medium) | whiting, dogfish, flatfish, bass | thin | 1 (C) | S4, T4 |
| K230 | West Portholland | sheltered beach | 50.2346, -4.8661 (medium) | bass (d), flatfish, pouting, whiting, bass | thin | 2 (C) | S4, T4 |
| K231 | Vault Beach | steep shingle beach | 50.2343, -4.7900 (medium) | dogfish, pouting, whiting, bass | thin | 1 (C) | S4, T4 |
| K232 | Hemmick Beach | sheltered beach | 50.2306, -4.8147 (medium) | bass (d, after blow), whiting, bass | thin | 1 (C) | S4, T4 |
| K233 | Dodman Point | deep-water rock mark | 50.2199, -4.7991 (medium) | pouting, conger (d), dogfish | thin | 4 (B/C) | S4 |
| K234 | Portloe | rock mark | 50.2185, -4.8906 (medium) | pouting, conger (d) | thin | 2 (C) | S4 |
| K235 | Carne Beach | surf beach | 50.2066, -4.9421 (medium) | flounder, bass, whiting, dogfish, flatfish | moderate | 3 (B/C) | S4, T4 |
| K236 | Pendower Beach | surf beach | 50.2058, -4.9485 (medium) | flounder, bass, bass (d), flatfish (d), dogfish | moderate | 3 (B/C) | S4, T4 |
| K237 | Nare Head | deep-water rock mark | 50.1986, -4.9160 (medium) | conger, bull huss, dogfish (d), pollack | moderate | 2 (B/C) | S4, T3 |
| K238 | Gull Rock (Veryan Bay) | island/offshore rock | 50.1895, -4.9150 (low) | - | thin | 1 (C) | S4 |
| K239 | Porthcurnick Beach | sheltered beach | 50.1861, -4.9729 (medium) | whiting, lesser spotted dogfish, bass | thin | 2 (C) | S4, T4 |
| K240 | Portscatho harbour and breakwater | pier/breakwater/quay | 50.1799, -4.9743 (medium) | pouting, poor cod, conger (odd) | thin | 2 (C) | S4, T2 |

## Polruan to the Tamar

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K241 | Cotehele Quay (and Calstock, up to Gunnislake Weir) | tidal river | 50.4912, -4.2232 (medium) | flounder | thin | 3 (A/B/C) | S5, T2 |
| K242 | Cargreen | tidal river | 50.4422, -4.2038 (medium) | flounder | thin | 1 (C) | S5 |
| K243 | Lynher (St Germans) River | tidal river | 50.4084, -4.3443 (medium) | whiting, flounder, flounder (d) | thin | 3 (A/C) | S5, T1 |
| K244 | Saltash Waterside | tidal river | 50.4076, -4.2058 (medium) | whiting, flounder, codling, dab, cod (d) | moderate | 6 (B/C) | S5, T1, T2 |
| K245 | Wilcove / Lower Tamar and Lynher mouth | estuary | 50.3862, -4.2075 (medium) | flounder | thin | 2 (B/C) | S5, T2 |
| K246 | Torpoint Foreshore | tidal river | 50.3770, -4.1950 (medium) | whiting, flounder, cod | moderate | 4 (B/C) | S5, T2 |
| K247 | Seaton Beach | surf beach | 50.3643, -4.3857 (medium) | whiting, flounder, bass, pouting, sole (d) | moderate | 2 (B/C) | S5, T4 |
| K248 | Finnygook Beach | surf beach | 50.3613, -4.3110 (medium) | whiting, bass, flatfish (d) | moderate | 2 (B/C) | S5, T4 |
| K249 | Portwrinkle (harbour and ledges) | rock mark | 50.3612, -4.3136 (medium) | conger, bass (nov, d: autumn run) | moderate | 2 (B/C) | S5, T2 |
| K250 | Millendreath Beach | surf beach | 50.3610, -4.4367 (medium) | whiting, flounder, bass, dogfish, flatfish (d) | moderate | 2 (B/C) | S5, T4 |
| K251 | Downderry Beach | surf beach | 50.3603, -4.3673 (medium) | whiting, bass, dogfish, conger (d) | moderate | 2 (B/C) | S5, T4 |
| K252 | Tregantle Beach and Fort frontage | surf beach | 50.3600, -4.2709 (medium) | bass (d), whiting (d) | moderate | 2 (B) | S5 |
| K253 | Plaidy Beach | sheltered beach | 50.3593, -4.4400 (medium) | whiting, bass, dogfish, flatfish (d) | moderate | 2 (B/C) | S5, T4 |
| K254 | Devil's Point / Mount Batten (Devon - context only) | rock mark | 50.3590, -4.1650 (low) | cod, conger | moderate | 1 (B) | S5 |
| K255 | West Looe Quay and Millpool | tidal river | 50.3578, -4.4631 (medium) | flounder | thin | 2 (B/C) | S5, T2 |
| K256 | East Looe Quay and River Looe (east side) | pier/breakwater/quay | 50.3542, -4.4545 (medium) | flounder, pollack, whiting, cod (bsf, rare), pollock, cod (d, low) | moderate | 5 (B/C) | S5, T1 |
| K257 | Whitsand Bay (general) | surf beach | 50.3515, -4.2700 (medium) | whiting, pouting, dogfish, plaice (d), dab, bass | moderate | 6 (A/B/C) | S5, T4 |
| K258 | Sharrow Beach | surf beach | 50.3477, -4.2602 (medium) | flounder, bass, whiting, dab | moderate | 4 (A/B/C) | S5, T4 |
| K259 | Hannafore (rocks and Hannafore Point) | rock mark | 50.3466, -4.4517 (high) | pollack, conger, pouting (d), whiting, pouting, mini-species (lrf), flounder, squid(site-ranked) | moderate | 7 (B/C) | S5, T2 |
| K260 | Freathy Beach | surf beach | 50.3463, -4.2549 (medium) | bass, whiting, dab | moderate | 4 (A/B/C) | S5, T4 |
| K261 | Tregonhawke Beach | surf beach | 50.3399, -4.2413 (medium) | whiting, dab, bass | moderate | 3 (B/C) | S5, T4 |
| K262 | Portnadler Bay | sheltered beach | 50.3379, -4.4707 (medium) | whiting, pouting, bass | thin | 2 (B/C) | S5, T4 |
| K263 | Looe Island (St George's Island) | island/offshore rock | 50.3372, -4.4509 (high) | pollack | thin | 3 (A/B) | S5, T3 |
| K264 | Talland Bay | rock mark | 50.3365, -4.4976 (medium) | pouting, rockling, conger, dogfish, flounder, bass | moderate | 2 (B/C) | S5, T4 |
| K265 | Kingsand Beach | sheltered beach | 50.3339, -4.2004 (medium) | whiting, pouting, dogfish | thin | 1 (C) | S5 |
| K266 | Lansallos Cove | rock mark | 50.3319, -4.5797 (medium) | pouting, pollack, bass | thin | 1 (C) | S5, T4 |
| K267 | Polperro Harbour | harbour | 50.3309, -4.5164 (medium) | whiting, flounder, cod, conger, pollack | moderate | 5 (B/C) | S5, T2 |
| K268 | Cawsand Beach | sheltered beach | 50.3309, -4.2016 (medium) | whiting, flounder, bass, pouting | moderate | 4 (B/C) | S5, T2, T4 |
| K269 | Lantic Bay | steep shingle beach | 50.3283, -4.6045 (medium) | bass (reduced, d), ballan wrasse (reduced, d), whiting, bass | thin | 2 (A/C) | S5, T4 |
| K270 | Pencarrow Head | headland | 50.3245, -4.5998 (medium) | pollack, conger | thin | 1 (C) | S5 |
| K271 | Rame Head | headland | 50.3122, -4.2230 (high) | pouting, conger, pollack (d) | moderate | 7 (A/B/C) | S5, T3 |

## Isles of Scilly

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K272 | St Martin's: Daymark headland, Higher Town, White Island | deep-water rock mark | 49.9665, -6.2661 (medium) | wrasse, pollack | thin | 4 (B/C) | SC, T3 |
| K273 | Shipman Head and cut-off gully | deep-water rock mark | 49.9655, -6.3599 (high) | pollack | moderate | 1 (B) | SC |
| K274 | Tresco: Long Point to Cromwell's Castle, Gimble Porth | rock mark | 49.9622, -6.3496 (medium) | wrasse | moderate | 1 (B) | SC |
| K275 | New Grimsby quay and Tresco west | pier/breakwater/quay | 49.9551, -6.3382 (medium) | wrasse, ballan wrasse (d: reduced activity in cold water) | thin | 3 (B) | SC, T3 |
| K276 | Popplestones / Gweal Hill / Mussel Rock | rock mark | 49.9541, -6.3585 (medium) | wrasse | thin | 1 (B) | SC |
| K277 | Hell Bay, Bryher | rock mark | 49.9516, -6.3574 (low) | wrasse | moderate | 2 (B) | SC |
| K278 | Pelistry Bay | sheltered beach | 49.9293, -6.2812 (low) | wrasse | thin | 1 (C) | SC |
| K279 | Deep Point / Gap Point | deep-water rock mark | 49.9214, -6.2764 (medium) | pollack | thin | 1 (B) | SC |
| K280 | Porth Mellon / Porthloo | sheltered beach | 49.9173, -6.3087 (medium) | wrasse | thin | 1 (C) | SC |
| K281 | Porth Hellick | rock mark | 49.9162, -6.2847 (medium) | wrasse, pollack | moderate | 2 (B/C) | SC |
| K282 | The Garrison shore | rock mark | 49.9150, -6.3260 (low) | wrasse | moderate | 1 (B) | SC |
| K283 | Airport gullies (under St Mary's airport) | rock mark | 49.9127, -6.2915 (low) | wrasse, pollack | moderate | 2 (B) | SC |
| K284 | Giant's Castle | rock mark | 49.9117, -6.2854 (medium) | wrasse, pollack | thin | 1 (B) | SC |
| K285 | Old Town Bay and Tolman Point | headland | 49.9107, -6.2976 (medium) | pollack, wrasse | moderate | 1 (C) | SC |
| K286 | Peninnis Head (outer head) | deep-water rock mark | 49.9055, -6.3039 (medium) | pollack, wrasse, conger, bull huss | moderate | 4 (B/C) | SC, T3 |
| K287 | Troy Town carns, St Agnes | rock mark | 49.8910, -6.3509 (medium) | wrasse | thin | 1 (B) | SC |
| K288 | Gugh / St Agnes bar south rocks, Hoe Point | rock mark | 49.8889, -6.3292 (medium) | wrasse | moderate | 2 (B/C) | SC |
| K289 | Beady Pool, St Agnes | rock mark | 49.8853, -6.3400 (medium) | pollack | thin | 1 (C) | SC |

## Thematic: estuaries

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K290 | Camel estuary (Padstow to Wadebridge, Porthilly, Little Petherick) | estuary | 50.5404, -4.9370 (low) | flounder (d) | thin | 1 (B) | T1 |
| K291 | Millbrook Lake / St John's Lake | estuary | 50.3539, -4.2168 (low) | not found | thin | 1 (B) | T1 |
| K292 | Truro River / Tresillian River / Malpas | tidal river | 50.2786, -4.9957 (low) | flounder (d), mullet (d) | thin | 1 (C) | T1 |
| K293 | Restronguet Creek (Devoran, Perran Wharf) | estuary | 50.2114, -5.0938 (low) | not found | thin | 1 (C) | T1 |
| K294 | Fal estuary / Carrick Roads (Pendennis, Flushing, Trefusis) | estuary | 50.2100, -5.0300 (low) | flounder, whiting, pouting, thornback (d) | thin | 3 (C) | T1 |
| K295 | Penryn River / Mylor Creek / Pill Creek / Percuil River | estuary | 50.1685, -5.1034 (low) | flounder (d) | thin | 1 (C) | T1 |

## Thematic: harbours and piers

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K296 | Flushing Quay / Flushing pier | pier/breakwater/quay | 50.1631, -5.0703 (medium) | whiting, codling, conger, dogfish | thin | 2 (C) | T2 |
| K297 | Newlyn North Pier | pier/breakwater/quay | 50.1065, -5.5497 (low) | whiting, pouting, pollack, conger, cod | moderate | 3 (B/C) | T2 |
| K298 | Hugh Town Quay and Harbour Wall, St Mary's | pier/breakwater/quay | 49.9150, -6.3150 (low) | pollack | thin | 2 (B) | T2 |

## Thematic: deep-water rock / islands / obscure

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K299 | The Rumps / Rumps Point (Pentire, east of Padstow) | deep-water rock mark | 50.5890, -4.9150 (low) | pollack, bull huss, conger, cod (bsf lists cod; d: winter cod unreliable now) | thin | 2 (B) | T3 |
| K300 | Park Head / Trenance / Trevose rock marks | deep-water rock mark | 50.4963, -5.0296 (medium) | pollack, conger | thin | 3 (A/B) | T3 |
| K301 | Talland Bay rocks / Banjo Pier (Polperro) | rock mark | 50.3290, -4.5250 (low) | whiting, flounder, cod (per bsf; not recent) | thin | 1 (B) | T3 |
| K302 | Clodgy Point / Man's Head / Portheras / Aire Point (cliff marks west of St Ives) | deep-water rock mark | 50.2191, -5.4963 (medium) | - | thin | 2 (A/B) | T3 |
| K303 | Penlee Point | headland | 50.0885, -5.5337 (high) | - | thin | 2 (A/B) | T3 |
| K304 | Black Head / Maenease Point (St Keverne to Gorran) | deep-water rock mark | 50.0036, -5.1015 (medium) | - | thin | 2 (A/B) | T3 |
| K305 | Deep Point / Gap Point (St Mary's) | deep-water rock mark | 49.9080, -6.3350 (low) | - | thin | 1 (B) | T3 |
| K306 | St Agnes / Bryher / St Martin's rock edges | rock mark | 49.8950, -6.3450 (low) | - | thin | 1 (C) | T3 |

## Thematic: surf and open beaches

| ID | Mark | Type | Lat, Lon (conf.) | Late-Nov species (per sources) | Quality | Sources (grades) | Sweeps |
|---|---|---|---|---|---|---|---|
| K307 | Hawker’s Cove | estuary | 50.5602, -4.9489 (medium) | whiting, flounder, dab, bass | thin | 1 (C) | T4 |
| K308 | Booby’s Bay | surf beach | 50.5387, -5.0259 (medium) | bass | thin | 1 (C) | T4 |

## Documentation gaps reported by the sweeps (stretches with NO angling documentation found)

Copied verbatim from the closing section of each sweep file. The 1 km coastline assessment (`coastline.md`) covers every one of these stretches physically regardless.

### North coast: Devon border to Camel mouth (`marks/N1.md`)

- No documentation found for: Millook, Dizzard, Varley Head, Kellan Head, Doyden, Carnweather, Bude canal sea-lock (Nominatim found no points for most; no angling pages found). wheresthefish has a Millook town page (raw saved) but no coordinates extracted.
- Stretches with no angling evidence: Millook to The Strangles (all of the Dizzard/Cambeak cliffs); Rocky Valley to Barras Nose; Backways Cove to Port Gaverne (Tregardock); Port Quin to Lundy Bay (Doyden/Carnweather).
- Sea Angler spot pages (seaangler.co.uk) blocked by Cloudflare; fishingmagic, gethooked, pressreader returned JS walls/403.
- No catch reports, record lists naming venue, or November-specific reports found for any mark. Every late-November claim is D (inference).
- Contradiction: none direct; Visit Bude says winter whiting/codling for Bude without naming marks.

### Camel estuary to Newquay (`marks/N2.md`)

Porthilly, Cant Cove, Dinham, Amble/Trewornan, Camel above Wadebridge tidal limit (only a forum snippet on mullet at Wadebridge and a trail dam), St Saviour's Point, Harbour Cove/Tregirls, Old Town Cove, Pinkson Creek, Butter Hole, Gunver Head, Trevone-Cataclews stretch, Cataclews Point, Merope Rocks, Dinas Head (Cornwall; searches returned only Wales), Trevelgue Head / Porth Island, Old Dane (separately), Gulland Rock, Newland Island, Quies, Newquay South Quay and harbour south side (no separate evidence), Pentire Point East beyond the generic entries. Cataclews/Butter Hole/Gunver/Merope/Gulland/Newland/Quies/Dinas Head have no coordinates here (Nominatim returned nothing usable); not invented.

### Crantock to St Ives (`marks/N3.md`)

No explicit gap section in this sweep file.

### West Penwith (St Ives to Mousehole) (`marks/W1.md`)

Hor Point, Pen Enys, The Carracks, Pendour Cove, Wicca Pool, River Cove, Bosigran, Levant, Botallack, Kenidjack, Porth Ledden, The Brisons, Porth Nanven, Carn Les Boel, Armed Knight, Enys Dodnan/Pordenack, Longships, Porthguarnon, Tater-du, St Clement's Isle, Wolf Rock, Runnel Stone. Not searched in depth: forums (worldseafishing, UK Sea Fishing), CFSA lists, Facebook/YouTube.

### Mount's Bay (Newlyn to Mullion) (`marks/S1.md`)

Newlyn north pier, Sandy Cove, Tolcarne, Wherrytown, Jubilee Pool, Lighthouse Pier, Penzance wet dock (beyond Albert Pier), Top Tieb, St Michael's Mount island rocks/harbour, The Greeb, Trenow Cove, Hoe Point, Lesceave (separately), Halzephron, Poldhu (searched, nothing), Tremearne, Breageside (separately). Also no CFSA/BCC record lists or dated catch reports naming these venues. Aspects are inferred (D). Note: aspect for Dollar/Church/Fishing Cove west-facing per WTF text (Fishing Cove) else inferred.

### The Lizard and Helford (`marks/S2.md`)

Vellan Head, Gew-graze (Soapy Cove), Pentreath, Old Lizard Head/Polpeor (beyond Lizard Point), Bumble Rock, Kilcobben, Parn Voose, Poltesco, Eastern Cliff, Carrick Luz, Lankidden, Downas Cove, Black Head, Chynhalls Point, Dolor Point/Mears beach (beyond Coverack), Dean Quarry, Manacle Point/The Manacles (only a boat-bass trade article titled 'Bass fishing on the Manacles' surfaced, intrafish.com, not read), Flushing/Dennis Head, Ponsence, Bosahan, Frenchman's Creek, Tremayne Quay, Polwheveral, Porth Navas, Helford village, Polgwidden, Toll Point, Mawnan Shear. Mullion Island: no fishing evidence.
Sources blocked/unavailable: worldseafishing.com (JS wall), fishingmagic, visitcornwall.tv (bot check), DuckDuckGo (captcha), seaangler.co.uk (403), issuu/pressreader (no text), talkseafishing Helford Passage thread (empty). britishseafishing.co.uk and cornwalls.co.uk/intocornwall have nothing for this sector.
Search rounds: round 1 (4 queries) and round 2 (3 queries) added no new marks beyond wtf list.

### Falmouth Bay and the Fal (`marks/S3.md`)

No explicit gap section in this sweep file.

### Roseland to Fowey (`marks/S4.md`)

No explicit gap section in this sweep file.

### Polruan to the Tamar (`marks/S5.md`)

No explicit gap section in this sweep file.

### Isles of Scilly (`marks/SC.md`)

No documentation: Rat Island, Porthcressa, Carn Morval, Halangy, Innisidgen, Watermill, Morning Point, Woolpack, Pentle Bay, Piper's Hole, Rushy Bay, Great Par, Anneka's Quay, Droppy Nose, Great Bay/Lower Town/Par Beach, Periglis, Wingletang, Samson, Annet, Western Rocks, Norrard Rocks (Mincarlo/Maiden Bower named by Tresco only), Eastern Isles, Round Island, St Helen's, Tean, Men-a-vaur, Hanjague, Seven Stones. No CFSA/IFCA venue records; no tide/forecast gathered. Late-Nov evidence: 16, 18, 30 Nov 2012 and 10-14 Nov 2013 blog posts only.

### Thematic: estuaries (`marks/T1.md`)

No documentation at all: Hayle estuary/Copperhouse; Restronguet/Devoran; Penryn, Mylor, Pill, Percuil creeks; Truro/Tresillian marks; Lynher/Tiddy/Seaton; Millbrook and St John's Lakes; Camel mark names; Red River mouth; Pentewan river reaches; Fowey tributary marks. Fetch failures: PressReader 403, Everand JS error, talkseafishing 404.

### Thematic: harbours and piers (`marks/T2.md`)

No explicit gap section in this sweep file.

### Thematic: deep-water rock / islands / obscure (`marks/T3.md`)

Bude to Tintagel (Hartland-Tintagel cliffs: Boscastle, Meachard, Tintagel Island, Trebarwith, Port Isaac); Gull Rocks at Portreath/Holywell/Veryan; Chapel Rock, Bawden Rocks, The Carracks, The Quies, Gulland, Newland, The Mouls; St Michael's Mount; Black Rock Falmouth; Wolf Rock, Longships, Brisons, Runnel Stone as shore fishing; Scilly outer/western rocks (Bishop Rock, Western Rocks, Annet, Gugh, Giant's Castle, Porth Hellick, Garrison); Gunwalloe, Loe Bar rock, Porthleven rocks; Dodman Point; Pendeen/Bosigran/Cape Cornwall cliff-foot ledges; British Conger Club/CFSA lists; old angling books.

### Thematic: surf and open beaches (`marks/T4.md`)

- Isles of Scilly beaches (Porthcressa, Par, Pelistry, Great Bay St Martin's, Old Grimsby etc.): NO source found in this stream (wtf Cornwall list does not cover Scilly).
- Sennen/Whitesand Bay, Gwithian-Godrevy detail beyond wtf, Poldhu, Church Cove Gunwalloe beyond wtf, Porthcothan-Treyarnon detail, Crackington/Millook beaches, Pentewan-Gorran Haven, Seaton-Downderry reports: wtf template text only.
- Sea Angler spot pages, Fishbrain, CFSA, club match reports, forums: not read (blocked / search exhausted).
- Per-beach swell height and wind direction preferences, sandbar/gutter positions: NOT FOUND (wtf gives generic phrases only).

