# Cross-Module Handoff Contracts

Handoffs make explicit what one skill or project module produced and what another module is expected to consume. They are useful whenever work crosses code, paper, slides, review, rebuttal, artifact, or release boundaries.

## Handoff Board

Track active handoffs in `memory/handoff-board.md`.

Use IDs:

- `HND-###`: cross-module handoff

## Standard Handoff Shape

```yaml
id: HND-001
status: proposed | ready | consumed | blocked | stale | cancelled
producer: experiment-report-writer
consumer: paper-result-asset-builder
from_component: code
to_component: paper
payload: ""
source_paths: []
expected_outputs: []
linked_claims: [CLM-001]
linked_evidence: [EVD-001]
linked_actions: [ACT-001]
acceptance_check: ""
staleness_trigger: ""
certainty: observed
last_updated: YYYY-MM-DD
```

## Common Handoff Types

| From | To | Payload |
|---|---|---|
| `research-idea-validator` | `literature-review-sprint` | idea, novelty uncertainty, must-read areas |
| `literature-review-sprint` | `baseline-selection-audit` | closest work, missing baselines, benchmark conventions |
| `algorithm-design-planner` | `experiment-design-planner` | hypotheses, ablations, failure modes |
| `experiment-design-planner` | `run-experiment` | runnable experiment matrix, configs, metrics, stop rules |
| `run-experiment` | `experiment-report-writer` | verified run pointers, configs, output paths |
| `experiment-report-writer` | `result-diagnosis` | surprising result, instability, failed hypothesis |
| `experiment-report-writer` | `paper-result-asset-builder` | stable CSV/report evidence for paper assets |
| `paper-evidence-gap-miner` | `experiment-design-planner` | evidence gap not fillable from existing results |
| `paper-result-asset-builder` | `figure-results-review` / `table-results-review` | generated asset plus provenance |
| `paper-writing-memory-manager` | section writers | stale prose, dependencies, section state |
| section writers | `paper-draft-consistency-editor` | changed claims, result wording, terminology |
| `paper-reviewer-simulator` | `paper-evidence-board` | reviewer risk, missing evidence, rewrite action |
| `rebuttal-strategist` | `run-experiment` / writers | promised experiment or clarification |
| `camera-ready-finalizer` | `artifact-evaluation-prep` / `release-code` | final release and artifact obligations |

## Acceptance Checks

A handoff is `ready` only when the consumer can act without re-inventing the producer's reasoning. Include:

- source paths or IDs
- expected output
- known limitations
- what must be verified first
- staleness trigger

Mark a handoff `consumed` when the consumer has created the promised output or created a new downstream handoff.

## When To Create a Handoff

Create a handoff when:

- a result moves from code to paper
- writing discovers an evidence gap
- review creates an experiment or rewrite obligation
- camera-ready creates artifact or release work
- advisor feedback creates a concrete next action across components

Do not create handoffs for tiny same-file edits. Use `memory/action-board.md` for simple tasks.
