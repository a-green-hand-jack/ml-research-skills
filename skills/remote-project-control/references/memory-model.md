# Memory Model

Use this skill's memory system to recover project context quickly across many coding-agent sessions without confusing long-lived facts with short-lived runtime state.

## The Four Layers

### 1. Stable Shared Memory

File: `infra/remote-projects.yaml`

This is the source of truth for facts that should survive many sessions and can usually be committed to git:

- project name
- local repo root
- default git remote and branch
- remote server names and SSH aliases
- remote repo roots
- scheduler type and default launch modes
- environment activation command
- shared data, checkpoint, scratch, and logs roots
- workflow and safety policies

This file should stay structured. Prefer YAML fields over prose.

### 2. Working Shared Memory

File: `docs/ops/current-status.md`

This is the current working state of the project. It is useful across sessions, but it is not fully authoritative:

- current focus
- active branch
- latest known synced commit
- latest known running or recent job
- open issues
- next planned step

Use prose and short bullets here. Keep it readable for both humans and agents.

### 3. Durable Rationale

File: `docs/ops/decision-log.md`

Record stable workflow decisions and why they exist:

- why one server is the default
- why jobs must go through `sbatch` instead of direct execution
- why checkpoints live on a certain filesystem
- why a repo uses one environment activation method

Use this when a future session would otherwise repeat the same investigation.

### 4. Private Local Overrides

File: `.agent/local-overrides.yaml`

This file is usually private and should often be gitignored. It stores user-specific or machine-specific values:

- a personal SSH alias
- a username override
- private scratch paths
- machine-local notes that should not be committed

## Merge Strategy

Treat the layers differently:

- `infra/remote-projects.yaml` is the structured baseline
- `.agent/local-overrides.yaml` may override private machine-specific fields
- `docs/ops/current-status.md` provides advisory working context
- live command results override all volatile assumptions

For execution-critical facts, use this precedence:

1. Live verification
2. `.agent/local-overrides.yaml`
3. `infra/remote-projects.yaml`
4. `docs/ops/current-status.md`

For narrative context, use:

1. `docs/ops/current-status.md`
2. `docs/ops/decision-log.md`

## What Must Be Re-verified

Never trust these purely from memory:

- current local dirty state
- current remote dirty state
- remote branch or commit
- active or queued jobs
- whether a checkpoint exists
- whether a log file exists
- whether a scheduler command is currently available

Re-check them before acting.

## What Should Be Written Back

Write back only after information becomes dependable:

- stable config changes -> `infra/remote-projects.yaml`
- current session outcomes -> `docs/ops/current-status.md`
- workflow rationale -> `docs/ops/decision-log.md`
- private machine facts -> `.agent/local-overrides.yaml`

Do not let one-off observations pollute the stable manifest.
