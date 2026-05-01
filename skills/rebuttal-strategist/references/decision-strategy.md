# Decision Strategy

Use this reference to decide what the rebuttal must accomplish.

## Goal

The goal is not to answer every sentence equally. The goal is to change the decision path.

## Decision State

Classify the current state:

- `likely-accept`: majority positive, rebuttal should avoid mistakes and fix minor issues
- `borderline-accept`: one serious concern could sink the paper
- `true-borderline`: mixed scores; one reviewer or AC synthesis likely decides
- `borderline-reject`: paper needs a strong response and evidence
- `likely-reject`: rebuttal may reduce damage but acceptance path is narrow

## Accept Path

Write the accept path explicitly:

```text
If we show [evidence], clarify [misunderstanding], and promise [revision], then R2 can move from weak reject to borderline/weak accept and the AC can justify acceptance based on [strength].
```

## Reject Path

Write the reject path explicitly:

```text
If reviewers continue to believe [core concern], the AC will likely reject because [reason].
```

## Prioritization Rules

Prioritize:

1. concerns shared by multiple reviewers
2. concerns from high-confidence negative reviewers
3. concerns likely to dominate AC summary
4. factual misunderstandings that can be corrected with evidence
5. quick new results that directly answer a reviewer question

Deprioritize:

- low-impact stylistic comments
- impossible new experiments
- broad philosophical objections
- reviewer preferences unrelated to venue criteria
- points already accepted by all other reviewers unless AC may care

## Response Budget

If the response is short:

- group repeated concerns
- answer pivotal issues first
- cite exact table/figure/appendix evidence
- avoid long literature review
- do not repeat reviewer text unless necessary

If per-review responses are allowed:

- start with each reviewer’s main decision-relevant issue
- answer direct questions succinctly
- cross-reference unified new experiments when appropriate

## AC-Oriented Framing

Include at least one sentence that helps the AC:

- name the strongest contribution
- see that the authors addressed shared concerns
- understand why remaining limitations do not invalidate acceptance

Avoid sounding like the paper is only promising future work. Rebuttal should rely on current or newly obtained evidence.

## Case-Derived Pattern: Mixed Scores Can Be Recoverable

Observed in a public ICLR 2024 OpenReview case:

- initial score pattern included one strong accept, two marginal accepts, and one marginal reject
- the marginal reject had high confidence and raised concrete issues about closest prior work, generalization, clarity, efficiency, and fairness
- authors supplied targeted new experiments, clarified methodology, and promised paper revisions
- the meta-review explicitly treated the author responses as satisfactory and recommended adding the new results and promised revisions
- final decision was accept poster

Use this pattern when analyzing a real rebuttal:

- Do not overreact to one negative review if it is concrete and addressable.
- Do prioritize a high-confidence borderline-negative reviewer because ACs may rely on that review to justify rejection.
- Make the accept path explicit: positive reviewers already value X; rebuttal must neutralize Y.
- Track promised revisions because ACs may condition acceptance confidence on them.
