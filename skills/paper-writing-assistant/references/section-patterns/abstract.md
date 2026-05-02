# Abstract Patterns

Use this file when drafting or revising an abstract. The abstract should make the paper's promise, mechanism or study design, evidence, and scope clear without turning into a teaser.

## Default Abstract Moves

1. Problem or gap: what is hard, missing, or mismeasured.
2. Consequence: why the gap matters for the target community.
3. Contribution: what the paper introduces or establishes.
4. Mechanism or design: how the method, benchmark, study, or theory works at a high level.
5. Evidence: the strongest verified result, theorem, analysis, or benchmark finding.
6. Scope: what the evidence covers and what it does not claim.

## Method Abstract

Use when the paper sells a method, objective, architecture, training recipe, inference procedure, or algorithm.

- Start with a specific failure mode, not a broad field slogan.
- Name the method only after the reader understands the failure it addresses.
- Describe the core mechanism in one concrete sentence.
- Use evidence as claim support: say what setting tests the mechanism.
- End with scope or implication, not a second vague contribution claim.

Avoid:

- "We propose a novel framework" before the problem is clear.
- listing components without explaining the mechanism
- reporting numbers without baseline, task, or metric context

## Empirical Study Abstract

Use when the paper sells a finding rather than a new method.

- Open with the unresolved question.
- State why existing evidence is incomplete or confounded.
- Describe the study design or comparison axes.
- State the main finding and its implication.
- Mention robustness checks or controls if they are central to credibility.

Avoid:

- sounding like a survey unless the paper is a survey
- describing many experiments without a single takeaway
- turning a correlation into a causal claim

## Benchmark / Dataset Abstract

Use when the paper sells a new task, dataset, benchmark, or protocol.

- Open with what current evaluation cannot measure.
- State the benchmark's design principle.
- Describe data/protocol scale only after the capability gap is clear.
- Explain what baseline results reveal.
- End with what future work can now evaluate.

Avoid:

- leading with size alone
- claiming realism without evidence of data quality or validity
- omitting what the benchmark reveals beyond existing benchmarks

## Theory Abstract

Use when the paper sells a theorem, guarantee, bound, or impossibility result.

- Open with the conceptual or technical question.
- State the assumption regime in plain language.
- State the result shape and why it matters.
- Give proof intuition or consequence, not proof detail.
- Connect back to empirical or methodological implications if relevant.

Avoid:

- overloading the abstract with notation
- leaving the theorem's consequence implicit
- claiming practical impact beyond the assumption regime
