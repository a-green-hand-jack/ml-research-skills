from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/run-status-monitor/scripts/run_status_probe.py"


class RunStatusMonitorSmokeTest(unittest.TestCase):
    def test_local_log_writes_short_status_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            log = root / "outputs/train.log"
            log.parent.mkdir(parents=True)
            log.write_text(
                "\n".join(
                    [
                        "epoch 1/4 val_loss=1.20",
                        "epoch 2/4 val_loss=0.80",
                    ]
                ),
                encoding="utf-8",
            )
            started_at = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
            config = root / ".agent/run-status/runs.json"
            config.parent.mkdir(parents=True)
            config.write_text(
                json.dumps(
                    {
                        "runs": {
                            "train": {
                                "backend": "local-log",
                                "log": "outputs/train.log",
                                "status_artifact": "docs/ops/runs/train-status.md",
                                "started_at": started_at,
                                "progress_patterns": {"epoch": r"epoch (?P<current>\d+)/(?P<total>\d+)"},
                                "metric_patterns": {"val_loss": r"val_loss=(?P<value>[0-9.]+)"},
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )

            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-root", str(root), "--run", "train"],
                check=True,
                capture_output=True,
                text=True,
            )

            status = (root / "docs/ops/runs/train-status.md").read_text(encoding="utf-8")
            self.assertIn("Run: train", proc.stdout)
            self.assertIn("- State: running", status)
            self.assertIn("- Progress: epoch=2/4", status)
            self.assertIn("- Latest metrics: val_loss=0.80", status)
            self.assertIn("- Raw scheduler output and logs are not copied here.", status)
            self.assertNotIn("epoch 1/4", status)

    def test_command_backend_summarizes_wrapper_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / "runs.json"
            output = root / "status.md"
            config.write_text(
                json.dumps(
                    {
                        "runs": {
                            "wrapped": {
                                "backend": "command",
                                "status_command": f"{sys.executable} -c \"print('state running epoch 3/6 score=0.42')\"",
                                "status_artifact": str(output),
                                "progress_patterns": {"epoch": r"epoch (?P<current>\d+)/(?P<total>\d+)"},
                                "metric_patterns": {"score": r"score=(?P<value>[0-9.]+)"},
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )

            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--project-root",
                    str(root),
                    "--config",
                    str(config),
                    "--run",
                    "wrapped",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            status = output.read_text(encoding="utf-8")
            self.assertIn("- State: running", status)
            self.assertIn("- Progress: epoch=3/6", status)
            self.assertIn("- Latest metrics: score=0.42", status)
            self.assertIn("exit 0", status)
            self.assertNotIn("state running epoch 3/6", status)


if __name__ == "__main__":
    unittest.main()
