# ml-research-skills Handoff Board

Track producer/consumer contracts between parts of the skill system.

| ID | Status | Producer | Consumer | Payload | Source paths | Expected output | Acceptance check | Linked IDs | Certainty | Updated |
|---|---|---|---|---|---|---|---|---|---|---|
| HND-001 | ready | sidecar-task-runner | token-usage-auditor | `.agent/sidecars/<task-id>/model.json` metadata | `skills/sidecar-task-runner/`, `skills/token-usage-auditor/` | Sidecar runs appear as `codex-sidecar` sessions when metadata exists. | `tests.test_token_usage_auditor` | CLM-003, CLM-004, EVD-004, EVD-005 | observed | 2026-05-05 |
| HND-002 | ready | code-reviewer | main-agent writer | `review.md`, `spark-output.md`, `fix-log.md` review artifacts | `skills/code-reviewer/` | Writer can triage findings and record fixes without reviewer chat context. | `tests.test_code_reviewer_bundle` plus manual isolated review | CLM-002, EVD-003 | observed | 2026-05-05 |
| HND-003 | proposed | memory | future skill changes | updated decisions, claims, risks, actions, and phase state | `memory/` | Future sessions start from current project state instead of rediscovering architecture decisions. | Memory writeback after next substantial change | CLM-001, RSK-004, ACT-001 | user-stated | 2026-05-05 |
