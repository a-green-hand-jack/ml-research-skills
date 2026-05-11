# Run Status Backends

## Recommended Pattern

Use a stable project or private wrapper command whenever possible:

```yaml
runs:
  train-smoke:
    backend: command
    status_command: "project-status train-smoke"
    logs_command: "project-tail train-smoke --lines 120"
```

This lets Codex approve one stable command prefix instead of many backend-specific SSH or scheduler commands.

For SSH-backed projects, prefer user-level wrappers:

```yaml
runs:
  train-smoke:
    backend: command
    status_command: "remote-bash epfl-haas /path/to/project scripts/ops/status_train_smoke.sh"
```

The project wrapper owns loops, `$variables`, `find`, `awk`, and path-specific logic. The status monitor only reads the short summary it emits.

## Backend Types

| Backend | Use for | Required fields |
|---|---|---|
| `local-log` | local nohup/tmux/process logs | `log` |
| `local-process` | PID + optional log | `pid_file` and optional `log` |
| `command` | project/private wrapper output | `status_command` and optional `logs_command` |
| `slurm` | local or SSH SLURM inspection | `job_id`; optional `host`, `log` |
| `runai` | RunAI/Kubernetes inspection | `job`; optional `project`, `host`, `wrapper` |

## Backend Notes

- `local-log`: reads only the last configured lines. Use for local files, tmux/nohup logs, and generated experiment logs.
- `local-process`: checks whether the PID exists and combines that with log markers.
- `command`: safest abstraction for custom projects. The command should already produce concise status or bounded logs.
- `slurm`: uses `squeue`/`sacct` and optional log tail. If `host` is set, the script runs those through SSH.
- `runai`: prefer a private wrapper such as `epfl-runai`. Without a wrapper, the script builds `runai describe job` and `runai logs` commands.

## Progress And Metric Patterns

Configure regexes with named groups:

```yaml
progress_patterns:
  epoch: "epoch (?P<current>\\d+)/(?P<total>\\d+)"
metric_patterns:
  val_loss: "val_loss[=: ]+(?P<value>[0-9.eE+-]+)"
  accuracy: "acc(?:uracy)?[=: ]+(?P<value>[0-9.eE+-]+)"
```

For ETA, the script needs:

- `started_at`, or
- a log file with a parseable modification/update time plus progress with `current` and `total`.

ETA is heuristic. Treat it as operational guidance, not evidence.

## Context Hygiene

- Do not paste raw probe output into chat.
- Do not store full logs in `docs/`.
- Keep raw captures under `.agent/run-status/raw/` only when needed and usually ignored.
- Promote durable findings to `experiment-report-writer` or `result-diagnosis` only after the run reaches a meaningful checkpoint.
