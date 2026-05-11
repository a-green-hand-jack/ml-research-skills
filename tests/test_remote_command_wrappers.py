from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REMOTE_CMD = REPO_ROOT / "skills" / "remote-project-control" / "scripts" / "remote-cmd"
REMOTE_BASH = REPO_ROOT / "skills" / "remote-project-control" / "scripts" / "remote-bash"


class RemoteCommandWrapperSmokeTest(unittest.TestCase):
    def test_remote_cmd_dry_run_quotes_shell_fragments(self) -> None:
        proc = subprocess.run(
            [
                str(REMOTE_CMD),
                "--dry-run",
                "server",
                "/remote/project",
                "--",
                "bash",
                "-lc",
                'for d in outputs/*; do echo "$d"; done',
            ],
            check=True,
            text=True,
            capture_output=True,
        )

        self.assertIn("ssh server", proc.stdout)
        self.assertIn("cd\\ /remote/project", proc.stdout)
        self.assertIn("exec\\ bash\\ -lc", proc.stdout)
        self.assertNotIn('echo "$d"', proc.stdout)
        self.assertIn("\\$d", proc.stdout)

    def test_remote_bash_remote_script_dry_run(self) -> None:
        proc = subprocess.run(
            [
                str(REMOTE_BASH),
                "--dry-run",
                "server",
                "/remote/project",
                "scripts/ops/status.sh",
                "--",
                "--run",
                "train-main",
            ],
            check=True,
            text=True,
            capture_output=True,
        )

        self.assertIn("ssh server", proc.stdout)
        self.assertIn("cd\\ /remote/project", proc.stdout)
        self.assertIn("exec\\ bash\\ scripts/ops/status.sh\\ --run\\ train-main", proc.stdout)

    def test_remote_bash_upload_dry_run(self) -> None:
        proc = subprocess.run(
            [
                str(REMOTE_BASH),
                "--upload",
                "--dry-run",
                "server",
                "/remote/project",
                "scripts/ops/status.sh",
                "--",
                "train-main",
            ],
            check=True,
            text=True,
            capture_output=True,
        )

        self.assertIn("bash\\ -s\\ --\\ train-main", proc.stdout)
        self.assertIn("< scripts/ops/status.sh", proc.stdout)


if __name__ == "__main__":
    unittest.main()
