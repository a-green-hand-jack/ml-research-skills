# Reference Reading Model Routing

Use cheap models to compress many sources into structured cards. Use stronger models only when misunderstanding the source would change project decisions.

## Tier Definitions

| Tier | Use for |
|---|---|
| Tier 0 deterministic tools | metadata, file hashes, PDF/OCR extraction, bundle inventory, file manifests |
| Tier 1 cheap sidecar | skim, relevance, role labels, simple card skeleton, writing-pattern extraction, bundle inventory |
| Tier 2 normal main model | method extraction, benchmark protocol, citation support, collaborator-feedback structuring, spec extraction |
| Tier 3 strong/deep model | core theory, closest work, must-have baseline, novelty boundary, project seed, collaborator decision conflict |

## Default By Reading Mode

| Mode | Default tier | Escalate when |
|---|---:|---|
| `skim` | Tier 1 | source appears closest work, method-critical, or project-seeding |
| `extract-writing` | Tier 1 | pattern will become a writing contract or major paper rewrite |
| `extract-method` | Tier 2 | algorithm becomes project core |
| `extract-theory` | Tier 3 | proof/assumption supports project claim |
| `extract-benchmark` | Tier 2 | protocol defines experiment validity |
| `extract-baseline` | Tier 2 | baseline may be must-have |
| `extract-risk` | Tier 3 | novelty or reviewer risk is high |
| `extract-feedback` | Tier 2 | collaborator comments conflict or define a major revision |
| `extract-spec` | Tier 2 | spec controls project deliverables or experiment validity |
| `extract-bundle` | Tier 1 | bundle seeds project memory or contains mixed code/docs/bib |
| `extract-implementation-hints` | Tier 2 | script/config will affect core implementation |
| `extract-project-seed` | Tier 3 | source defines the initial project direction |
| `deep-read` | Tier 3 | always |

## Escalation Triggers

- The source is closest prior work.
- The source defines a benchmark, dataset, metric, or split used by the project.
- The source introduces a baseline likely required by reviewers.
- The source's theory, algorithm, spec, or script would affect implementation.
- The source contains collaborator feedback that changes priorities or requested edits.
- The source or bundle seeds a new project.
- The reading result will enter paper prose, rebuttal, or claim/evidence memory.
- The cheap model output contains uncertainty, contradictions, or missing sections.

## Downgrade Triggers

- The task is metadata/status only.
- The source is only a writing exemplar.
- The output is a provisional card, not a project decision.
- The user only wants a reading queue.

## Trajectory Policy

Keep raw reading trajectories in `reference/.agent/runs/` by default. Source cards should contain summaries and page/section/file pointers, not raw copied text.
