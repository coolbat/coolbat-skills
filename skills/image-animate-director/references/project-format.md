# Project format and commands

## Plan

Version 1 plans contain:

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer 1 |
| `title`, `brief` | Shot name and requested action |
| `canvas` | Even integer `width`, `height`; explicit `background` color, e.g. `#ffffff` |
| `action_fps` | Integer timing ticks/second, normally 6, 8 or 12 |
| `output_fps` | Integer multiple of action_fps, normally 24 |
| `loop` | Boolean; true requires seam review |
| `invariants` | Nonempty list of stable visual features |
| `limits` | Positive `max_attempts_per_frame` and `max_total_attempts` |
| `references` | Approved objects with unique `id`, `role` and actual `path` |
| `frames` | Ordered entries with unique `id`, explicit `goal`, positive integer `hold`, and `reference_ids` |

Use ASCII IDs containing letters, digits, "_" or "-". Titles, goals and notes can be Chinese or another language. Playback follows array order, not filename order.

At 8 action ticks/second, `sum(hold)=24` means 3 seconds and, at 24fps, 72 encoded frames. Twelve poses held for two ticks each also last 3 seconds. Pose entries, timing ticks, video frames and generation attempts are different quantities.

Helper canvas limits are not image-model limits. Choose a backend-supported size before generation. For output rates not divisible by the action rate, explain the timing tradeoff and select an appropriate action rate. This release does not provide arbitrary rational timing or optical-flow interpolation.

Reference paths resolve relative to the plan file or can be absolute. Initialization copies them into the project. References can have different dimensions; generated frame images must match the canvas.

`assets/caterpillar-plan.json` is a complete 2-second, 16-pose plan. Supply a real inspected `master.png` beside a copied plan or replace the path. The asset does not bundle fabricated generated artwork. Adapt its poses to the user's character.

## Ledger

Initialization creates `project.json`, `references/` and `frames/`. Frames gain:
- `status`: planned, generating, candidate, approved, rejected or stale.
- `attempts`: historical prompts, input paths/roles/checksums, goal, timestamps, backend/request ID, and candidate paths/checksums.
- `reviews`: historical approval/rejection/revision notes.
- `image`, `sha256`: current candidate bytes, retained for repair.
- `review_context`: references inspected during latest approval, separate from generation provenance.

Use `revise` for changed goals. Keep attempt files immutable and back up the whole project. Editing referenced images directly invalidates checksums; create a new master/project revision instead. Limit direct ledger editing to deliberate planning/budget adjustments before work or under user authorization.

Use a single writer per project. Atomic JSON replacement is not a multi-writer database. Different shots can use different projects.

## Commands

All commands: `python "$SKILL_DIR/scripts/project.py" COMMAND PROJECT [options]`.

| Command | Options / behavior |
| --- | --- |
| init | `--plan PATH`; new directory only |
| status | Frame statuses, attempts used, duration and output count; not a quality certificate |
| prepare | `--frame ID`, optional `--repair`; reserves an attempt, prints prompt and ordered image references |
| record | `--frame ID --image PATH`; optional `--backend LABEL --request-id ID` |
| review | `--frame ID --decision approve\|reject --notes TEXT`; candidate/stale frames |
| fail | `--frame ID --notes TEXT`; closes active generation |
| revise | `--frame ID --goal TEXT`; retains versions and marks downstream work stale |
| loop-review | `--notes TEXT`; after inspecting seam |
| check | Requires approved frames, current file/context checksums and loop review |

`prepare` is stateful, not a dry run. Inspect saved attempts to recover prompts without reserving again. There are no automatic tool calls/retries. Failed calls consume reserved attempts even if billing is unknown.

Render with `python "$SKILL_DIR/scripts/render.py" video|gif|sheet PROJECT --out PATH`. Use .mp4, .gif and .png respectively. Outputs and sibling JSON reports must not already exist; choose versioned names. Contact sheets support partial work. Video/GIF require all frames to pass check.

Reports contain the exact selected image paths/checksums/holds, canvas/rates, ledger checksum, output checksum, duration and MP4 probe results. Retain the ledger and immutable files to recover generation provenance. Source images remain unchanged.

## Resume

1. Read status and ledger; do not infer progress from the highest filename.
2. Resolve active generation: record an existing tool result or fail with the observed reason before retrying.
3. Review candidates and resolve stale frames sequentially after upstream approval.
4. Generate from the first unresolved frame using the approved predecessor and master.
5. At budget exhaustion, save state and explain the remaining defect. Increase limits only within existing cost/time authorization or after a material budget decision; never automatically to conceal repeated failures.

## Optional motion planning and diagnostics

Existing version 1 projects remain valid. Add `motion` to a frame to make edit scope explicit:

```json
{"phase":"movement","change":["Raise face halfway toward the raised anchor"],
 "lock":["Feet, torso silhouette, eye spacing, camera and background"],
 "between":{"from":"neutral","to":"raised","progress":0.5}}
```

Allowed phases: `anticipation`, `movement`, `hold`, `recovery`, `settle`. Both `change` and `lock` are lists of strings. `between` is optional; its two distinct reference IDs must be present in that frame's `reference_ids`, and progress must be strictly between 0 and 1. Describe visible landmarks in `goal`; a numeric progress instruction is a target, not a model guarantee. Generate and inspect endpoint references before initializing a new shot, then generate intermediate frames in timeline order. This avoids depending on an unapproved future frame.

Use `timeline PROJECT` to print start/end times, phases and goals before generation. `prepare --kind generate|reuse|import` records the intended operation (default generate). Use reuse for existing generated artwork, import for supplied animation stills. Register with `record` and visually review either way. Reuse/import retain source path and checksum. All kinds occupy ledger attempts; `status.attempt_kinds` separates reservations. Legacy attempts remain labeled legacy rather than guessing historical call counts. Keep an external-call log for master/key-pose generation and failed tool calls; do not infer cost from the number of frames.

Use `reconsider PROJECT --frame ID --notes TEXT` after a justified goal revision or rejection when the retained image may now fit. It marks the frame stale for a fresh visual review, preserves attempt counts and never approves it. Do not weaken a target just to pass a failed frame; explain a material staging change and keep the original defect in history.

Optionally add locked inspection regions at project level:

```json
"inspection_regions": [
  {"id":"background-left","box":[0,0.1,0.06,0.8],"threshold":0.03},
  {"id":"feet-contact","box":[0.30,0.82,0.70,0.91],"threshold":0.04}
]
```

Boxes use normalized [left, top, right, bottom] coordinates. Choose regions from actual artwork; avoid intended moving areas. Threshold is mean absolute RGB difference divided by 255, not pixels of displacement or a probability. Lock regions are triage aids only. Small patches can miss drift elsewhere; a large changed region can reflect intended motion. Whole-frame difference has no automatic failure threshold.

```bash
python "$SKILL_DIR/scripts/inspect_motion.py" ./shot --out ./review-v2.html \
  --baseline ./accepted-v1/shot
```

This read-only command requires reviewed projects and emits a self-contained HTML preview plus JSON diagnostics. It preserves source bytes, deduplicates embedded assets, provides synchronized playback, 0.5× speed, a seek slider, pose stepping, and optional repeated preview. Repeated preview does not change the project's loop setting. Different shot durations hold the shorter shot's final pose. Reported pixel differences never approve or reject frames. Record actual playback observations separately after opening the preview. The script itself always reports playback as unperformed.

## Mode and alpha fields

Plans remain schema_version 1. `mode` is optional for backwards compatibility; missing means stop-motion. Canonical values are stop-motion, animated-sprite and gif-motion. A new plan should record its chosen mode explicitly. `alpha` is opaque or transparent; missing defaults to transparent for animated-sprite and opaque otherwise. Transparent projects reject fully opaque and fully invisible animation stills at record/check. This coarse gate does not replace visual alpha-edge inspection.

Animated-sprite requires `sprite: {"clip":"idle", "pivot":[0.5,0.85]}`; pivot uses normalized full-canvas coordinates. Other modes may also include sprite metadata for atlas export. Invalid names, non-finite coordinates and unsupported modes fail validation before project creation. No existing project is silently rewritten by load/status. Frame prompts use the mode's production requirements, while historical prompts and checksums remain intact.
