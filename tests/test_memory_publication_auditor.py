from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills/memory-publication-auditor/scripts/scan_publication_candidates.py"
)


class MemoryPublicationAuditorSmokeTest(unittest.TestCase):
    def test_scans_and_redacts_private_publication_risks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            private_dir = root / "private-memory"
            private_dir.mkdir()
            (private_dir / "ops.md").write_text(
                "\n".join(
                    [
                        "ssh alice@internal-host",
                        "connect to 10.0.0.5",
                        "path /Users/alice/project",
                        "token: abc123",
                    ]
                ),
                encoding="utf-8",
            )
            (private_dir / "pattern.md").write_text(
                "Reusable workflow: use route inspection and nc -vz with placeholders.",
                encoding="utf-8",
            )
            output = root / "audit.md"

            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--input", str(private_dir), "--output", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )

            report = output.read_text(encoding="utf-8")
            self.assertIn("Scanned 2 file(s)", proc.stdout)
            self.assertIn("private-only", report)
            self.assertIn("reusable-pattern", report)
            self.assertIn("&lt;private-ip&gt;", report)
            self.assertIn("&lt;user-path&gt;", report)
            self.assertIn("ssh &lt;target&gt;", report)
            self.assertIn("token: &lt;secret&gt;", report)
            self.assertNotIn("10.0.0.5", report)
            self.assertNotIn("/Users/alice", report)
            self.assertNotIn("alice@internal-host", report)
            self.assertNotIn("abc123", report)


if __name__ == "__main__":
    unittest.main()
