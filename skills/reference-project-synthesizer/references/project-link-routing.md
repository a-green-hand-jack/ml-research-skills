# Project Link Routing

Use this reference to decide how a source card should influence a project.

## Project Link Types

| Link type | Write target | Typical next skill |
|---|---|---|
| claim support | `memory/evidence-board.md`, `memory/provenance-board.md` | `paper-evidence-board` |
| claim challenge | `memory/claim-board.md`, `memory/risk-board.md` | `paper-positioning-planner` |
| baseline implication | `memory/action-board.md`, code benchmark/baseline plan | `baseline-selection-audit` |
| benchmark protocol | code `.agent/` or experiment docs | `experiment-design-planner` |
| method/theory idea | `memory/decision-log.md`, design docs | `algorithm-design-planner` |
| implementation hint | code `.agent/implementation-plan.md`, `memory/action-board.md` | `init-python-project`, `code-reviewer` |
| collaborator feedback | `memory/action-board.md`, `memory/risk-board.md`, paper writing memory | `paper-writing-memory-manager`, `advisor-update-writer` |
| project spec or constraint | `memory/decision-log.md`, `memory/current-status.md`, component `.agent/` | `project-init`, `algorithm-design-planner` |
| project seed | root `memory/`, `PROJECT.md`, action board | `research-idea-validator`, `project-init` |
| writing pattern | `paper/.agent/writing-contract.md`, style memory | `paper-writing-memory-manager` |
| citation placement | paper TODO or citation coverage memory | `citation-coverage-audit` |
| reviewer risk | `memory/risk-board.md` | `paper-reviewer-simulator` |

## Model Escalation

Use stronger reasoning when:

- the source is closest work
- it creates or removes a novelty claim
- it defines a must-have baseline
- it defines an experiment protocol
- it changes the algorithm, theory, implementation, or project spec
- it contains conflicted collaborator feedback
- it seeds a new project direction
- it will support a final paper claim or rebuttal

Routine writing exemplars, simple citation placement, and low-risk feedback triage can usually use normal main-agent reasoning over the card.

## Confidence Handling

| Card confidence | Allowed project action |
|---|---|
| `skim` | create candidate risk/action; do not finalize claims |
| `medium` | create project-use note and tentative memory links |
| `high` | update durable claim/evidence/risk/action memory |
| `needs-deep-read` | route back to reading summarizer before decisions |

## No Raw Source Memory

Project memory should store:

- source card path
- source ID
- claim/evidence/risk/action IDs
- concise implication
- confidence

It should not store raw extracted source text.
