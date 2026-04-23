# Evidence Model

Use this reference to decide how to turn raw project evidence into timeline blocks.

## Evidence Sources

Strong evidence:

- `git log` over the requested time window
- project docs updated during the same period
- experiment logs, progress notes, or decision logs
- user-provided status notes
- user-provided meeting notes or chat excerpts

Weak evidence:

- commit volume alone
- branch names without context
- one-line commit messages without file or doc context

## Ranking Rule

When sources disagree, prefer:

1. explicit user clarification
2. durable project docs or notes
3. git history plus touched files
4. inference from timing alone

## Block Construction Rule

A good timeline block usually corresponds to one of these:

- a feature or implementation phase
- a debugging or stabilization phase
- an experiment batch
- a paper-writing or reporting phase
- an infra or environment setup phase
- a planning or coordination phase

Avoid:

- one task per tiny commit
- one block that spans many unrelated goals
- attributing long date ranges from a single isolated commit

## Date Rules

- Use exact dates when commits, notes, or logs support them
- Use approximate ranges only when necessary
- If a range is inferred, say so in the text
- Do not fake precision by inventing exact day counts for planned work

## Multi-Project Rule

For multi-project reviews:

- keep separate project sections
- add a short allocation summary across projects
- avoid merging unrelated projects into one visual section unless the user explicitly wants a top-level "all work" view

## Mentor Report Rule

For mentor-facing reports:

- optimize for clarity and outcomes
- reduce low-level implementation noise
- explain why the work mattered
- link effort to deliverables, findings, or blockers

## Planning Rule

For forward planning:

- base plans on actual unfinished work, dependencies, and known goals
- distinguish committed work from optional work
- prefer milestone blocks over speculative micro-scheduling
