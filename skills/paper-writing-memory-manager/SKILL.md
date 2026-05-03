---
name: paper-writing-memory-manager
description: Maintain a dynamic writing memory for ML/AI papers across nonlinear drafting sessions. Use when writing state, section status, claim-to-text dependencies, edit impact, style/terminology decisions, open writing threads, stale prose, or cross-section change propagation must be tracked while sections, captions, tables, figures, claims, and evidence evolve.
argument-hint: "[paper-dir] [--mode init|snapshot|update|impact|handoff|close-session]"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Paper Writing Memory Manager

Maintain the paper's dynamic writing memory. This skill is the global state layer for nonlinear paper writing: it records what is being written, why wording changed, which claims appear where, which sections are stale, and what must be updated when evidence, claims, figures, tables, captions, or style decisions change.

Use this skill for:

- initializing `paper/.agent/writing-memory/`
- recovering the current writing state at the start of a session
- recording section status, paragraph status, caption/table/figure edits, and open writing threads
- mapping claims, evidence, results, figures, tables, captions, and paper locations into a dependency map
- deciding the impact of a local edit or new experiment result across the whole draft
- marking affected sections stale after claim/evidence/result changes
- recording style, terminology, rhythm, and venue-specific writing decisions
- handing off work between section-specific writing skills

Do not use this skill to write the prose itself. Use `paper-writing-assistant` and section-specific writing skills for drafting. Do not use it as the claim/evidence source of truth; use `paper-evidence-board` for claim/evidence status. Do not use it for long-term cross-project memory; use `research-project-memory` for project-level state.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── references/
│   ├── memory-schema.md
│   ├── update-protocol.md
│   └── impact-propagation.md
└── templates/
    ├── writing-state.md
    ├── section-ledger.md
    ├── dependency-map.md
    ├── edit-impact-log.md
    ├── style-and-terminology.md
    ├── open-writing-threads.md
    └── session-notes.md
```

## Progressive Loading

- Always read `references/memory-schema.md` and `references/update-protocol.md`.
- Read `references/impact-propagation.md` when a claim, result, table, figure, caption, title, abstract, or limitation changes.
- Use templates when initializing missing files under `paper/.agent/writing-memory/`.
- Read `paper/.agent/writing-contract.md`, `paper/.agent/paper-evidence-board.md`, `paper/.agent/evidence-completion-plan.md`, `paper/.agent/result-asset-provenance.md`, `paper/.agent/provisional-results.md`, and `paper/.agent/consistency-report.md` when present.
- Read target draft files only as needed for the requested section, paragraph, caption, table, or figure.

## Core Principles

- Writing is nonlinear; memory must preserve active threads, stale areas, and dependencies across sessions.
- A local edit can have global consequences. Record semantic impact, not just textual diff.
- The dependency map should make cross-section consistency tractable.
- Section status should distinguish `stable`, `draft`, `stale`, `blocked`, `missing`, and `needs-review`.
- Style and terminology decisions are part of writing memory because they affect future edits.
- Do not duplicate full paper text or long experiment reports. Store pointers, locations, IDs, and concise decisions.
- Every substantial writing action should leave a small memory trace: what changed, why, what it affects, and what remains open.

## Step 1 - Locate or Initialize Writing Memory

Find the paper root:

- `paper/` under a project control root
- current directory if it is the paper repo
- user-provided path

The memory directory is:

```text
paper/.agent/writing-memory/
```

If there is no `paper/` directory and the current directory is the paper repo, use:

```text
.agent/writing-memory/
```

Initialize missing files from `templates/`:

- `writing-state.md`
- `section-ledger.md`
- `dependency-map.md`
- `edit-impact-log.md`
- `style-and-terminology.md`
- `open-writing-threads.md`
- `session-notes.md`

## Step 2 - Build or Refresh the Writing Snapshot

Read `references/memory-schema.md`.

Create a compact snapshot:

```markdown
## Writing Memory Snapshot
- Venue:
- Paper archetype:
- Current positioning:
- Active writing focus:
- Stable sections:
- Draft sections:
- Stale sections:
- Blocked sections:
- Active claims:
- Recent evidence/result changes:
- Open writing threads:
- Highest-risk dependencies:
- Recommended next writing action:
```

Use local paper artifacts first. If no writing contract or evidence board exists, record that as a blocker and route to the appropriate skill.

## Step 3 - Update Section and Dependency Memory

For any writing action, update:

- `section-ledger.md`: status, claim roles, evidence dependencies, figures/tables, stale paragraphs, next action
- `dependency-map.md`: claim/result/evidence/asset IDs to paper locations
- `style-and-terminology.md`: new or changed terms, method names, caption style, claim-strength rules
- `open-writing-threads.md`: unresolved writing questions and blockers
- `edit-impact-log.md`: semantic change and affected locations
- `session-notes.md`: what happened in the current session

Keep entries concise and link to files/sections instead of copying long prose.

## Step 4 - Propagate Impact

Read `references/impact-propagation.md` when something changes.

Classify the changed object:

- claim
- result/evidence
- table
- figure
- caption
- method notation
- title/abstract/contribution
- related-work boundary
- limitation/scope
- terminology/style

Then mark affected locations:

- title
- abstract
- contribution bullets
- introduction
- method
- experiments/results
- figures/tables/captions
- related work
- limitations
- conclusion
- appendix

For each affected location, mark status: `update-needed`, `verify`, `stable`, `blocked`, or `cut-candidate`.

## Step 5 - Route the Next Writing Skill

Route by active thread:

- title/abstract/contribution -> `abstract-title-contribution-writer`
- introduction -> `paper-introduction-argument-writer`
- method explanation -> `method-section-explainer`
- results prose -> `experiment-story-writer`
- related work -> `related-work-positioning-writer`
- limitations/scope -> `limitations-scope-writer`
- result gap -> `paper-evidence-gap-miner`
- CSV-derived table/figure -> `paper-result-asset-builder`
- broad prose edit -> `paper-writing-assistant`
- full consistency pass -> `paper-draft-consistency-editor`

## Step 6 - Close the Session

At the end of a writing session, update `session-notes.md` and `writing-state.md`:

- what changed
- why it changed
- which dependencies were added or invalidated
- which sections are now stale or stable
- which evidence gaps remain
- next recommended action

## Final Sanity Check

Before finalizing:

- writing memory files exist and are compact
- active claims map to paper locations or are marked unplaced
- section statuses reflect current draft reality
- stale locations are explicitly marked after evidence or claim changes
- style and terminology decisions are recorded
- open writing threads have next actions
- other skills know what to do next
