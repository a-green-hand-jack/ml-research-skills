from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills/latex-layout-issue-bundler/scripts/create_layout_issue_bundle.py"
)


class LatexLayoutIssueBundlerSmokeTest(unittest.TestCase):
    def test_prepares_bundle_without_pdf_rendering_tools(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paper = Path(tmp) / "paper"
            paper.mkdir()
            pdf = paper / "main.pdf"
            pdf.write_bytes(b"%PDF-1.4\n% fake minimal test file\n")
            tex = paper / "method.tex"
            tex.write_text(
                "\\section{Method}\n"
                "Before the algorithm.\n"
                "\\begin{algorithm}\n"
                "\\caption{Example}\n"
                "\\end{algorithm}\n"
                "After the algorithm.\n",
                encoding="utf-8",
            )
            log = paper / "main.log"
            log.write_text(
                "Overfull \\hbox (12.0pt too wide) in paragraph at lines 3--5\n",
                encoding="utf-8",
            )

            proc = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--paper-dir",
                    str(paper),
                    "--pdf",
                    str(pdf),
                    "--page",
                    "1",
                    "--title",
                    "Algorithm bottom gap",
                    "--problem",
                    "Large blank space after the algorithm.",
                    "--object",
                    "Algorithm 1",
                    "--source",
                    "method.tex:2-5",
                    "--crop",
                    "bottom",
                    "--issue-id",
                    "alg-gap",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(proc.stdout.strip(), ".agent/layout-issues/alg-gap")
            bundle = paper / ".agent/layout-issues/alg-gap"
            self.assertTrue((bundle / "prompt.md").exists())
            self.assertTrue((bundle / "manifest.json").exists())
            self.assertTrue((bundle / "source-snippet.tex").exists())
            self.assertTrue((bundle / "compile-log-excerpt.txt").exists())

            manifest = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["issue_id"], "alg-gap")
            self.assertEqual(manifest["page"], 1)
            self.assertEqual(manifest["object"], "Algorithm 1")
            self.assertIn("source", manifest)

            prompt = (bundle / "prompt.md").read_text(encoding="utf-8")
            self.assertIn("Large blank space after the algorithm.", prompt)
            self.assertIn("Do not start with global", prompt)
            self.assertIn("source-snippet.tex", prompt)

            snippet = (bundle / "source-snippet.tex").read_text(encoding="utf-8")
            self.assertIn("Before the algorithm.", snippet)
            self.assertIn("\\caption{Example}", snippet)

            log_excerpt = (bundle / "compile-log-excerpt.txt").read_text(encoding="utf-8")
            self.assertIn("Overfull", log_excerpt)


if __name__ == "__main__":
    unittest.main()
