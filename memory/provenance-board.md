# ml-research-skills Provenance Board

Track how decisions, commits, tests, sidecar artifacts, and assets support project memory.

## Evidence Provenance

| ID | Status | Source class | Source paths | Transform / aggregation | Produces | Consumed by | Linked claims | Certainty | Updated |
|---|---|---|---|---|---|---|---|---|---|
| PRV-001 | available | repo-history | `git log`, README.md, AGENTS.md, CLAUDE.md, `memory/` | Summarize durable architecture state into project memory. | EVD-001, EVD-006 | `memory/current-status.md`, `memory/phase-dashboard.md` | CLM-001, CLM-005 | observed | 2026-05-05 |
| PRV-002 | available | workflow-test | `skills/code-reviewer/`, `tests/test_code_reviewer_bundle.py`, temporary isolated-review run summary | Convert test and review-bundle workflow into evidence for reviewer isolation. | EVD-002, EVD-003 | `memory/claim-board.md` | CLM-002 | observed | 2026-05-05 |
| PRV-003 | available | asset-and-sidecar | `skills/sidecar-task-runner/`, `tests/test_sidecar_task_runner.py`, `asset/`, local `.agent/sidecars/cleanup-assets-docs-slides/` | Use public code/tests/assets and local sidecar decision to support sidecar execution claim. | EVD-004, FIG-001 | README.md, `memory/claim-board.md` | CLM-003 | observed | 2026-05-05 |
| PRV-004 | available | telemetry | `skills/token-usage-auditor/`, `tests/test_token_usage_auditor.py` | Convert usage collector behavior and test fixtures into token telemetry evidence. | EVD-005 | `memory/claim-board.md`, future token reports | CLM-004 | observed | 2026-05-05 |

## Private Or Local Artifacts

- `.agent/sidecars/` is local/private by policy and excluded from tracked files through `.git/info/exclude`.
- Raw Codex/Claude Code session logs and local workstation facts must not be copied into this repo.

## Stale Provenance

- None known as of 2026-05-05.
