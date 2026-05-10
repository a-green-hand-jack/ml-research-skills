#!/usr/bin/env python3
"""Scan private memory/skill files for publication risks and candidates."""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".py",
    ".sh",
    ".tex",
    ".bib",
    ".rst",
    ".csv",
}

SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".mypy_cache", ".pytest_cache"}


@dataclass(frozen=True)
class Finding:
    path: Path
    line_no: int
    severity: str
    category: str
    evidence: str


PATTERNS: list[tuple[str, str, re.Pattern[str]]] = [
    ("high", "private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("high", "secret-like-assignment", re.compile(r"\b(api[_-]?key|token|secret|password|credential|auth[_-]?header)\b\s*[:=]", re.I)),
    ("high", "private-ipv4", re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b")),
    ("high", "email-address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("medium", "absolute-user-path", re.compile(r"(?<!\w)(?:/Users|/home)/[^/\s]+(?:/[^\s`'\"<>]*)?")),
    ("medium", "private-project-path", re.compile(r"(?<!\w)(?:/projects|/scratch|/mnt|/private)/[^\s`'\"<>]+")),
    ("medium", "ssh-target", re.compile(r"\bssh\s+(?:[A-Za-z0-9._-]+@)?[A-Za-z0-9._-]+")),
    ("medium", "internal-hostname", re.compile(r"\b[A-Za-z0-9._-]+\.(?:local|internal|lan)\b", re.I)),
]

PATTERN_HINTS = re.compile(
    r"\b(protocol|workflow|checklist|pattern|template|diagnos(?:e|is|tic)|route|fallback|redact|sanitize|audit|publishable|reusable)\b",
    re.I,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", required=True, help="Input private file or directory. Repeatable.")
    parser.add_argument("--output", default=".agent/publication-audits/audit.md", help="Output audit report path.")
    parser.add_argument("--max-bytes", type=int, default=1_000_000, help="Skip files larger than this limit.")
    return parser.parse_args()


def iter_files(inputs: list[Path], max_bytes: int) -> list[Path]:
    files: list[Path] = []
    for input_path in inputs:
        if input_path.is_file():
            candidates = [input_path]
        else:
            candidates = [p for p in input_path.rglob("*") if p.is_file()]
        for path in candidates:
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if path.stat().st_size > max_bytes:
                continue
            files.append(path)
    return sorted(set(files))


def redact(text: str) -> str:
    text = re.sub(r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "<private-key>", text)
    text = re.sub(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b", "<private-ip>", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "<email>", text)
    text = re.sub(r"(?<!\w)(?:/Users|/home)/[^/\s]+(?:/[^\s`'\"<>]*)?", "<user-path>", text)
    text = re.sub(r"(?<!\w)(?:/projects|/scratch|/mnt|/private)/[^\s`'\"<>]+", "<private-path>", text)
    text = re.sub(r"\bssh\s+(?:[A-Za-z0-9._-]+@)?[A-Za-z0-9._-]+", "ssh <target>", text)
    text = re.sub(r"(\b(?:api[_-]?key|token|secret|password|credential|auth[_-]?header)\b\s*[:=]\s*)\S+", r"\1<secret>", text, flags=re.I)
    return text.strip()


def display_path(path: Path, cwd: Path) -> str:
    try:
        return path.resolve().relative_to(cwd).as_posix()
    except ValueError:
        return path.name


def scan_file(path: Path) -> tuple[list[Finding], bool]:
    findings: list[Finding] = []
    has_pattern_hint = False
    text = path.read_text(encoding="utf-8", errors="replace")
    for line_no, line in enumerate(text.splitlines(), start=1):
        if PATTERN_HINTS.search(line):
            has_pattern_hint = True
        for severity, category, pattern in PATTERNS:
            if pattern.search(line):
                findings.append(Finding(path, line_no, severity, category, redact(line)))
    return findings, has_pattern_hint


def classify(findings: list[Finding], has_pattern_hint: bool) -> str:
    if any(f.severity == "high" for f in findings):
        return "private-only"
    if findings:
        return "redactable"
    if has_pattern_hint:
        return "reusable-pattern"
    return "publishable"


def write_report(output: Path, files: list[Path], findings_by_file: dict[Path, list[Finding]], hints_by_file: dict[Path, bool], cwd: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).date().isoformat()
    classifications = {path: classify(findings_by_file[path], hints_by_file[path]) for path in files}
    counts: dict[str, int] = {}
    for label in classifications.values():
        counts[label] = counts.get(label, 0) + 1

    lines = [
        "# Memory Publication Audit",
        "",
        f"- Generated: {generated}",
        f"- Files scanned: {len(files)}",
        f"- Private-only: {counts.get('private-only', 0)}",
        f"- Redactable: {counts.get('redactable', 0)}",
        f"- Publishable: {counts.get('publishable', 0)}",
        f"- Reusable-pattern: {counts.get('reusable-pattern', 0)}",
        "",
        "## Risk Findings",
        "",
        "| File | Line | Severity | Category | Redacted evidence |",
        "|---|---:|---|---|---|",
    ]
    all_findings = [finding for path in files for finding in findings_by_file[path]]
    if not all_findings:
        lines.append("| none |  |  |  | No sensitive patterns detected by deterministic scanner. |")
    for finding in all_findings:
        evidence = html.escape(finding.evidence)
        lines.append(
            f"| `{display_path(finding.path, cwd)}` | {finding.line_no} | {finding.severity} | {finding.category} | `{evidence}` |"
        )

    lines.extend(
        [
            "",
            "## Candidate Classifications",
            "",
            "| File | Classification | Reason | Suggested next step |",
            "|---|---|---|---|",
        ]
    )
    for path in files:
        classification = classifications[path]
        file_findings = findings_by_file[path]
        if any(f.severity == "high" for f in file_findings):
            reason = "Contains high-severity private or secret-like pattern."
            next_step = "Keep private; extract only an abstract sanitized pattern if needed."
        elif file_findings:
            reason = "Contains medium-severity identifiers or paths."
            next_step = "Redact identifiers before drafting public content."
        elif hints_by_file[path]:
            reason = "No sensitive pattern found and reusable workflow language detected."
            next_step = "Review as public skill/doc candidate."
        else:
            reason = "No sensitive pattern found by deterministic scanner."
            next_step = "Human review before publishing."
        lines.append(f"| `{display_path(path, cwd)}` | {classification} | {reason} | {next_step} |")

    lines.extend(
        [
            "",
            "## Reusable Pattern Candidates",
            "",
        ]
    )
    reusable = [path for path, label in classifications.items() if label in {"redactable", "reusable-pattern", "publishable"}]
    if reusable:
        for path in reusable:
            lines.append(f"- `{display_path(path, cwd)}` -> {classifications[path]}")
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Conservative Rule",
            "",
            "When in doubt, keep the raw source private and draft a separate sanitized pattern with placeholders.",
            "",
        ]
    )
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    cwd = Path.cwd().resolve()
    inputs = [Path(item).expanduser().resolve() for item in args.input]
    files = iter_files(inputs, args.max_bytes)
    findings_by_file: dict[Path, list[Finding]] = {}
    hints_by_file: dict[Path, bool] = {}
    for path in files:
        findings, has_hint = scan_file(path)
        findings_by_file[path] = findings
        hints_by_file[path] = has_hint
    output = Path(args.output)
    if not output.is_absolute():
        output = cwd / output
    write_report(output, files, findings_by_file, hints_by_file, cwd)
    print(f"Scanned {len(files)} file(s)")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
