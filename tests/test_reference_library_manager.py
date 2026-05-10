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
    def test_scans_reference_sources_and_writes_agent_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "project"
            papers = root / "reference" / "papers"
            papers.mkdir(parents=True)
            (papers / "Example Paper.pdf").write_bytes(b"%PDF-1.4\nexample\n")
            sources = root / "reference" / "sources"
            (sources / "collaborator-docs").mkdir(parents=True)
            (sources / "collaborator-docs" / "Reviewer Notes.docx").write_bytes(b"docx-placeholder")
            (sources / "markdown").mkdir()
            (sources / "markdown" / "seed.md").write_text("# Seed\n\nproject idea\n", encoding="utf-8")
            bundle = sources / "bundles" / "initial-bundle"
            bundle.mkdir(parents=True)
            (bundle / "README.md").write_text("# Bundle\n", encoding="utf-8")
            (bundle / "refs.bib").write_text("@article{x}\n", encoding="utf-8")

            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-root", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertIn("Scanned 4 source(s)", proc.stdout)
            agent_dir = root / "reference" / ".agent"
            source_index = (agent_dir / "source-index.md").read_text(encoding="utf-8")
            index = (agent_dir / "reference-index.md").read_text(encoding="utf-8")
            status = (agent_dir / "processing-status.md").read_text(encoding="utf-8")
            duplicates = (agent_dir / "duplicate-check.md").read_text(encoding="utf-8")

            self.assertIn("# Source Index", source_index)
            self.assertIn("example-paper", index)
            self.assertIn("reviewer-notes", index)
            self.assertIn("initial-bundle", index)
            self.assertIn("reference/cards/example-paper.md", index)
            self.assertIn("paper-or-pdf", status)
            self.assertIn("bundle", status)
            self.assertIn("skim | unread", status)
            self.assertIn("No exact duplicate sources found", duplicates)
            self.assertTrue((root / "reference" / "cards").is_dir())
            self.assertTrue((root / "reference" / "project-use").is_dir())


if __name__ == "__main__":
    unittest.main()
