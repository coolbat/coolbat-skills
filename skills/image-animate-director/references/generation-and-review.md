# Generation and continuity review

## Poses and timing

Specify each still as a photographed pose: position, facing, expression and contact. "Head halfway raised, eyes open" is more useful than "continue moving". Use small changes near contact, silhouette and occlusion transitions.

Arrange anticipation, movement, settling and holds. Control pauses with hold ticks instead of generating near-identical images. Design transition key poses for large transformations. Keep original identity/scene references throughout; add a phase reference when appearance intentionally changes.

A loop needs compatible endpoint poses and velocity. A duplicated first frame at the end can add an unwanted pause; inspect repeated playback.

## Reference roles

| Input | Purpose |
| --- | --- |
| Character master | Identity, proportions, color, material |
| Scene master | Camera, framing, lighting, props |
| Phase/key pose | Intended transformation stage |
| Previous approved frame | Immediate continuity |
| Existing same-frame image for repair | Edit target; preserve correct staging |

Keep inputs few and clearly labeled. During repair, the same-frame image is the edit target; the predecessor supplies continuity. Inspect the images actually sent. If a tool cannot include required references, consolidate approved masters or narrow the shot rather than silently omitting an anchor.

Scripts make no image-service calls. Map jobs to the available host image tool and its actual schema. Preserve source alpha. Never infer an API model from a UI label or invent seed/reproducibility controls.

For explicit OpenAI API/model work, check the current official [image-generation guide](https://developers.openai.com/api/docs/guides/image-generation) and [prompting guide](https://developers.openai.com/api/docs/guides/image-prompting). Guidance checked on 2026-09-09 listed `gpt-image-2.5-sunburst` for demanding precision and `gpt-image-2.5-flare` for speed. This is a reference point, not a hardcoded dependency or account-access guarantee. Compare representative sequences before trading quality for speed. Built-in generation does not require the user to supply an API key.

## Visual inspection

Inspect candidate, master, predecessor and next accepted frame when repairing:
- Identity: eye spacing, face shape, body/limb count, accessories, colors.
- Pose: the requested change is visible; direction and increment are plausible.
- Contact: gripping/hanging/standing points remain supported.
- Occlusion: front/back ordering stays stable; parts emerge plausibly.
- Composition: fixed camera, prop outlines and background landmarks.
- Appearance: stable exposure, lighting, material, edges; no distracting flicker.
- Timing: readable anticipation/holds; no unintended duplicate-pose pause.

Small deliberate texture variation may suit clay/felt aesthetics; distinguish it from unwanted full-frame flicker. A contact sheet cannot establish playback rhythm.

Hashes, dimensions and reference snapshots only establish file integrity. The review command records actual agent inspection; it does not run an automatic visual-quality model.

## Intermediate-pose discipline

Prefer accepted endpoint anchors plus the master for controlled movement. In the goal, describe where stable landmarks should fall between endpoints and what should remain stationary. Use a neckless character's face orientation carefully: moving eye marks upward alone may not read as head rotation. Inspect silhouette and facial orientation together. If the generated midpoint copies an endpoint, reject that specific defect; do not describe it as successful interpolation. At the attempt limit, retain the accepted baseline, simplify only within the brief, and report the unresolved improvement.

For blink edits, keep the head pose constant and change lids only. Reuse the same half-closed still for reopening when it fits; reuse symmetric return poses without regenerating. Keep review notes and actual call counts, including reused historical sources.

## Repair

Reject with a concrete defect; use the existing candidate as a repair target when helpful. Preserve its correct staging. When upstream artwork changes, retain attempt provenance and mark later work stale. Reinspect forward, reuse still-valid successors, and regenerate only visible failures. A new continuity review does not rewrite historical generation inputs.

For background drift, first narrow edit scope and strengthen the scene reference. A fixed plate plus foreground composition can help, but requires correct alpha, occlusion and contact shadows and an available authorized image editor. This version does not implement automatic segmentation/background replacement. Do not blindly paste pixels to hide unexplained movement.

For persistent failures, simplify motion, add intermediate poses or split shots. Preserve the actual problem and pending work at the budget limit.

## Delivery

Keep editable references, all versions and the ledger with outputs using the host's artifact-saving workflow. Successful encoding proves format/timing, not image consistency. State whether verification used synthetic fixtures, supplied frames or actual generation, and whether playback was inspected.

See [FFmpeg image2](https://ffmpeg.org/ffmpeg-formats.html#image2-1) for sequence assembly. The bundled renderer uses raw RGB to preserve explicit holds and verifies the MP4. GIF delays are quantized; use MP4 as the timing master.
