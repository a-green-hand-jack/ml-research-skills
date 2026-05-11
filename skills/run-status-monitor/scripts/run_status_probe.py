#!/usr/bin/env python3
"""Probe experiment status and write a short status artifact."""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_CONFIGS = (
    ".agent/run-status/runs.yaml",
    ".agent/run-status/runs.json",
    "docs/ops/runs.yaml",
    "docs/ops/runs.json",
)


@dataclass(frozen=True)
class CommandResult:
    command: str
    returncode: int
    output: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", help="Run monitor config path.")
    parser.add_argument("--run", required=True, help="Run ID from config.")
    parser.add_argument("--project-root", default=".", help="Project root.")
    parser.add_argument("--output", help="Override status artifact path.")
    parser.add_argument("--tail-lines", type=int, help="Override log tail lines.")
    parser.add_argument("--timeout", type=int, default=20, help="Command timeout in seconds.")
    return parser.parse_args()


def load_config(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        parsed = json.loads(text)
    else:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise SystemExit(f"YAML config requires PyYAML, or use JSON: {path}") from exc
        parsed = yaml.safe_load(text)
    if not isinstance(parsed, dict):
        raise SystemExit(f"Config must be a mapping: {path}")
    return parsed


def find_config(project_root: Path, explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser()
        return path if path.is_absolute() else project_root / path
    for candidate in DEFAULT_CONFIGS:
        path = project_root / candidate
        if path.exists():
            return path
    raise SystemExit("No run status config found. Create .agent/run-status/runs.yaml from the skill template.")


def resolve_path(project_root: Path, value: str | None) -> Path | None:
    if not value:
        return None
    path = Path(value).expanduser()
    return path if path.is_absolute() else project_root / path


def tail_text(path: Path, lines: int) -> tuple[str, str]:
    if not path.exists():
        return "", "missing"
    text = path.read_text(encoding="utf-8", errors="replace")
    parts = text.splitlines()
    return "\n".join(parts[-lines:]), datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def run_command(command: str, timeout: int) -> CommandResult:
    try:
        proc = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        output = "\n".join(part for part in (proc.stdout.strip(), proc.stderr.strip()) if part)
        return CommandResult(command, proc.returncode, output)
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or "") + "\n" + (exc.stderr or "")
        return CommandResult(command, 124, output.strip() or f"timeout after {timeout}s")


def ssh_wrap(host: str, command: str) -> str:
    return f"ssh {shlex.quote(host)} {shlex.quote(command)}"


def backend_commands(run: dict[str, Any]) -> tuple[str | None, str | None]:
    backend = run.get("backend", "local-log")
    if backend == "command":
        return run.get("status_command"), run.get("logs_command")
    if backend == "slurm":
        job_id = str(run.get("job_id", ""))
        if not job_id:
            raise SystemExit("slurm backend requires job_id")
        status = f"squeue -j {shlex.quote(job_id)} -o '%.18i %.9T %.10M %.6D %R'; sacct -j {shlex.quote(job_id)} --format=JobID,State,Elapsed,AllocGRES -n 2>/dev/null || true"
        log = run.get("log")
        logs = f"tail -n {int(run.get('tail_lines', 120))} {shlex.quote(log)}" if log else None
        host = run.get("host")
        if host:
            status = ssh_wrap(str(host), status)
            logs = ssh_wrap(str(host), logs) if logs else None
        return status, logs
    if backend == "runai":
        job = str(run.get("job", ""))
        if not job:
            raise SystemExit("runai backend requires job")
        project = run.get("project")
        wrapper = run.get("wrapper")
        if wrapper:
            status = f"{shlex.quote(str(wrapper))} describe {shlex.quote(job)} --lines {int(run.get('describe_lines', 160))}"
            logs = f"{shlex.quote(str(wrapper))} logs {shlex.quote(job)} --lines {int(run.get('tail_lines', 120))}"
        else:
            project_flag = f" -p {shlex.quote(str(project))}" if project else ""
            status = f"runai describe job {shlex.quote(job)}{project_flag}"
            logs = f"runai logs {shlex.quote(job)}{project_flag} | tail -n {int(run.get('tail_lines', 120))}"
        host = run.get("host")
        if host and not wrapper:
            status = ssh_wrap(str(host), status)
            logs = ssh_wrap(str(host), logs)
        return status, logs
    return None, None


def check_pid(pid_file: Path | None) -> tuple[str, str]:
    if not pid_file or not pid_file.exists():
        return "unknown", "pid file missing"
    raw = pid_file.read_text(encoding="utf-8").strip()
    try:
        pid = int(raw)
        os.kill(pid, 0)
        return "running", f"pid {pid} exists"
    except (ValueError, ProcessLookupError):
        return "failed", f"pid {raw} not running"
    except PermissionError:
        return "running", f"pid {raw} exists but permission is limited"


def newest_match(patterns: dict[str, str], text: str) -> dict[str, str]:
    results: dict[str, str] = {}
    for name, pattern_text in patterns.items():
        pattern = re.compile(pattern_text, re.IGNORECASE)
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        match = matches[-1]
        if "value" in match.groupdict():
            results[name] = match.group("value")
        elif "current" in match.groupdict() and "total" in match.groupdict():
            results[name] = f"{match.group('current')}/{match.group('total')}"
        else:
            results[name] = match.group(0)
    return results


def infer_state(run: dict[str, Any], backend: str, text: str, command_results: list[CommandResult], pid_state: str = "unknown") -> tuple[str, str]:
    lower = text.lower()
    if any(token in lower for token in ("traceback", "exception", "error", "failed", "oom", "out of memory", "nan")):
        return "failed", "failure marker found in recent output"
    if any(token in lower for token in ("succeeded", "completed", "finished", "done")):
        return "succeeded", "completion marker found"
    if backend == "local-process" and pid_state != "unknown":
        return pid_state, "pid check"
    if any(result.returncode == 124 for result in command_results):
        return "unknown", "probe command timed out"
    if any(result.returncode != 0 for result in command_results):
        return "unknown", "probe command returned nonzero"
    if text.strip():
        return "running", "recent output exists"
    return "unknown", "no output available"


def estimate_eta(progress: dict[str, str], run: dict[str, Any]) -> str:
    for value in progress.values():
        if "/" not in value:
            continue
        current_text, total_text = value.split("/", 1)
        try:
            current = float(current_text)
            total = float(total_text)
        except ValueError:
            continue
        if current <= 0 or total <= current:
            return "unknown"
        started_at = run.get("started_at")
        if not started_at:
            return "unknown; progress has total but no started_at"
        try:
            start = datetime.fromisoformat(str(started_at).replace("Z", "+00:00"))
        except ValueError:
            return "unknown; started_at is not ISO-like"
        now = datetime.now(start.tzinfo or timezone.utc)
        elapsed = (now - start).total_seconds()
        if elapsed <= 0:
            return "unknown"
        remaining = elapsed * (total - current) / current
        hours = remaining / 3600
        if hours >= 1:
            return f"~{hours:.1f}h"
        return f"~{remaining / 60:.0f}m"
    return "unknown"


def write_status(
    output: Path,
    run_id: str,
    backend: str,
    state: str,
    progress: dict[str, str],
    metrics: dict[str, str],
    last_update: str,
    eta: str,
    risk: str,
    commands: list[CommandResult],
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).isoformat()
    progress_text = ", ".join(f"{k}={v}" for k, v in progress.items()) or "unknown"
    metrics_text = ", ".join(f"{k}={v}" for k, v in metrics.items()) or "none detected"
    lines = [
        f"# Run Status: {run_id}",
        "",
        f"- Generated: {generated}",
        f"- Backend: {backend}",
        f"- State: {state}",
        f"- Progress: {progress_text}",
        f"- Latest metrics: {metrics_text}",
        f"- Last update: {last_update}",
        f"- ETA: {eta}",
        f"- Risk: {risk}",
        "",
        "## Probe Summary",
        "",
    ]
    if commands:
        for index, result in enumerate(commands, start=1):
            lines.append(f"- probe-{index} -> exit {result.returncode}")
    else:
        lines.append("- local file/process probe")
    lines.extend(
        [
            "",
            "## Raw Context Policy",
            "",
            "- Raw scheduler output and logs are not copied here.",
            "- This file is the short artifact the main agent should read.",
            "",
        ]
    )
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    config_path = find_config(project_root, args.config)
    config = load_config(config_path)
    runs = config.get("runs", {})
    if args.run not in runs:
        raise SystemExit(f"Run not found in config: {args.run}")
    run = runs[args.run] or {}
    backend = run.get("backend", "local-log")
    tail_lines = args.tail_lines or int(run.get("tail_lines", 120))
    output = resolve_path(project_root, args.output or run.get("status_artifact") or f"docs/ops/runs/{args.run}-status.md")
    assert output is not None

    log_text = ""
    last_update = "unknown"
    command_results: list[CommandResult] = []
    pid_state = "unknown"

    if backend in {"local-log", "local-process"}:
        log_path = resolve_path(project_root, run.get("log"))
        if log_path:
            log_text, last_update = tail_text(log_path, tail_lines)
        if backend == "local-process":
            pid_state, pid_note = check_pid(resolve_path(project_root, run.get("pid_file")))
            log_text = f"{pid_note}\n{log_text}"
    else:
        status_command, logs_command = backend_commands(run)
        for command in (status_command, logs_command):
            if not command:
                continue
            result = run_command(command, args.timeout)
            command_results.append(result)
            log_text += "\n" + result.output
        last_update = datetime.now(timezone.utc).isoformat()

    progress = newest_match(run.get("progress_patterns", {}) or {}, log_text)
    metrics = newest_match(run.get("metric_patterns", {}) or {}, log_text)
    state, risk = infer_state(run, backend, log_text, command_results, pid_state)
    eta = estimate_eta(progress, run)
    write_status(output, args.run, backend, state, progress, metrics, last_update, eta, risk, command_results)
    print(f"Run: {args.run}")
    print(f"State: {state}")
    print(f"Progress: {', '.join(f'{k}={v}' for k, v in progress.items()) or 'unknown'}")
    print(f"Latest metrics: {', '.join(f'{k}={v}' for k, v in metrics.items()) or 'none detected'}")
    print(f"ETA: {eta}")
    print(f"Artifact: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
