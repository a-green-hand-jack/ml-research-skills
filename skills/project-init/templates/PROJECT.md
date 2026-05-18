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
| code uv env | `.uv-envs/code` | ignored root path | shared uv environment for `code/` and `code-worktrees/*` |
| reference | `reference/` | root state dir or optional repo | project-local sources, source cards, processing status, and project-use notes |
| slides | `slides/` | optional independent repo | talks and advisor/lab presentations |
| reviewer | `reviewer/` | root state dir | simulated reviews and pre-submission risk |
| rebuttal | `rebuttal/` | root state dir | real reviews, responses, promised revisions |
| artifact | `artifact/` | root state dir | artifact evaluation and release handoff |

## GitHub Project Board

- status: <none|linked|planned>
- owner: <github-user-or-org>
- title: <project-title>
- number: <project-number>
- url: <project-url>
- role: collaborator-facing issues, PRs, blockers, milestones, and roadmap views
- not a replacement for: root `memory/`, component `.agent/`, code-side evidence docs, or paper worktree source-hygiene policy

Recommended fields: `Component`, `Workstream`, `Status`, `Priority`, `Target`, `Claim ID`, `Evidence ID`, `Worktree`, `Blocker`.
Recommended views: `Roadmap`, `Board`, `Experiments`, `Paper`, `Risks`, `Worktrees`.

## Documentation Boundary

- `memory/` stores durable claim/evidence/provenance/risk/action/handoff/decision state.
- `memory/claim-board.md` tracks claim lifecycle from idea to final or cut.
- `memory/provenance-board.md` tracks source-to-paper evidence provenance from runs, CSVs, reports, citations, assets, captions, and prose.
- `memory/handoff-board.md` tracks producer/consumer contracts between code, paper, slides, review, rebuttal, artifact, and release work.
- `memory/phase-dashboard.md` gives the current project-cycle phase, active gate, and next session entry point.
- `memory/source-visibility-board.md` tracks paper source visibility tiers, audiences, sync targets, allowed/forbidden files, and cleanup gates.
- `docs/overview.md` gives the current human-readable project overview.
- `docs/designs/` stores staged method and system design documents.
- `docs/experiments/` stores cross-component experiment plans before they become code-side run records.
- `reference/` stores project-local sources, cards, processing status, and project-use notes; raw reading trajectories under `reference/.agent/runs/` are local/private by default.
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
- reference source cards live in `reference/cards/` and project implications live in `reference/project-use/`; raw source text and raw reading trajectories should not be promoted into public memory
- when algorithm or experiment plans change, update both the relevant root `docs/` artifact and the matching `memory/` boards; update `code/docs/` only when code-side run details, implementation notes, or result evidence change

## Worktree Policy

- default code root: `code-worktrees/`
- default paper root: `paper-worktrees/`
- shared code uv env: `.uv-envs/code`
- naming: `<branch-type>-<branch-name>`
- every research or paper-version worktree needs `.agent/worktree-status.md`
- exit condition: merge, continue, park, or kill
- code worktrees should run uv with absolute `UV_PROJECT_ENVIRONMENT=<ProjectRoot>/.uv-envs/code` plus `uv run` from the active worktree; create a separate stage env only for dependency/Python/CUDA changes, destructive package tests, or real concurrent sync risk
- paper version worktrees must record target venue/release, submission mode, template/style differences, source visibility, cleanup requirements, and compile workflow
- paper source surfaces must record visibility tier, audience, sync target, allowed/forbidden files, cleanup gate, and audit status
- component worktree indexes live at `code/.agent/worktree-index.md` and `paper/.agent/worktree-index.md`

## Memory Policy

- project-level durable summaries live in `memory/`
- claim lifecycle, evidence provenance, phase status, and cross-module handoffs live in root `memory/`
- paper source visibility and cleanup gates live in root `memory/source-visibility-board.md`
- toolchain gate defaults live in root `memory/project.yaml`; component-specific overrides live in component guidance or worktree status
- component details live in `<component>/.agent/`
- project-level human-readable docs live in root `docs/`
- code-side run details live in `code/docs/`
- volatile scheduler or job state must be re-verified before action
