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

For scheduler/API authentication failures, use a circuit breaker:

- Treat OAuth/session refresh errors such as `invalid_grant`, `failed to refresh token`, missing client/session, or browser verification prompts as API auth blockage, not job failure.
- Do not repeatedly call `describe`, `logs`, or `list` after the first auth failure in the same monitoring turn.
- Switch to SSH filesystem checks, bounded project wrappers, or known output/status files when available.
- The status artifact should record `API monitoring blocked; login refresh required` and name one recovery action, not paste repeated auth output.

For pending jobs, include scheduler events or pending reasons when the backend can provide them. The status artifact should say whether the pending reason appears to be resource capacity, quota/fair-share, CPU or memory request, image pull, `ContainerCreating`, environment startup, or unknown. Do not treat a pending scheduler state as a code failure unless logs or events show the job actually started and failed.

For Kubernetes/RunAI jobs, `ContainerCreating`, long image pulls, and `ImagePullBackOff` are node/image startup issues unless the job has reached user code. For smoke/debug runs, recommend rerouting to a compatible pool or node family with lower startup overhead when the image pull consumes the smoke budget.

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

## Polling Policy

- The main agent should not be the long-lived observer for active experiments. Avoid transcript-visible loops such as repeated `sleep`, `describe`, `logs`, and filesystem checks unless the user explicitly asks for an inline live watch.
- One bounded probe is enough for an immediate answer. If the answer is "still running; check later", schedule or run a bounded monitor that writes/updates the status artifact instead of keeping raw observations in the main context.
- For multi-job or noisy runs, prefer a project wrapper that emits a compact state line per job plus paths to checkpoints/summaries. If interpretation is needed, use a sidecar task over bounded raw captures and have the main agent read only the sidecar/status artifact.
- Choose check cadence from expected signal, not impatience: short intervals only while waiting for startup failures or first output, longer intervals during known long forward/backward phases, and no agent polling when no new artifact can plausibly appear before the next human-visible milestone.
- The artifact should capture the next useful check condition, such as "first checkpoint exists", "summary file written", "scheduler terminal state", or "auth refreshed", so later agents can resume without replaying the polling history.
