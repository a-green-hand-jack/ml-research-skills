#!/usr/bin/env python3
"""Audit LaTeX citation keys, BibTeX entries, labels, and refs.

This script intentionally stays stdlib-only. It performs deterministic local
checks and leaves DOI/metadata/claim verification to the host agent.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


CITE_COMMAND_RE = re.compile(
    r"\\(?:cite|citet|citep|citealp|citealt|citeauthor|citeyear|citeyearpar|"
    r"citeposs|textcite|parencite|footcite|autocite|supercite)\*?"
    r"(?:\s*\[[^\]]*\])*"
    r"\s*\{([^{}]+)\}",
    re.DOTALL,
)
REF_COMMAND_RE = re.compile(
    r"\\(?:ref|pageref|eqref|autoref|cref|Cref|vref|Vref)\*?"
    r"(?:\s*\[[^\]]*\])*"
    r"\s*\{([^{}]+)\}",
    re.DOTALL,
)
LABEL_RE = re.compile(r"\\label\s*\{([^{}]+)\}")
INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^{}]+)\}")
BIBLIOGRAPHY_RE = re.compile(r"\\bibliography\s*\{([^{}]+)\}")
ADDBIBRESOURCE_RE = re.compile(r"\\addbibresource(?:\s*\[[^\]]*\])?\s*\{([^{}]+)\}")
BIB_ENTRY_RE = re.compile(r"@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)


@dataclass
class Occurrence:
    key: str
    file: str
    line: int
    context: str


@dataclass
class Audit:
    paper_dir: str
    main_tex: str
    tex_files: list[str] = field(default_factory=list)
    bib_files: list[str] = field(default_factory=list)
    missing_bib_files: list[str] = field(default_factory=list)
    citation_occurrences: list[Occurrence] = field(default_factory=list)
    ref_occurrences: list[Occurrence] = field(default_factory=list)
    label_occurrences: list[Occurrence] = field(default_factory=list)
    bib_entries: dict[str, list[str]] = field(default_factory=dict)
    issues: list[dict[str, str]] = field(default_factory=list)
    warnings: list[dict[str, str]] = field(default_factory=list)


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        out = []
        escaped = False
        for char in line:
            if char == "\\" and not escaped:
                escaped = True
                out.append(char)
                continue
            if char == "%" and not escaped:
                break
            out.append(char)
            escaped = False
        lines.append("".join(out))
    return "\n".join(lines)


def line_no(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def context_line(text: str, pos: int) -> str:
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    if end == -1:
        end = len(text)
    return re.sub(r"\s+", " ", text[start:end]).strip()


def split_keys(raw: str) -> list[str]:
    return [part.strip() for part in raw.replace("\n", " ").split(",") if part.strip()]


def resolve_tex_path(base: Path, raw: str) -> Path:
    candidate = (base / raw).expanduser()
    if candidate.suffix:
        return candidate
    return candidate.with_suffix(".tex")


def discover_tex_files(main: Path) -> list[Path]:
    seen: set[Path] = set()
    ordered: list[Path] = []

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in seen or not path.exists():
            return
        seen.add(path)
        ordered.append(path)
        text = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
        for match in INPUT_RE.finditer(text):
            child = resolve_tex_path(path.parent, match.group(1).strip())
            visit(child)

    visit(main)
    return ordered


def bib_paths_from_tex(tex_files: Iterable[Path], paper_dir: Path) -> tuple[list[Path], list[str]]:
    paths: list[Path] = []
    missing: list[str] = []
    seen: set[Path] = set()
    for tex_file in tex_files:
        text = strip_comments(tex_file.read_text(encoding="utf-8", errors="replace"))
        raw_paths: list[str] = []
        for match in BIBLIOGRAPHY_RE.finditer(text):
            raw_paths.extend(split_keys(match.group(1)))
        for match in ADDBIBRESOURCE_RE.finditer(text):
            raw_paths.append(match.group(1).strip())
        for raw in raw_paths:
            candidate = (tex_file.parent / raw).expanduser()
            if not candidate.suffix:
                candidate = candidate.with_suffix(".bib")
            if not candidate.exists():
                alt = paper_dir / candidate.name
                if alt.exists():
                    candidate = alt
            if candidate.exists():
                resolved = candidate.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    paths.append(resolved)
            else:
                missing.append(raw)
    if not paths:
        default_paths = sorted(paper_dir.glob("**/*.bib"))
        for path in default_paths:
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                paths.append(resolved)
    return paths, missing


def collect_occurrences(tex_files: Iterable[Path], root: Path) -> tuple[list[Occurrence], list[Occurrence], list[Occurrence]]:
    cites: list[Occurrence] = []
    refs: list[Occurrence] = []
    labels: list[Occurrence] = []
    for tex_file in tex_files:
        raw = tex_file.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        rel = str(tex_file.relative_to(root)) if tex_file.is_relative_to(root) else str(tex_file)
        for match in CITE_COMMAND_RE.finditer(text):
            for key in split_keys(match.group(1)):
                cites.append(Occurrence(key, rel, line_no(text, match.start()), context_line(text, match.start())))
        for match in REF_COMMAND_RE.finditer(text):
            for key in split_keys(match.group(1)):
                refs.append(Occurrence(key, rel, line_no(text, match.start()), context_line(text, match.start())))
        for match in LABEL_RE.finditer(text):
            labels.append(Occurrence(match.group(1).strip(), rel, line_no(text, match.start()), context_line(text, match.start())))
    return cites, refs, labels


def collect_bib_entries(bib_files: Iterable[Path], root: Path) -> dict[str, list[str]]:
    entries: dict[str, list[str]] = {}
    for bib_file in bib_files:
        text = bib_file.read_text(encoding="utf-8", errors="replace")
        rel = str(bib_file.relative_to(root)) if bib_file.is_relative_to(root) else str(bib_file)
        for match in BIB_ENTRY_RE.finditer(text):
            key = match.group(2).strip()
            entries.setdefault(key, []).append(f"{rel}:{line_no(text, match.start())}")
    return entries


def add_issue(audit: Audit, severity: str, kind: str, message: str, location: str = "") -> None:
    target = audit.issues if severity == "blocking" else audit.warnings
    target.append({"severity": severity, "kind": kind, "message": message, "location": location})


def run_audit(paper_dir: Path, main_tex: Path) -> Audit:
    root = paper_dir.resolve()
    main = main_tex if main_tex.is_absolute() else root / main_tex
    main = main.resolve()
    audit = Audit(paper_dir=str(root), main_tex=str(main))

    if not main.exists():
        add_issue(audit, "blocking", "missing_main_tex", f"Main TeX file does not exist: {main}")
        return audit

    tex_files = discover_tex_files(main)
    audit.tex_files = [str(path.relative_to(root)) if path.is_relative_to(root) else str(path) for path in tex_files]

    bib_files, missing_bibs = bib_paths_from_tex(tex_files, root)
    audit.bib_files = [str(path.relative_to(root)) if path.is_relative_to(root) else str(path) for path in bib_files]
    audit.missing_bib_files = missing_bibs
    for raw in missing_bibs:
        add_issue(audit, "blocking", "missing_bib_file", f"Bibliography file referenced but not found: {raw}")

    cites, refs, labels = collect_occurrences(tex_files, root)
    audit.citation_occurrences = cites
    audit.ref_occurrences = refs
    audit.label_occurrences = labels
    audit.bib_entries = collect_bib_entries(bib_files, root)

    cited_keys = {item.key for item in cites}
    bib_keys = set(audit.bib_entries)
    label_keys = [item.key for item in labels]
    label_set = set(label_keys)
    ref_keys = {item.key for item in refs}

    for key in sorted(cited_keys - bib_keys):
        occ = next(item for item in cites if item.key == key)
        add_issue(audit, "blocking", "missing_bib_entry", f"Cited key `{key}` has no BibTeX entry.", f"{occ.file}:{occ.line}")

    for key, locations in sorted(audit.bib_entries.items()):
        if len(locations) > 1:
            add_issue(audit, "blocking", "duplicate_bib_key", f"BibTeX key `{key}` appears {len(locations)} times.", ", ".join(locations))

    for key in sorted(bib_keys - cited_keys):
        add_issue(audit, "warning", "unused_bib_entry", f"BibTeX key `{key}` is not cited in TeX.", "; ".join(audit.bib_entries[key]))

    seen_labels: dict[str, list[Occurrence]] = {}
    for occ in labels:
        seen_labels.setdefault(occ.key, []).append(occ)
    for key, occurrences in sorted(seen_labels.items()):
        if len(occurrences) > 1:
            add_issue(
                audit,
                "blocking",
                "duplicate_label",
                f"Label `{key}` appears {len(occurrences)} times.",
                ", ".join(f"{occ.file}:{occ.line}" for occ in occurrences),
            )

    for key in sorted(ref_keys - label_set):
        occ = next(item for item in refs if item.key == key)
        add_issue(audit, "blocking", "undefined_ref", f"Reference `{key}` has no matching label.", f"{occ.file}:{occ.line}")

    for key in sorted(label_set - ref_keys):
        occ = next(item for item in labels if item.key == key)
        add_issue(audit, "warning", "unreferenced_label", f"Label `{key}` is never referenced.", f"{occ.file}:{occ.line}")

    for tex_file in tex_files:
        text = strip_comments(tex_file.read_text(encoding="utf-8", errors="replace"))
        rel = str(tex_file.relative_to(root)) if tex_file.is_relative_to(root) else str(tex_file)
        for marker in ("??", "[?]", "Citation?"):
            pos = text.find(marker)
            if pos != -1:
                add_issue(audit, "warning", "unresolved_placeholder", f"Possible unresolved placeholder `{marker}`.", f"{rel}:{line_no(text, pos)}")

    return audit


def print_text_report(audit: Audit) -> None:
    print("# Citation Audit")
    print(f"Paper root: {audit.paper_dir}")
    print(f"Main TeX: {audit.main_tex}")
    print(f"TeX files: {len(audit.tex_files)}")
    print(f"BibTeX files: {len(audit.bib_files)}")
    print(f"Cited keys: {len({item.key for item in audit.citation_occurrences})}")
    print(f"BibTeX entries: {len(audit.bib_entries)}")
    print(f"Labels: {len({item.key for item in audit.label_occurrences})}")
    print(f"Refs: {len({item.key for item in audit.ref_occurrences})}")
    print()

    if not audit.issues and not audit.warnings:
        print("Status: PASS")
        return

    print(f"Blocking issues: {len(audit.issues)}")
    for issue in audit.issues:
        loc = f" ({issue['location']})" if issue.get("location") else ""
        print(f"- [{issue['kind']}] {issue['message']}{loc}")

    print()
    print(f"Warnings: {len(audit.warnings)}")
    for warning in audit.warnings:
        loc = f" ({warning['location']})" if warning.get("location") else ""
        print(f"- [{warning['kind']}] {warning['message']}{loc}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit LaTeX citation keys, BibTeX entries, labels, and refs.")
    parser.add_argument("--paper-dir", default=".", help="Paper root directory.")
    parser.add_argument("--main", default="main.tex", help="Main TeX file, relative to paper dir unless absolute.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text report.")
    args = parser.parse_args()

    audit = run_audit(Path(args.paper_dir), Path(args.main))
    if args.json:
        print(json.dumps(audit, default=lambda obj: obj.__dict__, indent=2, sort_keys=True))
    else:
        print_text_report(audit)
    return 1 if audit.issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
