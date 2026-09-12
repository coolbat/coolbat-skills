# Asset exports

Mode and format are independent. All exports below require approved, checksum-verified frames and loop review when applicable. Source frames are never changed. Choose fresh output names; existing outputs/reports are refused.

## RGBA sprite atlas

Provide `sprite.clip` and `sprite.pivot` in the plan even if exporting an atlas from another mode. For a legacy project without sprite metadata, create a copied project revision with the explicitly chosen pivot; preserve the original ledger. Do not invent an origin from the changing bounding box.

```bash
python "$SKILL_DIR/scripts/export_assets.py" atlas ./idle --out ./idle-atlas.png --columns 4 --padding 2
```

The output is PNG plus `.png.json` using `image-animate-director.atlas.v1`. Each frame has its own cell in array order, untrimmed/unscaled, surrounded by transparent padding. Rectangles exclude padding. The sheet retains source RGBA values. It does not remove backgrounds or extrude border texels; configure engine sampling/padding appropriately. Limits: maximum edge 16384, at most 64 million pixels. Split clips or deliberately prepare smaller source art if needed.

Metadata records `clip`, normalized pivot, loop, action_fps, frame rectangle/source size, start_tick, hold_ticks, duration_ms and source checksums. Exact timing is hold_ticks/action_fps; floating duration_ms is convenient for consumers. JSON uses a custom schema, not engine-native animation resources. One project exports one clip; export multiple actions to separate atlases and provide their relationship in an engine adapter.

## Animated WebP

```bash
python "$SKILL_DIR/scripts/export_assets.py" webp ./shot --out ./reaction.webp
```

Preserve original alpha using lossless encoding; verify codec support at runtime. Transparent artwork must already contain actual alpha. Set loop in the ledger, not at export time; true requires prior seam review. Frame delays are rounded cumulatively to milliseconds. A non-looping file plays once. Identical images can collapse to fewer encoded frames; when an entirely static file results, the report states its duration is not encoded as animation. Inspect the file in the target player before claiming playback compatibility.

## Existing exports

`render.py video|gif|sheet` remains compatible. MP4 and GIF composite alpha onto canvas.background. The contact sheet is a labeled review artifact; an atlas is an engine-facing image without labels. Do not substitute one for the other.

Transparent GIF, APNG, native engine resources and auto grid extraction are not bundled exporters. Add and verify an exporter when required rather than claiming support from the mode name.
