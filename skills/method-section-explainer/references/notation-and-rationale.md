# Notation and Rationale

## Notation Introduction

Introduce notation when:

- it is used in the next few sentences
- it reduces ambiguity
- it is needed for an equation, theorem, or algorithm box

Avoid notation when:

- a plain-language description is clearer
- the symbol appears only once
- the symbol duplicates standard terms without helping

## Notation Flow

A stable order:

1. Dataset or input object.
2. Model or transformation.
3. Output or prediction.
4. Objective or loss.
5. Optimization or inference step.

Each notation block should answer:

- what the symbol represents
- its shape or domain when relevant
- why the reader needs it

## Equation Framing

Before an equation:

- state what the equation formalizes
- name the important terms

After an equation:

- explain the role of each non-obvious term
- connect the equation to the method's claim or design rationale

Do not let equations replace the prose argument.

## Algorithm Box Placement

Use an algorithm box when:

- the procedure has sequential steps
- implementation order matters
- reviewers need to compare the method to a baseline procedure

Avoid an algorithm box when:

- the method is better explained as architecture or objective
- the box would duplicate prose without adding clarity

## Design Rationale

Each major component should have one of:

- a theoretical reason
- an empirical motivation
- a practical systems reason
- a connection to prior limitations
- a direct link to an ablation

Weak rationale patterns:

- "to improve performance"
- "for robustness"
- "to make it efficient"

Stronger rationale patterns:

- state the failure mode
- state the design response
- state how the paper will test it

## Appendix Boundaries

Move detail to appendix when it is:

- necessary for reproduction but not for understanding
- a long derivation after the main idea is clear
- a complete hyperparameter/configuration list
- an extended proof
- a secondary implementation path

Main text should still include enough information for reviewers to understand the method's novelty and evaluate whether experiments test it.
