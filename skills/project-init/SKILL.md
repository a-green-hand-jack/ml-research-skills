---
name: project-init
description: Initialize a full ML research project control root with independent paper, code, and optional slide repositories, shared project memory, root-level agent guidance, code-owned worktree policy, and component handoffs. Use when starting a new research project, setting up a project root for agents, connecting paper/code/slides repos, or replacing a simple paper+code workspace with a lifecycle-aware research project structure.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Project Init Workflow

Initialize a research project as a control root, not just as two sibling repos.

Use this skill when the user wants a new ML research project where agents should work from `<ProjectName>/` while `paper/`, `code/`, and optional `slides/` remain independent component repositories.

Pair this skill with:

- `research-project-memory` to bootstrap cross-component memory
- `init-latex-project` to create the paper repo
- `init-python-project` to create the code repo
- `new-workspace` to create code-owned branches or worktrees
- `remote-project-control` when code runs on SSH/HPC servers
- `safe-git-ops` before non-trivial Git work

## Expected Project Shape

Default shape:

```text
<ProjectName>/
├── PROJECT.md
├── AGENTS.md
├── memory/
│   ├── project.yaml
│   ├── component-index.yaml
│   ├── current-status.md
│   ├── decision-log.md
│   ├── claim-board.md
│   ├── evidence-board.md
│   ├── risk-board.md
│   └── action-board.md
├── paper/                 # independent LaTeX git repo
├── code/                  # independent Python/ML git repo
├── code-worktrees/         # sibling worktree root for code repo branches
├── slides/                # optional independent git repo
├── reviewer/              # reviewer simulation state
├── rebuttal/              # real review and response state
├── artifact/              # artifact-evaluation and release handoff state
└── docs/
    ├── updates/
    ├── audits/
    └── timelines/
```

Do not create a top-level `experiments/` directory by default. Experiment execution, run summaries, result reports, and raw artifact pointers belong inside `code/` or the relevant code worktree.

Recommended code-side evidence paths:

```text
code/docs/results/         # stable result summaries, table notes, figure notes
code/docs/reports/         # experiment-report-writer outputs
code/docs/runs/            # run registry, job pointers, config and commit pointers
```

## Core Principles

- `<ProjectName>/` is the agent control root.
- `paper/`, `code/`, and `slides/` are component repos, not mere folders.
- The code component owns algorithm implementation, experiment execution, run records, result reports, remote execution state, and code worktrees.
- Code worktrees should not be nested inside `code/` by default. Use the sibling root `code-worktrees/` so Git, IDEs, search tools, and agents do not confuse worktrees with normal source files.
- Project memory stores durable cross-component state; code docs store code-side experiment details.
- Root Git is optional. If enabled, do not accidentally commit nested component repos unless the user explicitly wants submodules.

## Step 1 - Gather Project Information

Ask for these fields in one message:

1. Project name and parent directory.
2. Research summary: method idea, target problem, datasets, baselines, metrics, and current maturity.
3. Target venue or milestone, if known.
4. Component choices:
   - paper repo: create new, connect existing, or skip for now
   - code repo: create new, connect existing, or skip for now
   - slides repo: create new, connect existing, or skip
   - reviewer/rebuttal/artifact state dirs: create now or later
5. Git policy:
   - root control-plane git repo: yes/no
   - component remotes for paper/code/slides, if available
   - whether component repos should be submodules or ignored by root Git
6. Code worktree policy:
   - default sibling root: `<ProjectName>/code-worktrees/`
   - remote server worktree root, if different
   - branch naming conventions, if any

Wait for the user's answers before creating files.

## Step 2 - Create the Control Root

Create:

```text
<parent-dir>/<ProjectName>/
├── memory/
├── docs/updates/
├── docs/audits/
├── docs/timelines/
├── reviewer/.agent/
├── rebuttal/.agent/
├── artifact/.agent/
└── code-worktrees/
```

Create optional `slides/` only when the user wants a slides component now.

If root Git is enabled, initialize it at `<ProjectName>/` and add a root `.gitignore` that ignores component repos and worktrees unless the user explicitly wants submodules:

```gitignore
/paper/
/code/
/slides/
/code-worktrees/
```

If the user wants submodules, use submodule commands deliberately rather than relying on accidental nested Git behavior.

## Step 3 - Bootstrap Project Memory

Use `research-project-memory` templates or equivalent files to create:

- `memory/project.yaml`
- `memory/component-index.yaml`
- `memory/current-status.md`
- `memory/decision-log.md`
- `memory/claim-board.md`
- `memory/evidence-board.md`
- `memory/risk-board.md`
- `memory/action-board.md`

The component index should record:

```yaml
components:
  code:
    path: code
    worktree_root: code-worktrees
    owns:
      - algorithm implementation
      - experiment execution
      - code-side result reports
      - remote execution state
  paper:
    path: paper
    owns:
      - paper claims and narrative
      - figures and tables selected for submission
  slides:
    path: slides
    status: optional
  reviewer:
    path: reviewer
  rebuttal:
    path: rebuttal
  artifact:
    path: artifact
```

Root memory should store pointers to code-side evidence, not duplicate detailed run logs.

## Step 4 - Create Root-Level Agent Guidance

Write `<ProjectName>/AGENTS.md`.

It must state:

- agents start from `<ProjectName>/` unless a task is explicitly component-local
- use `git -C code ...`, `git -C paper ...`, and `git -C slides ...` for component repos
- code worktrees live under `code-worktrees/` by default
- experiment results live under `code/docs/results/`, `code/docs/reports/`, `code/docs/runs/`, or the same paths inside a code worktree
- raw outputs, logs, checkpoints, and wandb/tensorboard caches are not project-root artifacts
- project memory gets durable claim/evidence/risk/action summaries
- use `update-docs` during code changes, not only at release time
- use `add-git-tag` for stable code, paper, artifact, or root milestones

## Step 5 - Initialize or Connect Component Repos

### Paper

If creating a new paper repo, use `init-latex-project` at:

```text
<ProjectName>/paper/
```

If connecting an existing paper repo, clone or record its path and remote. Then create `paper/.agent/` if missing.

### Code

If creating a new code repo, use `init-python-project` at:

```text
<ProjectName>/code/
```

For ML projects, ensure the code repo has:

```text
code/docs/results/
code/docs/reports/
code/docs/runs/
```

If connecting an existing code repo, do not force a full scaffold. Add missing high-value memory/docs paths only after reporting gaps.

### Slides

If requested, create or connect:

```text
<ProjectName>/slides/
```

Slides may be a separate git repo. Create `slides/.agent/` for story, audience, and stale-evidence notes.

## Step 6 - Establish Code Worktree Policy

Default policy:

```text
main code repo:       <ProjectName>/code/
code worktree root:   <ProjectName>/code-worktrees/
worktree path:        <ProjectName>/code-worktrees/<branch-type>-<branch-name>/
```

Record this in:

- `memory/project.yaml`
- `memory/component-index.yaml`
- `<ProjectName>/AGENTS.md`
- `code/docs/ops/current-status.md` when remote execution is involved

If the remote server only has the code repo, record the remote-specific worktree root in `code/infra/remote-projects.yaml` or `code/docs/ops/current-status.md`. Do not assume the remote server has `paper/` or root project memory.

## Step 7 - Write PROJECT.md

Create `<ProjectName>/PROJECT.md` with:

```markdown
# <ProjectName>

> <one-line research description>

## Project Control Root

Agents should start from this directory for cross-component work. Component repos are independent.

## Components

| Component | Path | Git | Purpose |
|---|---|---|---|
| paper | `paper/` | independent repo | LaTeX paper and paper-facing claims |
| code | `code/` | independent repo | implementation, experiments, code-side evidence |
| code worktrees | `code-worktrees/` | linked worktrees of code repo | isolated experiments, baselines, rebuttal fixes |
| slides | `slides/` | optional independent repo | talks and advisor/lab presentations |
| reviewer | `reviewer/` | root state dir | simulated reviews and pre-submission risk |
| rebuttal | `rebuttal/` | root state dir | real reviews, responses, promised revisions |
| artifact | `artifact/` | root state dir | artifact evaluation and release handoff |

## Code Evidence Policy

- runnable experiment logic lives in `code/experiments/`
- stable code-side result summaries live in `code/docs/results/`
- experiment reports live in `code/docs/reports/`
- run pointers and job summaries live in `code/docs/runs/`
- raw outputs, logs, checkpoints, and wandb/tensorboard caches stay outside Git or in ignored paths
- paper-facing evidence is promoted through `paper-evidence-board` or `project-sync`

## Worktree Policy

- default root: `code-worktrees/`
- naming: `<branch-type>-<branch-name>`
- every research worktree needs `.agent/worktree-status.md`
- exit condition: merge, continue, park, or kill

## Memory Policy

- project-level durable summaries live in `memory/`
- component details live in `<component>/.agent/`
- code-side run details live in `code/docs/`
- volatile scheduler or job state must be re-verified before action
```

## Step 8 - Final Summary

Report:

```text
Project initialized: <ProjectName>
Control root: <path>

Components:
  paper: <created|connected|skipped>
  code: <created|connected|skipped>
  slides: <created|connected|skipped>
  reviewer/rebuttal/artifact state: <created|deferred>

Code worktree root:
  <ProjectName>/code-worktrees/

Next skills:
  research-project-memory -> inspect or update project state
  new-workspace -> create a code branch/worktree
  remote-project-control -> configure SSH/HPC execution for code
  experiment-design-planner -> plan first experiment matrix
```

## Final Sanity Check

Before finishing:

- root agent guidance exists
- root memory files exist or are explicitly deferred
- `paper/`, `code/`, and `slides/` Git boundaries are clear
- `code-worktrees/` policy is recorded
- there is no top-level `experiments/` directory unless the user explicitly requested it
- code-side evidence paths are inside `code/docs/`
- component remotes and root Git policy are not ambiguous
