# Writeback Protocol

Write the smallest durable update that will help the next session. Do not turn memory into a transcript.

## Routing Table

| New information | Write to |
|---|---|
| Project identity, target venue, component paths, memory policy | `memory/project.yaml` |
| Current focus, active milestone, top blockers, next session entry point | `memory/current-status.md` |
| Durable rationale for choosing a direction, baseline policy, venue, architecture, or workflow | `memory/decision-log.md` |
| A paper or project claim is added, revised, supported, weakened, or cut | `memory/claim-board.md` |
| An experiment, analysis, proof, citation, figure, or qualitative result appears | `memory/evidence-board.md` |
| A reviewer, novelty, baseline, mechanism, writing, execution, or rebuttal risk appears | `memory/risk-board.md` |
| A concrete task needs to be tracked | `memory/action-board.md` |
| Paper section status, writing decision, figure location | `paper/.agent/` |
| Code architecture, implementation status, experiment entry point, remote execution pointer | `code/.agent/` or relevant code worktree `.agent/` |
| Code-side result summaries, experiment reports, and run pointers | `code/docs/results/`, `code/docs/reports/`, `code/docs/runs/`, plus project evidence board summaries |
| Slide story, audience feedback, outdated slide evidence | `slides/.agent/` |
| Simulated reviewer findings | `reviewer/.agent/` plus project risk board |
| Real reviews, rebuttal issues, promised revisions | `rebuttal/.agent/` plus project risk/action boards |
| Accepted-paper camera-ready status, final upload, release handoff | `paper/.agent/`, `rebuttal/.agent/`, and project decision/action boards |
| Artifact evaluation package state, smoke tests, reviewer instructions, data/checkpoint manifest | `code/.agent/`, `paper/.agent/`, and project evidence/risk/action boards |
| Advisor, mentor, lab, or collaborator feedback | `memory/current-status.md`, `memory/decision-log.md`, `memory/action-board.md`, and affected component `.agent/` folders |
| Skill-system roadmap, lifecycle audit, routing audit, or repository-level skill maintenance decision | project-level roadmap memory, audit reports, and relevant repo docs |

## Skill Writeback Expectations

- `research-idea-validator`: write decisions, early risks, and next actions.
- `literature-review-sprint`: write closest-work risks, citation/evidence pointers, and positioning decisions.
- `algorithm-design-planner`: write method assumptions, design decisions, linked claims, and expected ablations.
- `experiment-design-planner`: write planned evidence, experiment families, controls, and falsification actions.
- `baseline-selection-audit`: write must-have baseline decisions, fairness risks, planned comparison evidence, and run/justify actions.
- `run-experiment`: write run pointers and volatile job context only after verification, preferably into `code/docs/runs/` or the active code worktree's `docs/runs/`.
- `result-diagnosis`: write diagnosis decisions, weakened or revised claims, evidence status changes, and next actions.
- `experiment-report-writer`: write completed evidence summaries, result decisions, and stale/updated claims; code-side reports usually belong in `code/docs/reports/` or a code worktree's `docs/reports/`.
- `advisor-update-writer`: write advisor decisions, feedback-derived actions, current status changes, and newly raised risks.
- `figure-results-review`: write figure/table evidence status, visual/statistical reviewer risks, caption actions, and claim-scope changes.
- `paper-evidence-board`: write paper-facing claim/evidence/figure/section alignment and open evidence gaps.
- `paper-positioning-planner`: write paper archetype, contribution hierarchy, scoped claims, related-work boundary, and positioning actions.
- `conference-writing-adapter`: write section mapping, claim wording decisions, and writing risks.
- `paper-reviewer-simulator`: write reviewer risks and actions.
- `citation-coverage-audit`: write missing-citation risks and actions.
- `citation-audit`: write correctness risks and blocking fixes.
- `rebuttal-strategist`: write review issues, response plan, promised revisions, and post-rebuttal actions.
- `camera-ready-finalizer`: write final accepted-paper state, fulfilled promises, final claim/evidence status, residual risks, and release/artifact handoff actions.
- `artifact-evaluation-prep`: write artifact readiness, claim-to-artifact coverage, smoke-test status, package blockers, and reviewer-instruction actions.
- `submit-paper`: write final pre-submission blockers and readiness decisions.
- `release-code`: write public-release readiness, release blockers, tags, and reproducibility handoff.
- `skill-system-auditor`: write skill-system roadmap decisions, lifecycle coverage conclusions, audit reports, stale-doc fixes, and next hardening actions.
- `remote-project-control`: write remote execution state in its own files and summarize linked experiment state in project memory when needed.

## Update Style

Use short entries:

- ID
- status
- one-sentence summary
- links to related IDs
- source path or command result pointer
- certainty
- last updated date

Avoid:

- full command transcripts
- large paper excerpts
- unverified assumptions presented as facts
- private credentials or machine-specific paths in shared memory
- duplicating the same detailed note in multiple files

## Conflict Handling

If memory conflicts with current files or user input:

1. Trust current user input for intent.
2. Trust live verification for volatile state.
3. Mark stale memory explicitly.
4. Add an action if the conflict needs cleanup.

Never silently overwrite a durable decision. Append a new decision entry that supersedes the old one.
