from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills/reference-library-manager/scripts/scan_reference_library.py"
)


class ReferenceLibraryManagerSmokeTest(unittest.TestCase):
    def test_scans_reference_pdfs_and_writes_agent_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "project"
            papers = root / "reference" / "papers"
            papers.mkdir(parents=True)
            (papers / "Example Paper.pdf").write_bytes(b"%PDF-1.4\nexample\n")
            (papers / "Another-Paper.pdf").write_bytes(b"%PDF-1.4\nanother\n")

            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-root", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertIn("Scanned 2 PDF(s)", proc.stdout)
            agent_dir = root / "reference" / ".agent"
            index = (agent_dir / "reference-index.md").read_text(encoding="utf-8")
            status = (agent_dir / "reading-status.md").read_text(encoding="utf-8")
            duplicates = (agent_dir / "duplicate-check.md").read_text(encoding="utf-8")

            self.assertIn("example-paper", index)
            self.assertIn("another-paper", index)
            self.assertIn("reference/cards/example-paper.md", index)
            self.assertIn("skim | unread", status)
            self.assertIn("No exact duplicate PDFs found", duplicates)
            self.assertTrue((root / "reference" / "cards").is_dir())
            self.assertTrue((root / "reference" / "project-use").is_dir())


if __name__ == "__main__":
    unittest.main()
