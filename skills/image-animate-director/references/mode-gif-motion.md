# GIF-motion mode

Set `mode` to `gif-motion`. Treat this as a short expressive loop/sticker workflow rather than a file extension. Select a readable gesture: blink, look around, wave, bounce, smile, breathing, or a small illustration effect. Keep text and logos stable when present.

For an unspecified loop, start with 1–3 seconds and 8 or 12 action ticks/second; retain the user's timing when given. Build compatible start/end poses and direction of movement. Reuse suitable return poses; do not reverse a blink, splash, or jump blindly. Keep intentional pauses explicit and inspect repeated playback.

Set `alpha: "transparent"` for stickers intended to overlay another scene. Use the available image tool for extraction/edits and inspect alpha edges on contrasting backgrounds; a rendered checkerboard is not transparency. For a full-scene illustration, use `alpha: "opaque"`.

Output options:
- GIF via render.py for a matte preview against the chosen canvas background.
- WebP via export_assets.py for a lossless animated file preserving the supplied alpha.
- PNG source frames for later editing and other platform-specific packaging.

Current helpers do not encode transparent GIF or APNG. If the user specifically requires transparent GIF, implement and verify that derivative (palette, binary transparency and disposal), or state the limitation before delivering an alternative. Never label a matte GIF transparent. GIF is not a guarantee of smooth motion; the actual poses and timing determine the result.
