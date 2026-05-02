# Paper Method Bridge

Use this when the design needs to become a paper method section.

## Method Section Jobs

A method section should:

- define the problem and notation
- state the baseline briefly
- introduce the new mechanism
- explain why the mechanism is expected to help
- specify the training or inference algorithm
- name assumptions and constraints
- make implementation details reproducible
- avoid claims that need experiments before they are proven

## Paragraph Plan

Recommended structure:

1. Problem setup and notation.
2. Baseline recap focused only on what the method changes.
3. Core idea in one paragraph.
4. Formal method: equation, objective, module, or algorithm.
5. Training or inference procedure.
6. Practical implementation details.
7. Expected behavior and limitations.

For theory-guided methods, separate:

- principle or theorem
- practical approximation
- diagnostic prediction
- empirical claim

## Algorithm Box

Include:

- inputs
- outputs
- required hyperparameters
- main loop
- new operation or objective
- return value

Keep standard training boilerplate out unless it matters.

## Claims to Avoid Before Evidence

Avoid:

- "guarantees better performance" unless proved
- "solves" when the evidence only mitigates
- "the first" before citation coverage
- "efficient" without cost evidence
- mechanism explanations without diagnostics

Use:

- "is designed to"
- "targets"
- "we hypothesize"
- "we test whether"
- "under the following assumptions"

## Reviewer Preemption

Method prose should preempt:

- what is new relative to baseline
- why the added component is not arbitrary
- how many new hyperparameters exist
- whether inference cost changes
- which assumptions are required
- how the mechanism will be tested
