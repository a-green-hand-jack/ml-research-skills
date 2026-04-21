#!/usr/bin/env python3
"""Minimal validator for ml-research-skills.

Checks:
1. Every skill has a parseable YAML frontmatter block.
2. The frontmatter `name` matches the skill directory name.
3. Common helper-file references in `SKILL.md` exist.
4. Skill instructions do not hardcode Claude-only install paths.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
SKILL_NAME_RE = re.compile(r"^[a-z0-9-]+$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
RELATIVE_SUPPORT_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_])((?:scripts|templates|references|assets)/[A-Za-z0-9_./-]+)"
)
SKILL_DIR_PLACEHOLDER_RE = re.compile(r"<([a-z0-9-]+)-skill-dir>/(.+)")
CLAUDE_ONLY_PATH_RE = re.compile(r"~/.claude/skills/")
COMMON_SUPPORT_FILES = ("sources.yaml", "environments.yaml", "checklist.md")


@dataclass(frozen=True)
class Issue:
    path: Path
    message: str


def extract_frontmatter(text: str) -> str | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    return match.group(1)


def parse_yaml(frontmatter: str) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ImportError:
        return parse_yaml_with_ruby(frontmatter)

    parsed = yaml.safe_load(frontmatter)
    if not isinstance(parsed, dict):
        raise ValueError("frontmatter must parse to a mapping")
    return parsed


def parse_yaml_with_ruby(frontmatter: str) -> dict[str, Any]:
    cmd = [
        "ruby",
        "-r",
        "yaml",
        "-r",
        "json",
        "-e",
        (
            "data = YAML.safe_load(ARGF.read, permitted_classes: [], aliases: false); "
            "abort('frontmatter must parse to a mapping') unless data.is_a?(Hash); "
            "puts JSON.generate(data)"
        ),
    ]
    proc = subprocess.run(
        cmd,
        input=frontmatter,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "unknown YAML parse error"
        raise ValueError(detail)
    parsed = json.loads(proc.stdout)
    if not isinstance(parsed, dict):
        raise ValueError("frontmatter must parse to a mapping")
    return parsed


def is_allowed_claude_path_line(line: str) -> bool:
    allowed_markers = (
        "Do not assume",
        "for example",
        "such as",
        "target agent's skill home",
    )
    return any(marker in line for marker in allowed_markers)


def iter_helper_refs(skill_dir: Path, text: str) -> list[tuple[int, str]]:
    refs: list[tuple[int, str]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        explicit_placeholder = None
        placeholder_match = SKILL_DIR_PLACEHOLDER_RE.search(line)
        if placeholder_match:
            explicit_placeholder = placeholder_match.group(1)
            if explicit_placeholder != skill_dir.name:
                continue

        helper_context = any(
            marker in line
            for marker in (
                "<installed-skill-dir>/",
                f"<{skill_dir.name}-skill-dir>/",
                "├──",
                "└──",
                "│",
            )
        )
        if not helper_context and explicit_placeholder is None:
            continue

        for match in RELATIVE_SUPPORT_PATH_RE.finditer(line):
            refs.append((line_no, match.group(1).rstrip(".,)")))

        for basename in COMMON_SUPPORT_FILES:
            if basename in line:
                refs.append((line_no, basename))

    return refs


def validate_skill(skill_dir: Path) -> list[Issue]:
    issues: list[Issue] = []
    skill_file = skill_dir / "SKILL.md"
    rel_skill_file = skill_file.relative_to(REPO_ROOT)

    if not skill_file.exists():
        return [Issue(rel_skill_file, "missing SKILL.md")]

    text = skill_file.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(text)
    if frontmatter is None:
        issues.append(Issue(rel_skill_file, "missing YAML frontmatter block"))
        return issues

    try:
        metadata = parse_yaml(frontmatter)
    except Exception as exc:  # noqa: BLE001
        issues.append(Issue(rel_skill_file, f"invalid YAML frontmatter: {exc}"))
        return issues

    name = metadata.get("name")
    if not isinstance(name, str) or not name.strip():
        issues.append(Issue(rel_skill_file, "frontmatter missing non-empty `name`"))
    else:
        if name != skill_dir.name:
            issues.append(
                Issue(
                    rel_skill_file,
                    f"frontmatter name `{name}` does not match directory `{skill_dir.name}`",
                )
            )
        if not SKILL_NAME_RE.fullmatch(name):
            issues.append(Issue(rel_skill_file, f"invalid skill name `{name}`"))

    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        issues.append(Issue(rel_skill_file, "frontmatter missing non-empty `description`"))

    for line_no, line in enumerate(text.splitlines(), start=1):
        if CLAUDE_ONLY_PATH_RE.search(line) and not is_allowed_claude_path_line(line):
            issues.append(
                Issue(
                    rel_skill_file,
                    f"line {line_no} contains hardcoded Claude-only path `~/.claude/skills/`",
                )
            )

    seen_refs: set[str] = set()
    for line_no, ref in iter_helper_refs(skill_dir, text):
        if ref in seen_refs:
            continue
        seen_refs.add(ref)
        if not (skill_dir / ref).exists():
            issues.append(
                Issue(
                    rel_skill_file,
                    f"line {line_no} references missing helper path: `{ref}`",
                )
            )

    return issues


def main() -> int:
    if not SKILLS_ROOT.exists():
        print(f"skills directory not found: {SKILLS_ROOT}", file=sys.stderr)
        return 2

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    all_issues: list[Issue] = []
    for skill_dir in skill_dirs:
        all_issues.extend(validate_skill(skill_dir))

    if all_issues:
        for issue in all_issues:
            print(f"ERROR {issue.path}: {issue.message}")
        print(f"\nValidation failed: {len(all_issues)} issue(s) across {len(skill_dirs)} skill(s).")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s); no issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
