#!/usr/bin/env python3
"""Local, single-writer image-animation project ledger. No network or model calls."""
import argparse
import hashlib
import json
import math
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageColor


def require(condition, message):
    if not condition:
        raise ValueError(message)


def stamp():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(root, data):
    temp = root / "project.json.tmp"
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(root / "project.json")


def local(root, value):
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()), "Project file path escapes project directory")
    require(path.is_file(), f"Missing file: {path}")
    return path


MODES = ("stop-motion", "animated-sprite", "gif-motion")


def mode(data):
    return data.get("mode", "stop-motion")


def alpha_mode(data):
    return data.get("alpha", "transparent" if mode(data) == "animated-sprite" else "opaque")


def validate_alpha(image, data):
    if alpha_mode(data) == "transparent":
        low, high = image.convert("RGBA").getchannel("A").getextrema()
        require(low < 255 and high > 0, "Transparent artwork required; opaque backgrounds/checkerboards and empty frames are not alpha")


def validate(data):
    require(data.get("schema_version") == 1, "schema_version must be 1")
    require(mode(data) in MODES, "mode must be stop-motion, animated-sprite or gif-motion")
    require(alpha_mode(data) in ("opaque", "transparent"), "alpha must be opaque or transparent")
    if "sprite" in data:
        sprite = data["sprite"]
        require(isinstance(sprite, dict), "sprite must be an object")
        require(isinstance(sprite.get("clip"), str) and re.fullmatch(r"[a-zA-Z0-9_-]+", sprite["clip"]), "sprite.clip must be an ASCII identifier")
        pivot = sprite.get("pivot", [])
        require(len(pivot) == 2 and all(type(x) in (int,float) and math.isfinite(x) and 0 <= x <= 1 for x in pivot),
                "sprite.pivot must be normalized [x,y] coordinates")
    if mode(data) == "animated-sprite":
        require("sprite" in data, "animated-sprite requires sprite.clip and sprite.pivot")
    for field in ("title", "brief"):
        require(isinstance(data.get(field), str) and data[field].strip(), f"{field} is required")
    for field in ("action_fps", "output_fps"):
        require(type(data.get(field)) is int and 1 <= data[field] <= 120, f"Invalid {field}")
    require(data["output_fps"] % data["action_fps"] == 0,
            "output_fps must be an integer multiple of action_fps to preserve even holds")
    canvas = data["canvas"]
    for axis in ("width", "height"):
        require(type(canvas.get(axis)) is int and 2 <= canvas[axis] <= 8192 and canvas[axis] % 2 == 0,
                f"canvas.{axis} must be a positive even integer between 2 and 8192")
    ImageColor.getrgb(canvas["background"])
    require(type(data.get("loop")) is bool, "loop must be boolean")
    require(isinstance(data.get("invariants"), list) and data["invariants"] and
            all(isinstance(x, str) and x.strip() for x in data["invariants"]), "invariants must be nonempty strings")
    for field in ("max_attempts_per_frame", "max_total_attempts"):
        require(type(data["limits"].get(field)) is int and data["limits"][field] > 0, f"Invalid limit: {field}")
    for region in data.get("inspection_regions", []):
        require(isinstance(region.get("id"), str) and region["id"].strip(), "Region id required")
        box = region.get("box", [])
        require(len(box) == 4 and all(type(v) in (int, float) and math.isfinite(v) and 0 <= v <= 1 for v in box)
                and box[0] < box[2] and box[1] < box[3], "Region box must be normalized [left,top,right,bottom]")
        threshold = region.get("threshold", 0.03)
        require(type(threshold) in (int, float) and math.isfinite(threshold) and 0 <= threshold <= 1,
                "Region threshold must be between zero and one")
    ids = set()
    for ref in data["references"]:
        require(re.fullmatch(r"[a-zA-Z0-9_-]+", ref["id"]) and ref["id"] not in ids, "Invalid or duplicate reference id")
        ids.add(ref["id"])
        require(isinstance(ref["role"], str) and ref["role"].strip(), "Reference role is required")
    require(ids, "At least one approved master reference is required")
    require(isinstance(data["frames"], list) and data["frames"], "frames must not be empty")
    frame_ids = set()
    for frame in data["frames"]:
        require(re.fullmatch(r"[a-zA-Z0-9_-]+", frame["id"]) and frame["id"] not in frame_ids, "Invalid or duplicate frame id")
        frame_ids.add(frame["id"])
        require(isinstance(frame["goal"], str) and frame["goal"].strip(), "Each frame requires an explicit goal")
        require(type(frame["hold"]) is int and frame["hold"] > 0, "hold must be a positive integer")
        require(frame["reference_ids"] and set(frame["reference_ids"]) <= ids, "Unknown or empty reference_ids")
        motion = frame.get("motion", {})
        require(isinstance(motion, dict), "motion must be an object")
        if motion:
            require(motion.get("phase") in ("anticipation", "movement", "hold", "recovery", "settle"), "Invalid motion phase")
            for key in ("change", "lock"):
                require(isinstance(motion.get(key), list) and all(isinstance(x, str) and x.strip() for x in motion[key]),
                        f"motion.{key} must be a list of nonempty strings")
            if "between" in motion:
                b = motion["between"]
                require(b["from"] != b["to"] and {b["from"], b["to"]} <= set(frame["reference_ids"]),
                        "Both distinct endpoint references must be supplied")
                require(type(b["progress"]) in (int, float) and math.isfinite(b["progress"]) and 0 < b["progress"] < 1,
                        "Intermediate pose progress must be strictly between zero and one")


def load(root):
    data = json.loads((root / "project.json").read_text(encoding="utf-8"))
    validate(data)
    return data


def verified_image(root, item):
    path = local(root, item["image"])
    require(digest(path) == item["sha256"], f"Image changed outside ledger: {path}")
    return path


def context(root, data, index):
    frame = data["frames"][index]
    refs = []
    for rid in frame["reference_ids"]:
        ref = next(r for r in data["references"] if r["id"] == rid)
        path = local(root, ref["path"])
        require(digest(path) == ref["sha256"], f"Reference changed: {rid}; create a new project revision")
        refs.append({"path": ref["path"], "sha256": ref["sha256"], "role": ref["role"], "asset_id": rid})
    if index:
        previous = data["frames"][index - 1]
        require(previous["status"] == "approved", f"Approve predecessor {previous['id']} first")
        verified_image(root, previous)
        refs.append({"path": previous["image"], "sha256": previous["sha256"],
                     "role": "Previous approved frame: continuity; default edit target only when no same-frame repair source is supplied",
                     "frame_id": previous["id"]})
    return refs


def validate_prefix(root, data, end):
    for index in range(end):
        frame = data["frames"][index]
        require(frame["status"] == "approved", f"Frame {frame['id']} is {frame['status']}")
        path = verified_image(root, frame)
        with Image.open(path) as im:
            validate_alpha(im, data)
            require(im.size == (data["canvas"]["width"], data["canvas"]["height"]), "Frame dimensions differ from canvas")
        require(frame.get("review_context") == context(root, data, index), f"Frame {frame['id']} needs continuity review")


def invalidate_after(data, index):
    for frame in data["frames"][index + 1:]:
        if frame["status"] in ("approved", "candidate", "stale"):
            frame["status"] = "stale"
    data["loop_review"] = None


def init(root, plan_path):
    require(not root.exists(), "Project directory already exists; resume it or choose a new directory")
    data = json.loads(plan_path.read_text(encoding="utf-8"))
    validate(data)
    sources = []
    for ref in data["references"]:
        source = (plan_path.parent / ref["path"]).resolve()
        with Image.open(source) as im:
            im.verify()
        sources.append(source)
    root.mkdir(parents=True)
    (root / "references").mkdir()
    (root / "frames").mkdir()
    for ref, source in zip(data["references"], sources):
        destination = root / "references" / (ref["id"] + source.suffix.lower())
        shutil.copyfile(source, destination)
        ref.update(path=str(destination.relative_to(root)), sha256=digest(destination))
    for frame in data["frames"]:
        for key in list(frame):
            if key not in ("id", "goal", "hold", "reference_ids", "motion"):
                del frame[key]
        frame.update(status="planned", attempts=[], reviews=[])
    data.update(created_at=stamp(), loop_review=None)
    save(root, data)
    return summary(data)


def summary(data):
    ticks = sum(f["hold"] for f in data["frames"])
    return {"title": data["title"], "mode": mode(data), "alpha": alpha_mode(data), "duration_seconds": ticks / data["action_fps"],
            "action_ticks": ticks, "unique_frame_entries": len(data["frames"]),
            "video_frames": ticks * (data["output_fps"] // data["action_fps"]),
            "attempts_used": sum(len(f["attempts"]) for f in data["frames"]),
            "attempt_kinds": {kind: sum(a.get("kind", "legacy") == kind for f in data["frames"] for a in f["attempts"])
                              for kind in ("generate", "reuse", "import", "legacy")},
            "count_note": "Reservations are not confirmed external calls or billing; master/key-pose calls outside the ledger are separate",
            "frames": [{"id": f["id"], "status": f["status"], "attempts": len(f["attempts"])} for f in data["frames"]]}


def prepare(root, data, index, repair=False, kind="generate"):
    require(kind in ("generate", "reuse", "import"), "Invalid attempt kind")
    frame = data["frames"][index]
    require(frame["status"] in ("planned", "rejected", "stale"), "Review/fail current candidate or revise approved frame first")
    require(not any(f["status"] == "generating" for f in data["frames"]), "Finish or fail the active generation before preparing another")
    validate_prefix(root, data, index)
    require(len(frame["attempts"]) < data["limits"]["max_attempts_per_frame"], "Per-frame attempt budget exhausted")
    require(sum(len(f["attempts"]) for f in data["frames"]) < data["limits"]["max_total_attempts"], "Total attempt budget exhausted")
    refs = context(root, data, index)
    if repair:
        require(frame.get("image"), "No existing frame image to repair")
        verified_image(root, frame)
        refs.append({"path": frame["image"], "sha256": frame["sha256"], "repair_source": True,
                     "role": "Existing image of THIS frame: edit target; preserve its pose except the requested correction"})
    roles = "\n".join(f"Image {i + 1} ({r.get('asset_id', r.get('frame_id', 'repair'))}): {r['role']}" for i, r in enumerate(refs))
    direction = {
        "stop-motion": "Create one standalone stop-motion animation frame with deliberate pose stepping.",
        "animated-sprite": "Create one standalone 2D game sprite animation frame. Keep the sprite canvas and action origin fixed; never auto-center each pose.",
        "gif-motion": "Create one standalone frame for a short expressive animated sticker or looping illustration."
    }[mode(data)]
    prompt = (f"{direction}\nProject: {data['brief']}\n"
              f"Reference roles, in supplied order:\n{roles}\n"
              f"This frame's target pose: {frame['goal']}\n"
              "Keep these invariants:\n" + "\n".join(f"- {x}" for x in data["invariants"]) +
              f"\nCanvas: {data['canvas']['width']}x{data['canvas']['height']}. "
              "Keep the framing fixed. Produce one clean exposure, without panels, frame numbers, captions, "
              "or motion blur. Follow the stated target pose; preserve the original character identity. "
              "The previous frame, when present, supplies motion continuity; reference poses do not override the target pose.")
    if alpha_mode(data) == "transparent":
        prompt += "\nUse a genuinely transparent alpha background. No painted checkerboard, colored matte, floor, text or UI. Preserve soft alpha edges."
    if mode(data) == "animated-sprite":
        prompt += f"\nAnimation clip: {data['sprite']['clip']}. Fixed action origin at normalized canvas coordinate {data['sprite']['pivot']}; it is not the moving character's bounding-box center."
    if frame.get("motion"):
        m = frame["motion"]
        prompt += "\nMotion phase: " + m["phase"] + "\nChange only: " + "; ".join(m["change"])
        prompt += "\nExplicitly lock: " + "; ".join(m["lock"])
        if m.get("between"):
            b = m["between"]
            prompt += (f"\nGenerate a distinct intermediate pose {b['progress']:.0%} from reference {b['from']} "
                       f"toward reference {b['to']}. Do not copy either endpoint. These are pose anchors, not a collage.")
    attempt = {"number": len(frame["attempts"]) + 1, "started_at": stamp(), "kind": kind,
               "status": "started", "goal": frame["goal"], "references": refs, "prompt": prompt}
    frame["attempts"].append(attempt)
    frame["status"] = "generating"
    invalidate_after(data, index)
    save(root, data)
    return {"frame": frame["id"], "attempt": attempt["number"], "prompt": prompt,
            "reference_images": [{**r, "path": str(local(root, r["path"]))} for r in refs]}


def record(root, data, index, image, backend, request_id):
    frame = data["frames"][index]
    require(frame["status"] == "generating", "Run prepare before recording a generated frame")
    with Image.open(image) as im:
        validate_alpha(im, data)
        require(im.size == (data["canvas"]["width"], data["canvas"]["height"]), "Generated image dimensions differ from canvas")
        require(getattr(im, "n_frames", 1) == 1, "Record a single still image")
    with Image.open(image) as im:
        im.verify()
    attempt = frame["attempts"][-1]
    base_refs = [r for r in attempt["references"] if not r.get("repair_source")]
    require(base_refs == context(root, data, index), "References changed while generating")
    for ref in attempt["references"]:
        require(digest(local(root, ref["path"])) == ref["sha256"], "Generation reference changed")
    destination = root / "frames" / f"{frame['id']}-v{attempt['number']:03d}{image.suffix.lower()}"
    require(not destination.exists(), "Candidate file already exists")
    shutil.copyfile(image, destination)
    path = str(destination.relative_to(root))
    checksum = digest(destination)
    attempt.update(status="candidate", image=path, sha256=checksum, backend=backend,
                   request_id=request_id, recorded_at=stamp())
    if attempt.get("kind") in ("reuse", "import"):
        attempt["source"] = {"path": str(image.resolve()), "sha256": checksum}
    frame.update(status="candidate", image=path, sha256=checksum)
    save(root, data)
    return {"frame": frame["id"], "status": "candidate", "image": str(destination)}


def review(root, data, index, decision, notes):
    frame = data["frames"][index]
    require(frame["status"] in ("candidate", "stale"), "Only a candidate or stale frame can be reviewed")
    require(notes.strip(), "Record visual review notes")
    refs = None
    if decision == "approve":
        validate_prefix(root, data, index)
        verified_image(root, frame)
        refs = context(root, data, index)
        frame["review_context"] = refs
    frame["reviews"].append({"at": stamp(), "decision": decision, "notes": notes,
                              "image": frame["image"], "context": refs})
    frame["status"] = "approved" if decision == "approve" else "rejected"
    invalidate_after(data, index)
    save(root, data)
    return {"frame": frame["id"], "status": frame["status"]}


def check(root, data):
    validate_prefix(root, data, len(data["frames"]))
    if data["loop"]:
        expected = [data["frames"][-1]["sha256"], data["frames"][0]["sha256"]]
        require(data.get("loop_review") and data["loop_review"]["endpoints"] == expected, "Inspect loop seam and run loop-review")
    return {"ready": True, **summary(data)}


def timeline(data):
    ticks = 0
    rows = []
    for frame in data["frames"]:
        start = ticks / data["action_fps"]
        ticks += frame["hold"]
        rows.append({"id": frame["id"], "start": start, "end": ticks / data["action_fps"],
                     "phase": frame.get("motion", {}).get("phase", "unspecified"), "goal": frame["goal"]})
    return {"duration_seconds": ticks / data["action_fps"], "timeline": rows}


def reconsider(root, data, index, notes):
    frame = data["frames"][index]
    require(not any(f["status"] == "generating" for f in data["frames"]), "Close active generation first")
    require(frame["status"] in ("planned", "rejected") and frame.get("image") and notes.strip(),
            "A retained image, revised/rejected frame and concrete reconsideration notes are required")
    verified_image(root, frame)
    frame["reviews"].append({"at": stamp(), "decision": "reconsider", "notes": notes, "image": frame["image"]})
    frame["status"] = "stale"
    invalidate_after(data, index)
    save(root, data)
    return {"frame": frame["id"], "status": "stale", "note": "Visual review required; attempts unchanged"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["init", "status", "prepare", "record", "review", "revise", "fail", "check", "loop-review", "timeline", "reconsider"])
    parser.add_argument("project", type=Path)
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--frame")
    parser.add_argument("--image", type=Path)
    parser.add_argument("--goal")
    parser.add_argument("--notes", default="")
    parser.add_argument("--decision", choices=["approve", "reject"])
    parser.add_argument("--backend", default="unspecified")
    parser.add_argument("--request-id")
    parser.add_argument("--kind", choices=["generate", "reuse", "import"], default="generate")
    parser.add_argument("--repair", action="store_true", help="Use this frame's existing image as a local repair target")
    args = parser.parse_args()
    root = args.project.resolve()
    if args.command == "init":
        require(args.plan is not None, "--plan is required")
        result = init(root, args.plan.resolve())
    else:
        data = load(root)
        if args.command == "status":
            result = summary(data)
        elif args.command == "timeline":
            result = timeline(data)
        elif args.command == "check":
            result = check(root, data)
        elif args.command == "loop-review":
            require(data["loop"] and args.notes.strip(), "A looping project and review notes are required")
            validate_prefix(root, data, len(data["frames"]))
            data["loop_review"] = {"at": stamp(), "notes": args.notes,
                "endpoints": [data["frames"][-1]["sha256"], data["frames"][0]["sha256"]]}
            save(root, data)
            result = {"loop_reviewed": True}
        else:
            indices = [i for i, f in enumerate(data["frames"]) if f["id"] == args.frame]
            require(indices, "--frame must identify an existing frame")
            index = indices[0]
            frame = data["frames"][index]
            if args.command == "prepare":
                result = prepare(root, data, index, args.repair, args.kind)
            elif args.command == "record":
                require(args.image is not None, "--image is required")
                result = record(root, data, index, args.image, args.backend, args.request_id)
            elif args.command == "review":
                require(args.decision is not None, "--decision is required")
                result = review(root, data, index, args.decision, args.notes)
            elif args.command == "reconsider":
                result = reconsider(root, data, index, args.notes)
            elif args.command == "fail":
                require(frame["status"] == "generating" and args.notes.strip(), "Active generation and failure notes required")
                frame["attempts"][-1].update(status="failed", notes=args.notes, ended_at=stamp())
                frame["status"] = "rejected"
                save(root, data)
                result = {"frame": frame["id"], "status": "rejected"}
            else:
                require(not any(f["status"] == "generating" for f in data["frames"]), "Finish or fail the active generation before revising")
                require(args.goal and args.goal.strip(), "--goal is required")
                frame["reviews"].append({"at": stamp(), "decision": "revise", "old_goal": frame["goal"], "new_goal": args.goal})
                frame.update(goal=args.goal, status="planned")
                invalidate_after(data, index)
                save(root, data)
                result = {"frame": frame["id"], "status": "planned"}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, StopIteration) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)
