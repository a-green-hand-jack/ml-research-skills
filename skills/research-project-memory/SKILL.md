---
name: research-project-memory
description: Maintain hierarchical ML research project memory. Use for claim, evidence, provenance, risk, action, handoff, worktree, phase, source-visibility, paper/code/slides, review, and rebuttal state.
argument-hint: "[project-root] [--bootstrap] [--closeout] [--check]"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Research Project Memory

Maintain project memory as a layered system, not a flat notes file. This skill gives agents a shared protocol for remembering what a research project is trying to prove, what evidence exists, what risks remain, and which component owns each next action.

Use this skill when:

- a project needs cross-session memory beyond remote execution state
- the user wants memory across `paper/`, `code/`, worktrees, `slides/`, reviewer simulation, or rebuttal
- claims, experiments, figures, paper sections, reviewer risks, and actions need to stay aligned
- a session materially changes project direction, evidence, writing, review risks, or planned experiments
- a new agent session needs bootstrap context before acting
- the user asks for a memory system, project state graph, claim/evidence board, worktree memory, or closeout protocol

This is a coordination skill. It does not replace `remote-project-control`, `experiment-design-planner`, `conference-writing-adapter`, `paper-reviewer-simulator`, or `rebuttal-strategist`; it tells them where and how to persist trusted project state.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── references/
│   ├── closeout-protocol.md
│   ├── consistency-checks.md
│   ├── claim-lifecycle-protocol.md
│   ├── cross-module-handoff-contracts.md
│   ├── evidence-provenance-protocol.md
│   ├── memory-architecture.md
│   ├── object-schemas.md
│   ├── paper-source-visibility-protocol.md
│   ├── phase-dashboard-protocol.md
│   └── writeback-protocol.md
└── templates/
    ├── component/
    │   ├── component-status.md
    │   ├── worktree-index.md
    │   └── worktree-status.md
    └── memory/
        ├── action-board.md
        ├── claim-board.md
        ├── component-index.yaml
        ├── current-status.md
        ├── decision-log.md
        ├── evidence-board.md
        ├── handoff-board.md
        ├── phase-dashboard.md
        ├── provenance-board.md
        ├── project.yaml
        ├── risk-board.md
        └── source-visibility-board.md
```

## Progressive Loading

- Always read `references/memory-architecture.md`, `references/object-schemas.md`, and `references/writeback-protocol.md`.
- Read `references/claim-lifecycle-protocol.md`, `references/evidence-provenance-protocol.md`, `references/phase-dashboard-protocol.md`, and `references/cross-module-handoff-contracts.md` when claims, evidence, project phase, paper writing, experiment planning, review, rebuttal, or cross-component handoffs are involved.
- Read `references/paper-source-visibility-protocol.md` when paper branches, Overleaf/GitHub sync, collaborator-visible source, anonymous submission source, arXiv, camera-ready source packages, or paper worktree cleanup are involved.
- Read `references/consistency-checks.md` when asked to audit project state, prepare a milestone, submit, write, review, or rebut.
- Read `references/closeout-protocol.md` before ending a substantial session or updating memory after meaningful work.
- Use `templates/` as the source of truth when bootstrapping missing memory files.

## Core Principles

- Memory is coordination context, not execution truth.
- Stable claims, decisions, risks, and component mappings belong in repo memory.
- Volatile facts such as dirty git state, queue state, active jobs, and file existence must be re-verified.
- Claims move through an explicit lifecycle from idea to final or cut; do not let paper prose silently use unsupported claims.
- Evidence must keep enough provenance to trace paper-facing tables, figures, captions, and result sentences back to CSVs, reports, runs, citations, analyses, or assets.
- Paper source visibility is a first-class policy. If a paper branch is linked to Overleaf or visible to coauthors, treat it as `author-visible`, not agent-private.
- The project phase dashboard gives the global cycle view; detailed boards still own the underlying claim, evidence, risk, action, provenance, and handoff objects.
- Cross-module handoffs should be explicit when work moves between idea, method, code, paper, slides, review, rebuttal, artifact, or release modules.
- Every important claim should link to evidence, a paper location, and current risks.
- Every reviewer or rebuttal risk should link to an action, a decision to accept the risk, or a reason it is out of scope.
- Every worktree should have a purpose and an exit condition: merge, continue, park, or kill.
- Paper version worktrees should also record target venue/release, submission mode, template/style differences, source visibility, cleanup requirements, and compile workflow.
- Agent-private paper state such as `.agent/`, `AGENTS.md`, `CLAUDE.md`, writing memory, raw CSVs, plotting scripts, internal result docs, and reviewer strategy must not be hidden in author-visible, submission, arXiv, or camera-ready source.
- Component-local memory is a rollup, not a replacement for project memory. `code/docs/ops/current-status.md` and `code/docs/ops/decision-log.md` can record code operational state, but cross-component and cross-worktree coordination should still be visible in root `memory/` and component `.agent/` indexes.
- Cross-worktree state has three levels: global registry in `memory/component-index.yaml`, component rollup in `<component>/.agent/worktree-index.md`, and leaf status in each `<component-worktree>/.agent/worktree-status.md`.
- GitHub Projects, when configured, are a collaborator-facing cloud board for issues, PRs, blockers, and roadmap/status views across component repos. They do not replace root `memory/`, component `.agent/`, or worktree memory.
- Mark certainty: `observed`, `user-stated`, `inferred`, `stale`, or `needs-verification`.
- Write memory at the most specific layer that will help the next session.

## Step 1 - Locate the Project and Existing Memory

Detect the project root:

```bash
git rev-parse --show-toplevel 2>/dev/null || pwd
```

Then inspect likely memory files:

- `memory/project.yaml`
- `memory/component-index.yaml`
- `memory/current-status.md`
- `memory/decision-log.md`
- `memory/claim-board.md`
- `memory/evidence-board.md`
- `memory/risk-board.md`
- `memory/action-board.md`
- `memory/provenance-board.md`
- `memory/handoff-board.md`
- `memory/phase-dashboard.md`
- `memory/source-visibility-board.md`
- `paper/.agent/`
- `paper/.agent/worktree-index.md`
- `code/.agent/`
- `code/.agent/worktree-index.md`
- `slides/.agent/`
- `reviewer/.agent/`
- `rebuttal/.agent/`
- GitHub Project URL/number in `memory/project.yaml`, if configured

If the project uses another layout, adapt the component paths but keep the same memory roles.

## Step 2 - Bootstrap Missing Memory

If the user asks to initialize memory, or if memory is missing and the task depends on it, create the minimum useful files from templates:

- `templates/memory/project.yaml` -> `memory/project.yaml`
- `templates/memory/component-index.yaml` -> `memory/component-index.yaml`
- `templates/memory/current-status.md` -> `memory/current-status.md`
- `templates/memory/decision-log.md` -> `memory/decision-log.md`
- `templates/memory/claim-board.md` -> `memory/claim-board.md`
- `templates/memory/evidence-board.md` -> `memory/evidence-board.md`
- `templates/memory/risk-board.md` -> `memory/risk-board.md`
- `templates/memory/action-board.md` -> `memory/action-board.md`
- `templates/memory/provenance-board.md` -> `memory/provenance-board.md`
- `templates/memory/handoff-board.md` -> `memory/handoff-board.md`
- `templates/memory/phase-dashboard.md` -> `memory/phase-dashboard.md`
- `templates/memory/source-visibility-board.md` -> `memory/source-visibility-board.md`
- `templates/component/component-status.md` -> `<component>/.agent/<component>-status.md`
- `templates/component/worktree-index.md` -> `<component>/.agent/worktree-index.md` when the component uses worktrees
- `templates/component/worktree-status.md` -> `<component-worktree>/.agent/worktree-status.md` when a code or paper worktree needs its own memory

Ask only for fields that cannot be inferred safely:

- project name
- project root
- component paths
- current research question
- current target venue or milestone, if any
- GitHub Project owner/title/URL/number, if the user wants cloud board integration
- whether memory files should be committed

## Step 3 - Build the Bootstrap Summary

Before substantial work, summarize:

- project name and root
- current research question and positioning
- target venue or milestone
- active components and paths
- current claim IDs
- current evidence IDs and latest reliable result
- current phase and active gate
- active provenance gaps and provisional results
- open cross-module handoffs
- paper source visibility surfaces and cleanup blockers
- top risks and blockers
- active actions and owners
- stale or missing memory
- facts that must be verified before acting

Keep the summary compact. Do not paste entire boards unless the user asks.

## Step 4 - Write to the Right Layer

Read `references/writeback-protocol.md`.

Use this routing:

- whole-project identity, target venue, component paths, memory policy -> `memory/project.yaml`
- GitHub Project board owner, URL, number, scope, and sync policy -> `memory/project.yaml`
- current focus, active milestone, next session entry point -> `memory/current-status.md`
- durable project decisions and why -> `memory/decision-log.md`
- paper claims and their status -> `memory/claim-board.md`
- experiments, analyses, proofs, citations, and figures that support claims -> `memory/evidence-board.md`
- raw-result, CSV, report, asset, caption, and prose traceability -> `memory/provenance-board.md`
- reviewer, novelty, baseline, writing, execution, and rebuttal risks -> `memory/risk-board.md`
- concrete next tasks and owners -> `memory/action-board.md`
- project phase, active gate, readiness, and next phase trigger -> `memory/phase-dashboard.md`
- cross-component producer/consumer payloads and acceptance checks -> `memory/handoff-board.md`
- paper source visibility tier, audience, sync target, allowed/forbidden files, and cleanup gate -> `memory/source-visibility-board.md`
- component-specific state -> `<component>/.agent/<component>-status.md`
- global worktree registry and root paths -> `memory/component-index.yaml`
- component-local cross-worktree rollup -> `<component>/.agent/worktree-index.md`
- code worktree purpose, or paper version policy and exit condition -> `<worktree>/.agent/worktree-status.md`

When in doubt, write a short pointer at the project layer and details in the component layer.

## Step 5 - Maintain the Claim-Evidence-Risk-Action Graph

Read `references/object-schemas.md`.
Read `references/claim-lifecycle-protocol.md` and `references/evidence-provenance-protocol.md` when a claim or evidence item changes.

Use stable IDs:

- `CLM-###`: claim
- `EVD-###`: evidence item
- `EXP-###`: experiment or run family
- `FIG-###`: figure or table
- `PRV-###`: provenance link from source data or analysis to evidence/assets/prose
- `RSK-###`: risk
- `ACT-###`: action
- `DEC-###`: decision
- `WTR-###`: worktree
- `REV-###`: review or rebuttal issue
- `HND-###`: cross-module handoff
- `VIS-###`: paper source visibility surface or policy

Every major update should preserve links:

```text
CLM-001 -> supported_by EVD-003 -> traced_by PRV-002 -> visualized_by FIG-002 -> threatened_by RSK-004 -> resolved_by ACT-007
```

Avoid orphan objects. If a claim has no evidence, mark it as `planned`, `evidence-needed`, `provisional`, or `cut`.

## Step 6 - Maintain Phase and Handoff State

Read `references/phase-dashboard-protocol.md` and `references/cross-module-handoff-contracts.md`.

Update `memory/phase-dashboard.md` when a project crosses or regresses across a major phase gate: idea validation, positioning, method design, implementation, experiment design, evidence production, paper asset building, drafting, internal review, submission, rebuttal, camera-ready, artifact release, or maintenance.

Update `memory/handoff-board.md` when one module produces payload another module should consume, such as method design to experiment design, experiment report to paper asset builder, evidence gap miner to experiment design, result asset builder to figure/table review, writing memory to section writers, reviewer simulator to evidence board, rebuttal strategist to experiments/writers, or camera-ready finalizer to artifact/release.

Each handoff should state producer, consumer, payload, source paths, expected output, acceptance check, staleness trigger, linked objects, and status.

## Step 7 - Maintain Paper Source Visibility

Read `references/paper-source-visibility-protocol.md`.

Update `memory/source-visibility-board.md` when:

- a paper branch or worktree is linked to Overleaf/GitHub
- `paper/main` is treated as collaborator-visible rather than private
- a venue, anonymous submission, arXiv, camera-ready, or publisher source worktree is created
- paper assets move from private generation sources into visible source
- `.agent/`, `AGENTS.md`, `CLAUDE.md`, raw CSVs, internal docs, plotting scripts, private paths, reviewer notes, or provenance files are found in a visible source surface

Use visibility tiers: `agent-private`, `author-visible`, `anonymous-submission`, `public-preprint`, `camera-ready-public`, and `publisher-artifact`.

## Step 8 - Run Consistency Checks

Read `references/consistency-checks.md` when auditing memory.

Check for:

- paper claims without evidence
- evidence without a claim or paper location
- evidence, tables, figures, captions, or result prose without provenance
- reviewer risks without actions
- rebuttal promises without paper/code follow-up
- cross-module handoffs that are ready but unconsumed, blocked without an action, or stale
- source visibility surfaces that contain forbidden agent/private files
- phase dashboard gates that contradict current claim/evidence/provenance/risk/action/handoff boards
- worktrees without exit condition
- worktrees missing from the global registry or component worktree index
- stale results still used in writing
- slides that contradict paper status
- volatile state recorded as stable truth

Report mismatches as project risks or actions.

## Step 9 - Close Out the Session

Read `references/closeout-protocol.md`.

Before ending a substantial session, update:

- `memory/current-status.md`
- `memory/phase-dashboard.md` if the active phase or gate changed
- any changed claim/evidence/provenance/risk/action/handoff board
- `memory/provenance-board.md` if a result, asset, caption, table, figure, or result sentence changed source or verification status
- `memory/handoff-board.md` if a module produced, consumed, blocked, or invalidated a handoff
- `memory/source-visibility-board.md` if a paper branch, worktree, Overleaf branch, submission source, or public source package changed visibility or cleanup status
- relevant component status file
- worktree status file if a code branch direction or paper version policy changed
- component worktree index and `memory/component-index.yaml` if worktrees were added, closed, parked, merged, or killed
- `memory/decision-log.md` if a durable decision was made

Closeout should answer: what changed, what is trustworthy, what is stale, what should the next agent verify, and what is the next concrete action.

## Final Sanity Check

Before finalizing:

- stable and volatile facts are separated
- new claims link to evidence or are marked `evidence-needed`, `provisional`, `parked`, or `cut`
- new evidence links to a claim, component, and source path
- new evidence has provenance or an action explaining what provenance is missing
- active phase and next gate are visible when the project is not in an initial state
- active cross-module handoffs have producer, consumer, acceptance check, and staleness trigger
- visible paper source surfaces have a visibility tier, allowed/forbidden file policy, cleanup gate, and latest audit status
- new risks link to actions or accepted-risk decisions
- worktree memory has a purpose and exit condition
- active worktrees appear in both the root registry and the relevant component worktree index
- current-status gives the next session a clear starting point
- no private local path or credential is written into shared memory unless the user explicitly wants it
