# ml-research-skills Phase Dashboard

> Global project-cycle view for this skill-system repository.

## Current Phase

- Phase: `maintenance`
- Readiness: `partial`
- Objective: keep the skill collection coherent, installable, memory-backed, and auditable as the workflow architecture evolves.
- Active gate: choose Fast / Skill / Code / Risk closeout path, then run only the validation needed for the selected path before push.
- Next phase trigger: a tagged skill-system release or a successful full audit showing memory, sidecar routing, personalization writeback, source-card routing, publication audits, token telemetry, and code review protocols are consistently wired across high-value skills.
- Last updated: 2026-05-10

## Phase Table

| Phase | Status | Gate | Linked claims | Linked evidence | Blocking risks | Active actions |
|---|---|---|---|---|---|---|
| idea | done | project has clear purpose and lifecycle scope | CLM-001 | EVD-001 |  |  |
| positioning | done | skill system positioned as ML research lifecycle tooling | CLM-001 | EVD-001 | RSK-001 | ACT-003 |
| method-design | done | memory, sidecar, reviewer, token, and toolchain protocols defined | CLM-001, CLM-002, CLM-003, CLM-004, CLM-005 | EVD-002, EVD-003, EVD-004, EVD-005 | RSK-002, RSK-004 | ACT-001, ACT-002 |
| implementation | partial | skills and helper scripts exist and pass focused checks | CLM-002, CLM-003, CLM-004, CLM-005 | EVD-003, EVD-004, EVD-005 | RSK-005 | ACT-005 |
| internal-review | partial | periodic skill-system audit and isolated reviews catch drift | CLM-002, CLM-005 | EVD-003 | RSK-001, RSK-005 | ACT-003 |
| artifact-release | partial | install command succeeds for Codex and Claude Code | CLM-005 | EVD-006 | RSK-001 | ACT-005 |
| maintenance | partial | docs, memory, sidecars, tags, telemetry, personalization writeback, source-card routing, publication audits, paper-layout protocols, visual-style memory, layered writing contracts, and commit closeout paths remain current | CLM-001, CLM-003, CLM-004, CLM-006, CLM-008, CLM-009, CLM-010, CLM-011, CLM-012, CLM-013, CLM-014 | EVD-004, EVD-006, EVD-007, EVD-010, EVD-011, EVD-012, EVD-013, EVD-014, EVD-015, EVD-016 | RSK-003, RSK-004, RSK-002, RSK-006, RSK-007, RSK-008 | ACT-001, ACT-004, ACT-006, ACT-011, ACT-012, ACT-013, ACT-014, ACT-015, ACT-016, ACT-017 |

## Stale Or Regressed Objects

| Object | Why stale/regressed | Required check | Owner | Updated |
|---|---|---|---|---|
| README/AGENTS/CLAUDE skill summaries | They drift whenever skills are added or behavior changes. | `python3 scripts/validate_skills.py` and manual summary check. | agent | 2026-05-05 |
| Installed global skills | They drift after skill commits unless reinstalled. | Prefer targeted `npx skills add ... -s <skill-name> -y`; use full reinstall when inventory or many skills changed. | agent | 2026-05-06 |

## Next Session Entry Point

- Open: `memory/current-status.md`.
- Verify: `git status --short --branch`.
- Then: run the relevant validation gates for the files being changed.
