"""Offline integration checks; geometric fixtures are not image-model validation."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

SCRIPTS = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="stop-motion-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.project = self.root / "project with spaces"
        Image.new("RGB", (64, 64), "blue").save(self.root / "master.png")
        self.plan = {
            "schema_version": 1, "title": "Fixture", "brief": "Move a square",
            "canvas": {"width": 64, "height": 64, "background": "#ffffff"},
            "action_fps": 8, "output_fps": 24, "loop": False,
            "invariants": ["Fixed camera"],
            "limits": {"max_attempts_per_frame": 3, "max_total_attempts": 9},
            "references": [{"id": "master", "role": "Identity", "path": "master.png"}],
            "frames": [
                {"id": "f0001", "goal": "At left", "hold": 1, "reference_ids": ["master"]},
                {"id": "f0002", "goal": "At middle", "hold": 2, "reference_ids": ["master"]},
                {"id": "f0003", "goal": "At right", "hold": 1, "reference_ids": ["master"]}
            ]}

    def run_cli(self, script, *args, ok=True):
        result = subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)],
                                capture_output=True, text=True)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def init(self):
        path = self.root / "plan.json"
        path.write_text(json.dumps(self.plan))
        return self.run_cli("project.py", "init", self.project, "--plan", path)

    def accept(self, frame, color):
        self.run_cli("project.py", "prepare", self.project, "--frame", frame)
        source = self.root / (frame + ".png")
        Image.new("RGB", (64, 64), color).save(source)
        self.run_cli("project.py", "record", self.project, "--frame", frame, "--image", source)
        self.run_cli("project.py", "review", self.project, "--frame", frame,
                     "--decision", "approve", "--notes", "Fixture inspected")

    def test_render_preserves_holds_order_duration_and_rejects_unreviewed(self):
        self.init()
        video = self.root / "movie.mp4"
        self.run_cli("render.py", "video", self.project, "--out", video, ok=False)
        self.assertFalse(video.exists())
        for fid, color in [("f0001", "red"), ("f0002", "lime"), ("f0003", "blue")]:
            self.accept(fid, color)
        self.run_cli("render.py", "video", self.project, "--out", video)
        probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=nb_frames,r_frame_rate,duration", "-of", "json", str(video)],
            check=True, capture_output=True, text=True)
        stream = json.loads(probe.stdout)["streams"][0]
        self.assertEqual(stream["nb_frames"], "12")
        self.assertEqual(stream["r_frame_rate"], "24/1")
        self.assertAlmostEqual(float(stream["duration"]), 0.5, places=3)
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-f", "rawvideo",
            "-pix_fmt", "rgb24", "pipe:1"], check=True, capture_output=True).stdout
        colors = [max(range(3), key=lambda c: raw[i * 64 * 64 * 3 + c]) for i in range(12)]
        self.assertEqual(colors, [0] * 3 + [1] * 6 + [2] * 3)
        report = json.loads(video.with_suffix('.mp4.json').read_text())
        self.assertEqual([f['hold'] for f in report['source_frames']], [1, 2, 1])
        self.assertTrue(all(f['image'] and len(f['sha256']) == 64 for f in report['source_frames']))
        self.run_cli("render.py", "video", self.project, "--out", video, ok=False)
        gif = self.root / "movie.gif"
        self.run_cli("render.py", "gif", self.project, "--out", gif)
        with Image.open(gif) as im:
            total = 0
            for i in range(im.n_frames):
                im.seek(i)
                total += im.info["duration"]
            self.assertEqual(total, 500)
            self.assertNotIn("loop", im.info)
        self.run_cli("render.py", "sheet", self.project, "--out", self.root / "sheet.png")

    def test_revision_marks_descendants_stale_and_allows_visual_revalidation(self):
        self.init()
        for fid, color in [("f0001", "red"), ("f0002", "lime"), ("f0003", "blue")]:
            self.accept(fid, color)
        self.run_cli("project.py", "revise", self.project, "--frame", "f0001", "--goal", "Eyes fixed")
        data = json.loads((self.project / "project.json").read_text())
        self.assertEqual([f["status"] for f in data["frames"]], ["planned", "stale", "stale"])
        self.run_cli("render.py", "video", self.project, "--out", self.root / "stale.mp4", ok=False)
        self.accept("f0001", "yellow")
        self.run_cli("project.py", "review", self.project, "--frame", "f0002",
                     "--decision", "approve", "--notes", "Still fits revised predecessor")
        self.run_cli("project.py", "review", self.project, "--frame", "f0003",
                     "--decision", "approve", "--notes", "Continuity checked")
        self.run_cli("project.py", "check", self.project)

    def test_budget_and_dimensions_and_reference_integrity(self):
        self.plan["limits"]["max_attempts_per_frame"] = 1
        self.init()
        self.run_cli("project.py", "prepare", self.project, "--frame", "f0002", ok=False)
        self.run_cli("project.py", "prepare", self.project, "--frame", "f0001")
        wrong = self.root / "wrong.png"
        Image.new("RGB", (32, 32)).save(wrong)
        self.run_cli("project.py", "record", self.project, "--frame", "f0001", "--image", wrong, ok=False)
        self.run_cli("project.py", "fail", self.project, "--frame", "f0001", "--notes", "Bad output size")
        self.run_cli("project.py", "prepare", self.project, "--frame", "f0001", ok=False)

    def test_approved_image_tampering_is_rejected(self):
        self.init()
        self.accept("f0001", "red")
        data = json.loads((self.project / "project.json").read_text())
        image = self.project / data["frames"][0]["image"]
        Image.new("RGB", (64, 64), "yellow").save(image)
        self.run_cli("project.py", "prepare", self.project, "--frame", "f0002", ok=False)

    def test_invalid_timeline_is_rejected_before_creation(self):
        self.plan["output_fps"] = 25
        path = self.root / "plan.json"
        path.write_text(json.dumps(self.plan))
        self.run_cli("project.py", "init", self.project, "--plan", path, ok=False)
        self.assertFalse(self.project.exists())

    def test_repair_keeps_original_target_and_loop_requires_seam_review(self):
        self.plan["loop"] = True
        self.init()
        for fid, color in [("f0001", "red"), ("f0002", "lime"), ("f0003", "blue")]:
            self.accept(fid, color)
        self.run_cli("project.py", "check", self.project, ok=False)
        self.run_cli("project.py", "loop-review", self.project, "--notes", "Seam inspected")
        self.run_cli("project.py", "check", self.project)
        self.run_cli("project.py", "revise", self.project, "--frame", "f0002", "--goal", "Correct eyes")
        result = self.run_cli("project.py", "prepare", self.project, "--frame", "f0002", "--repair")
        job = json.loads(result.stdout)
        self.assertTrue(any(r.get("repair_source") for r in job["reference_images"]))
        self.run_cli("project.py", "record", self.project, "--frame", "f0002", "--image", self.root / "f0002.png")
        self.run_cli("project.py", "review", self.project, "--frame", "f0002", "--decision", "approve", "--notes", "Eyes repaired")


if __name__ == "__main__":
    unittest.main()
