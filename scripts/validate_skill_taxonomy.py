#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6.0"]
# ///
"""
validate_skill_taxonomy.py — Taxonomy consistency checks for ml-research-skills.

Checks:
1. Router child consistency: skills named in route-table.md files all exist.
2. expected_path chains: all skills in routing-evals.json expected_path exist.
3. Contrastive-routing skill mentions: all named skills in contrastive-routing.md exist.
4. Memory contract completeness: applies_to, required_facts, always_read verified.
5. skill-index.yaml consistency: all index entries exist; all real skills are indexed.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
SKILL_NAME_RE = re.compile(r"^[a-z0-9-]+$")
BACKTICK_SKILL_RE = re.compile(r"`([a-z0-9-]+)`")
# Pseudo-values allowed in applies_to that are not real skill names
CONTRACT_APPLIES_TO_KEYWORDS = {"all-skills", "session-start", "any-skill"}


@dataclass(frozen=True)
class Issue:
    path: str
    message: str


def _load_yaml(path: Path) -> dict | list | None:
    try:
        import yaml  # type: ignore
    except ImportError:
        return None
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def _skill_names_in_text(text: str, known: set[str]) -> set[str]:
    """Return backtick-quoted tokens that look like skill names and exist in known."""
    found = set()
    for m in BACKTICK_SKILL_RE.finditer(text):
        candidate = m.group(1)
        if SKILL_NAME_RE.fullmatch(candidate) and candidate in known:
            found.add(candidate)
    return found


def _all_backtick_names(text: str) -> set[str]:
    """Return all backtick-quoted tokens matching skill-name pattern."""
    return {m.group(1) for m in BACKTICK_SKILL_RE.finditer(text) if SKILL_NAME_RE.fullmatch(m.group(1))}


# ---------------------------------------------------------------------------
# Check 1 — Router child consistency
# ---------------------------------------------------------------------------

def validate_router_children(skill_names: set[str]) -> list[Issue]:
    """Every skill named in a route-table.md must exist in skills/."""
    issues: list[Issue] = []
    for skill_dir in sorted(SKILLS_ROOT.iterdir()):
        if not skill_dir.is_dir():
            continue
        route_table = skill_dir / "references" / "route-table.md"
        if not route_table.exists():
            continue
        text = route_table.read_text(encoding="utf-8")
        named = _all_backtick_names(text)
        rel = str(route_table.relative_to(REPO_ROOT))
        for name in sorted(named):
            if name not in skill_names:
                issues.append(Issue(rel, f"references unknown skill `{name}`"))
    return issues


# ---------------------------------------------------------------------------
# Check 2 — expected_path chain consistency
# ---------------------------------------------------------------------------

def validate_expected_paths(skill_names: set[str]) -> list[Issue]:
    """All skills in expected_path arrays in routing-evals.json must exist."""
    evals_path = REPO_ROOT / "tests" / "routing-evals.json"
    if not evals_path.exists():
        return []
    issues: list[Issue] = []
    rel = str(evals_path.relative_to(REPO_ROOT))
    try:
        data = json.loads(evals_path.read_text())
    except json.JSONDecodeError as exc:
        return [Issue(rel, f"invalid JSON: {exc}")]
    for entry in data.get("evals", []):
        eid = entry.get("id", "?")
        path = entry.get("expected_path", [])
        if not isinstance(path, list):
            issues.append(Issue(rel, f"{eid} expected_path must be a list"))
            continue
        for step in path:
            if step not in skill_names:
                issues.append(Issue(rel, f"{eid} expected_path contains unknown skill `{step}`"))
    return issues


# ---------------------------------------------------------------------------
# Check 3 — Contrastive-routing skill mentions
# ---------------------------------------------------------------------------

def validate_contrastive_routing(skill_names: set[str]) -> list[Issue]:
    """Skill names in contrastive-routing.md files must exist."""
    issues: list[Issue] = []
    for skill_dir in sorted(SKILLS_ROOT.iterdir()):
        if not skill_dir.is_dir():
            continue
        cr_file = skill_dir / "references" / "contrastive-routing.md"
        if not cr_file.exists():
            continue
        text = cr_file.read_text(encoding="utf-8")
        named = _all_backtick_names(text)
        rel = str(cr_file.relative_to(REPO_ROOT))
        for name in sorted(named):
            if name not in skill_names:
                issues.append(Issue(rel, f"references unknown skill `{name}`"))
    return issues


# ---------------------------------------------------------------------------
# Check 4 — Memory contract completeness
# ---------------------------------------------------------------------------

def validate_memory_contracts(skill_names: set[str]) -> list[Issue]:
    """
    For each YAML in taxonomy/memory-contracts/:
    - applies_to skills exist
    - required_facts IDs exist in memory/fact-index.yaml
    - always_read files that are not conditional exist on disk
    """
    contracts_dir = REPO_ROOT / "taxonomy" / "memory-contracts"
    if not contracts_dir.exists():
        return []

    # Load known fact IDs
    fact_ids: set[str] = set()
    fact_index_path = REPO_ROOT / "memory" / "fact-index.yaml"
    if fact_index_path.exists():
        data = _load_yaml(fact_index_path)
        if isinstance(data, dict):
            for fact in data.get("facts", []):
                if isinstance(fact, dict) and "id" in fact:
                    fact_ids.add(fact["id"])

    issues: list[Issue] = []
    for contract_file in sorted(contracts_dir.glob("*.yaml")):
        rel = str(contract_file.relative_to(REPO_ROOT))
        data = _load_yaml(contract_file)
        if not isinstance(data, dict):
            issues.append(Issue(rel, "could not parse as YAML mapping"))
            continue

        # applies_to skills exist (skip known pseudo-keywords)
        for skill in data.get("applies_to", []):
            if skill in CONTRACT_APPLIES_TO_KEYWORDS:
                continue
            if skill not in skill_names:
                issues.append(Issue(rel, f"applies_to references unknown skill `{skill}`"))

        # required_facts IDs exist in fact-index.yaml
        if fact_ids:
            for fid in data.get("required_facts", []):
                if fid not in fact_ids:
                    issues.append(Issue(rel, f"required_facts references unknown fact ID `{fid}`"))

        # always_read files exist (skip conditional patterns with spaces like "if ...")
        for read_path in data.get("always_read", []):
            if " " in read_path:
                continue
            full_path = REPO_ROOT / read_path
            if not full_path.exists():
                issues.append(Issue(rel, f"always_read file missing: `{read_path}`"))

    return issues


# ---------------------------------------------------------------------------
# Check 5 — skill-index.yaml consistency
# ---------------------------------------------------------------------------

def validate_skill_index(skill_names: set[str]) -> list[Issue]:
    """
    If taxonomy/skill-index.yaml exists:
    - Every skill in the index must exist in skills/.
    - Every real skill must appear in the index.
    - Router skills must have role == "router".
    """
    index_path = REPO_ROOT / "taxonomy" / "skill-index.yaml"
    if not index_path.exists():
        return []

    rel = str(index_path.relative_to(REPO_ROOT))
    data = _load_yaml(index_path)
    if not isinstance(data, dict):
        return [Issue(rel, "could not parse as YAML mapping")]

    skills_section = data.get("skills", {})
    if not isinstance(skills_section, dict):
        return [Issue(rel, "`skills` must be a YAML mapping keyed by skill name")]

    issues: list[Issue] = []
    indexed_names = set(skills_section.keys())

    # Every indexed skill must exist
    for name in sorted(indexed_names):
        if name not in skill_names:
            issues.append(Issue(rel, f"index entry `{name}` does not exist in skills/"))

    # Every real skill must be indexed
    for name in sorted(skill_names - indexed_names):
        issues.append(Issue(rel, f"skill `{name}` exists in skills/ but is missing from index"))

    # Routers section consistency
    routers_section = data.get("routers", {})
    if isinstance(routers_section, dict):
        root = routers_section.get("root")
        if root and root not in skill_names:
            issues.append(Issue(rel, f"routers.root `{root}` does not exist in skills/"))
        for name in routers_section.get("domain", []):
            if name not in skill_names:
                issues.append(Issue(rel, f"routers.domain entry `{name}` does not exist in skills/"))

    # Router skills must have role == "router"
    for name, entry in skills_section.items():
        if not isinstance(entry, dict):
            continue
        role = entry.get("role")
        if role == "router" and name not in skill_names:
            issues.append(Issue(rel, f"index marks `{name}` as router but skill does not exist"))

    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    if not SKILLS_ROOT.exists():
        print(f"skills directory not found: {SKILLS_ROOT}", file=sys.stderr)
        return 2

    skill_names = {p.name for p in SKILLS_ROOT.iterdir() if p.is_dir()}
    all_issues: list[Issue] = []

    checks = [
        ("router-children", validate_router_children(skill_names)),
        ("expected-paths", validate_expected_paths(skill_names)),
        ("contrastive-routing", validate_contrastive_routing(skill_names)),
        ("memory-contracts", validate_memory_contracts(skill_names)),
        ("skill-index", validate_skill_index(skill_names)),
    ]

    for check_name, issues in checks:
        if issues:
            for issue in issues:
                print(f"ERROR [{check_name}] {issue.path}: {issue.message}")
        all_issues.extend(issues)

    if all_issues:
        print(f"\nTaxonomy validation failed: {len(all_issues)} issue(s).")
        return 1

    router_count = sum(
        1 for p in SKILLS_ROOT.iterdir()
        if p.is_dir() and (p / "references" / "route-table.md").exists()
    )
    print(
        f"Taxonomy OK: {len(skill_names)} skills, {router_count} routers with route tables, "
        f"no issues found."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
