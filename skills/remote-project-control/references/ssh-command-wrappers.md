# SSH Command Wrapper Policy

Use this reference when an SSH command contains shell variables, command substitution, pipes, loops, globs, `find`, `awk`, or multi-line logic.

## Problem

This command shape is fragile:

```bash
ssh <host> "cd <repo> && for d in outputs/*; do echo "$d"; find "$d/metrics" -type f | wc -l; done"
```

The outer double quotes let the local shell expand `$d`, `$(...)`, backticks, and some globs before SSH sends the command to the server. The result can silently drop directory names or run a different command from the one intended.

## Default Rule

- Simple command with normal arguments: use `remote-cmd`.
- Project script or multi-line logic: use `remote-bash`.
- Repeated experiment/status checks: create a project wrapper under `scripts/ops/` and call it from `remote-bash` or `run-status-monitor`.
- Avoid complex SSH double-quoted one-liners.

## User-Level Wrappers

Install these scripts into a user-local bin directory when available:

```text
remote-cmd   # simple argv-style remote commands
remote-bash  # remote project scripts or uploaded local scripts
```

The public skill ships reference implementations in `scripts/remote-cmd` and `scripts/remote-bash`. A private workstation may symlink stable copies into `~/.local/bin/`.

## Usage

Simple command:

```bash
remote-cmd <ssh-alias> <remote-repo-root> -- git status --short
```

Remote project script:

```bash
remote-bash <ssh-alias> <remote-repo-root> scripts/ops/count_outputs.sh
```

Upload and run a local script:

```bash
remote-bash --upload <ssh-alias> <remote-repo-root> ./scripts/ops/count_outputs.sh -- --limit 20
```

Dry-run before a risky command:

```bash
remote-cmd --dry-run <ssh-alias> <remote-repo-root> -- bash -lc 'echo "$PWD"'
remote-bash --dry-run <ssh-alias> <remote-repo-root> scripts/ops/status.sh
```

## Wrapper Selection

Use `remote-cmd` only when the remote command can be represented as a command plus arguments. It quotes every argument before sending the command through SSH, so shell metacharacters such as `|` are treated as literal arguments rather than pipelines.

Use `remote-bash` when the task needs shell syntax. Put the shell logic in a script file so variables such as `$d` are expanded only on the server.

If an inline command must use shell syntax, prefer a single-quoted remote shell string and keep it short:

```bash
ssh <ssh-alias> 'cd /path/to/repo && for d in outputs/*; do echo "$d"; done'
```

Do not use this pattern for long logic. Promote long logic to `scripts/ops/<name>.sh`.

## Project Wrapper Pattern

For experiment outputs, make project-local scripts small and read-only:

```bash
#!/usr/bin/env bash
set -euo pipefail

for d in outputs/stage1_sweeps/*; do
  [[ -d "$d" ]] || continue
  printf 'DIR %s\n' "$d"
  find "$d/metrics" -type f 2>/dev/null | wc -l
done
```

Then call:

```bash
remote-bash <ssh-alias> <remote-repo-root> scripts/ops/count_stage1_outputs.sh
```

## Agent Guardrails

- Do not paste long remote scripts into chat when a project wrapper can be created.
- Do not approve a broad SSH prefix only to compensate for fragile quoting.
- Keep private SSH aliases, server paths, and user-specific wrapper locations out of public repo docs.
- If a wrapper command is missing, create or propose the project wrapper instead of falling back to a long one-liner.
