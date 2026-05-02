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

## Memory

- State-changing skills have writeback expectations.
- Memory writes are durable summaries, not transcripts.
- Component memory paths are consistent.
- Claim/evidence/risk/action IDs remain meaningful across stages.

## Validation

- Repository validator passes.
- Helper paths referenced by `SKILL.md` exist.
- Template placeholders are valid.
- Syntax checks pass for bundled scripts.
