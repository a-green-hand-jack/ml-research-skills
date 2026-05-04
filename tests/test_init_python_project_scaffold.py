from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    REPO_ROOT
    / "skills"
    / "init-python-project"
    / "scripts"
    / "scaffold_new_project.py"
)


@unittest.skipUnless(shutil.which("uv"), "uv is required for scaffold smoke tests")
class ScaffoldNewProjectSmokeTest(unittest.TestCase):
    maxDiff = None

    def run_scaffold(self, target_dir: Path, *, project_name: str = "demo-ml") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "python3",
                str(SCRIPT),
                str(target_dir),
                "--project-name",
                project_name,
                "--package-name",
                "demo_ml",
                "--description",
                "Demo ML project",
                "--python-version",
                "3.11",
                "--author-name",
                "Test User",
                "--author-email",
                "test@example.com",
                "--repo-url",
                "git@github.com:example/demo-ml.git",
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_scaffold_creates_expected_structure_and_renders_templates(self) -> None:
        with tempfile.TemporaryDirectory(prefix="init-python-project-") as tmp:
            target_dir = Path(tmp) / "demo-ml"
            proc = self.run_scaffold(target_dir)

            self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)
            self.assertTrue((target_dir / ".gitignore").is_file())
            self.assertTrue((target_dir / ".env.example").is_file())
            self.assertTrue((target_dir / ".pre-commit-config.yaml").is_file())
            self.assertTrue((target_dir / "pyproject.toml").is_file())
            self.assertFalse((target_dir / "pyproject.toml.tmpl").exists())
            self.assertTrue((target_dir / "experiments" / "config.py").is_file())
            self.assertTrue((target_dir / "infra" / "envs" / "local.yaml").is_file())
            self.assertTrue((target_dir / "infra" / "remote-projects.yaml").is_file())
            self.assertTrue((target_dir / "docs" / "ops" / "current-status.md").is_file())
            self.assertTrue((target_dir / "docs" / "ops" / "decision-log.md").is_file())
            self.assertTrue((target_dir / "docs" / "results" / ".gitkeep").is_file())
            self.assertTrue((target_dir / "docs" / "reports" / ".gitkeep").is_file())
            self.assertTrue((target_dir / "docs" / "runs" / ".gitkeep").is_file())
            self.assertTrue((target_dir / ".agent" / "local-overrides.yaml").is_file())
            self.assertTrue((target_dir / "scripts" / "train.py").is_file())
            self.assertTrue((target_dir / "tests" / "conftest.py").is_file())
            self.assertTrue((target_dir / ".vscode" / "settings.json").is_file())
            self.assertTrue((target_dir / ".env").is_file())

            readme = (target_dir / "README.md").read_text(encoding="utf-8")
            claude = (target_dir / "CLAUDE.md").read_text(encoding="utf-8")
            pyproject = (target_dir / "pyproject.toml").read_text(encoding="utf-8")
            pre_commit = (target_dir / ".pre-commit-config.yaml").read_text(
                encoding="utf-8"
            )
            train_script = (target_dir / "scripts" / "train.py").read_text(encoding="utf-8")
            remote_manifest = (target_dir / "infra" / "remote-projects.yaml").read_text(
                encoding="utf-8"
            )
            current_status = (target_dir / "docs" / "ops" / "current-status.md").read_text(
                encoding="utf-8"
            )
            local_overrides = (target_dir / ".agent" / "local-overrides.yaml").read_text(
                encoding="utf-8"
            )
            gitignore = (target_dir / ".gitignore").read_text(encoding="utf-8")

            for text in (
                readme,
                claude,
                pyproject,
                pre_commit,
                train_script,
                remote_manifest,
                current_status,
                local_overrides,
            ):
                self.assertNotIn("{{PROJECT_NAME}}", text)
                self.assertNotIn("{{PACKAGE_NAME}}", text)

            self.assertIn("demo-ml", readme)
            self.assertIn("demo_ml", pyproject)
            self.assertIn("gitleaks", pre_commit)
            self.assertIn("shellcheck", pre_commit)
            self.assertIn("ruff format --check", pre_commit)
            self.assertIn("from demo_ml.data import load_data", train_script)
            self.assertIn(str(target_dir), remote_manifest)
            self.assertIn("/path/to/demo-ml", remote_manifest)
            self.assertIn("cluster-a", current_status)
            self.assertIn(".agent/", gitignore)
            self.assertIn("/runs/", gitignore)
            self.assertIn("docs/results/", readme)

    def test_scaffold_rejects_non_empty_target_directory(self) -> None:
        with tempfile.TemporaryDirectory(prefix="init-python-project-") as tmp:
            target_dir = Path(tmp) / "existing-project"
            target_dir.mkdir()
            (target_dir / "keep.txt").write_text("existing\n", encoding="utf-8")

            proc = self.run_scaffold(target_dir, project_name="existing-project")

            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("target directory already exists and is not empty", proc.stderr + proc.stdout)


if __name__ == "__main__":
    unittest.main()
