# ml-research-skills Claim Board

Track project-level claims about this skill system. These are architecture and workflow claims, not paper claims.

| ID | Lifecycle state | Claim | Type | Required evidence | Location | Supported by | Threatened by | Next gate | Certainty | Updated |
|---|---|---|---|---|---|---|---|---|---|---|
| CLM-001 | active | A committed project memory layer will make this skill system easier to maintain across sessions. | system | Memory files exist and are used during future changes. | `memory/` | EVD-001 | RSK-004 | maintenance | user-stated | 2026-05-05 |
| CLM-002 | supported | Fresh-context reviewer bundles improve review independence for core code changes. | system | Review bundle workflow and isolated CLI protocol exist; temporary isolated review caught real issues. | `skills/code-reviewer/` | EVD-002, EVD-003 | RSK-002 | review | observed | 2026-05-05 |
| CLM-003 | active | Spark sidecars are useful for bounded low/medium-risk mechanical tasks across the lifecycle. | system | `sidecar-task-runner` exists; cleanup task used read-only sidecar successfully. | `skills/sidecar-task-runner/` | EVD-004 | RSK-002 | maintenance | observed | 2026-05-05 |
| CLM-004 | active | Token usage can act as project attention and friction telemetry when interpreted with artifacts and outcomes. | system | `token-usage-auditor` supports Codex, Claude Code, and sidecar metadata. | `skills/token-usage-auditor/` | EVD-005 | RSK-003 | telemetry | user-stated | 2026-05-05 |
| CLM-005 | supported | Explicit toolchain gates reduce skill, docs, and helper-script drift. | system | Validator and focused smoke tests pass after recent workflow changes. | `scripts/`, `tests/`, docs | EVD-006 | RSK-001, RSK-005 | validation | observed | 2026-05-05 |
| CLM-006 | active | Paper layout debugging should be handled as local, visual, reversible optimization over prose, floats, and page breaks. | system | User-tested protocol is encoded in paper-readiness skills and used in future layout fixes. | `skills/submit-paper/references/layout-debugging.md` | EVD-007 | RSK-004 | maintenance | user-stated | 2026-05-05 |

## Cut or Superseded Claims

- None.
