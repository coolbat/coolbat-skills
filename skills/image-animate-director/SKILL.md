---
name: image-animate-director
description: Animate character references or still images with stop-motion, animated-sprite, and gif-motion workflows. Use for 定格动画, GIF动图, animated stickers, 2D game actions, sprite sheets, image-to-animation, or the former stop-motion-director workflow. Plan poses, preserve identity, review continuity, repair frames, and export MP4, GIF, transparent WebP, or RGBA sprite atlases with timing metadata.
---

# Image animate director

Produce animation through deliberate still-image edits, visual inspection, and explicit frame timing. Keep character and scene references stable while changing the planned pose. Retain every version and the references actually used.

## Select one production mode

Follow the requested mode. Otherwise infer it from intended use and announce the choice without asking the user to learn the mode names. Normalize `animatedsprite` and `animated_sprite` to `animated-sprite` when writing plans. Use only canonical values in project JSON.

| Mode | Select for | Read before planning |
| --- | --- | --- |
| `stop-motion` | Handmade stepping, clay/felt/paper animation, fixed-scene short films | [mode-stop-motion.md](references/mode-stop-motion.md) |
| `animated-sprite` | Game sprites, idle/walk/jump/attack sets, engine-facing atlases | [mode-animated-sprite.md](references/mode-animated-sprite.md) |
| `gif-motion` | Expressive loops, stickers, reactions, animated illustrations | [mode-gif-motion.md](references/mode-gif-motion.md) |

Modes set production and review priorities, not mutually exclusive output formats. A game animation can also have a GIF preview; a stop-motion clip can also be packed into an atlas. Keep `mode`, art style, generation strategy, and requested delivery formats distinct. Do not infer pixel-art style from game use or clay style from this skill's history.

For a new generic “make this move” request, prefer `gif-motion`; for an existing project without `mode`, retain legacy `stop-motion`. This is the renamed continuation of stop-motion-director, not a second independent skill. Old ledgers, checksums and scripts remain usable; mention the new invocation name when helpful, without promising a platform-level alias.

## Defaults and resources

Follow the user's approved brief and existing authorization. Announce sensible defaults and proceed without extra approval gates for routine generation, inspection, or local rendering.

Use mode-specific defaults below. When no timing is specified, a practical proof is one fixed-camera shot, one character, 2 seconds, 8 action ticks/second, and 24fps preview output. Choose framing from the user's intended use. Use their style; clay, felt and paper cutouts are options, not mandatory substitutions. A 2-second proof can have 16 distinct poses or fewer poses with explicit holds.

Assemble explicit poses with holds by default, without optical-flow interpolation, crossfades or motion blur. Choose pose spacing and exposure timing for the mode; do not impose a choppy handmade look on all outputs. Treat requested interpolation as a separate derivative and inspect occlusion/deformation artifacts. Design intermediate key poses for large transformations; two endpoints alone rarely explain an emerging butterfly or opening object. Split moving-camera/multi-shot stories into manageable shots; the helpers assume fixed composition within one project.

Resolve `SKILL_DIR` to this installed skill's actual directory, which may be renamed after installation.

- Read [project-format.md](references/project-format.md) to prepare or resume a ledger.
- Read [generation-and-review.md](references/generation-and-review.md) before generating/repairing frames.
- Use `scripts/project.py` to manage references, jobs, versions and reviews.
- Use `scripts/render.py` for contact sheets, MP4 and matte GIF previews.
- Use `scripts/export_assets.py` for untrimmed RGBA atlases with timing/pivot metadata and lossless WebP preserving source alpha; read [asset-exports.md](references/asset-exports.md).
- Use `scripts/inspect_motion.py` for locked-region difference reports and portable synchronized playback against an accepted baseline.
- Adapt `assets/caterpillar-plan.json` as a 2-second, 16-pose worked example.

Helpers require Python 3.10+ and Pillow (animated WebP needs its codec support); MP4 also requires FFmpeg with libx264 and FFprobe. Use available runtime dependencies. Name a missing dependency accurately rather than silently changing the image backend.

## 1. Prepare the shot

Inspect the supplied artwork and brief. Distinguish artwork from surrounding screenshot UI. When necessary, use the available image editor to create a clean master, preserving the uploaded source. Request a specific missing attachment only when it cannot be read.

Define invariant character details, material, camera, background, lighting and contact points. Add per-frame `motion` phases, allowed changes and explicit locks. For challenging intermediate poses, create and inspect both endpoint references first, then supply both with `motion.between`; retain the character master. Do not rely on a long chain of predecessor-only edits. Write visible target poses rather than "next frame". Design anticipation, movement, settling and holds. Do not present a stylized metamorphosis as a scientifically accurate sequence.

Use inspected supplied artwork as a master or generate approved master/key-pose references first. Label each reference's role. Write a concrete plan JSON with actual reference paths using the project format. Include canonical `mode`; for transparent artwork set `alpha: "transparent"`. Game clips require explicit `sprite.clip` and normalized `sprite.pivot`. At least one approved master is required. Reference images may have different dimensions; animation frame images must match the chosen, backend-supported canvas exactly.

Set an attempt budget proportional to the brief: three attempts means one initial attempt plus two retries. Budget master/key-pose generation separately; ledger limits count frame attempts, not every external call or monetary spend. Imported versions occupy ledger attempts but imply no billed generation.

```bash
python "$SKILL_DIR/scripts/project.py" init ./shot --plan ./plan.json
python "$SKILL_DIR/scripts/project.py" status ./shot
python "$SKILL_DIR/scripts/project.py" timeline ./shot
```

Initialization copies references into the new project. Resume existing work with `status`. Store artwork and project state outside the installed skill. Apply the host's durable artifact-saving workflow to completed outputs and reusable projects.

## 2. Generate or import frames

Prepare the next unapproved frame immediately before one image-tool call:

```bash
python "$SKILL_DIR/scripts/project.py" prepare ./shot --frame f0001
```

The JSON contains the full prompt and ordered `reference_images` with absolute paths and roles. This reserves one attempt and records its inputs; it does not generate an image or call an API. Use one writer per project. Frames depend on an approved predecessor.

Use the host's available image-generation/editing tool, following its actual schema:
- Inspect local references before editing. If `referenced_image_paths` is supported, pass the ordered job paths. If only recent-conversation references are supported, load the required images and select the smallest supported count containing all targets. Do not combine incompatible mechanisms or silently drop an anchor.
- Use the host's required display mechanism for returned images. Copy a tool-returned local still into the project when required for the requested animation. Do not invent a save-path argument or claim a model version the tool does not expose.
- Generate sequentially within a shot. Multiple image variations are not temporal frames.
- For an explicitly requested API/model route, verify current official documentation and use a configured integration. Do not silently substitute a model or request an API key when the built-in image tool is usable.
- If no image backend is available, preserve the plan/jobs and explain the missing capability. Do not substitute code-drawn artwork for requested generated images.

Register the actual returned still without stretching/cropping it to hide framing errors:

```bash
python "$SKILL_DIR/scripts/project.py" record ./shot --frame f0001 \
  --image ./generated-frame.png --backend built-in-image-tool
```

Add `--request-id` when supplied. For supplied animation stills, prepare with `--kind import`, then record with `--backend user-supplied`. For reused generated artwork use `--kind reuse`; both need visual review, but neither needs an image-tool call. Report actual new calls separately from reused assets and ledger reservations. Registration copies original bytes into a new versioned filename and records its checksum.

If a tool call fails or returns no usable still, close the attempt using `fail --frame ID --notes TEXT` before retrying. After interruption, check whether the active job already returned an image before calling again. Stop at the budget; preserve failed attempts instead of resetting counters.

## 3. Inspect and repair

Inspect each candidate alongside the master, predecessor, and next accepted frame when repairing. Check identity, target pose, anatomy, contact, occlusion, camera/background stability, lighting and distracting texture flicker. Checksums cannot establish visual consistency.

```bash
python "$SKILL_DIR/scripts/project.py" review ./shot --frame f0001 \
  --decision approve --notes "Face matches master; attachment fixed; intended head tilt is visible."
```

Use `--decision reject` with concrete defects when needed. Notes must reflect inspection actually performed, not canned assertions. Review before generating the dependent frame.

For a previously approved frame needing correction:

```bash
python "$SKILL_DIR/scripts/project.py" revise ./shot --frame f0004 \
  --goal "Keep this pose; restore the master's eye size and spacing."
python "$SKILL_DIR/scripts/project.py" prepare ./shot --frame f0004 --repair
```

`--repair` adds the existing image of this same frame as the edit target. Preserve its staging while correcting the defect; other references establish identity and continuity.

Upstream changes mark later approved/candidate frames `stale`, retaining files and original generation provenance. After approving the correction, inspect stale frames in order. Reapprove usable frames with notes; regenerate only visible failures. New review contexts do not rewrite original generation inputs. Rendering remains blocked until stale frames are resolved.

## 4. Assemble and deliver

Create and open a contact sheet, including for partial projects:

```bash
python "$SKILL_DIR/scripts/render.py" sheet ./shot --out ./review-v1.png
```

Examine suspect frames at full resolution. For loops, inspect the final-to-first transition and record `loop-review ./shot --notes TEXT`. Avoid unintentionally duplicating endpoint holds.

```bash
python "$SKILL_DIR/scripts/project.py" check ./shot
python "$SKILL_DIR/scripts/render.py" video ./shot --out ./animation-v1.mp4
python "$SKILL_DIR/scripts/render.py" gif ./shot --out ./animation-v1.gif
```

Generate a portable review with `python "$SKILL_DIR/scripts/inspect_motion.py" ./shot --out ./review.html`, optionally `--baseline ./accepted-shot`. Select locked `inspection_regions` from the actual artwork to flag adjacent-frame changes; these numbers cannot certify identity, pose correctness or a fixed camera. Play the animation to judge rhythm and flicker. The video helper repeats frames using integer holds, verifies dimensions/rate/count/duration with FFprobe, and saves a JSON report. It synthesizes no intermediate motion. GIF timing is rounded cumulatively to 10ms; MP4 is the timing master. MP4/GIF composite alpha against the explicit canvas background; original frame alpha remains intact.

Deliver the requested video/preview and reusable project (references, versioned frames, ledger, reports). Add sound when appropriate to the brief and available authorized assets. Report mechanical verification separately from visual inspection. If playback or real model-generation testing was unavailable, state that limit; do not claim smooth motion or proven image consistency.
