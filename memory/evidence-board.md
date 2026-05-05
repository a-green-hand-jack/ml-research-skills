# ml-research-skills Evidence Board

Track evidence for project-level skill-system claims.

| ID | Kind | Status | Summary | Source paths | Supports | Weakens | Traced by | Certainty | Updated |
|---|---|---|---|---|---|---|---|---|---|
| EVD-001 | analysis | available | The repo previously lacked committed project memory; `memory/` was bootstrapped on 2026-05-05. | `memory/` | CLM-001 |  | PRV-001 | observed | 2026-05-05 |
| EVD-002 | review | available | A temporary isolated Codex reviewer test found concrete issues in a sample implementation, validating the writer/reviewer separation idea. | local temp artifact, conversation summary | CLM-002 |  | PRV-002 | observed | 2026-05-05 |
| EVD-003 | implementation | verified | `code-reviewer` includes review bundles, fresh CLI launcher guidance, Spark pre-review routing, and tests for bundle preparation. | `skills/code-reviewer/`, `tests/test_code_reviewer_bundle.py` | CLM-002 |  | PRV-002 | observed | 2026-05-05 |
| EVD-004 | implementation | verified | `sidecar-task-runner` creates prompt/input/output/model/decision artifacts and was used for a read-only cleanup preflight. | `skills/sidecar-task-runner/`, `tests/test_sidecar_task_runner.py` | CLM-003 |  | PRV-003 | observed | 2026-05-05 |
| EVD-005 | implementation | verified | `token-usage-auditor` reads Codex, Claude Code, and `.agent/sidecars/*/model.json` usage metadata without copying raw prompts. | `skills/token-usage-auditor/`, `tests/test_token_usage_auditor.py` | CLM-004 |  | PRV-004 | observed | 2026-05-05 |
| EVD-006 | validation | verified | Repository validation and targeted unit tests passed before recent commits. | `scripts/validate_skills.py`, `tests/` | CLM-005 |  | PRV-001 | observed | 2026-05-05 |
| EVD-007 | qualitative | available | User-provided LaTeX layout debugging summary distilled into a durable skill protocol for local, screenshot-driven paper layout fixes. | `skills/submit-paper/references/layout-debugging.md`, `skills/camera-ready-finalizer/references/final-submission-audit.md`, `skills/figure-results-review/SKILL.md`, `skills/table-results-review/SKILL.md` | CLM-006 |  | PRV-001 | user-stated | 2026-05-05 |

## Figures and Assets

| ID | Kind | Status | Location | Shows | Source paths | Traced by | Updated |
|---|---|---|---|---|---|---|---|
| FIG-001 | figure | current | README visual overview set | system overview, lifecycle workflow, project anatomy, memory bus, workspace architecture, tool loop, infra/audit layer, lifecycle variants, and visual asset index | `asset/README.md`, `asset/system-overview.png`, `asset/tool-memory-workflow.png`, `asset/project-anatomy.png`, `asset/memory-project-bus.png`, `asset/workspace-component-architecture.png`, `asset/tool-calling-loop.png`, `asset/infra-ops-audit-layer.png`, `asset/lifecycle-skills-overview.png`, `asset/lifecycle-system-collage.png` | PRV-003 | 2026-05-06 |
