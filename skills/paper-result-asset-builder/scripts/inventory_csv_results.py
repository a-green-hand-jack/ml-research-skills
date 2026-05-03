#!/usr/bin/env python3
"""Inventory CSV result files for paper-facing evidence selection.

This script intentionally uses only the Python standard library. It prints a
Markdown inventory with path, row count, headers, and candidate result columns.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DEFAULT_PATTERNS = (
    "code/docs/results/**/*.csv",
    "code/docs/runs/**/*.csv",
    "code/docs/reports/**/*.csv",
    "code/outputs/**/*.csv",
    "code/results/**/*.csv",
    "outputs/**/*.csv",
    "results/**/*.csv",
    "docs/results/**/*.csv",
    "docs/runs/**/*.csv",
    "docs/reports/**/*.csv",
)

KEY_HINTS = {
    "run",
    "run_id",
    "experiment",
    "experiment_id",
    "method",
    "model",
    "baseline",
    "dataset",
    "task",
    "split",
    "seed",
    "metric",
    "step",
    "epoch",
}

METRIC_HINTS = {
    "acc",
    "accuracy",
    "f1",
    "auc",
    "loss",
    "error",
    "score",
    "bleu",
    "rouge",
    "perplexity",
    "ppl",
    "latency",
    "throughput",
    "memory",
    "flops",
    "time",
}


def iter_csv_paths(root: Path, patterns: tuple[str, ...]) -> list[Path]:
    paths: set[Path] = set()
    for pattern in patterns:
        paths.update(path for path in root.glob(pattern) if path.is_file())
    return sorted(paths)


def inspect_csv(path: Path) -> tuple[int | None, list[str], list[str], list[str], str | None]:
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            headers = list(reader.fieldnames or [])
            row_count = 0
            for row_count, _row in enumerate(reader, start=1):
                pass
    except Exception as exc:  # noqa: BLE001
        return None, [], [], [], str(exc)

    lower_headers = {header: header.lower() for header in headers}
    candidate_keys = [
        header for header, lowered in lower_headers.items()
        if lowered in KEY_HINTS or any(token in lowered for token in ("run", "seed", "method", "dataset", "metric"))
    ]
    candidate_metrics = [
        header for header, lowered in lower_headers.items()
        if lowered in METRIC_HINTS or any(token in lowered for token in METRIC_HINTS)
    ]
    return row_count, headers, candidate_keys, candidate_metrics, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Project root to scan")
    parser.add_argument(
        "--pattern",
        action="append",
        help="Additional glob pattern to scan, relative to root. Can be repeated.",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    patterns = DEFAULT_PATTERNS + tuple(args.pattern or ())
    paths = iter_csv_paths(root, patterns)

    print("# CSV Result Inventory")
    print()
    print(f"- Root: `{root}`")
    print(f"- CSV files found: {len(paths)}")
    print()
    print("| CSV | Rows | Columns | Candidate keys | Candidate metrics | Status |")
    print("|---|---:|---|---|---|---|")

    for path in paths:
        row_count, headers, candidate_keys, candidate_metrics, error = inspect_csv(path)
        rel_path = path.relative_to(root) if path.is_relative_to(root) else path
        if error:
            print(f"| `{rel_path}` |  |  |  |  | error: {error} |")
            continue
        print(
            "| `{}` | {} | {} | {} | {} | ok |".format(
                rel_path,
                row_count if row_count is not None else "",
                ", ".join(headers),
                ", ".join(candidate_keys),
                ", ".join(candidate_metrics),
            )
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
