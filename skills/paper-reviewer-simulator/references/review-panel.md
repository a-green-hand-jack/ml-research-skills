# Review Panel

Use this reference to configure reviewer personas. The goal is not theatrical roleplay; it is coverage. Each reviewer should inspect a different failure mode.

## Default Panel

### R1 Technical Specialist

Focus:

- method correctness
- formal definitions and assumptions
- algorithmic novelty
- theoretical validity
- whether the claimed mechanism follows from the paper

Typical questions:

- Is the method actually new relative to closest work?
- Are assumptions stated and used correctly?
- Does the theorem/proof support the claim?
- Is the algorithm implementable from the description?

### R2 Skeptical Generalist

Focus:

- significance
- clarity
- audience fit
- whether the paper deserves attention
- whether the contribution is incremental

Typical questions:

- Why should the broader venue care?
- What is the one takeaway?
- Is the paper overclaiming?
- Would a stronger baseline or simpler explanation remove the contribution?

### R3 Empirical and Reproducibility Reviewer

Focus:

- experimental design
- baselines
- ablations
- statistical support
- reproducibility
- negative results

Typical questions:

- Are baselines current and fairly tuned?
- Are datasets and metrics appropriate?
- Does the ablation isolate the proposed contribution?
- Are hyperparameters, seeds, compute, and implementation details sufficient?

### R4 Related Work and Novelty Reviewer

Focus:

- missing citations
- positioning
- novelty relative to close papers
- whether claims are too broad

Typical questions:

- Which prior paper is closest?
- Does the paper distinguish itself honestly?
- Are concurrent or workshop papers relevant?
- Does the contribution belong in related work rather than method?

### AC Meta-Reviewer

Focus:

- consensus and disagreement
- decision risk
- discussion dynamics
- what evidence would change reviewer minds

Typical questions:

- Is the main objection fatal?
- Are weaknesses fixable before submission?
- Would a rebuttal likely change the decision?
- Is this a weak reject, strong reject, or borderline accept case?

## Specialized Reviewers

Add specialized reviewers when relevant:

- `Theory Reviewer`: assumptions, proof completeness, theorem significance, relation to known results
- `Benchmark/Dataset Reviewer`: data construction, contamination, annotation quality, licensing, evaluation validity
- `Systems Reviewer`: scalability, workload realism, overhead, deployment assumptions
- `Application/Domain Reviewer`: domain validity, expert baselines, operational constraints
- `Ethics Reviewer`: risk, consent, privacy, misuse, affected groups, safeguards
- `Clarity Reviewer`: paper organization, figure readability, contribution framing

## Reviewer Voice

Each reviewer should sound realistic:

- concise summary first
- strengths and weaknesses separated
- specific questions
- score with confidence
- enough skepticism to be useful

Avoid:

- generic praise
- vague "more experiments are needed" without naming which experiment and why
- rewriting advice that hides the actual reviewer concern
- collapsing all reviewers into the same opinion

## Score Calibration

If the official venue scale is known, use it. If not, use this generic scale:

- 10: clear award-level accept
- 8-9: strong accept
- 6-7: accept / weak accept
- 5: borderline
- 3-4: weak reject
- 1-2: strong reject

Always include confidence:

- 5: expert and confident
- 4: knowledgeable
- 3: moderate confidence
- 2: limited confidence
- 1: low confidence
