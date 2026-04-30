# Venue Review Styles

These profiles are seed guidance. Always verify current official reviewer guidelines and review forms when scoring matters.

## Shared Top-Conference Review Axes

Most ML/AI venues evaluate:

- soundness and correctness
- novelty
- significance
- empirical or theoretical support
- clarity
- reproducibility
- related work
- ethics, broader impact, limitations, or societal considerations when required

Common rejection paths:

- contribution is incremental
- missing or weak baselines
- evidence does not support the central claim
- unclear problem motivation
- method is not reproducible
- theory assumptions are unrealistic or disconnected from experiments
- related work misses close prior work
- claims are too broad for the evidence

## NeurIPS

Reviewer style:

- broad ML significance matters
- reviewers expect strong evidence across settings
- diverse archetypes are acceptable, but the main claim must be important
- reproducibility, limitations, ethics, and checklist issues matter
- reviewers often ask whether the result changes how ML researchers think or build systems

Likely attacks:

- "The contribution is incremental for a broad NeurIPS audience."
- "The empirical evidence is too narrow."
- "The method is evaluated on weak or outdated baselines."
- "The theory does not explain the empirical results."
- "The paper does not discuss limitations or broader impact adequately."

## ICML

Reviewer style:

- technical precision and clean problem formulation matter
- method/theory/optimization claims are scrutinized closely
- reviewers value fair baselines, ablations, and controlled comparisons
- novelty should be stated technically, not rhetorically

Likely attacks:

- "The formal setup hides strong assumptions."
- "The algorithmic novelty over prior work is unclear."
- "Ablations do not isolate the proposed component."
- "The empirical gain may come from tuning rather than the method."
- "The theory is correct but too weak or disconnected from practice."

## ICLR

Reviewer style:

- conceptual insight matters
- OpenReview discussion can amplify unclear claims and assumption issues
- reviewers strongly probe baselines, reproducibility, and overclaiming
- simple ideas are welcome if the mechanism is clear and evidence is convincing

Likely attacks:

- "The core insight is not clearly distinguished from prior work."
- "The method works but the explanation is not convincing."
- "The claim is too broad for the experiments."
- "Important implementation details are missing."
- "The paper does not address obvious failure cases."

## CVPR / ICCV / ECCV

Reviewer style:

- benchmark strength and visual evidence matter
- method novelty is judged against fast-moving prior work
- qualitative examples, failure cases, and architecture/objective details are scrutinized
- dataset and evaluation protocol validity are important

Likely attacks:

- "The comparison is missing current vision baselines."
- "The improvement is marginal relative to method complexity."
- "Qualitative examples are cherry-picked."
- "The dataset or benchmark protocol is biased."
- "The method is not clearly reproducible."

## ACL / EMNLP / NAACL

Reviewer style:

- task definition, data validity, annotation quality, and evaluation design matter
- reviewers are sensitive to leakage, artifacts, prompt contamination, and ethics
- analysis and error categories often carry weight

Likely attacks:

- "The dataset contains artifacts or leakage."
- "The evaluation metric does not measure the claimed ability."
- "Human annotation quality is insufficiently documented."
- "The paper overclaims about language understanding or reasoning."
- "Ethics and limitations are underdeveloped."

## How To Use Venue Profiles

For every review:

1. identify the target venue
2. map the paper archetype to venue expectations
3. choose likely attack lines from the relevant profile
4. verify current official criteria when assigning scores
5. state uncertainty if no current review form was checked
