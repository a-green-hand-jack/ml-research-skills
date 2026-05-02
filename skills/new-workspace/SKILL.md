---
name: new-workspace
description: Create a new Git branch or code worktree for experiments, features, baselines, rebuttal fixes, or method revisions. Use when starting an isolated code direction, creating a branch, creating a project-aware code worktree under a project control root, or setting up a worktree with UV sync, IDE config copying, linked assets, and worktree memory.
allowed-tools: Read, Write, Bash, Glob
---

# Create New Git Workspace

Create a branch or Git worktree without confusing project-level management with code-repo management.

Use this skill for code, experiment, baseline, feature, or rebuttal branches. In a full research project, the usual target repo is `<ProjectName>/code/`, and worktrees should live under `<ProjectName>/code-worktrees/`.

Pair this skill with:

- `safe-git-ops` for non-trivial Git state, conflicts, or sandbox write failures
- `research-project-memory` to record worktree purpose and exit condition
- `remote-project-control` when the worktree will be used on an SSH/HPC server
- `run-experiment` when the new workspace immediately launches jobs

## Core Principles

- Create worktrees for the code repo, not for the whole project root.
- Prefer sibling code worktrees under `<ProjectName>/code-worktrees/`.
- Avoid nested worktrees inside `code/` unless the user explicitly requires that layout.
- Every research worktree should have a purpose, linked claim/risk/experiment, and exit condition.
- `experiments/` is runnable logic; stable result summaries belong in `docs/results/`, reports in `docs/reports/`, and run pointers in `docs/runs/`.
- Each worktree gets its own `.venv/` after `uv sync`.

## Step 1 - Classify the Target

Ask the user for:

- workspace type: `branch` or `worktree`
- branch type: `feature`, `exp`, `baseline`, `debug`, `rebuttal`, `paper-fix`, or custom
- branch name without prefix
- target repo path, if not obvious
- whether to write worktree memory

If running inside `<ProjectName>/`, prefer the `code/` repo for experiment, baseline, debug, and rebuttal implementation work.

If running inside `<ProjectName>/code/`, infer:

```text
code repo root:      <ProjectName>/code/
project control root: <ProjectName>/
worktree root:      <ProjectName>/code-worktrees/
```

If running inside a standalone code repo, use the fallback worktree root:

```text
<code-repo-parent>/worktrees/
```

## Step 2 - Verify Git State

In the target repo:

```bash
git -C <repo-root> rev-parse --show-toplevel
git -C <repo-root> status --short
git -C <repo-root> branch --show-current
git -C <repo-root> worktree list
```

If there are uncommitted changes, ask whether to commit, stash, continue with a branch only, or cancel.

## Step 3 - Choose Branch Name

Use:

```text
<branch-type>/<branch-name>
```

Examples:

- `exp/new-loss`
- `baseline/fair-tuning`
- `debug/nan-loss`
- `rebuttal/add-ablation`
- `feature/data-loader`

The worktree directory name should be filesystem-friendly:

```text
<branch-type>-<branch-name-with-slashes-replaced-by-hyphens>
```

## Step 4 - Create a Branch

For branch-only work:

```bash
git -C <repo-root> checkout -b <branch-type>/<branch-name>
```

Then update component memory if the branch has a research purpose.

## Step 5 - Create a Worktree

Determine the worktree root:

1. If `<repo-root>` is `<ProjectName>/code/`, use `<ProjectName>/code-worktrees/`.
2. If `<repo-root>/../code-worktrees/` exists, use that.
3. If project memory declares a code worktree root, use that.
4. Otherwise use `<repo-root>/../worktrees/`.

Create the worktree:

```bash
mkdir -p <worktree-root>
git -C <repo-root> worktree add <worktree-root>/<worktree-dir-name> -b <branch-type>/<branch-name>
```

If the branch already exists, ask whether to create the worktree from the existing branch:

```bash
git -C <repo-root> worktree add <worktree-root>/<worktree-dir-name> <branch-type>/<branch-name>
```

## Step 6 - Copy Local Tooling and Link Shared Assets

Copy local IDE/tooling directories when present:

```text
.vscode/
.cursor/
.claude/
```

Copy, do not symlink, because each worktree may need independent IDE state.

If `<repo-root>/.worktree-links` exists, read relative paths from it and symlink shared large assets into the worktree. Typical entries:

```text
data/
models/
.env
configs/local_settings.yaml
```

Use absolute symlink targets so links remain valid from the worktree path.

## Step 7 - Prepare Code-Side Evidence Paths

In the worktree, ensure:

```text
docs/results/
docs/reports/
docs/runs/
.agent/
```

Use these paths for branch-local evidence:

- `docs/results/`: stable result summaries, table notes, figure notes
- `docs/reports/`: experiment reports and result narratives
- `docs/runs/`: job IDs, config paths, commit hashes, remote paths, short metrics
- `.agent/worktree-status.md`: purpose, linked claims/risks, latest reliable state, exit condition

Do not store raw logs, checkpoints, wandb runs, tensorboard caches, or large outputs in `docs/`.

## Step 8 - Sync Environment

If `pyproject.toml` exists in the worktree:

```bash
cd <worktree-path>
uv sync
```

If `uv sync` fails, report the error but do not delete the worktree. The user may still want to inspect or fix the branch.

## Step 9 - Write Worktree Memory

If the workspace has a research purpose, create or update:

```text
<worktree>/.agent/worktree-status.md
```

Include:

- branch
- path
- created date
- parent branch
- purpose
- linked claims, experiments, risks, or reviewer issues
- expected difference from main branch
- result/output paths
- exit condition: merge, continue, park, or kill
- next verification step

If project memory exists, also add a short pointer to:

- `memory/component-index.yaml`: known worktree path
- `memory/action-board.md`: next action for the worktree
- `memory/current-status.md`: only if this is the active focus

## Step 10 - Final Summary

Report:

```text
Workspace created

Repo: <repo-root>
Branch: <branch-type>/<branch-name>
Worktree: <path or branch-only>
Evidence paths:
  docs/results/
  docs/reports/
  docs/runs/
Memory:
  .agent/worktree-status.md <created|skipped>

Next:
  cd <worktree-path>
  uv sync
  run or edit the planned experiment
```

## Error Handling

- Not a Git repo: stop and ask for the target repo.
- Dirty tree: ask whether to commit, stash, continue, or cancel.
- Branch exists: ask whether to use existing branch or choose a new name.
- Worktree path exists: ask whether to choose a new name or inspect existing path.
- Sandbox blocks Git metadata writes: treat as a permission issue and use `safe-git-ops`.
- UV sync fails: keep the worktree and report the environment issue.

## Configuration File Template

If `.worktree-links` does not exist, offer to create:

```text
# .worktree-links
#
# Symlinks to create in new worktrees.
# List paths relative to the code repo root.

# data/
# models/
# .env
# configs/local_settings.yaml
```

## Final Sanity Check

Before finishing:

- branch or worktree was created in the intended code repo
- worktree is not nested inside `code/` unless explicitly requested
- `git worktree list` shows the expected path
- evidence paths exist in the worktree
- worktree memory records purpose and exit condition when relevant
- project memory is updated only with durable pointers, not logs
