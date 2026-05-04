#!/usr/bin/env python3
"""Prepare a fresh-context code review bundle.

The bundle is intended to be handed to an independent reviewer agent without
sharing the writer's conversation context.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


REVIEW_TEMPLATE = """# Code Review: {change_id}

- Reviewer:
- Date:
- Base: {base_label}
- Head: {head_label}
- Scope:
- Verdict: request changes | acceptable with nits | approve

## Summary

Briefly state what was reviewed and the highest-risk area.

## Findings

### High

None.

### Medium

None.

### Low

None.

## Missing Tests

List tests that should exist before this change is trusted.

## Design Risks

List risks that are not immediate bugs but may affect future work.

## Verification Notes

Commands inspected or run, and any limits of the review.
"""


FIX_LOG_TEMPLATE = """# Review Fix Log: {change_id}

- Writer:
- Date:
- Review file: `.agent/code-reviews/{change_id}/review.md`

## Response Summary

Briefly summarize what changed after review.

## Findings Response

| Finding | Action | Evidence | Status |
|---|---|---|---|
|  |  |  | fixed / deferred / rejected |

## Tests Rerun

```text
<commands and results>
```

## Deferred Items

Record any intentionally deferred review items and why they are out of scope.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository path.")
    parser.add_argument("--output-root", default=".agent/code-reviews", help="Review bundle root.")
    parser.add_argument("--change-id", help="Stable review id. Defaults to timestamp plus HEAD short sha.")
    parser.add_argument("--base", default="main", help="Base ref for committed changes.")
    parser.add_argument("--head", default="HEAD", help="Head ref for committed changes.")
    parser.add_argument("--working-tree", action="store_true", help="Use working tree diff instead of base...head.")
    parser.add_argument("--staged", action="store_true", help="Use staged diff instead of base...head.")
    parser.add_argument("--request", help="Task contract text.")
    parser.add_argument("--request-file", help="Read task contract from this file.")
    parser.add_argument("--writer-summary", help="Writer summary text.")
    parser.add_argument("--writer-summary-file", help="Read writer summary from this file.")
    parser.add_argument("--test-output-file", help="Copy test output from this file.")
    return parser.parse_args()


def run_git(repo: Path, args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        capture_output=True,
        check=check,
    )


def git_output(repo: Path, args: list[str], default: str = "") -> str:
    proc = run_git(repo, args, check=False)
    if proc.returncode != 0:
        return default
    return proc.stdout.strip()


def read_text_arg(text: str | None, file_path: str | None, repo: Path, fallback: str) -> str:
    if file_path:
        path = Path(file_path)
        if not path.is_absolute():
            path = repo / path
        return path.read_text(encoding="utf-8").strip() + "\n"
    if text:
        return text.strip() + "\n"
    return fallback


def default_change_id(repo: Path) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    short_head = git_output(repo, ["rev-parse", "--short", "HEAD"], default="nohead")
    return f"{timestamp}-{short_head}"


def collect_diff(repo: Path, args: argparse.Namespace) -> tuple[str, str, str]:
    if args.working_tree and args.staged:
        raise SystemExit("--working-tree and --staged are mutually exclusive")

    if args.working_tree:
        stat = git_output(repo, ["diff", "--stat"], default="")
        patch = git_output(repo, ["diff", "--binary"], default="")
        return "working-tree", "working-tree", f"{stat}\n\n{patch}".strip() + "\n"

    if args.staged:
        stat = git_output(repo, ["diff", "--cached", "--stat"], default="")
        patch = git_output(repo, ["diff", "--cached", "--binary"], default="")
        return "index", "staged", f"{stat}\n\n{patch}".strip() + "\n"

    base = args.base
    head = args.head
    stat = git_output(repo, ["diff", "--stat", f"{base}...{head}"], default="")
    patch = git_output(repo, ["diff", "--binary", f"{base}...{head}"], default="")
    if not patch and not stat:
        stat = git_output(repo, ["diff", "--stat", f"{base}..{head}"], default="")
        patch = git_output(repo, ["diff", "--binary", f"{base}..{head}"], default="")
    return base, head, f"{stat}\n\n{patch}".strip() + "\n"


def write_file(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    repo = Path(args.repo).expanduser().resolve()
    git_root_text = git_output(repo, ["rev-parse", "--show-toplevel"])
    if not git_root_text:
        print(f"Not a git repository: {repo}", file=sys.stderr)
        return 2
    repo = Path(git_root_text)

    change_id = args.change_id or default_change_id(repo)
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = repo / output_root
    bundle = output_root / change_id
    bundle.mkdir(parents=True, exist_ok=False)

    base_label, head_label, diff_text = collect_diff(repo, args)
    request_text = read_text_arg(
        args.request,
        args.request_file,
        repo,
        "# Request\n\nTODO: Add original task contract and acceptance criteria.\n",
    )
    summary_text = read_text_arg(
        args.writer_summary,
        args.writer_summary_file,
        repo,
        "# Writer Summary\n\nTODO: Summarize files changed, tests run, and known risks.\n",
    )

    test_output = "No test output provided.\n"
    if args.test_output_file:
        test_source = Path(args.test_output_file)
        if not test_source.is_absolute():
            test_source = repo / test_source
        test_output = test_source.read_text(encoding="utf-8")

    head_sha = git_output(repo, ["rev-parse", "HEAD"], default="")
    status = git_output(repo, ["status", "--short", "--branch"], default="")
    created_at = datetime.now(timezone.utc).isoformat()

    metadata = "\n".join(
        [
            f"# Review Bundle: {change_id}",
            "",
            f"- Created at: {created_at}",
            f"- Repo: `{repo}`",
            f"- Base: `{base_label}`",
            f"- Head: `{head_label}`",
            f"- HEAD SHA: `{head_sha}`",
            "",
            "## Git Status",
            "",
            "```text",
            status,
            "```",
            "",
        ]
    )

    reviewer_prompt = f"""You are the code-reviewer.

Review only the bundle at `{bundle.relative_to(repo)}/`.
Do not modify production code.

Read:
- `request.md`
- `writer-summary.md`
- `diff.patch`
- `test-output.md`

Open only source files needed to verify the diff. Do not use the writer's chat context.
Write findings to `{bundle.relative_to(repo)}/review.md`.

Prioritize correctness, edge cases, tests, design risk, and maintainability.
Use severity High / Medium / Low.
End with verdict: request changes, acceptable with nits, or approve.
"""

    write_file(bundle / "metadata.md", metadata)
    write_file(bundle / "request.md", request_text)
    write_file(bundle / "writer-summary.md", summary_text)
    write_file(bundle / "diff.patch", diff_text or "No diff captured.\n")
    write_file(bundle / "test-output.md", test_output)
    write_file(bundle / "reviewer-prompt.md", reviewer_prompt)
    write_file(bundle / "review.md", REVIEW_TEMPLATE.format(change_id=change_id, base_label=base_label, head_label=head_label))
    write_file(bundle / "fix-log.md", FIX_LOG_TEMPLATE.format(change_id=change_id))

    if args.test_output_file:
        source = Path(args.test_output_file)
        if not source.is_absolute():
            source = repo / source
        if source.exists():
            shutil.copy2(source, bundle / "test-output.raw.txt")

    print(bundle.relative_to(repo))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
