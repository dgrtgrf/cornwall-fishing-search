export const meta = {
  name: 'cornwall-coastline-review',
  description: 'Workstream 7: full-model qualitative review of every shoreline segment, batch by batch, then adversarial verification',
  whenToUse: 'Pass args.batches = [batch numbers]; each batch is reviewed by one agent and then checked by a second',
  phases: [
    { title: 'Review', detail: 'one agent per geographic batch assesses every segment in it from first principles' },
    { title: 'Verify', detail: 'a skeptic checks completeness, place identification, sources and every large adjustment' },
  ],
}

const ROOT = '/home/user/cornwall-fishing-search'
const REV = ROOT + '/fishing/research/coastline/review'

const CONTEXT = `CONTEXT (read fully). You are part of a large, deliberately exhaustive study: "Find the single best shore-fishing spot in Cornwall (UK) - the entire Cornish shoreline including every estuary and the Isles of Scilly - for one session on SUNDAY 22 NOVEMBER 2026 (any window within the 24 h; local time = GMT), any species, any method." It is purely hypothetical: nobody is going. Locations are judged SOLELY on fishing quality. Ignore human factors completely (access, danger, comfort, whether a person could stand there): assume a superhuman angler who can fish any point where land meets water - cliff foot, island, offshore rock, drying reef, harbour wall - in any conditions. Weather and sea matter only through their effect on fish and on presenting a bait or lure.
NOW: Saturday 21 November 2026, ${(args && args.now) || 'evening'}. The session date is TOMORROW. Repository root: ${ROOT}.

WORKSTREAM 7 - SYSTEMATIC COASTLINE COVERAGE. The whole shoreline has been cut into 2,009 consecutive segments of no more than 1 km (Ordnance Survey high-water line; mainland IDs M0001-M0971 run from the Devon border on the north coast clockwise to the Tamar; F = mainland side pieces; I = Cornish islets and rocks; S = Isles of Scilly; D / DS = detached drying reefs and banks that are land only below high water). A script has attached physical descriptors to every segment and computed a provisional score. Read the method first: sed -n '1,75p' ${ROOT}/fishing/research/coastline.md (sections 1-3: data sources, their limits, and the scoring formulas).
What the computed data CANNOT see, and you must supply or flag: gullies, ledges, kelp, small reefs and sand patches (bathymetry is ~115 m cells; the seabed map is broad-scale and missing inshore for half the segments), tidal flow at the segment, man-made structure (piers, harbour walls, quays, lights), outfalls, and whether the automatic classification is simply wrong.

THE DAY (22 Nov 2026), from the other workstreams - details in ${ROOT}/fishing/research/weather.md, sea_state.md, tides.md, light_moon.md, species_sst.md, intel.md:
- Wind: south-easterly gale (110-125 deg, 18-27 kn, gusts 32-45 kn) from the evening of the 21st until an abrupt veer to west / west-north-west (270-290 deg, 17-30 kn, gusts 30-47 kn) that reaches Scilly ~03:00, Land's End / Penzance ~04:00, Falmouth ~05:00, Mevagissey ~07:00, Looe / Rame ~09:00 GMT (12 models; timing spread 3-8 h, widest in the east). Westerly gale then persists all day, easing after midnight. Pressure bottoms ~997-1000 hPa at 03-06 h then rises ~3 hPa per 3 h. Rain overnight and morning. Overcast nearly all day.
- Sea (offshore of each coast; your CSV has a per-segment nearshore estimate at 3-hourly steps): south coast and Scilly 2-3 m short south-easterly sea overnight; north coast ~1 m residual westerly swell under an offshore wind until the veer; then a westerly sea builds to ~4 m on the north and west coasts and Scilly by afternoon, ~2.7 m in Mount's Bay, while east-facing south-coast shores (Lizard east side, Falmouth Bay, Mevagissey to Looe) fall to 1.5-2.4 m in the lee. Lead-in: big W/WNW groundswell 17-20 Nov (4-4.7 m at Perranporth, periods to 18 s), down to ~1 m by the afternoon of the 21st. Water colour is inferred only (no observation): open north and west coast beaches coloured; south-east coast clearer; estuaries carry rain run-off.
- Tide: Newlyn HW 02:17 (4.97 m), LW 08:55 (1.48 m), HW 14:35 (5.23 m), LW 21:18 (1.24 m); Padstow HW 02:57, LW 09:25, HW 15:18, LW 21:50; Falmouth HW 02:49, LW 09:23, HW 15:06, LW 21:49; Devonport HW 03:21, LW 09:35, HW 15:41, LW 22:00. About 85 % of mean spring range and building (Brest coefficient 70 then 76). Surge ~+0.4 m on the early-morning HW, ~+0.1 m on the afternoon HW.
- Light: sunrise ~07:46, sunset ~16:30 (Newlyn); civil twilight 07:10-07:46 and 16:30-17:06. Moon 91-96 % lit: sets ~05:00, rises ~14:48, so the only astronomically dark hour is ~05:00-05:50, but cloud should hide the moon most of the time.
- Sea temperature 13.1-13.5 C on every coast (slightly above normal). Late-November species ranking from the species workstream: bass first (big shore bass still being caught at night in West Cornwall to 16 Nov), then bull huss, pollack, conger, small-eyed ray, ballan wrasse (swell-limited), squid (needs clear calm water), whiting / dogfish / pouting (most certain, least quality), flounder in estuaries, thick-lipped mullet.

HARD RULES
1. Never invent a depth, a feature, a catch or a source. Every item you add must carry its source (URL and the time you accessed it) and a grade: A official / instrument / primary; B reputable secondary (pilot book, dive guide, conservation-site description, established angling guide); C anecdotal; D your own inference or unsourced background knowledge (say which). Where you cannot find out, write THIN rather than guess.
2. ACCESS BOUNDARIES: if a site refuses automated access (bot challenge, HTTP 403, login wall, paywall), record it as INACCESSIBLE and move on. Do not try to get round a refusal in any way - no web-archive or cached copies of the refusing site, no proxies or mirrors, no spoofed browser fingerprints.
3. There is no token budget to protect: never thin the work to save tokens. The only constraint is your context window - save downloads to disk and extract with python / grep rather than pasting whole pages.
4. Write your output file early and after every few segments so partial work survives an interruption. If your output file already exists, read it and continue from where it stops rather than starting again.
5. Write only your own batch files. No git commands that change state.
TOOLS: Bash (curl through a preconfigured proxy; never disable TLS verification), python3, Read (it displays PNG / JPG images - use it on the map and satellite image), WebSearch / WebFetch if available (load with ToolSearch "select:WebSearch,WebFetch"), Chromium + Playwright for openly served JavaScript pages.`

function reviewPrompt(b) {
  const nn = String(b).padStart(2, '0')
  return CONTEXT + `

=== YOUR TASK: review batch ${nn} ===
Inputs:
- ${REV}/batch_${nn}.csv - one row per segment in this batch with the computed descriptors (columns explained in coastline.md section 2): position, names, setting, aspect, intertidal width, depth within 150/300/1000 m, distance to the 5/10/20 m depth, seabed class at 100/300/1000 m and nearest mapped class, bedrock, stream outflows, fetch, nearshore wave estimate at 00/03/06/09/12/15/18/21 h, wind onshore component (+1 dead onshore, -1 dead offshore) at 00/12/18 h, tide port, habitat score H and guild, provisional score P, its guild and 3-hour window, documented marks within 600 m, thin-data flags.
- ${REV}/batch_${nn}.png - map of the batch with every segment labelled (blue = tidal water, tan = foreshore that dries, dashed = low-water mark). VIEW IT with the Read tool.
- ${ROOT}/fishing/research/raw/coastline_review/batch_${nn}_s2.jpg - Sentinel-2 cloudless mosaic (EOX s2cloudless-2020, 10 m pixels, CC BY-NC-SA 4.0) of the same box: pale = sand, dark inshore = reef / kelp / deep water, white = surf. VIEW IT. Fetch closer crops if useful: https://tiles.maps.eox.at/wms?service=WMS&version=1.1.1&request=GetMap&layers=s2cloudless-2020&styles=&srs=EPSG:4326&bbox=<minlon>,<minlat>,<maxlon>,<maxlat>&width=1200&height=1200&format=image/jpeg
- ${ROOT}/fishing/research/coastline/segments_scored.csv - the full table (all columns including the 36-direction fetch) if you need more.
- ${ROOT}/fishing/research/marks_merged.jsonl - the documented marks (grep the K-number shown in the known_marks_600m column).

For EVERY segment in the CSV, in CSV order, with no exceptions:
1. Say what the place actually is (named cove, beach, headland, zawn, quay, creek, drying reef, cliff run...) using the names columns, the map, the imagery and sources.
2. Check the computed descriptors against the map and imagery and record anything wrong (aspect, setting class, seabed class, depth, a "beach" that is really boulders, an "open coast" that is inside a harbour...).
3. Add what the data cannot see, each item with source and grade: reefs, skerries, ledges, gullies, kelp, sand patches and bars, stream and river outflows, outfalls, harbour walls / piers / quays / slipways / lights, mussel beds, wrecks close in, tidal-stream strength, eddies and races, freshwater influence. Good open sources: Natural England / JNCC conservation-advice packages and site descriptions for the SACs and MCZs (detailed on reef, kelp and sediment habitats), Cornwall Wildlife Trust / Seasearch dive survey summaries, dive-site guides, harbour-authority pilotage notes, sea-kayak guides (tidal streams off headlands), surf-spot guides (bars and rips), geological guides, Ordnance Survey names, Environment Agency and Cornwall Council beach descriptions.
4. Judge the fishing on 22 Nov at that segment from first principles: which habitat guild fits (SURF sandy surf beach / EDGE reef-meets-sand / ROUGH rough ground or deep-water rock / STEEP steep-to beach with depth close in / EST estuary or creek / STRUCTURE harbour wall, pier, quay / NONE), which species are realistic, how the day's wind and sea hit this segment period by period (use the per-segment wave and onshore columns, and say if you think the geometric wave estimate is wrong for this spot, e.g. swell wrapping round a headland), which 3-hour window would be best and why.
5. Give a score adjustment between -30 and +30 relative to the provisional P, with a one-line reason, and the resulting reviewed_score (0-100). Set candidate = true if this segment deserves to go forward to Phase 2 whatever its score, with the reason.
6. State what is THIN for this segment.
Runs of near-identical shore (a long cliff, a uniform beach, a mud creek) may be researched together, but you must still write one line per segment.

Outputs:
(a) ${REV}/batch_${nn}_review.jsonl - one JSON object per segment with exactly these keys: seg_id, place, ground, depth_note, features (array of {type, description, source, grade}), tidal_flow, structures, data_issues, exposure_22nov, best_guild, late_nov_species (array), best_window, score_adjustment (integer), adjustment_reason, reviewed_score (integer), confidence (high|medium|low), thin_data, candidate (true|false), candidate_reason.
(b) ${REV}/batch_${nn}_review.md - a narrative for the batch: what this stretch of coast is; the three to six strongest segments on 22 Nov and why; systematic problems you found in the computed data here; the sources you used (with access times) and the ones that were inaccessible.
Before finishing, verify with a script that the JSONL parses and contains every seg_id from the CSV exactly once.
RETURN VALUE (consumed by an orchestrator): number of segments reviewed, the candidate segments with reviewed scores and one-line reasons, the biggest corrections to the computed data, and what stayed thin.`
}

function verifyPrompt(b, res) {
  const nn = String(b).padStart(2, '0')
  return CONTEXT + `

=== YOUR ROLE: ADVERSARIAL VERIFIER of the review of batch ${nn} ===
A reviewer has just written ${REV}/batch_${nn}_review.jsonl and ${REV}/batch_${nn}_review.md from ${REV}/batch_${nn}.csv, the map ${REV}/batch_${nn}.png and the satellite image ${ROOT}/fishing/research/raw/coastline_review/batch_${nn}_s2.jpg. Your job is to REFUTE the review, not to admire it.
1. Completeness: with a script, confirm the JSONL parses, has exactly the required keys, and contains every seg_id in the CSV exactly once. Repair it if not (write the missing lines yourself after doing the assessment properly).
2. Re-check EVERY segment where candidate is true or the absolute score adjustment is 10 or more, plus a sample of at least one in five of the remaining segments (choose them with a fixed rule, e.g. every fifth line):
   - Is the place identification right? View the map and the satellite image yourself and compare with the coordinates.
   - Open each cited source that is openly reachable and confirm it says what is claimed; anything unsupported becomes grade D or is removed.
   - Challenge every depth, ground, kelp, tidal-stream and structure claim; challenge the exposure reasoning against the day's wind and sea given above; challenge the adjustment (is it double-counting something the formula already scores? is it driven by reputation rather than evidence?).
3. Look for segments the reviewer under-assessed: view the imagery for the whole batch and name any segment whose features (reef edge beside sand, outflow, deep water under a cliff, a bar across a river mouth) deserve a higher score than it was given.
4. Fix errors directly in the JSONL (add a key "verifier_note" to every line you change, saying what changed and why) and append a "## Verification log" to the .md (segment, claim checked, source, result = confirmed / corrected / unverifiable).
Default to "unverifiable" when unsure. RETURN VALUE: counts confirmed / corrected / unverifiable, the final candidate list for this batch with reviewed scores, and the most important corrections.

The reviewer's closing summary (do not trust it):
${res}`
}

const batches = (args && args.batches) || []
if (!batches.length) throw new Error('args.batches is required, e.g. [0,1,2]')
log('Coastline review, batches: ' + batches.join(', '))

const out = await pipeline(
  batches,
  b => agent(reviewPrompt(b), { label: 'review:batch_' + String(b).padStart(2, '0'), phase: 'Review' }),
  (res, b) => {
    if (!res) return { batch: b, review: null, verification: null }
    return agent(verifyPrompt(b, res), { label: 'verify:batch_' + String(b).padStart(2, '0'), phase: 'Verify' })
      .then(v => ({ batch: b, review: res, verification: v }))
  }
)
return { batches, results: out }
