# Global Consistency Audit

Date: 2026-05-02
Repo: `/Users/jieke/Projects/project-skills`

## Scope

This audit originally checked whether the 30-skill collection was coherent as a lifecycle system. A same-day follow-up added three extension skills, bringing the collection to 33 skills:

- top-level inventory and lifecycle ordering
- role-based categories
- cross-skill routing and pair-with guidance
- `research-project-memory` writeback expectations
- obsolete "future skill" references
- remaining lifecycle gaps

This is a system-level audit, not a new skill.

## Current Lifecycle Coverage

The main ML research paper lifecycle is now covered end to end:

```text
research-project-memory
-> research-idea-validator
-> literature-review-sprint
-> algorithm-design-planner
-> project-init / init-latex-project / init-python-project / new-workspace / remote-project-control
-> experiment-design-planner
-> baseline-selection-audit
-> run-experiment
-> result-diagnosis
-> project-sync
-> experiment-report-writer
-> figure-results-review
-> paper-evidence-board
-> paper-positioning-planner
-> conference-writing-adapter
-> paper-reviewer-simulator
-> citation-coverage-audit
-> citation-audit
-> submit-paper
-> rebuttal-strategist
-> camera-ready-finalizer
-> release-code / update-docs / work-timeline-planner / add-git-tag
```

## Findings Fixed

| Finding | Fix |
|---|---|
| README still listed `camera-ready-finalizer` as a future skill after it had been implemented. | Updated the future list to `artifact-evaluation-prep`, `advisor-update-writer`, and `skill-system-auditor`. |
| `experiment-design-planner` still described `baseline-selection-audit` as future. | Updated pair-with guidance to route to `baseline-selection-audit` before finalizing reviewer-sensitive baseline matrices. |
| `research-project-memory` writeback protocol did not mention newer lifecycle skills. | Added writeback expectations for `baseline-selection-audit`, `result-diagnosis`, `figure-results-review`, `paper-evidence-board`, `paper-positioning-planner`, `camera-ready-finalizer`, `submit-paper`, and `release-code`. |
| `paper-evidence-board` gap triage routed writing issues only to `conference-writing-adapter`. | Added routing to `paper-positioning-planner` when the strategic story or claim hierarchy is wrong. |
| `paper-evidence-board` did not explicitly route figure/table ambiguity to `figure-results-review`. | Added a dedicated figure/table review triage branch. |
| Rebuttal workflow did not explicitly hand off to camera-ready after acceptance. | Added `camera-ready-finalizer` pairing to `rebuttal-strategist`. |

## Remaining Gaps and Follow-Up

At audit time, these were real remaining gaps, not inconsistencies. Follow-up status is included to avoid stale roadmap interpretation.

| Gap | Status | Why it matters |
|---|---|---|
| `artifact-evaluation-prep` | Implemented after audit | Needed when a venue has artifact evaluation, reproducibility badges, install demos, checkpoints, data packaging, or runtime constraints. |
| `advisor-update-writer` | Implemented after audit | Useful for decision-oriented mentor/lab updates that are broader than experiment reports. |
| `skill-system-auditor` | Implemented after audit | Formalizes this exact global consistency audit as a reusable maintenance skill. |
| End-to-end synthetic project test | Not yet in repo | Would validate skill handoff across the full lifecycle rather than one skill at a time. |

The remaining item is the end-to-end synthetic project test and richer case-based validation.

## Consistency Decision

The project is now coherent enough to call the main research-paper lifecycle complete. The remaining work is extension and hardening:

- implement artifact/evaluation packaging if needed
- implement advisor/lab-update writing if useful
- create an end-to-end synthetic lifecycle test
- optionally convert this audit into a reusable maintenance skill later

## Validation

Repository validator after the original fixes:

```text
python3 scripts/validate_skills.py
Validated 30 skill(s); no issues found.
```

Repository validator after implementing `artifact-evaluation-prep`, `advisor-update-writer`, and `skill-system-auditor`:

```text
python3 scripts/validate_skills.py
Validated 33 skill(s); no issues found.
```
