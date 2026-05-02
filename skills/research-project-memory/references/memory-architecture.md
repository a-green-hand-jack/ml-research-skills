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
- `component-index.yaml`: paths and roles for paper, code, code worktrees, paper worktrees, slides, reviewer, rebuttal, artifact, component memory, and the global worktree registry
- `current-status.md`: session-to-session working state
- `decision-log.md`: durable decisions and why they were made
- `claim-board.md`: active, revised, cut, and planned claims
- `evidence-board.md`: experiments, analyses, proofs, citations, figures, and result summaries
- `risk-board.md`: novelty, baseline, mechanism, writing, execution, reviewer, and rebuttal risks
- `action-board.md`: concrete tasks linked to claims, evidence, risks, or components

Project memory should be committed when it is useful for collaborators and not private.

### Optional Cloud Coordination: GitHub Project

A GitHub Project can be linked from `memory/project.yaml` when the research project spans several repos. Treat it as a collaborator-facing task board, not as the durable research memory layer.

Use GitHub Projects for:

- issues and PRs across root, code, paper, and slides repos
- owner/status/priority/blocker tracking
- roadmap, board, table, experiment, paper, risk, and worktree views
- public or collaborator-visible target dates and milestones

Keep in project memory instead:

- claim rationale and evidence interpretation
- private reviewer-risk notes
- detailed experiment provenance
- paper worktree source-visibility and arXiv cleanup policies
- decisions that must survive even if GitHub fields or views are reorganized

Recommended `memory/project.yaml` fields:

```yaml
github_project:
  enabled: true
  owner: <github-user-or-org>
  title: <project-title>
  number: <project-number>
  url: <project-url>
  sync_policy: issue-pr-links
  scope_required: project
```

When using `gh project ...`, verify `gh auth status` and refresh the `project` token scope if needed. In sandboxed agent runtimes, a failed `gh auth status` may be a Keychain or network access problem; recheck with the appropriate permission before asking the user to log in again.

## Layer 3: Component Memory

Path: `<component>/.agent/`

Common components:

- `paper/`: section map, figure/table map, writing decisions, venue adaptation state, and paper worktree rollup
- `code/`: code status, experiment index, implementation decisions, remote execution pointers, and code worktree rollup
- `slides/`: presentation story, audience feedback, outdated figures
- `reviewer/`: simulated review history and risk register
- `rebuttal/`: real review issue board, response plan, promised revisions
- `artifact/`: artifact evaluation package state, reproduction instructions, and release handoff

Component memory should contain details that are too local for project boards but important for agents working inside that component.

Recommended component memory files:

- `<component>/.agent/<component>-status.md`: component summary, linked claims/evidence/risks/actions, local decisions, stale facts, and next step
- `<component>/.agent/worktree-index.md`: component-local rollup of active and recently closed worktrees
- `<component-worktree>/.agent/worktree-status.md`: leaf memory for one branch/worktree

For code, `code/docs/ops/current-status.md` and `code/docs/ops/decision-log.md` are useful repo-native operational memory. They are not enough by themselves for cross-worktree coordination because they do not naturally list sibling worktrees, paper versions, or project-level claim/evidence/risk/action links. Use them alongside `code/.agent/worktree-index.md` and root `memory/component-index.yaml`.

For paper, `.agent/paper-status.md`, `.agent/figure-table-map.md`, and `.agent/worktree-index.md` should carry writing state, figure/table mapping, and venue/arXiv/camera-ready version state. Public-source cleanup decisions should be summarized here or in root memory, not hidden in released `.tex` comments.

## Layer 4: Worktree / Branch Memory

Path: `<component-worktree>/.agent/worktree-status.md`

Default project-control-root layout:

```text
<ProjectName>/
├── code/
├── code-worktrees/
│   └── <branch-type>-<branch-name>/
├── paper/
└── paper-worktrees/
    └── <version-type>-<venue-or-name>/
```

Avoid nesting linked worktrees inside `code/` or `paper/` unless the project explicitly chose that layout.

Every code research worktree should state:

- purpose
- hypothesis or issue being tested
- difference from main branch
- linked claim, evidence, or risk IDs
- latest result
- exit condition: merge, continue, park, or kill
- next verification step

Every paper worktree should additionally state:

- target venue or release, such as NeurIPS, ICML, ICLR, CVPR, ACL, EMNLP, arXiv, or camera-ready
- submission mode: anonymous, preprint, camera-ready, rebuttal, or internal
- style/template differences from the main paper branch
- source visibility: private conference source, uploaded submission source, public arXiv source, or publisher source
- cleanup requirements for source release or anonymity
- compile workflow, especially GitHub-linked Overleaf status

This prevents abandoned branches and unclear experiment variants.

Cross-worktree management has three surfaces:

1. `memory/component-index.yaml`: global registry of worktree roots and known worktrees across code and paper.
2. `<component>/.agent/worktree-index.md`: component-local rollup for active, parked, merged, and killed worktrees.
3. `<component-worktree>/.agent/worktree-status.md`: detailed leaf status for one branch/version.

When a worktree is created, merged, parked, or killed, update all relevant surfaces. If a worktree appears in `git worktree list` but not in memory, mark it as `needs-verification` rather than assuming it is abandoned.

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
