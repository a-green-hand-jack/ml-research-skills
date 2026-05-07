# Project Link Routing

Use this reference to decide how a paper card should influence a project.

## Project Link Types

| Link type | Write target | Typical next skill |
|---|---|---|
| claim support | `memory/evidence-board.md`, `memory/provenance-board.md` | `paper-evidence-board` |
| claim challenge | `memory/claim-board.md`, `memory/risk-board.md` | `paper-positioning-planner` |
| baseline implication | `memory/action-board.md`, code benchmark/baseline plan | `baseline-selection-audit` |
| benchmark protocol | code `.agent/` or experiment docs | `experiment-design-planner` |
| method/theory idea | `memory/decision-log.md`, design docs | `algorithm-design-planner` |
| writing pattern | `paper/.agent/writing-contract.md`, style memory | `paper-writing-memory-manager` |
| citation placement | paper TODO or citation coverage memory | `citation-coverage-audit` |
| reviewer risk | `memory/risk-board.md` | `paper-reviewer-simulator` |

## Model Escalation

Use stronger reasoning when:

- the paper is closest work
- it creates or removes a novelty claim
- it defines a must-have baseline
- it defines an experiment protocol
- it changes the algorithm or theory
- it will support a final paper claim or rebuttal

Routine writing exemplars and citation placement can usually use normal main-agent reasoning over the card.

## Confidence Handling

| Card confidence | Allowed project action |
|---|---|
| `skim` | create candidate risk/action; do not finalize claims |
| `medium` | create project-use note and tentative memory links |
| `high` | update durable claim/evidence/risk/action memory |
| `needs-deep-read` | route back to reading summarizer before decisions |

## No Raw PDF Memory

Project memory should store:

- card path
- paper ID
- claim/evidence/risk/action IDs
- concise implication
- confidence

It should not store raw extracted paper text.
