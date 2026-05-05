#!/usr/bin/env python3
"""Prepare an artifact directory for a one-shot sidecar agent task."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository path.")
    parser.add_argument("--output-root", default=".agent/sidecars", help="Sidecar artifact root.")
    parser.add_argument("--task-id", help="Stable task id. Defaults to timestamp plus title slug.")
    parser.add_argument("--title", required=True, help="Short task title.")
    parser.add_argument("--phase", default="tooling", help="Project lifecycle phase label.")
    parser.add_argument("--task-type", default="audit", help="Task type label.")
    parser.add_argument("--model", default="gpt-5.3-codex-spark", help="Sidecar model id.")
    parser.add_argument("--sandbox", default="read-only", choices=("read-only", "workspace-write"))
    parser.add_argument("--prompt", help="Prompt text.")
    parser.add_argument("--prompt-file", help="Read prompt text from this file.")
    parser.add_argument(
        "--input",
        action="append",
        default=[],
        help="Input path, command, diff, or artifact the sidecar may inspect. Repeatable.",
    )
    return parser.parse_args()


def run_git(repo: Path, args: list[str]) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        return ""
    return proc.stdout.strip()


def resolve_repo(path: str) -> Path:
    repo = Path(path).expanduser().resolve()
    root = run_git(repo, ["rev-parse", "--show-toplevel"])
    if root:
        return Path(root)
    return repo


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return slug[:48] or "sidecar-task"


def default_task_id(title: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{stamp}-{slugify(title)}"


def read_prompt(args: argparse.Namespace, repo: Path) -> str:
    if args.prompt_file:
        path = Path(args.prompt_file)
        if not path.is_absolute():
            path = repo / path
        return path.read_text(encoding="utf-8").strip() + "\n"
    if args.prompt:
        return args.prompt.strip() + "\n"
    return (
        f"# Sidecar Task: {args.title}\n\n"
        "TODO: Replace this with a bounded task prompt before launching the sidecar.\n"
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    repo = resolve_repo(args.repo)
    task_id = args.task_id or default_task_id(args.title)

    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = repo / output_root
    task_dir = output_root / task_id
    task_dir.mkdir(parents=True, exist_ok=False)

    created_at = datetime.now(timezone.utc).isoformat()
    prompt = read_prompt(args, repo)
    status = run_git(repo, ["status", "--short", "--branch"])
    head = run_git(repo, ["rev-parse", "HEAD"])
    branch = run_git(repo, ["branch", "--show-current"])

    manifest_lines = [
        f"# Sidecar Input Manifest: {task_id}",
        "",
        f"- Created at: {created_at}",
        f"- Repo: `{repo}`",
        f"- Title: {args.title}",
        f"- Phase: {args.phase}",
        f"- Task type: {args.task_type}",
        f"- HEAD: `{head}`",
        f"- Branch: `{branch}`",
        "",
        "## Allowed Inputs",
        "",
    ]
    if args.input:
        manifest_lines.extend(f"- {item}" for item in args.input)
    else:
        manifest_lines.append("- Prompt-defined repository files and read-only git inspection.")
    manifest_lines.extend(["", "## Git Status", "", "```text", status, "```", ""])

    command_task_dir = task_dir.relative_to(repo) if task_dir.is_relative_to(repo) else task_dir
    command_task_dir_text = str(command_task_dir)
    command = (
        "codex exec --ephemeral "
        f"-m {args.model} "
        "-C . "
        f"-s {args.sandbox} "
        f"-o {command_task_dir_text}/output.md "
        f"\"$(cat {command_task_dir_text}/prompt.md)\""
    )

    model_payload = {
        "task_id": task_id,
        "created_at": created_at,
        "runner": "codex-cli",
        "model_provider": "openai",
        "model": args.model,
        "sandbox": args.sandbox,
        "repo": str(repo),
        "phase": args.phase,
        "task_type": args.task_type,
        "command": command,
        "usage": {
            "input_tokens": None,
            "cached_input_tokens": None,
            "output_tokens": None,
            "reasoning_output_tokens": None,
            "total_tokens": None,
        },
    }

    model_md = "\n".join(
        [
            f"# Sidecar Model: {task_id}",
            "",
            f"- Runner: codex-cli",
            f"- Model: `{args.model}`",
            f"- Sandbox: `{args.sandbox}`",
            f"- Created at: {created_at}",
            "",
            "## Launch Command",
            "",
            "```bash",
            command,
            "```",
            "",
            "## Token Usage",
            "",
            "Token usage: unavailable until copied from the Codex CLI run output.",
            "",
        ]
    )

    decision = "\n".join(
        [
            f"# Main-Agent Decision: {task_id}",
            "",
            "- Decision: accept | partially accept | reject | escalate",
            "- Decider:",
            "- Date:",
            "",
            "## Rationale",
            "",
            "Record how the main agent used the sidecar output and what was ignored.",
            "",
            "## Follow-Up",
            "",
            "- ",
            "",
        ]
    )

    write_text(task_dir / "prompt.md", prompt)
    write_text(task_dir / "input-manifest.md", "\n".join(manifest_lines))
    write_text(task_dir / "output.md", "")
    write_text(task_dir / "findings.md", "# Sidecar Findings\n\n")
    write_text(task_dir / "decision.md", decision)
    write_text(task_dir / "model.md", model_md)
    write_text(task_dir / "model.json", json.dumps(model_payload, indent=2, sort_keys=True) + "\n")

    rel = task_dir.relative_to(repo) if task_dir.is_relative_to(repo) else task_dir
    print(f"Prepared sidecar task: {rel}")
    print(command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
