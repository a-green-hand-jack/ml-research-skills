---
name: project-init
description: Initialize a full ML research project control root with independent paper, code, and optional slide repositories, shared project memory, root project docs, root-level agent guidance, code and paper worktree policies, and component handoffs. Use when starting a new research project, setting up a project root for agents, connecting paper/code/slides repos, or replacing a simple paper+code workspace with a lifecycle-aware research project structure.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Project Init Workflow

Initialize a research project as a control root, not just as two sibling repos.

Use this skill when the user wants a new ML research project where agents should work from `<ProjectName>/` while `paper/`, `code/`, and optional `slides/` remain independent component repositories.

Pair this skill with:

- `research-project-memory` to bootstrap cross-component memory
- `init-latex-project` to create the paper repo
- `init-python-project` to create the code repo
- `research-slide-deck-builder` to create or maintain the optional slides repo using the external `progress-slides` template
- `new-workspace` to create code experiment worktrees or paper version worktrees
- `remote-project-control` when code runs on SSH/HPC servers
- `safe-git-ops` before non-trivial Git work

## Expected Project Shape

Default shape:

```text
<ProjectName>/
├── PROJECT.md
├── AGENTS.md
├── CLAUDE.md
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
├── paper-worktrees/        # sibling worktree root for paper venue/arXiv/camera-ready versions
├── slides/                # optional independent git repo
├── reviewer/              # reviewer simulation state
├── rebuttal/              # real review and response state
├── artifact/              # artifact-evaluation and release handoff state
└── docs/
    ├── overview.md
    ├── designs/
    ├── experiments/
    ├── updates/
    ├── audits/
    └── timelines/
```

Do not create a top-level `experiments/` directory by default. Experiment execution, run summaries, result reports, and raw artifact pointers belong inside `code/` or the relevant code worktree.

Root-level `docs/` is still useful, but it is project-level documentation, not a replacement for code-side evidence. Use it for staged method designs, cross-component experiment plans, project overviews, audits, timelines, and handoffs that coordinate `paper/`, `code/`, `slides/`, review, rebuttal, and artifact work.

Recommended code-side evidence paths:

```text
code/docs/results/         # stable result summaries, table notes, figure notes
code/docs/reports/         # experiment-report-writer outputs
code/docs/runs/            # run registry, job pointers, config and commit pointers
```

## Core Principles

- `<ProjectName>/` is the agent control root.
- `paper/`, `code/`, and `slides/` are component repos, not mere folders.
- The code component owns algorithm implementation, experiment execution, run records, result reports, server execution state, and code worktrees.
- Code worktrees should not be nested inside `code/` by default. Use the sibling root `code-worktrees/` so Git, IDEs, search tools, and agents do not confuse worktrees with normal source files.
- The paper component owns paper source, venue templates, submission modes, arXiv/public-source cleanup, camera-ready revisions, and paper worktrees.
- Paper worktrees should not be nested inside `paper/` by default. Use the sibling root `paper-worktrees/` for venue retargeting, arXiv releases, rebuttal paper edits, and camera-ready branches.
- Project memory stores durable cross-component state; root `docs/` stores project-level design and planning artifacts; code docs store code-side implementation, run, and result details.
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
   - whether GitHub/GitLab repos should be created now, and if so whether `gh auth status` is valid
6. Worktree policy:
   - default sibling root: `<ProjectName>/code-worktrees/`
   - default paper sibling root: `<ProjectName>/paper-worktrees/`
   - server worktree root, if different
   - branch naming conventions, if any

Wait for the user's answers before creating files.

## Step 2 - Create the Control Root

Create:

```text
<parent-dir>/<ProjectName>/
├── memory/
├── docs/overview.md
├── docs/designs/
├── docs/experiments/
├── docs/updates/
├── docs/audits/
├── docs/timelines/
├── reviewer/.agent/
├── rebuttal/.agent/
├── artifact/.agent/
├── code-worktrees/
└── paper-worktrees/
```

Create optional `slides/` only when the user wants a slides component now.

If root Git is enabled, initialize it at `<ProjectName>/` and add a root `.gitignore` that ignores component repos and worktrees unless the user explicitly wants submodules:

```gitignore
/paper/
/code/
/slides/
/code-worktrees/
/paper-worktrees/
```

If the user wants submodules, use submodule commands deliberately rather than relying on accidental nested Git behavior.

If the user wants GitHub/GitLab repositories created during setup, first check the hosting CLI authentication such as `gh auth status`. If authentication fails, finish the local workspace setup and record Git remote creation as a blocker; do not let repo creation failure obscure the project initialization result.

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
    worktree_index_path: code/.agent/worktree-index.md
    owns:
      - algorithm implementation
      - experiment execution
      - code-side result reports
      - server execution state
  paper:
    path: paper
    worktree_root: paper-worktrees
    worktree_index_path: paper/.agent/worktree-index.md
    owns:
      - paper claims and narrative
      - figures and tables selected for submission
      - venue/arXiv/camera-ready versions
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

Write both root agent entrypoints:

- `<ProjectName>/AGENTS.md` for Codex and universal agent guidance
- `<ProjectName>/CLAUDE.md` for Claude Code compatibility

They should stay semantically aligned. Prefer either mirrored content or a short `CLAUDE.md` that tells Claude Code to follow `AGENTS.md` as the canonical project-control-root policy.

The root guidance must state:

- agents start from `<ProjectName>/` unless a task is explicitly component-local
- use `git -C code ...`, `git -C paper ...`, and `git -C slides ...` for component repos
- code worktrees live under `code-worktrees/` by default
- paper worktrees live under `paper-worktrees/` by default for venue, arXiv, and camera-ready versions
- root `docs/` is for project-level overviews, staged method designs, cross-component experiment plans, audits, timelines, and handoffs
- `code/docs/` is for code-side result summaries, run records, implementation reports, and server execution notes
- experiment results live under `code/docs/results/`, `code/docs/reports/`, `code/docs/runs/`, or the same paths inside a code worktree
- raw outputs, logs, checkpoints, and wandb/tensorboard caches are not project-root artifacts
- paper version notes live in the relevant paper worktree `.agent/worktree-status.md` and durable decisions live in root `memory/`
- cross-worktree rollups live in `code/.agent/worktree-index.md`, `paper/.agent/worktree-index.md`, and root `memory/component-index.yaml`
- arXiv/public-source paper worktrees must remove TODOs, internal comments, hidden figure/table descriptions, reviewer-response notes, and author-comment macros before source release
- anonymous conference paper worktrees must enforce venue anonymity and formatting rules
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

Ensure the paper repo has both `paper/AGENTS.md` and `paper/CLAUDE.md` when agents will edit it. `AGENTS.md` is the universal/Codex entrypoint; `CLAUDE.md` is the Claude Code entrypoint. Keep them aligned with the same paper-local compile, venue, source hygiene, figure, table, and memory rules.

### Code

If creating a new code repo, use `init-python-project` at:

```text
<ProjectName>/code/
```

For ML projects, ensure the code repo has:

```text
code/AGENTS.md
code/CLAUDE.md
code/docs/results/
code/docs/reports/
code/docs/runs/
```

If connecting an existing code repo, do not force a full scaffold. Add missing high-value memory/docs paths only after reporting gaps.

When the code repo is cloned from an upstream project, do not assume `origin` is writable. Record whether `origin` is upstream, a fork, or a newly created project repo, and keep it separate from the root control-plane repo remote.

### Slides

If requested, create or connect:

```text
<ProjectName>/slides/
```

Slides may be a separate git repo. Prefer using the external `progress-slides` template as the slides component instead of inventing a local scaffold:

```bash
git clone https://github.com/a-green-hand-jack/progress-slides.git <ProjectName>/slides
```

After cloning, inspect `slides/README.md`, `slides/package.json`, and the existing slide source files before editing. Use `research-slide-deck-builder` for deck structure, template-compatible source writing, preview/build commands, and `slides/.agent/` story, audience, source-evidence, and stale-evidence notes.

## Step 6 - Establish Worktree Policy

Default code policy:

```text
main code repo:       <ProjectName>/code/
code worktree root:   <ProjectName>/code-worktrees/
worktree path:        <ProjectName>/code-worktrees/<branch-type>-<branch-name>/
```

Default paper policy:

```text
main paper repo:      <ProjectName>/paper/
paper worktree root:  <ProjectName>/paper-worktrees/
worktree path:        <ProjectName>/paper-worktrees/<version-type>-<venue-or-name>/
```

Use paper worktrees for:

- different conference targets with different templates or style files
- arXiv/preprint releases where LaTeX source may become public
- camera-ready versions after acceptance
- paper-only rebuttal edits that should not disturb the main submission branch

Paper version hygiene:

- arXiv/public source: remove TODOs, internal figure/table descriptions in TeX comments, reviewer notes, hidden comments, author-comment macros, and anonymization leftovers
- anonymous conference: enforce anonymity, venue mode, and formatting; do not assume source comments are safe if source is uploaded
- camera-ready: de-anonymize, add acknowledgements/funding, close rebuttal promises, and remove draft-only notes

Record this in:

- `memory/project.yaml`
- `memory/component-index.yaml`
- `<ProjectName>/AGENTS.md`
- `<ProjectName>/CLAUDE.md`
- `code/docs/ops/current-status.md` when server execution is involved

If the execution server only has the code repo, record the server-specific worktree root in `code/infra/remote-projects.yaml` or `code/docs/ops/current-status.md`. Do not assume the server has `paper/` or root project memory.

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
| paper worktrees | `paper-worktrees/` | linked worktrees of paper repo | venue submissions, arXiv releases, camera-ready versions |
| slides | `slides/` | optional independent repo | talks and advisor/lab presentations |
| reviewer | `reviewer/` | root state dir | simulated reviews and pre-submission risk |
| rebuttal | `rebuttal/` | root state dir | real reviews, responses, promised revisions |
| artifact | `artifact/` | root state dir | artifact evaluation and release handoff |

## Documentation Boundary

- `memory/` stores durable claim/evidence/risk/action/decision state.
- `docs/overview.md` gives the current human-readable project overview.
- `docs/designs/` stores staged method and system design documents.
- `docs/experiments/` stores cross-component experiment plans before they become code-side run records.
- `code/docs/results/`, `code/docs/reports/`, and `code/docs/runs/` store code-side evidence and run provenance.
- Detailed paper prose belongs in `paper/`; detailed implementation docs belong in `code/`.

## Code Evidence Policy

- runnable experiment logic lives in `code/experiments/`
- stable code-side result summaries live in `code/docs/results/`
- experiment reports live in `code/docs/reports/`
- run pointers and job summaries live in `code/docs/runs/`
- raw outputs, logs, checkpoints, and wandb/tensorboard caches stay outside Git or in ignored paths
- paper-facing evidence is promoted through `paper-evidence-board` or `project-sync`

## Project-Level Docs Policy

- project overview lives in `docs/overview.md` and should summarize current project positioning, components, blockers, and next stage
- staged method/system designs live in `docs/designs/`
- cross-component experiment plans live in `docs/experiments/`
- advisor/lab updates live in `docs/updates/`
- consistency or readiness audits live in `docs/audits/`
- retrospective or forward-looking schedules live in `docs/timelines/`
- when algorithm or experiment plans change, update both the relevant root `docs/` artifact and the matching `memory/` boards; update `code/docs/` only when code-side run details, implementation notes, or result evidence change

## Worktree Policy

- default code root: `code-worktrees/`
- default paper root: `paper-worktrees/`
- naming: `<branch-type>-<branch-name>`
- every research or paper-version worktree needs `.agent/worktree-status.md`
- exit condition: merge, continue, park, or kill
- paper version worktrees must record target venue/release, submission mode, template/style differences, source visibility, cleanup requirements, and compile workflow
- component worktree indexes live at `code/.agent/worktree-index.md` and `paper/.agent/worktree-index.md`

## Memory Policy

- project-level durable summaries live in `memory/`
- component details live in `<component>/.agent/`
- project-level human-readable docs live in root `docs/`
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
Paper worktree root:
  <ProjectName>/paper-worktrees/

Next skills:
  research-project-memory -> inspect or update project state
  new-workspace -> create a code branch/worktree or paper version worktree
  remote-project-control -> configure SSH/HPC execution for code
  experiment-design-planner -> plan first experiment matrix
  research-slide-deck-builder -> create progress/advisor/lab slides with progress-slides
```

## Final Sanity Check

Before finishing:

- root agent guidance exists in both `AGENTS.md` and `CLAUDE.md`
- component repos that agents edit have paired `AGENTS.md` and `CLAUDE.md`
- root memory files exist or are explicitly deferred
- `paper/`, `code/`, and `slides/` Git boundaries are clear
- root and component Git remotes have been inspected separately when GitHub/GitLab setup is involved
- `gh auth status` or equivalent hosting CLI auth has been checked before attempting repo creation
- `code-worktrees/` policy is recorded
- `paper-worktrees/` policy is recorded
- there is no top-level `experiments/` directory unless the user explicitly requested it
- root `docs/` has a clear project-level role and is not confused with `code/docs/`
- code-side evidence paths are inside `code/docs/`
- component remotes and root Git policy are not ambiguous
