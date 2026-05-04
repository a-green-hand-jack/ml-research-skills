# Writeback Protocol

Write the smallest durable update that will help the next session. Do not turn memory into a transcript.

## Routing Table

| New information | Write to |
|---|---|
| Project identity, target venue, component paths, memory policy | `memory/project.yaml` |
| GitHub Project owner, title, URL, number, visibility, and sync policy | `memory/project.yaml`; optionally `memory/component-index.yaml` for linked repos |
| Current focus, active milestone, top blockers, next session entry point | `memory/current-status.md` |
| Durable rationale for choosing a direction, baseline policy, venue, architecture, or workflow | `memory/decision-log.md` |
| A paper or project claim is added, revised, supported, weakened, or cut | `memory/claim-board.md` |
| An experiment, analysis, proof, citation, figure, or qualitative result appears | `memory/evidence-board.md` |
| Source traceability changes for a raw run, CSV, report, citation, analysis, figure, table, caption, or result sentence | `memory/provenance-board.md` |
| A reviewer, novelty, baseline, mechanism, writing, execution, or rebuttal risk appears | `memory/risk-board.md` |
| A concrete task needs to be tracked | `memory/action-board.md` |
| Project phase, active gate, readiness, stale objects, or next phase trigger changes | `memory/phase-dashboard.md` |
| One module produces payload another module should consume | `memory/handoff-board.md` |
| Paper branch/worktree/source package visibility, Overleaf sync audience, allowed/forbidden source files, or cleanup gate changes | `memory/source-visibility-board.md` |
| A concrete task should be visible to collaborators or attached to a PR/issue | GitHub issue/PR/project item plus a short pointer in `memory/action-board.md` when it affects claims, evidence, risks, or worktrees |
| Paper section status, writing decision, figure location | `paper/.agent/` |
| Paper version target, template differences, source visibility, cleanup policy, compile workflow | relevant paper worktree `.agent/worktree-status.md` plus durable decisions in `memory/decision-log.md` |
| Code architecture, implementation status, experiment entry point, remote execution pointer | `code/.agent/` or relevant code worktree `.agent/` |
| Worktree created, merged, parked, killed, or found stale | `memory/component-index.yaml`, `<component>/.agent/worktree-index.md`, and the relevant worktree `.agent/worktree-status.md` |
| Code-side result summaries, experiment reports, and run pointers | `code/docs/results/`, `code/docs/reports/`, `code/docs/runs/`, plus project evidence board summaries |
| Slide component status, deck registry, audience feedback, outdated slide evidence | `slides/.agent/slides-status.md`, `slides/.agent/deck-index.md`, and optionally `slides/.agent/decks/<deck-id>.md` |
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
- `run-experiment`: write run pointers and volatile job context only after verification, preferably into `code/docs/runs/` or the active code worktree's `docs/runs/`; create or update provenance when a run becomes a stable source for evidence.
- `result-diagnosis`: write diagnosis decisions, weakened or revised claims, evidence status changes, and next actions.
- `experiment-report-writer`: write completed evidence summaries, result decisions, stale/updated claims, and a handoff to paper-facing asset or writing work when results are ready; code-side reports usually belong in `code/docs/reports/` or a code worktree's `docs/reports/`.
- `advisor-update-writer`: write advisor decisions, feedback-derived actions, current status changes, and newly raised risks.
- `project-init`: write GitHub Project board metadata and sync policy when the user creates or links a board.
- `figure-results-review`: write figure/table evidence status, visual/statistical reviewer risks, caption actions, and claim-scope changes.
- `paper-evidence-board`: write paper-facing claim/evidence/figure/section alignment and open evidence gaps.
- `paper-evidence-gap-miner`: write evidence-gap handoffs to experiment design only after checking existing result sources.
- `paper-result-asset-builder`: write CSV/report-to-figure/table provenance and handoffs to figure/table review or result prose writing.
- `new-workspace`: write paper worktree source visibility tier, sync target, cleanup gate, and forbidden-file policy when creating paper worktrees.
- `submit-paper`: write final pre-submission blockers, readiness decisions, source visibility audit status, and cleanup actions for author-visible, anonymous, arXiv, camera-ready, or publisher-visible source.
- `init-latex-project`: initialize paper-local source hygiene policy and default ignore rules so agent-private files do not enter visible paper source by accident.
- `paper-positioning-planner`: write paper archetype, contribution hierarchy, scoped claims, related-work boundary, and positioning actions.
- `conference-writing-adapter`: write section mapping, claim wording decisions, and writing risks.
- `paper-writing-memory-manager`: write stale prose, dependency, provisional-result, and section-state pointers into paper-local memory; summarize cross-component effects through claim, provenance, handoff, or action boards when needed.
- `paper-reviewer-simulator`: write reviewer risks and actions.
- `citation-coverage-audit`: write missing-citation risks and actions.
- `citation-audit`: write correctness risks and blocking fixes.
- `rebuttal-strategist`: write review issues, response plan, promised revisions, and post-rebuttal actions.
- `camera-ready-finalizer`: write final accepted-paper state, fulfilled promises, final claim/evidence status, residual risks, release/artifact handoff actions, final source visibility, and public-clean source/package status.
- `artifact-evaluation-prep`: write artifact readiness, claim-to-artifact coverage, smoke-test status, package blockers, and reviewer-instruction actions.
- `release-code`: write public-release readiness, release blockers, tags, and reproducibility handoff.
- `skill-system-auditor`: write skill-system roadmap decisions, lifecycle coverage conclusions, audit reports, stale-doc fixes, and next hardening actions.
- `remote-project-control`: write remote execution state in its own files and summarize linked experiment state in project memory when needed.
- GitHub Project operations: write only stable board metadata, issue/PR pointers, and action links into project memory. Do not mirror private research reasoning into GitHub unless the user explicitly wants it visible there.

Update `memory/phase-dashboard.md` after a major phase transition or regression. Do not update it for every small edit.

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
