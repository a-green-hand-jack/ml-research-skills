from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_PUSH = REPO_ROOT / "skills" / "safe-git-ops" / "scripts" / "project-push"


class ProjectPushWrapperSmokeTest(unittest.TestCase):
    def test_project_push_dry_run_uses_stable_git_c_shape(self) -> None:
        proc = subprocess.run(
            [str(PROJECT_PUSH), "--dry-run", ".", "origin", "main"],
            cwd=REPO_ROOT,
            check=True,
            text=True,
            capture_output=True,
        )

        self.assertEqual(proc.stdout, "git -C . push origin main \n")

    def test_project_push_defaults_to_current_branch(self) -> None:
        branch = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=REPO_ROOT,
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()

        proc = subprocess.run(
            [str(PROJECT_PUSH), "--dry-run", "."],
            cwd=REPO_ROOT,
            check=True,
            text=True,
            capture_output=True,
        )

        self.assertEqual(proc.stdout, f"git -C . push origin {branch} \n")

    def test_project_push_rejects_non_repo(self) -> None:
        proc = subprocess.run(
            [str(PROJECT_PUSH), "--dry-run", "/tmp"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("not a git worktree", proc.stderr)


if __name__ == "__main__":
    unittest.main()
