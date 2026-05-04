from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/code-reviewer/scripts/prepare_review_bundle.py"


class CodeReviewerBundleSmokeTest(unittest.TestCase):
    def test_prepares_fresh_context_review_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True, text=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo, check=True)

            source = repo / "example.py"
            source.write_text("def answer():\n    return 1\n", encoding="utf-8")
            subprocess.run(["git", "add", "example.py"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "initial"], cwd=repo, check=True, capture_output=True, text=True)

            source.write_text("def answer():\n    return 42\n", encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--repo",
                    str(repo),
                    "--working-tree",
                    "--change-id",
                    "answer-change",
                    "--request",
                    "Change answer to 42.",
                    "--writer-summary",
                    "Updated example.py; tests not run.",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(proc.stdout.strip(), ".agent/code-reviews/answer-change")
            bundle = repo / ".agent/code-reviews/answer-change"
            self.assertTrue((bundle / "request.md").exists())
            self.assertTrue((bundle / "writer-summary.md").exists())
            self.assertTrue((bundle / "diff.patch").exists())
            self.assertTrue((bundle / "reviewer-prompt.md").exists())
            self.assertIn("return 42", (bundle / "diff.patch").read_text(encoding="utf-8"))
            self.assertIn("Do not use the writer's chat context", (bundle / "reviewer-prompt.md").read_text(encoding="utf-8"))
            self.assertIn("Change answer to 42.", (bundle / "request.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
