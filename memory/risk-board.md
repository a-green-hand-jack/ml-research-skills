# ml-research-skills Risk Board

Track risks that could break the skill system, project memory, release process, or agent workflows.

| ID | Kind | Status | Severity | Probability | Summary | Threatens | Mitigation | Actions | Certainty | Updated |
|---|---|---|---|---|---|---|---|---|---|---|
| RSK-001 | execution | open | medium | medium | Skill inventory and routing docs can drift from actual `skills/` contents or installed copies. | CLM-005 | Run `scripts/validate_skills.py`, update README/AGENTS/CLAUDE, reinstall after skill changes. | ACT-003, ACT-005 | observed | 2026-05-05 |
| RSK-002 | reviewer | open | high | medium | Spark sidecars may be over-trusted for high-risk design, security, or final review decisions. | CLM-003 | Keep sidecar outputs advisory; require main-agent or strong fresh reviewer for high-risk decisions. | ACT-002 | inferred | 2026-05-05 |
| RSK-003 | source-visibility | open | high | low | Private local facts, raw prompts, or session logs could leak into public repo memory. | CLM-001, CLM-004 | Keep `.agent/sidecars/` local, avoid raw transcripts, use private local memory for machine facts. | ACT-001 | observed | 2026-05-05 |
| RSK-004 | maintenance | open | medium | medium | Project memory could become stale if agents update skills but forget writeback. | CLM-001 | Use `research-project-memory` closeout/writeback after meaningful changes. | ACT-001 | inferred | 2026-05-05 |
| RSK-005 | evaluation | open | medium | medium | More skills may get scripts without matching smoke tests or realistic end-to-end validation. | CLM-005 | Add focused tests for helper scripts and run end-to-end install checks after behavior changes. | ACT-005 | inferred | 2026-05-05 |
| RSK-006 | personalization | open | medium | medium | Automatic trajectory scans may over-promote one-off corrections, noisy inferred preferences, or private details into durable memory. | CLM-011 | Use scope, confidence, privacy, and promotion gates; keep raw logs out of public memory; require main-agent review before writeback. | ACT-014 | inferred | 2026-05-07 |
| RSK-007 | source-visibility | open | high | medium | Raw PDFs, extracted paper text, or reading trajectories could leak copyrighted, licensed, or private material into public project memory. | CLM-012 | Keep raw PDFs and reading runs local/private by default; commit summarized cards and project-use notes only after copyright-safe compression. | ACT-015 | user-stated | 2026-05-08 |

## Accepted Risks

- Local sidecar artifacts remain outside git by default. This sacrifices shared replayability for privacy and repository hygiene.
