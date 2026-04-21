#!/usr/bin/env python3
"""Scaffold a new ML Python project from bundled templates."""

from __future__ import annotations

import argparse
from datetime import date
import json
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scaffold a new ML Python project using bundled templates."
    )
    parser.add_argument("target_dir", help="Target project directory to create")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--package-name", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--python-version", default="3.11")
    parser.add_argument("--author-name", required=True)
    parser.add_argument("--author-email", required=True)
    parser.add_argument("--repo-url", default="TBD")
    return parser.parse_args()


def render_text(text: str, replacements: dict[str, str]) -> str:
    for key, value in replacements.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def load_manifest(skill_dir: Path) -> dict:
    manifest_path = skill_dir / "template_manifest.json"
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def materialize_template(
    templates_root: Path,
    src: Path,
    dest_root: Path,
    replacements: dict[str, str],
) -> None:
    rel = src.relative_to(templates_root)
    if len(rel.parts) < 2:
        raise SystemExit(f"template path must include a template group prefix: {src}")
    rel = Path(*rel.parts[1:])
    if rel.name.endswith(".tmpl"):
        rel = rel.with_name(rel.name[:-5])
    dest = dest_root / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = src.read_text(encoding="utf-8")
    dest.write_text(render_text(content, replacements), encoding="utf-8")


def copy_template_groups(
    skill_dir: Path,
    group_names: list[str],
    dest_root: Path,
    replacements: dict[str, str],
    manifest: dict,
) -> None:
    groups = manifest["template_groups"]
    templates_root = skill_dir / "templates"
    for group_name in group_names:
        for rel_path in groups[group_name]:
            src = skill_dir / rel_path
            materialize_template(templates_root, src, dest_root, replacements)


def ensure_clean_target(target_dir: Path) -> None:
    if not target_dir.exists():
        return
    if any(target_dir.iterdir()):
        raise SystemExit(f"target directory already exists and is not empty: {target_dir}")


def run_uv_init(target_dir: Path, package_name: str, python_version: str) -> None:
    cmd = ["uv", "init", "--name", package_name, "--python", python_version]
    proc = subprocess.run(cmd, cwd=target_dir, check=False)
    if proc.returncode != 0:
        raise SystemExit("uv init failed; ensure `uv` is installed and working")


def make_source_layout(target_dir: Path, package_name: str, manifest: dict, project_type: str) -> None:
    project_cfg = manifest["project_types"][project_type]
    package_root = target_dir / "src" / package_name
    for subdir in project_cfg["package_subdirs"]:
        path = package_root / subdir
        path.mkdir(parents=True, exist_ok=True)
        (path / "__init__.py").touch()
    package_root.mkdir(parents=True, exist_ok=True)
    (package_root / "__init__.py").touch()

    for rel in project_cfg["create_dirs"]:
        path = target_dir / rel
        path.mkdir(parents=True, exist_ok=True)

    (target_dir / "tests" / "__init__.py").touch()


def write_env_file(target_dir: Path) -> None:
    env_path = target_dir / ".env"
    if not env_path.exists():
        env_path.write_text(
            "# Copy from .env.example and fill in actual values.\n",
            encoding="utf-8",
        )


def write_gitkeeps(target_dir: Path, manifest: dict, project_type: str) -> None:
    for rel in manifest["project_types"][project_type]["gitkeep_files"]:
        path = target_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()


def remove_uv_defaults(target_dir: Path) -> None:
    # `uv init` may create a top-level hello-world script. Keep the scaffold focused.
    for rel in ("main.py",):
        path = target_dir / rel
        if path.exists():
            path.unlink()

    src_dir = target_dir / "src"
    if src_dir.exists():
        for candidate in src_dir.iterdir():
            if candidate.is_dir():
                continue
            if candidate.name.endswith(".py"):
                candidate.unlink()


def main() -> int:
    args = parse_args()
    target_dir = Path(args.target_dir).expanduser().resolve()
    skill_dir = Path(__file__).resolve().parents[1]
    manifest = load_manifest(skill_dir)

    ensure_clean_target(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    run_uv_init(target_dir, args.package_name, args.python_version)
    remove_uv_defaults(target_dir)
    make_source_layout(target_dir, args.package_name, manifest, "ml")

    replacements = {
        "PROJECT_NAME": args.project_name,
        "PACKAGE_NAME": args.package_name,
        "DESCRIPTION": args.description,
        "PYTHON_VERSION": args.python_version,
        "AUTHOR_NAME": args.author_name,
        "AUTHOR_EMAIL": args.author_email,
        "REPO_URL": args.repo_url,
        "LOCAL_REPO_ROOT": str(target_dir),
        "DEFAULT_BRANCH": "main",
        "DEFAULT_SERVER_NAME": "cluster-a",
        "DEFAULT_SSH_ALIAS": "cluster-a",
        "DEFAULT_REMOTE_REPO_ROOT": f"/path/to/{args.project_name}",
        "DEFAULT_SCHEDULER": "slurm",
        "DEFAULT_LAUNCH_MODE": "sbatch",
        "DEFAULT_ENV_ACTIVATION": "source .venv/bin/activate",
        "DATE": date.today().isoformat(),
    }

    copy_template_groups(
        skill_dir,
        manifest["project_types"]["ml"]["template_groups"],
        target_dir,
        replacements,
        manifest,
    )
    write_env_file(target_dir)
    write_gitkeeps(target_dir, manifest, "ml")

    print(f"Scaffolded ML project at {target_dir}")
    print("Next: install dependencies, run tests, then initialize git if desired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
