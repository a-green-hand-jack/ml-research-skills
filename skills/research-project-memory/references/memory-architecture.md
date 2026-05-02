# Memory Architecture

Use a layered architecture so research feedback loops can survive across sessions without mixing stable project knowledge with volatile runtime state.

## Layer 1: User / Researcher Memory

Scope: cross-project preferences and constraints.

Examples:

- user's long-term research area
- preferred venues
- advisor or collaborator style
- common compute environments
- recurring reviewer risks

This layer usually lives outside the project in agent memory. Do not write it into a project repo unless the user asks.

## Layer 2: Project Memory

Path: `memory/`

Purpose: the project-level source of coordination truth.

Files:

- `project.yaml`: stable project identity, components, policies, and current target
- `component-index.yaml`: paths and roles for paper, code, code worktrees, slides, reviewer, rebuttal, artifact, and component memory
- `current-status.md`: session-to-session working state
- `decision-log.md`: durable decisions and why they were made
- `claim-board.md`: active, revised, cut, and planned claims
- `evidence-board.md`: experiments, analyses, proofs, citations, figures, and result summaries
- `risk-board.md`: novelty, baseline, mechanism, writing, execution, reviewer, and rebuttal risks
- `action-board.md`: concrete tasks linked to claims, evidence, risks, or components

Project memory should be committed when it is useful for collaborators and not private.

## Layer 3: Component Memory

Path: `<component>/.agent/`

Common components:

- `paper/`: section map, figure/table map, writing decisions, venue adaptation state
- `code/`: code status, experiment index, implementation decisions, remote execution pointers, and code-side evidence under `docs/results/`, `docs/reports/`, and `docs/runs/`
- `slides/`: presentation story, audience feedback, outdated figures
- `reviewer/`: simulated review history and risk register
- `rebuttal/`: real review issue board, response plan, promised revisions
- `artifact/`: artifact evaluation package state, reproduction instructions, and release handoff

Component memory should contain details that are too local for project boards but important for agents working inside that component.

## Layer 4: Worktree / Branch Memory

Path: `<code-worktree>/.agent/worktree-status.md`

Default project-control-root layout:

```text
<ProjectName>/
├── code/
└── code-worktrees/
    └── <branch-type>-<branch-name>/
```

Avoid nesting linked worktrees inside `code/` unless the project explicitly chose that layout.

Every research worktree should state:

- purpose
- hypothesis or issue being tested
- difference from main branch
- linked claim, evidence, or risk IDs
- latest result
- exit condition: merge, continue, park, or kill
- next verification step

This prevents abandoned branches and unclear experiment variants.

## Layer 5: Session / Volatile Memory

Scope: current agent session.

Examples:

- command output seen in the session
- active job status
- dirty git state
- temporary files
- whether a log existed at a moment in time

Volatile memory can be summarized in `current-status.md` only as advisory context. Execution-critical volatile facts must be re-verified.

## Merge and Trust Strategy

For stable project intent:

1. user instruction in current session
2. `memory/project.yaml`
3. `memory/decision-log.md`
4. component memory
5. old `current-status.md`

For execution-critical facts:

1. live verification
2. local component memory
3. project memory
4. old notes

For narrative and research rationale:

1. `claim-board.md`
2. `evidence-board.md`
3. `risk-board.md`
4. `decision-log.md`
5. component-specific notes

If layers disagree, do not silently choose one. Report the mismatch and either resolve it or create an action to resolve it.
