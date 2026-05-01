# Review Intent Analysis

Use this reference to infer what each reviewer is trying to do.

## Reviewer Stance Labels

- `champion`: clearly likes the paper and may defend it
- `likely-accept`: positive but has fixable concerns
- `borderline-persuadable`: mixed review; can move with evidence or clarification
- `skeptical-fixable`: negative but objections are concrete and addressable
- `likely-reject`: rejects core contribution, evidence, or novelty
- `unmovable-reject`: objections require unrealistic new work or reject the premise

## Signals

Positive signals:

- acknowledges importance or novelty
- asks concrete clarifying questions
- score is moderate/high with medium/high confidence
- weaknesses are mostly presentation or limited ablations
- says "I would like to see" rather than "the paper fails to"

Negative signals:

- rejects core premise or significance
- calls work incremental or not novel
- identifies missing closest baseline or known prior work
- questions correctness of theorem/method
- asks for broad new experiments impossible during rebuttal
- high confidence with low score

Persuadable signals:

- score near borderline
- low or medium confidence
- misunderstanding of paper that can be corrected
- requests a specific result already available or quick to obtain
- praises contribution but worries about one major issue

## Intent Questions

For each reviewer, answer:

- Do they understand the paper's main claim?
- Do they believe the problem matters?
- Do they believe the method is novel?
- Do they believe the evidence supports the claim?
- Are their concerns factual, interpretive, or preference-based?
- What single response would most improve their stance?
- Are they asking for small fixes or building a rejection case?

## Reviewer Intent Map

```markdown
| Reviewer | Score/confidence | Stance | Core concern | Persuadable? | Best move |
|---|---|---|---|---|---|
```

## Misunderstanding vs Real Weakness

Misunderstanding:

- reviewer missed text already in paper
- reviewer asks a question answered in appendix
- reviewer compares against an irrelevant method
- reviewer misstates the method

Real weakness:

- paper did not make the point clear enough
- baseline/ablation is genuinely missing
- theorem assumption is unstated or too strong
- novelty boundary is underdeveloped

In rebuttal, even misunderstandings should usually be framed as a clarity problem the authors will fix.
