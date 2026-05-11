---
name: run-status-monitor
description: Monitor running experiments without polluting the main agent context. Use when the user asks where an experiment is, what intermediate results exist, whether a job is stuck, or how long it may take across local logs, local processes, SSH servers, SLURM, RunAI, tmux/nohup, or project-specific status wrappers.
argument-hint: "[run-id] [--config .agent/run-status/runs.yaml] [--output docs/ops/runs/<run-id>-status.md]"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Run Status Monitor

Answer lightweight operational questions about active runs while keeping raw logs out of the main conversation.

Use this skill for:

- "现在实验进行到哪里了？"
- "有什么中间结果？"
- "预计还要多久结束？"
- "这个 job 是卡住了还是还在跑？"

Do not paste long scheduler output or training logs into chat. Probe, compress, write a short status artifact, and report only the summary.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── scripts/
│   └── run_status_probe.py
├── references/
│   └── backends.md
└── templates/
    ├── runs.yaml
    └── status.md
```

## Core Contract

- Raw logs stay in their original location or private `.agent/` run artifacts.
- The main agent reads only a short generated status artifact.
- Prefer project/private wrapper commands for server-specific probes. For SSH-backed status checks, prefer `remote-cmd` for simple commands and `remote-bash` for project scripts or any command containing loops, `$variables`, command substitution, pipes, globs, `find`, or `awk`.
- Use `sidecar-task-runner` only when summarizing noisy status output would otherwise consume main context.
- If a run appears failed, stale, or scientifically surprising, route to `result-diagnosis` after creating the status artifact.

## Expected Project Layout

```text
.agent/run-status/
├── runs.yaml              # project-local run monitor config, private if it contains hosts/paths
└── raw/                   # optional raw probe captures, ignored/private

docs/ops/runs/
└── <run-id>-status.md     # short status artifact safe for main-agent reading
```

## Workflow

1. Locate project root.
2. Read `references/backends.md`.
3. Locate run config in this order:
   - user-provided `--config`
   - `.agent/run-status/runs.yaml`
   - `docs/ops/runs.yaml`
   - `infra/remote-projects.yaml` plus project-specific notes
4. Run the probe script when a config exists:

```bash
python3 <installed-skill-dir>/scripts/run_status_probe.py \
  --config .agent/run-status/runs.yaml \
  --run <run-id>
```

5. If no config exists, create one from `templates/runs.yaml` with the minimum backend fields and ask only for missing run identity fields.
6. Read only the generated `status_artifact`, not raw logs, before answering the user.
7. Update `docs/ops/current-status.md` or project memory only when the status changes durable project state.

## Output Rules

Every user-facing answer should fit this shape:

```text
Run: <id>
State: running | pending | succeeded | failed | stale | unknown
Progress: <short>
Latest metrics: <short>
Last update: <time or unknown>
ETA: <estimate or unknown>
Risk: <short>
Artifact: <status artifact path>
```

Escalate when:

- the run is failed/stale
- metrics are surprising
- logs show repeated exceptions, OOM, NaN, or checkpoint failures
- ETA cannot be estimated because progress markers are absent
- the probe command needs network/server approval
