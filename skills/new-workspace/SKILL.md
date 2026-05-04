---
name: new-workspace
description: Create a new Git branch or worktree for code experiments, features, baselines, rebuttal fixes, method revisions, paper venue versions, arXiv releases, or camera-ready paper versions. Use when starting an isolated code direction, creating a project-aware code worktree under code-worktrees, creating a paper version worktree under paper-worktrees, or setting up worktree memory.
allowed-tools: Read, Write, Bash, Glob
---

# Create New Git Workspace

Create a branch or Git worktree without confusing project-level management with component-repo management.

Use this skill for:

- code, experiment, baseline, feature, debug, or rebuttal implementation branches
- paper venue branches such as NeurIPS, ICML, ICLR, CVPR, ACL, or EMNLP submissions
- arXiv paper releases
- camera-ready paper versions

In a full research project, code worktrees should live under `<ProjectName>/code-worktrees/`, and paper worktrees should live under `<ProjectName>/paper-worktrees/`.

Pair this skill with:

- `safe-git-ops` for non-trivial Git state, conflicts, or sandbox write failures
- `research-project-memory` to record worktree purpose and exit condition
- `remote-project-control` when a code worktree will be used on an SSH/HPC server
- `run-experiment` when the new workspace immediately launches jobs
- `submit-paper` when a paper worktree is for a submission, arXiv, or camera-ready version
- `camera-ready-finalizer` when a paper worktree is for an accepted version

## Core Principles

- Create worktrees for component repos, not for the whole project root.
- Prefer sibling code worktrees under `<ProjectName>/code-worktrees/`.
- Prefer sibling paper worktrees under `<ProjectName>/paper-worktrees/`.
- Avoid nested worktrees inside `code/` or `paper/` unless the user explicitly requires that layout.
- Every research worktree should have a purpose, linked claim/risk/experiment, and exit condition.
- Paper worktrees should also record target venue/version, submission mode, template/style differences, cleanup requirements, and source-visibility assumptions.
- Paper source visibility is independent of venue. A paper worktree may be `agent-private`, `author-visible`, `anonymous-submission`, `public-preprint`, `camera-ready-public`, or `publisher-artifact`.
- `experiments/` is runnable logic; stable result summaries belong in `docs/results/`, reports in `docs/reports/`, and run pointers in `docs/runs/`.
- Code worktrees get their own `.venv/` after `uv sync`. Paper worktrees do not need a local TeX install by default; Overleaf/GitHub compile may be the source of truth.

## Step 1 - Classify the Target

Ask the user for:

- workspace type: `branch` or `worktree`
- component: `code` or `paper`
- branch type:
  - code: `feature`, `exp`, `baseline`, `debug`, `rebuttal`, or custom
  - paper: `venue`, `submission`, `arxiv`, `camera-ready`, `rebuttal`, `paper-fix`, or custom
- branch name without prefix
- target repo path, if not obvious
- for paper workspaces: source visibility tier, audience, sync target, and cleanup gate
- whether to write worktree memory

If running inside `<ProjectName>/`, prefer the `code/` repo for experiment, baseline, debug, and rebuttal implementation work.
Prefer the `paper/` repo for venue retargeting, arXiv releases, camera-ready versions, source cleanup, paper-only rebuttal edits, or submission formatting.

If running inside `<ProjectName>/code/`, infer:

```text
code repo root:      <ProjectName>/code/
project control root: <ProjectName>/
worktree root:      <ProjectName>/code-worktrees/
```

If running inside `<ProjectName>/paper/`, infer:

```text
paper repo root:      <ProjectName>/paper/
project control root: <ProjectName>/
worktree root:        <ProjectName>/paper-worktrees/
```

If running inside a standalone code repo, use the fallback worktree root:

```text
<code-repo-parent>/worktrees/
```

If running inside a standalone paper repo, use the fallback worktree root:

```text
<paper-repo-parent>/paper-worktrees/
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
- `venue/neurips`
- `venue/icml`
- `arxiv/v1`
- `camera-ready/neurips`
- `private/draft`
- `overleaf/main-clean`

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

For code:

1. If `<repo-root>` is `<ProjectName>/code/`, use `<ProjectName>/code-worktrees/`.
2. If `<repo-root>/../code-worktrees/` exists, use that.
3. If project memory declares a code worktree root, use that.
4. Otherwise use `<repo-root>/../worktrees/`.

For paper:

1. If `<repo-root>` is `<ProjectName>/paper/`, use `<ProjectName>/paper-worktrees/`.
2. If `<repo-root>/../paper-worktrees/` exists, use that.
3. If project memory declares a paper worktree root, use that.
4. Otherwise use `<repo-root>/../paper-worktrees/`.

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

## Step 7 - Prepare Component-Specific Paths

### Code Worktrees

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

### Paper Worktrees

In a paper worktree, ensure:

```text
.agent/
```

Create or update `.agent/worktree-status.md` with paper-version fields:

- target venue or release: NeurIPS, ICML, ICLR, CVPR, ACL, EMNLP, arXiv, camera-ready
- submission mode: anonymous, preprint, camera-ready, rebuttal, or internal
- style/template differences from main paper
- source visibility tier:
  - `agent-private`: may contain `.agent/`, `AGENTS.md`, `CLAUDE.md`, writing memory, provenance notes, internal result docs, CSVs, and plotting scripts; should not sync to Overleaf/public remotes
  - `author-visible`: coauthor/Overleaf-visible; must exclude `.agent/`, `AGENTS.md`, `CLAUDE.md`, raw CSVs, internal docs, plotting scripts, reviewer strategy, and private paths
  - `anonymous-submission`: venue/source-upload-visible; must enforce anonymity and exclude agent/private files
  - `public-preprint`: arXiv/public source; must be public-clean
  - `camera-ready-public`: final accepted public/publisher source; must be de-anonymized and public-clean
  - `publisher-artifact`: final public source plus artifact/release-facing files only
- audience and sync target: none, Overleaf-GitHub, GitHub, submission-system, arXiv, publisher, or artifact
- allowed paths and forbidden paths
- cleanup gate: before-push, before-submission, before-arxiv, before-camera-ready, or before-release
- cleanup requirements:
  - arXiv/public source: remove TODOs, author comments, reviewer notes, internal figure/table descriptions in TeX comments, hidden notes, and anonymization leftovers
  - author-visible / Overleaf: remove or avoid `.agent/`, `AGENTS.md`, `CLAUDE.md`, raw CSVs, internal result docs, plotting scripts, private paths, and agent-only notes
  - conference anonymous: enforce anonymity and venue format; source comments may still be risky if the source is uploaded, so do not rely on them
  - camera-ready: de-anonymize, add acknowledgements/funding, close rebuttal promises, and remove draft-only notes
- Overleaf/GitHub compile status and branch mapping, if used

Do not copy code-side `docs/results/`, `docs/reports/`, or `docs/runs/` conventions into paper worktrees unless the user explicitly wants paper-local notes. Prefer `.agent/` for paper-version memory and root `memory/` for durable cross-version state.

## Step 8 - Sync Environment

For code worktrees, if `pyproject.toml` exists in the worktree:

```bash
cd <worktree-path>
uv sync
```

If `uv sync` fails, report the error but do not delete the worktree. The user may still want to inspect or fix the branch.

For paper worktrees, do not install TeX by default. Use the project's compile workflow: local static checks plus GitHub-linked Overleaf unless the user explicitly wants local TeX.

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
- for paper worktrees: target venue/version, template/style differences, source cleanup policy, and public/private source assumptions
- for paper worktrees: source visibility tier, audience, sync target, allowed/forbidden file policy, and cleanup gate
- result/output paths
- exit condition: merge, continue, park, or kill
- next verification step

If project memory exists, also add a short pointer to:

- `memory/component-index.yaml`: known worktree path
- `<component>/.agent/worktree-index.md`: component-local active worktree rollup
- `memory/source-visibility-board.md`: source visibility tier and cleanup gate for paper worktrees or visible branches
- `memory/action-board.md`: next action for the worktree
- `memory/current-status.md`: only if this is the active focus

The root registry and component worktree index are the cross-worktree memory surfaces. Do not rely on one worktree's leaf status file to tell future agents what other sibling branches or paper versions exist.

## Step 10 - Final Summary

Report:

```text
Workspace created

Repo: <repo-root>
Branch: <branch-type>/<branch-name>
Worktree: <path or branch-only>
Evidence paths:
  <code worktree only: docs/results/, docs/reports/, docs/runs/>
Memory:
  .agent/worktree-status.md <created|skipped>

Next:
  cd <worktree-path>
  <code: uv sync and run/edit the planned experiment>
  <paper: run submit-paper checks and sync to Overleaf/GitHub if needed>
```

## Error Handling

- Not a Git repo: stop and ask for the target repo.
- Dirty tree: ask whether to commit, stash, continue, or cancel.
- Branch exists: ask whether to use existing branch or choose a new name.
- Worktree path exists: ask whether to choose a new name or inspect existing path.
- Sandbox blocks Git metadata writes: treat as a permission issue and use `safe-git-ops`.
- UV sync fails: keep the worktree and report the environment issue.
- Paper compile unavailable locally: do not install TeX by default; route through Overleaf/GitHub.

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

- branch or worktree was created in the intended component repo
- worktree is not nested inside `code/` or `paper/` unless explicitly requested
- `git worktree list` shows the expected path
- code evidence paths exist for code worktrees
- paper version policy is recorded for paper worktrees
- paper source visibility policy is recorded for paper worktrees, especially Overleaf/coauthor-visible and public-source branches
- worktree memory records purpose and exit condition when relevant
- project memory is updated only with durable pointers, not logs
