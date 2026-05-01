# Citation Coverage Taxonomy

Use this taxonomy to decide what kinds of references a paper must cover.

## Foundational Classics

Purpose:

- establish intellectual lineage
- show the authors understand the field
- prevent reviewers from seeing the work as ahistorical

Examples:

- original algorithm or theory
- standard architecture or objective
- canonical dataset, benchmark, or evaluation metric
- seminal survey or textbook result when primary citation is too broad

Reviewer risk if missing:

- "The paper ignores foundational work."
- "The authors appear unaware of the history of this problem."

## Closest Prior Work

Purpose:

- define novelty boundary
- show what is actually new
- preempt "this is just X" objections

Closest prior work usually shares:

- same task or problem
- same method family
- same theoretical object
- same benchmark or dataset
- same claimed insight

Reviewer risk if missing:

- "Novelty is unclear."
- "The paper does not compare to the closest work."
- "This seems previously known."

## Direct Competitors and Baselines

Purpose:

- justify experimental comparison
- make empirical claims credible
- show fair evaluation

Missing competitor citations can imply missing experiments.

Reviewer risk if missing:

- "Important baselines are missing."
- "Comparison is unfair."
- "The claimed improvement is not meaningful."

## Recent and Concurrent Work

Purpose:

- avoid stale related work
- acknowledge parallel discoveries
- show awareness of current venue/arXiv/OpenReview context

For fast-moving ML areas, search recent arXiv, OpenReview submissions, and last one or two conference cycles.

Reviewer risk if missing:

- "Several concurrent papers address the same problem."
- "The paper omits recent relevant work."
- "The claimed novelty is overstated."

## Dataset, Benchmark, and Metric Sources

Purpose:

- attribute data and evaluation protocols
- support reproducibility
- clarify exact benchmark version

Reviewer risk if missing:

- "Dataset source is unclear."
- "Metric/protocol is not properly cited."
- "Potential data leakage or version mismatch."

## Method and Tooling Components

Purpose:

- attribute components used inside the proposed method
- distinguish contribution from borrowed machinery

Examples:

- optimizer, model backbone, tokenizer, sampler, solver, library, prompt method, pretraining recipe

Reviewer risk if missing:

- "The method appears to claim existing components as novel."
- "Implementation is not reproducible."

## Theory and Proof Technique Sources

Purpose:

- connect assumptions, lemmas, bounds, or proof strategies to prior theory
- prevent reviewers from viewing a known theorem as new

Reviewer risk if missing:

- "The theoretical result is a restatement of known work."
- "Assumptions are standard but not cited."

## Negative or Limitation Citations

Purpose:

- support claims that prior methods fail, cannot handle a case, or lack a property

These are high risk. A negative claim needs strong support or careful wording.

Reviewer risk if missing:

- "The paper mischaracterizes prior work."
- "The claimed gap is not substantiated."

## Surveys and Taxonomies

Purpose:

- provide broad context
- organize related work when there are many variants

Do not use surveys as substitutes for closest primary papers.

Reviewer risk if missing:

- usually low, unless the area has a canonical taxonomy reviewers expect

## Venue-Specific Citations

Purpose:

- show awareness of papers accepted in the target community
- address likely reviewer familiarity

For NeurIPS/ICML/ICLR, recent OpenReview and proceedings papers can be especially important. For ACL/CVPR, anthology/proceedings and benchmark leaderboards often matter.
