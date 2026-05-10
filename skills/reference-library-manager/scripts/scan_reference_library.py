#!/usr/bin/env python3
"""Scan a project reference source library and write index/status files."""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".pdf": "paper-or-pdf",
    ".doc": "collaborator-doc",
    ".docx": "collaborator-doc",
    ".md": "markdown",
    ".markdown": "markdown",
    ".txt": "text-note",
    ".bib": "bibliography",
    ".tex": "latex-source",
    ".py": "script",
    ".sh": "script",
    ".ipynb": "notebook",
    ".yaml": "config-or-spec",
    ".yml": "config-or-spec",
    ".json": "config-or-spec",
}

EXCLUDED_DIR_NAMES = {".agent", "cards", "project-use", "summaries", "notes"}


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    source_type: str
    rel_path: str
    size_bytes: int
    sha256: str
    updated: str
    item_count: int = 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=".", help="Project control root.")
    parser.add_argument("--reference-dir", default="reference", help="Reference/source directory path.")
    parser.add_argument("--hash-bytes", type=int, default=0, help="Hash only the first N bytes; 0 hashes full files.")
    return parser.parse_args()


def slugify(text: str) -> str:
    stem = re.sub(r"\.[A-Za-z0-9]+$", "", text)
    stem = re.sub(r"[^A-Za-z0-9]+", "-", stem.lower()).strip("-")
    return stem[:80] or "source"


def sha256_file(path: Path, limit: int = 0) -> str:
    digest = hashlib.sha256()
    remaining = limit
    with path.open("rb") as handle:
        while True:
            read_size = 1024 * 1024
            if limit and remaining <= 0:
                break
            if limit:
                read_size = min(read_size, remaining)
            chunk = handle.read(read_size)
            if not chunk:
                break
            digest.update(chunk)
            if limit:
                remaining -= len(chunk)
    return digest.hexdigest()


def human_size(size: int) -> str:
    value = float(size)
    for unit in ("B", "K", "M", "G"):
        if value < 1024 or unit == "G":
            if unit == "B":
                return f"{int(value)}B"
            return f"{value:.1f}{unit}"
        value /= 1024
    return f"{value:.1f}G"


def source_type_for_file(path: Path) -> str:
    return SUPPORTED_EXTENSIONS.get(path.suffix.lower(), "file")


def should_skip(path: Path, reference_dir: Path) -> bool:
    rel_parts = path.relative_to(reference_dir).parts
    if any(part in EXCLUDED_DIR_NAMES for part in rel_parts):
        return True
    return any(part.startswith(".") and part != "." for part in rel_parts)


def source_roots(reference_dir: Path) -> list[Path]:
    roots: list[Path] = []
    sources_dir = reference_dir / "sources"
    papers_dir = reference_dir / "papers"
    if sources_dir.exists():
        roots.append(sources_dir)
    if papers_dir.exists():
        roots.append(papers_dir)
    if roots:
        return roots
    return [reference_dir]


def directory_digest(path: Path, hash_bytes: int) -> tuple[int, int, str, str]:
    digest = hashlib.sha256()
    size = 0
    count = 0
    latest_mtime = 0.0
    for child in sorted(p for p in path.rglob("*") if p.is_file()):
        if ".agent" in child.parts:
            continue
        stat = child.stat()
        count += 1
        size += stat.st_size
        latest_mtime = max(latest_mtime, stat.st_mtime)
        digest.update(child.relative_to(path).as_posix().encode("utf-8"))
        digest.update(sha256_file(child, hash_bytes).encode("ascii"))
    updated = datetime.fromtimestamp(latest_mtime or path.stat().st_mtime, timezone.utc).date().isoformat()
    return count, size, digest.hexdigest(), updated


def add_record(
    records: list[SourceRecord],
    used_ids: dict[str, int],
    *,
    source_type: str,
    source_path: Path,
    project_root: Path,
    size_bytes: int,
    sha256: str,
    updated: str,
    item_count: int = 1,
) -> None:
    rel = source_path.relative_to(project_root).as_posix()
    base_id = slugify(source_path.name)
    count = used_ids.get(base_id, 0)
    used_ids[base_id] = count + 1
    source_id = base_id if count == 0 else f"{base_id}-{count + 1}"
    records.append(
        SourceRecord(
            source_id=source_id,
            source_type=source_type,
            rel_path=rel,
            size_bytes=size_bytes,
            sha256=sha256,
            updated=updated,
            item_count=item_count,
        )
    )


def scan(project_root: Path, reference_dir: Path, hash_bytes: int) -> list[SourceRecord]:
    records: list[SourceRecord] = []
    used_ids: dict[str, int] = {}
    seen_files: set[Path] = set()

    bundle_root = reference_dir / "sources" / "bundles"
    if bundle_root.exists():
        for bundle in sorted(p for p in bundle_root.iterdir() if p.is_dir()):
            if should_skip(bundle, reference_dir):
                continue
            item_count, size, digest, updated = directory_digest(bundle, hash_bytes)
            add_record(
                records,
                used_ids,
                source_type="bundle",
                source_path=bundle,
                project_root=project_root,
                size_bytes=size,
                sha256=digest,
                updated=updated,
                item_count=item_count,
            )
            seen_files.update(p.resolve() for p in bundle.rglob("*") if p.is_file())

    for root in source_roots(reference_dir):
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            if path.resolve() in seen_files:
                continue
            if should_skip(path, reference_dir):
                continue
            if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue
            stat = path.stat()
            add_record(
                records,
                used_ids,
                source_type=source_type_for_file(path),
                source_path=path,
                project_root=project_root,
                size_bytes=stat.st_size,
                sha256=sha256_file(path, hash_bytes),
                updated=datetime.fromtimestamp(stat.st_mtime, timezone.utc).date().isoformat(),
            )
    return sorted(records, key=lambda record: record.rel_path)


def write_index(reference_dir: Path, records: list[SourceRecord]) -> None:
    agent_dir = reference_dir / ".agent"
    agent_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).date().isoformat()
    lines = [
        "# Source Index",
        "",
        "Generated by `reference-library-manager`. Keep paths project-relative.",
        "",
        "| Source ID | Type | Path | Items | Size | SHA256 | Metadata status | Roles | Processing state | Card | Project use | Updated |",
        "|---|---|---|---:|---:|---|---|---|---|---|---|---|",
    ]
    for record in records:
        short_hash = record.sha256[:12]
        card = f"reference/cards/{record.source_id}.md"
        project_use = f"reference/project-use/{record.source_id}.md"
        lines.append(
            f"| `{record.source_id}` | {record.source_type} | `{record.rel_path}` | {record.item_count} | {human_size(record.size_bytes)} | `{short_hash}` | missing |  | unread | `{card}` | `{project_use}` | {record.updated} |"
        )
    lines.extend(["", f"- Last scan: {today}", f"- Source count: {len(records)}", ""])
    text = "\n".join(lines)
    (agent_dir / "source-index.md").write_text(text, encoding="utf-8")
    (agent_dir / "reference-index.md").write_text(text.replace("# Source Index", "# Reference Index"), encoding="utf-8")


def write_status(reference_dir: Path, records: list[SourceRecord]) -> None:
    agent_dir = reference_dir / ".agent"
    today = datetime.now(timezone.utc).date().isoformat()
    lines = [
        "# Source Processing Status",
        "",
        "| Source ID | Type | Priority | Roles | Processing mode | State | Owner | Next action | Updated |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| `{record.source_id}` | {record.source_type} | skim |  | skim | unread | agent | create source card if relevant | {today} |"
        )
    lines.append("")
    text = "\n".join(lines)
    (agent_dir / "processing-status.md").write_text(text, encoding="utf-8")
    (agent_dir / "reading-status.md").write_text(text.replace("# Source Processing Status", "# Reference Reading Status"), encoding="utf-8")


def write_gaps(reference_dir: Path, records: list[SourceRecord]) -> None:
    agent_dir = reference_dir / ".agent"
    lines = ["# Metadata Gaps", "", "| Source ID | Type | Missing fields | Suggested action |", "|---|---|---|---|"]
    for record in records:
        if record.source_type == "paper-or-pdf":
            missing = "title, authors, year, venue"
        elif record.source_type == "bundle":
            missing = "bundle purpose, owner, source roles"
        else:
            missing = "title/purpose, owner/origin, source roles"
        lines.append(f"| `{record.source_id}` | {record.source_type} | {missing} | verify metadata during source-card creation |")
    lines.append("")
    (agent_dir / "metadata-gaps.md").write_text("\n".join(lines), encoding="utf-8")


def write_duplicates(reference_dir: Path, records: list[SourceRecord]) -> None:
    agent_dir = reference_dir / ".agent"
    by_hash: dict[str, list[SourceRecord]] = {}
    for record in records:
        by_hash.setdefault(record.sha256, []).append(record)
    lines = ["# Duplicate Check", "", "| SHA256 | Files |", "|---|---|"]
    duplicates = 0
    for digest, items in sorted(by_hash.items()):
        if len(items) < 2:
            continue
        duplicates += 1
        files = "<br>".join(f"`{item.rel_path}`" for item in items)
        lines.append(f"| `{digest[:12]}` | {files} |")
    if duplicates == 0:
        lines.append("| none | No exact duplicate sources found. |")
    lines.append("")
    (agent_dir / "duplicate-check.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    reference_dir = Path(args.reference_dir)
    if not reference_dir.is_absolute():
        reference_dir = project_root / reference_dir
    reference_dir.mkdir(parents=True, exist_ok=True)
    (reference_dir / "sources").mkdir(exist_ok=True)
    (reference_dir / "papers").mkdir(exist_ok=True)
    (reference_dir / "cards").mkdir(exist_ok=True)
    (reference_dir / "project-use").mkdir(exist_ok=True)
    (reference_dir / "summaries").mkdir(exist_ok=True)
    (reference_dir / "notes").mkdir(exist_ok=True)
    (reference_dir / ".agent" / "runs").mkdir(parents=True, exist_ok=True)

    records = scan(project_root, reference_dir, args.hash_bytes)
    write_index(reference_dir, records)
    write_status(reference_dir, records)
    write_gaps(reference_dir, records)
    write_duplicates(reference_dir, records)
    print(f"Scanned {len(records)} source(s) under {reference_dir}")
    print(f"Wrote {reference_dir / '.agent' / 'source-index.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
