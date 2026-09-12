# Animated-sprite mode

Set `mode` to `animated-sprite`. Accept `animatedsprite` as a conversational alias. Focus on game-ready frame organization and visual continuity, while stating which engine integration has actually been tested.

## Clip contract

Use one ledger per action, such as idle, walk, jump or attack, sharing copied approved character references. Before generating, establish source canvas, art style, facing, silhouette, scale, ground line, action origin, loop setting and contact/airborne phases. Include:

```json
{"mode":"animated-sprite","alpha":"transparent",
 "sprite":{"clip":"idle","pivot":[0.5,0.85]}}
```

Pivot is a fixed point in the full frame, measured from top-left; it is not recomputed from each image's bounding box. Animate jumping above that origin rather than recentering the body. For in-place walk clips, game code moves the actor. If root movement is baked into art, document the path so the engine does not apply it twice. Do not silently mirror asymmetric weapons or markings.

Pick frame timing per action. A held idle and a fast attack need different exposures. The shared ledger still requires an integer output/action FPS ratio for MP4 previews; the atlas retains exact hold ticks. Do not assume all game animation must have 16 frames.

## Generate and inspect

Prefer endpoint/key-pose anchors and individual frame repair for production. A one-call grid can be explored as a draft, but it must be cut using measured cell geometry and every extracted pose inspected. Check count, order, consistent cell dimensions, clipping and duplicated poses. Current helpers export atlases; they do not auto-detect or import generated sprite-sheet grids. Use explicit extraction tooling only when required, retain the original sheet/crop geometry, and register stills through prepare/record/review. Do not mistake a multi-variation sheet for temporal animation.

Generate true alpha via the available image tool. Validation rejects an entirely opaque or empty image for a transparent project, but it does not prove clean fur edges or detect a mostly opaque checkerboard with a stray transparent pixel. Inspect on light/dark backgrounds. Never turn an opaque sample into a claimed transparent sprite merely by placing it on a larger transparent atlas.

Review planted feet, joint/limb consistency, readable anticipation, impact/landing phases, loop seams and silhouette. Compare matching anchors across actions and preview idle→walk→idle and jump→idle before claiming an animation set is ready. For attack/footstep events, record intended timing separately and bind it in the chosen engine; current metadata does not implement hitboxes or events.

## Deliver

Use export_assets.py atlas to pack approved frames into an untrimmed RGBA PNG and custom JSON with clip name, frame rectangles, pivot, holds and loop setting. Packing never scales, aligns, recenters, or modifies source poses. Keep original PNGs and the ledger. Export GIF/WebP as optional previews.

Engine adapters are separate work. Atlas JSON is not a native Godot SpriteFrames, Unity controller or Phaser animation file. When requested, create and verify that engine-specific import/demo against the actual target version. Until then describe the result as sprite frames/atlas ready for import, not a tested playable game character. Skeletal rigs, mesh deformation, auto hitboxes and pixel-art cleanup are outside this mode's current helpers.
