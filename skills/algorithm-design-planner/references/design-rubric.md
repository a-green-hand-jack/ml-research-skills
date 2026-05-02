# Design Rubric

Use this rubric to turn an idea into a method design that can survive implementation and review.

## Problem Formulation

Check:

- What is the input?
- What is the output?
- What distribution, task, model family, or environment is assumed?
- What baseline is being modified?
- What failure or limitation of the baseline motivates the change?
- What quantity does the method optimize, estimate, constrain, or preserve?

Good formulation:

- names variables and objects
- states the baseline
- makes the target property measurable
- defines the regime where the method is intended to help

Weak formulation:

- says "improve performance" without specifying where or why
- changes the model without naming the baseline limitation
- has no falsifiable target property

## Mechanism

Check:

- What is the smallest new mechanism?
- Why should it change the target behavior?
- Which assumption makes the mechanism plausible?
- What would happen if the mechanism is removed?
- Could the same effect come from regularization, tuning, compute, data, or implementation detail?

Good mechanism:

- links cause to expected effect
- produces a diagnostic prediction
- is separable from tuning and compute

Weak mechanism:

- is only "add a module/loss"
- cannot explain when it should fail
- has no ablation or diagnostic

## Minimality

Check:

- Which parts are essential to the claim?
- Which parts are engineering convenience?
- Can the first prototype test only the essential part?
- Does the design introduce too many hyperparameters?

Prefer:

- core method first
- optional extension later
- one new conceptual variable at a time

## Baseline Relationship

State:

- unchanged baseline components
- modified components
- new parameters or compute
- new data or supervision
- training/inference differences
- fair comparison requirements

If the method changes multiple axes, mark this as a reviewer risk and plan controls.

## Cost and Practicality

Estimate:

- training overhead
- inference overhead
- memory overhead
- additional data or preprocessing
- implementation complexity
- sensitivity to hyperparameters

If cost is nontrivial, the method needs a quality/cost tradeoff claim.

## Design Decision

End with one of:

- `prototype`: design is ready for minimal implementation
- `revise`: mechanism or formulation needs change before coding
- `literature-check`: closest method may already exist
- `experiment-design`: design is specific enough to plan experiments
- `park`: blocked by resources or missing prerequisites
- `kill`: design cannot support a meaningful claim
