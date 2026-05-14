# Global Consistency Audit

Date: 2026-05-14
Repo: `/Users/jieke/Projects/project-skills`
Mode: audit + fix

## Scope

Full audit of the 57-skill collection (grew from 33 since 2026-05-02 audit). Dimensions checked:

- routing signal quality
- content-promise alignment
- internal and cross-skill reference integrity
- cross-skill handoff coverage
- memory writeback contracts
- body conciseness (500-line limit)
- frontmatter compliance

## Inventory

- Implemented skills: 57
- Documentation files checked: README.md, AGENTS.md, CLAUDE.md, `skills/*/SKILL.md`, `skills/*/references/`
- Validation command: `python3 scripts/validate_skills.py` → **Validated 57 skill(s); no issues found.**

## Lifecycle Coverage

The May 2 audit established a complete end-to-end lifecycle. Since then, 24 new skills were added:

| New Skill | Phase |
|---|---|
| run-status-monitor | experiment execution (monitoring) |
| sidecar-task-runner | infrastructure / utilities |
| personalization-memory | infrastructure / utilities |
| memory-publication-auditor | infrastructure / utilities |
| code-reviewer | implementation / pre-submission |
| token-usage-auditor | infrastructure / telemetry |
| safe-git-ops | project setup / git |
| reference-library-manager | literature / reference management |
| reference-reading-summarizer | literature / reference management |
| reference-project-synthesizer | literature → algorithm bridge |
| paper-evidence-gap-miner | result diagnosis / pre-compute audit |
| paper-result-asset-builder | result → paper assets |
| paper-writing-memory-manager | paper writing (coordination) |
| paper-writing-contract-planner | paper writing (pre-draft) |
| paper-writing-assistant | paper writing (prose) |
| paper-introduction-argument-writer | paper writing (intro) |
| method-section-explainer | paper writing (method) |
| limitations-scope-writer | paper writing (limitations) |
| related-work-positioning-writer | paper writing (related work) |
| abstract-title-contribution-writer | paper writing / submission prep |
| paper-draft-consistency-editor | paper writing (editing) |
| experiment-story-writer | result → results prose |
| latex-layout-issue-bundler | submission debugging |
| table-results-review | result review |

Coverage is complete. No real lifecycle gaps identified. Two structural observations:

- **Writing phase (9 skills)**: well-staffed but creates orchestration complexity; `paper-writing-memory-manager` serves as the coordination layer and is correctly paired by most writing skills.
- **Utilities cluster (5 skills)**: cross-phase enablers without lifecycle anchors; acceptable since they are infrastructure, not workflow steps.

## Findings Fixed

| Finding | Fix | Files |
|---|---|---|
| `memory-publication-auditor` line 63 routes to `skill-creator`, which does not exist as a real skill in the collection (was a broken symlink, removed 2026-05-14). | Updated route to `skill-system-auditor` for collection-level skill promotion, or user-manual creation. | `skills/memory-publication-auditor/SKILL.md` |
| `remote-project-control` had no routing to `run-status-monitor` despite being the natural upstream for job monitoring after server submission. | Added `run-status-monitor` to Pair-with section. | `skills/remote-project-control/SKILL.md` |
| `project-init` at 592 lines exceeded the 500-line SKILL.md limit. | Moved GitHub Projects API setup detail, worktree path policies, and memory layout tables to `references/project-structure.md`. | `skills/project-init/SKILL.md`, `skills/project-init/references/project-structure.md` |
| `reference-library-manager` and `reference-reading-summarizer` had no memory writeback guidance. | Added minimal writeback note: status updates go to `reference/.agent/processing-status.md`; project-level writeback is handled by `reference-project-synthesizer` after synthesis. | `skills/reference-library-manager/SKILL.md`, `skills/reference-reading-summarizer/SKILL.md` |

## Remaining Issues

| Issue | Severity | Recommendation |
|---|---|---|
| 11 writing/ops skills have WEAK memory writeback (mention `paper-writing-memory-manager` or memory boards but don't specify what entries to create). | low | Acceptable by design: `paper-writing-memory-manager` is the coordination layer. Each skill delegates writeback to it. Add specifics only if agents repeatedly miss state updates. |
| Writing phase orchestration (9 skills in sequence) has no overview diagram. | low | Consider adding a flow diagram to `asset/` if new contributors or agents frequently ask "which writing skill to use first". Not urgent. |
| `experiment-story-writer` doesn't explicitly mention routing to `paper-writing-memory-manager` for recording stale prose dependencies. | low | Add one-line routing note on next skill pass. |

## Real Gaps vs Hardening

| Item | Type | Rationale |
|---|---|---|
| End-to-end synthetic lifecycle test | hardening | Carried over from May 2 audit; validates skill handoff across full pipeline rather than per-skill. Still not in repo. |
| Writing-phase orchestration entry point | hardening | With 9 writing skills, a clearer "start here" flow in `paper-writing-memory-manager` or `paper-writing-contract-planner` would reduce agent confusion about sequencing. |
| Reference→algorithm design bridge clarity | hardening | `reference-project-synthesizer` bridges the gap but its routing to `algorithm-design-planner` is present and correct; no new skill needed. |

## Validation

```
python3 scripts/validate_skills.py
Validated 57 skill(s); no issues found.
```

Cross-skill references verified:
- `paper-draft-consistency-editor` and `paper-writing-contract-planner` both reference `paper-writing-assistant/references/` files — all 4 files exist ✓
- `project-init` reference to `<submit-paper-skill-dir>/scripts/check.sh` uses runtime path expansion — not a broken reference ✓

## Recommended Next Step

The collection is coherent. Priority order for follow-up:

1. Install updated skills (`npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -y`) to propagate fixes.
2. Add `experiment-story-writer` → `paper-writing-memory-manager` writeback note (one-liner, low effort).
3. Consider a writing-phase entry-point flow note in `paper-writing-contract-planner` if orchestration confusion arises in practice.
4. End-to-end synthetic lifecycle test remains the only real infrastructure gap.
