# Method Spec Template

Use this template for the core design document.

## Method Identity

- Name:
- Short description:
- Design mode: method / objective / architecture / theory / system / revision
- Target claim:
- Baseline:
- Closest prior method to check:

## Problem Formulation

Define:

- data or input object:
- target output:
- model:
- training objective or evaluation objective:
- relevant variables:
- target regime:

## Baseline

State:

- baseline training:
- baseline inference:
- baseline objective:
- baseline assumptions:
- what remains unchanged:

## Proposed Method

Specify:

- new component:
- where it enters:
- equation, pseudocode, or algorithm:
- hyperparameters:
- schedules:
- constraints:
- inference-time behavior:

## Assumptions and Invariants

- Assumption A1:
- Assumption A2:
- Invariant I1:
- Invariant I2:

Use assumptions for scientific claims and invariants for implementation checks.

## Expected Effects

For each expected effect:

- metric or diagnostic:
- direction:
- mechanism explanation:
- alternative explanation:
- falsification condition:

## Components

| Component | Purpose | Required for claim? | Ablation | Diagnostic | Risk |
|---|---|---|---|---|---|
| C1 |  | yes/no |  |  |  |

## Complexity

- training cost:
- inference cost:
- memory:
- implementation complexity:
- additional data:

## Handoff

- implementation files:
- config flags:
- smoke test:
- logs:
- first experiment:
- exit condition:
