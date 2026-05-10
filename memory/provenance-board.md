# ml-research-skills Provenance Board

Track how decisions, commits, tests, sidecar artifacts, and assets support project memory.

## Evidence Provenance

| ID | Status | Source class | Source paths | Transform / aggregation | Produces | Consumed by | Linked claims | Certainty | Updated |
|---|---|---|---|---|---|---|---|---|---|
| PRV-001 | available | repo-history | `git log`, README.md, AGENTS.md, CLAUDE.md, `memory/` | Summarize durable architecture state into project memory. | EVD-001, EVD-006 | `memory/current-status.md`, `memory/phase-dashboard.md` | CLM-001, CLM-005 | observed | 2026-05-05 |
| PRV-002 | available | workflow-test | `skills/code-reviewer/`, `tests/test_code_reviewer_bundle.py`, temporary isolated-review run summary | Convert test and review-bundle workflow into evidence for reviewer isolation. | EVD-002, EVD-003 | `memory/claim-board.md` | CLM-002 | observed | 2026-05-05 |
| PRV-003 | available | asset-and-sidecar | `skills/sidecar-task-runner/`, `tests/test_sidecar_task_runner.py`, `asset/`, local `.agent/sidecars/cleanup-assets-docs-slides/` | Use public code/tests/assets and local sidecar decision to support sidecar execution claim. | EVD-004, FIG-001 | README.md, `memory/claim-board.md` | CLM-003 | observed | 2026-05-05 |
| PRV-004 | available | telemetry | `skills/token-usage-auditor/`, `tests/test_token_usage_auditor.py` | Convert usage collector behavior and test fixtures into token telemetry evidence. | EVD-005 | `memory/claim-board.md`, future token reports | CLM-004 | observed | 2026-05-05 |
| PRV-005 | available | helper-script-and-test | `skills/latex-layout-issue-bundler/`, `tests/test_latex_layout_issue_bundler.py`, README.md, AGENTS.md, CLAUDE.md | Convert the layout-bundle helper script, skill instructions, and smoke test into evidence for screenshot-free LaTeX layout debugging handoffs. | EVD-008 | `memory/claim-board.md`, `memory/action-board.md` | CLM-007 | observed | 2026-05-06 |
| PRV-006 | available | skill-and-sidecar-template | `skills/personalization-memory/`, `skills/sidecar-task-runner/templates/personalization-scanner.md`, `tests/test_sidecar_task_runner.py` | Convert the personalization writeback skill, sidecar scanner preset, and smoke test into evidence for automatic preference capture. | EVD-013 | `memory/claim-board.md`, `memory/action-board.md`, README.md | CLM-011 | observed | 2026-05-07 |
| PRV-007 | available | skill-and-helper-script | `skills/reference-library-manager/`, `skills/reference-reading-summarizer/`, `skills/reference-project-synthesizer/`, `tests/test_reference_library_manager.py` | Convert the reference-management skill trio, card/project-use templates, model routing, and scanner smoke test into evidence for project-local reference infrastructure. | EVD-014 | `memory/claim-board.md`, README.md, AGENTS.md, CLAUDE.md | CLM-012 | observed | 2026-05-08 |
| PRV-008 | available | skill-and-helper-script | `skills/reference-library-manager/`, `skills/reference-reading-summarizer/`, `skills/reference-project-synthesizer/`, `tests/test_reference_library_manager.py` | Convert the generalized source scanner, source-card templates, project-use routing, and smoke test into evidence for source-centric project knowledge intake. | EVD-015 | `memory/claim-board.md`, README.md, AGENTS.md, CLAUDE.md | CLM-013 | observed | 2026-05-10 |
| PRV-009 | available | skill-and-helper-script | `skills/memory-publication-auditor/`, `tests/test_memory_publication_auditor.py` | Convert the publication-audit skill, classification policy, redacting scanner, templates, and smoke test into evidence for safe private-to-public knowledge extraction. | EVD-016 | `memory/claim-board.md`, README.md, AGENTS.md, CLAUDE.md | CLM-014 | observed | 2026-05-10 |

## Private Or Local Artifacts

- `.agent/sidecars/` is local/private by policy and excluded from tracked files through `.git/info/exclude`.
- Raw Codex/Claude Code session logs and local workstation facts must not be copied into this repo.

## Stale Provenance

- None known as of 2026-05-05.
