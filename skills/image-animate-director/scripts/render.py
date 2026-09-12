#!/usr/bin/env python3
"""Assemble reviewed stills into MP4/GIF or a labeled contact sheet; no interpolation."""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

from project import check, digest, load, local, require, summary, verified_image


def rgb_image(path, background):
    with Image.open(path) as source:
        rgba = source.convert("RGBA")
    base = Image.new("RGBA", rgba.size, background)
    return Image.alpha_composite(base, rgba).convert("RGB")


def video(root, data, destination):
    require(shutil.which("ffmpeg") and shutil.which("ffprobe"), "Install ffmpeg and ffprobe before video rendering")
    info = check(root, data)
    width, height = data["canvas"]["width"], data["canvas"]["height"]
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo",
               "-pixel_format", "rgb24", "-video_size", f"{width}x{height}",
               "-framerate", str(data["output_fps"]), "-i", "pipe:0", "-an",
               "-frames:v", str(info["video_frames"]), "-c:v", "libx264", "-crf", "18",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(destination)]
    with tempfile.TemporaryFile() as error_log:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=error_log)
        try:
            for frame in data["frames"]:
                pixels = rgb_image(verified_image(root, frame), data["canvas"]["background"]).tobytes()
                for _ in range(frame["hold"] * (data["output_fps"] // data["action_fps"])):
                    process.stdin.write(pixels)
            process.stdin.close()
            code = process.wait()
        except BaseException:
            process.kill()
            process.wait()
            raise
        error_log.seek(0)
        require(code == 0, error_log.read().decode("utf-8", "replace"))
    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,nb_frames,r_frame_rate,duration", "-of", "json", str(destination)],
        capture_output=True, text=True, check=True)
    stream = json.loads(probe.stdout)["streams"][0]
    require(int(stream["nb_frames"]) == info["video_frames"], "Encoded frame count mismatch")
    require(stream["r_frame_rate"] == f"{data['output_fps']}/1", "Encoded frame rate mismatch")
    require(abs(float(stream["duration"]) - info["duration_seconds"]) < 0.001, "Encoded duration mismatch")
    require((stream["width"], stream["height"]) == (width, height), "Encoded dimensions mismatch")
    return {"verification": stream, "assembly": "Frame holds only; no generated in-betweens"}


def gif(root, data, destination):
    check(root, data)
    images, durations = [], []
    elapsed_ticks = 0
    previous_ms = 0
    for frame in data["frames"]:
        image = rgb_image(verified_image(root, frame), data["canvas"]["background"])
        images.append(image)
        elapsed_ticks += frame["hold"]
        elapsed_ms = round(elapsed_ticks * 100 / data["action_fps"]) * 10
        durations.append(elapsed_ms - previous_ms)
        previous_ms = elapsed_ms
    require(all(d >= 20 for d in durations), "GIF preview would require very short delays; use MP4 or longer holds")
    options = {"loop": 0} if data["loop"] else {}
    images[0].save(destination, save_all=True, append_images=images[1:], duration=durations,
                   disposal=2, optimize=False, **options)
    return {"duration_ms": sum(durations), "note": "GIF delays quantized cumulatively to 10 ms; MP4 is the timing master"}


def sheet(root, data, destination):
    columns, cell_w, cell_h = 4, 224, 260
    rows = (len(data["frames"]) + columns - 1) // columns
    require(rows * cell_h <= 40000, "Too many frames for one contact sheet; split into shots")
    result = Image.new("RGB", (columns * cell_w, rows * cell_h), "#171b22")
    draw = ImageDraw.Draw(result)
    elapsed = 0
    for index, frame in enumerate(data["frames"]):
        x, y = (index % columns) * cell_w, (index // columns) * cell_h
        if frame.get("image"):
            source = rgb_image(verified_image(root, frame), data["canvas"]["background"])
            thumb = ImageOps.contain(source, (208, 208))
            result.paste(thumb, (x + (cell_w - thumb.width) // 2, y + 8 + (208 - thumb.height) // 2))
        else:
            draw.rectangle((x + 8, y + 8, x + 216, y + 216), fill="#2b3240")
        label = f"{frame['id']} | {frame['status']}"
        draw.text((x + 8, y + 222), label, fill="white")
        draw.text((x + 8, y + 238), f"t={elapsed / data['action_fps']:.3f}s hold={frame['hold']}", fill="#bdc7d8")
        elapsed += frame["hold"]
    result.save(destination)
    return {"frames_shown": len(data["frames"]), "note": "Contact sheet is a review aid, not visual approval"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("format", choices=["video", "gif", "sheet"])
    parser.add_argument("project", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    root, out = args.project.resolve(), args.out.resolve()
    data = load(root)
    suffix = {"video": ".mp4", "gif": ".gif", "sheet": ".png"}[args.format]
    require(out.suffix.lower() == suffix, f"Output must use {suffix}")
    require(not out.exists(), "Output exists; choose a new versioned filename")
    report_path = out.with_suffix(out.suffix + ".json")
    require(not report_path.exists(), "Render report already exists; choose a new versioned filename")
    if args.format != "sheet":
        check(root, data)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="stop-motion-render-", dir=out.parent) as staging:
        target = Path(staging) / ("output" + suffix)
        result = {"video": video, "gif": gif, "sheet": sheet}[args.format](root, data, target)
        require(not out.exists(), "Output appeared during render; refusing overwrite")
        target.rename(out)
    source_frames = [{"id": frame["id"], "image": frame.get("image"),
                      "sha256": frame.get("sha256"), "hold": frame["hold"]} for frame in data["frames"]]
    report = {"file": str(out), "sha256": digest(out), "project_sha256": digest(root / "project.json"),
              "canvas": data["canvas"], "action_fps": data["action_fps"], "output_fps": data["output_fps"],
              "source_frames": source_frames, **summary(data), **result}
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, subprocess.SubprocessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)
