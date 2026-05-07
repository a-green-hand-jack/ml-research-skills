# Reference Reading Model Routing

Use cheap models to compress many references into structured cards. Use stronger models only when misunderstanding the paper would change project decisions.

## Tier Definitions

| Tier | Use for |
|---|---|
| Tier 0 deterministic tools | PDF text extraction, OCR, page screenshots, metadata, file hashes |
| Tier 1 cheap sidecar | skim, relevance, role labels, simple card skeleton, writing-pattern extraction |
| Tier 2 normal main model | method extraction, benchmark protocol, citation support, structured card completion |
| Tier 3 strong/deep model | core theory, closest work, must-have baseline, novelty boundary, rebuttal-sensitive reading |

## Default By Reading Mode

| Mode | Default tier | Escalate when |
|---|---:|---|
| `skim` | Tier 1 | paper appears closest work or method-critical |
| `extract-writing` | Tier 1 | pattern will become a writing contract or major paper rewrite |
| `extract-method` | Tier 2 | algorithm becomes project core |
| `extract-theory` | Tier 3 | proof/assumption supports project claim |
| `extract-benchmark` | Tier 2 | protocol defines experiment validity |
| `extract-baseline` | Tier 2 | baseline may be must-have |
| `extract-risk` | Tier 3 | novelty or reviewer risk is high |
| `deep-read` | Tier 3 | always |

## Escalation Triggers

- The paper is closest prior work.
- The paper defines a benchmark, dataset, metric, or split used by the project.
- The paper introduces a baseline likely required by reviewers.
- The paper's theory or algorithm would affect implementation.
- The reading result will enter paper prose, rebuttal, or claim/evidence memory.
- The cheap model output contains uncertainty, contradictions, or missing sections.

## Downgrade Triggers

- The task is metadata/status only.
- The paper is only a writing exemplar.
- The output is a provisional card, not a project decision.
- The user only wants a reading queue.

## Trajectory Policy

Keep raw reading trajectories in `reference/.agent/runs/` by default. Paper cards should contain summaries and page pointers, not raw copied text.
