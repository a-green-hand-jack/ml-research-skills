# Experiments and Results Patterns

Use this file when drafting or revising experiment setup, result prose, analysis sections, ablations, and result-facing captions.

## Experiment Section Sequence

1. Evaluation questions: map experiments to claims.
2. Setup: datasets, baselines, metrics, protocol, implementation, and compute details needed for trust.
3. Main results: answer the primary claim first.
4. Ablations or diagnostics: test mechanism and rule out alternatives.
5. Robustness or sensitivity: test scope and limits.
6. Qualitative or case analysis: explain behavior when helpful.
7. Summary: state what is supported, narrowed, or unresolved.

## Evaluation Question Paragraph

Job: prevent experiments from looking like a list.

Pattern:

- "Our evaluation asks three questions: [Q1 linked to CLM-001], [Q2 linked to CLM-002], and [Q3 linked to scope or robustness]."
- "The first tests whether [main claim]. The second isolates [mechanism]. The third probes [boundary condition]."

Avoid:

- "We conduct extensive experiments..."
- listing datasets before the reader knows what they test

## Setup Paragraph

Job: give enough protocol context for the first result.

Include:

- datasets/tasks and why they are appropriate
- baselines and what comparison each represents
- metrics and directionality
- split/protocol details that affect interpretation
- implementation details that affect fairness

Move to appendix:

- low-level hyperparameters unless they are part of the claim
- long dataset descriptions not needed for the first result
- secondary baselines that do not change the story

## Main Result Paragraph

Job: turn a figure/table into claim evidence.

Pattern:

1. State the claim or question.
2. Point to the figure/table.
3. Report the key comparison with setting and metric.
4. Interpret why the comparison supports the claim.
5. State mixed results or limits.

Avoid:

- "Table 1 shows the results."
- reporting every number in reading order
- claiming dominance from mixed or narrow wins

## Ablation Paragraph

Job: isolate the mechanism.

Pattern:

1. State the alternative explanation or design question.
2. Describe the ablation.
3. State the observed change.
4. Explain what this rules in or rules out.
5. Link back to the method claim.

## Negative or Mixed Result Paragraph

Job: preserve credibility while narrowing the claim.

Pattern:

1. State the mixed result plainly.
2. Identify the condition where the claim does not hold.
3. Explain whether the result contradicts, narrows, or contextualizes the claim.
4. State what evidence or future work would resolve it.
