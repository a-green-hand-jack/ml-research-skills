# Decision Rules

Choose one final positioning decision.

## Decisions

`lock-position`
: The paper story, archetype, audience, claims, evidence, and closest-work boundary are coherent. Proceed to `conference-writing-adapter` or detailed drafting.

`revise-positioning`
: The paper remains viable, but title, abstract, main claim, figure order, related-work boundary, or contribution hierarchy must change.

`narrow-claim`
: Evidence supports a smaller claim than the current draft or user goal.

`change-archetype`
: The paper should become a different kind of paper, such as method to empirical analysis, method to diagnostic study, or theory paper to theory-guided method.

`need-evidence`
: The best story depends on a missing baseline, ablation, figure, theorem, dataset, or literature check.

`park-paper`
: There is no coherent publishable story yet with current evidence.

## Lock Requirements

Use `lock-position` only when:

- primary contribution is clear
- closest-work distinction is credible
- main evidence supports the primary claim
- fatal baseline and figure risks are resolved or accepted
- target audience is explicit
- claims to avoid are known

## Narrowing Triggers

Choose `narrow-claim` when:

- evidence covers one dataset, scale, or metric
- result is single-seed or preliminary
- missing baselines block a broad claim
- theory diagnostic is suggestive but not decisive
- figure review shows overclaiming

## Archetype Change Triggers

Choose `change-archetype` when:

- method performance is weak but analysis is strong
- theory is interesting but method gains are small
- benchmark/protocol contribution is stronger than method novelty
- negative results are more valuable than the original method
- the strongest evidence answers a different question from the draft

## Need Evidence Triggers

Choose `need-evidence` when:

- two plausible stories depend on one missing result
- closest-work comparison is unresolved
- main figure is not ready
- baseline fairness is not established
- the venue fit depends on current accepted-paper patterns
