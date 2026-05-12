# Audit Rubric

## Inventory

- Every `skills/<name>/SKILL.md` has matching frontmatter name.
- Every implemented skill appears in README, AGENTS, and CLAUDE inventory tables.
- No top-level table lists non-existent skills.
- Skill names are lowercase hyphenated and stable.

## Lifecycle

Check whether the collection covers:

- project memory and coordination
- idea validation
- literature review
- algorithm design
- project/workspace setup
- experiment design
- baseline selection
- experiment execution
- result diagnosis
- experiment reporting
- figure/table review
- paper evidence board
- paper positioning
- venue-specific writing
- reviewer simulation
- citation coverage
- citation correctness
- submission
- real review and rebuttal
- camera-ready finalization
- artifact evaluation
- public release
- advisor/collaborator communication
- maintenance and retrospective

## Routing

- Each skill points to immediate upstream/downstream skills when useful.
- Pair-with sections are current.
- Stale "future" references are removed after implementation.
- Feedback loops are represented, especially experiments <-> writing <-> review <-> rebuttal.
- User-observed regressions are reflected in routing descriptions, not only buried in long references.
- Common failure vocabulary that should trigger a skill appears in the relevant `description` or project guidance.

## Memory

- State-changing skills have writeback expectations.
- Memory writes are durable summaries, not transcripts.
- Component memory paths are consistent.
- Claim/evidence/risk/action IDs remain meaningful across stages.

## Behavior Hardening

- Repeated agent mistakes have explicit stop conditions and fallbacks.
- Token-expensive loops are replaced with bounded artifacts, sidecars, wrappers, or project-local monitors.
- Stable wrapper command shapes exist when sandbox approvals, shell quoting, or equivalent command drift caused repeated failures.
- Runtime installation state is checked after skill behavior changes, not inferred from the repo diff alone.

## Validation

- Repository validator passes.
- Helper paths referenced by `SKILL.md` exist.
- Template placeholders are valid.
- Syntax checks pass for bundled scripts.
