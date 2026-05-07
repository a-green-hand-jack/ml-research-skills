from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/sidecar-task-runner/scripts/prepare_sidecar_task.py"


class SidecarTaskRunnerSmokeTest(unittest.TestCase):
    def test_prepares_sidecar_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)

            proc = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--repo",
                    str(repo),
                    "--task-id",
                    "docs-scan",
                    "--title",
                    "Docs scan",
                    "--phase",
                    "maintenance",
                    "--task-type",
                    "audit",
                    "--prompt",
                    "Scan docs for drift.",
                    "--input",
                    "README.md",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            task_dir = repo / ".agent/sidecars/docs-scan"
            self.assertIn("Prepared sidecar task: .agent/sidecars/docs-scan", proc.stdout)
            self.assertTrue((task_dir / "prompt.md").exists())
            self.assertTrue((task_dir / "input-manifest.md").exists())
            self.assertTrue((task_dir / "model.json").exists())
            self.assertIn("Scan docs for drift.", (task_dir / "prompt.md").read_text(encoding="utf-8"))
            self.assertIn("README.md", (task_dir / "input-manifest.md").read_text(encoding="utf-8"))

            model = json.loads((task_dir / "model.json").read_text(encoding="utf-8"))
            self.assertEqual(model["model"], "gpt-5.3-codex-spark")
            self.assertEqual(model["sandbox"], "read-only")
            self.assertEqual(model["phase"], "maintenance")

    def test_prepares_precommit_classifier_preset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--repo",
                    str(repo),
                    "--task-id",
                    "precommit-check",
                    "--title",
                    "Precommit classifier",
                    "--phase",
                    "maintenance",
                    "--task-type",
                    "audit",
                    "--preset",
                    "precommit-classifier",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            prompt = (repo / ".agent/sidecars/precommit-check/prompt.md").read_text(encoding="utf-8")
            self.assertIn("# Precommit Classifier Sidecar", prompt)
            self.assertIn("Fast Path", prompt)
            self.assertIn("Skill Path", prompt)
            self.assertIn("Do not commit", prompt)

    def test_prepares_personalization_scanner_preset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--repo",
                    str(repo),
                    "--task-id",
                    "personalization-scan",
                    "--title",
                    "Personalization scan",
                    "--phase",
                    "maintenance",
                    "--task-type",
                    "audit",
                    "--preset",
                    "personalization-scanner",
                    "--input",
                    "memory/current-status.md",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            prompt = (repo / ".agent/sidecars/personalization-scan/prompt.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("# Personalization Scanner Sidecar", prompt)
            self.assertIn("Recommended Writeback", prompt)
            self.assertIn("Do not ask the user questions", prompt)


if __name__ == "__main__":
    unittest.main()
