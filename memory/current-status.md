# ml-research-skills Current Status

> Cross-session working memory. Re-verify git state before acting.

## Current Focus

- Summary: The repository is in skill-system hardening mode, with sidecar execution, code-reviewer isolation, token telemetry, toolchain gates, and now repo-native project memory.
- Active milestone: make the skill collection self-maintaining through memory, sidecar task artifacts, validation gates, and clear public/private boundaries.
- Current phase: `maintenance`.
- Active gate: keep README/AGENTS/CLAUDE, skill inventory, tests, and memory aligned before commit/push.
- Last updated: 2026-05-06.

## Latest Reliable State

- 51 skills are present and installable.
- `sidecar-task-runner` exists and was installed globally for Codex and Claude Code on 2026-05-05.
- `code-reviewer` supports Spark pre-review plus strong isolated review.
- `token-usage-auditor` supports Codex, Claude Code, and repo-local sidecar metadata.
- `add-git-tag` can use read-only sidecar proposal generation while preserving human gates for tag creation and push.
- `asset/` images are tracked with semantic file names; README embeds the system overview, execution loop, project anatomy, memory bus, workspace architecture, infra/audit layer, and detailed workflow panels.
- `asset/README.md` indexes each public diagram's role, README placement, and maintenance rules.
- Local `.agent/sidecars/` artifacts are private/local and excluded from this repo's tracked files.
- `submit-paper` now includes a screenshot/page/object-first LaTeX layout debugging protocol, with short pointers from camera-ready, figure review, and table review skills.
- `latex-layout-issue-bundler` now creates `.agent/layout-issues/` bundles so PDF layout problems can be handed to agents without manual screenshots.

## Top Open Risks

- `RSK-001`: Skill inventory drift between `skills/`, README, AGENTS, CLAUDE, and installed runtime copies.
- `RSK-002`: Sidecar output could be over-trusted for high-risk design or final review decisions.
- `RSK-003`: Private local facts or agent session logs could leak into public shared memory.
- `RSK-004`: Memory could become stale if not updated after skill behavior changes.

## Active Actions

- `ACT-001`: Keep project memory current after meaningful workflow or skill-system decisions.
- `ACT-002`: Add sidecar execution contracts gradually to high-value mechanical skills.
- `ACT-003`: Periodically run `skill-system-auditor` against this repo.
- `ACT-004`: Keep token telemetry tied to artifacts and outcomes, not treated as quality by itself.
- `ACT-006`: Keep LaTeX layout debugging guidance aligned across paper submission, camera-ready, figure, and table review skills.
- `ACT-007`: Keep README visual panels aligned with renamed `asset/` files.
- `ACT-008`: Use `asset/README.md` as the entry point before changing public diagram assets.
- `ACT-009`: Use `latex-layout-issue-bundler` before screenshot-based LaTeX layout debugging when a rendered PDF is available.

## Needs Verification Next Session

- `git status --short --branch`
- `python3 scripts/validate_skills.py`
- Relevant unit tests for any changed helper scripts.
- Whether installed `~/.agents/skills/` and `~/.claude/skills/` copies need refresh after skill changes.

## Next Step

- Commit, push, and reinstall after adding `latex-layout-issue-bundler`.
