# Evidence Standards

Use this reference to decide how much evidence an experiment needs.

## Evidence Levels

### Internal Direction Check

Purpose:

- decide whether to continue an idea
- debug a mechanism
- choose between variants

Minimum evidence:

- one credible baseline
- one dataset or slice
- clear logging
- one or more seeds depending on noise

Do not overbuild; the goal is a decision.

### Paper Claim Support

Purpose:

- support a claim in a paper
- convince reviewers

Minimum evidence usually needs:

- strongest relevant baseline
- at least one simple baseline
- ablation isolating the claimed component
- multiple datasets/tasks when the claim is broad
- seeds, confidence intervals, or variance if results are noisy
- failure cases or limitations for broad claims

### Rebuttal Evidence

Purpose:

- answer a specific reviewer concern under time pressure

Minimum evidence:

- directly targets the concern
- uses same protocol as paper when possible
- small but credible table or analysis
- honest fallback if result is partial or negative

### Theory-Aligned Diagnostic

Purpose:

- test whether empirical behavior matches a theoretical prediction

Minimum evidence:

- measurable proxy for the theoretical quantity
- controlled setting where assumptions roughly hold
- counterexample or stress case if possible
- explanation of mismatch between theory and practice

## Claim Width

Match evidence to claim width:

- narrow claim: one setting may be enough
- method claim: multiple datasets/tasks and baselines
- generalization claim: varied domains, model sizes, or data regimes
- efficiency claim: runtime, memory, or compute comparison
- robustness claim: perturbations, shifts, or stress tests
- interpretability/analysis claim: controls and alternative explanations

If evidence is narrow, narrow the claim.

## Reviewer-Proofing

Strong experiment designs preempt:

- missing SOTA baseline
- unfair tuning
- one-dataset overclaim
- cherry-picked metric
- no variance
- no ablation
- hidden compute cost
- unclear train/validation/test split
- mismatch between claim and evidence
