# Conference Profiles

These are seed profiles, not permanent truth. Always verify current official rules for the target year, and update project-local memory when new exemplar patterns are observed.

## Shared ML Conference Expectations

Most top ML venues reward papers that make the reviewer's evaluation easy:

- the main claim is visible by the end of the first page
- contributions are specific and testable
- experiments answer reviewer questions rather than follow implementation chronology
- baselines are credible and current
- limitations are specific enough to show scientific control
- figures and tables are designed as evidence, not decoration
- appendix carries reproducibility detail without hiding core evidence

## NeurIPS

Typical taste:

- broad ML relevance and strong evidence
- clear problem motivation for a wide but technical audience
- tolerance for diverse archetypes: method, benchmark, theory, systems, empirical study, analysis
- expectation that claims survive scrutiny across settings
- strong interest in dataset/model/evaluation implications when broadly useful

Writing implications:

- make the paper's general ML significance obvious early
- tie contributions to measurable evidence
- use the introduction to explain why the problem matters beyond one niche setup
- include careful limitations, ethics, and reproducibility details
- if the paper is specialized, explicitly state the general lesson

Common successful shapes:

- new method with broad experimental validation
- empirical finding that changes understanding of model behavior
- benchmark/dataset revealing a gap in current evaluation
- theory result with interpretable implications
- systems contribution enabling a new scale or capability

## ICML

Typical taste:

- technical clarity and disciplined claims
- method, theory, optimization, representation learning, and empirical ML contributions
- appreciation for clean problem formulation
- strong concern for fair baselines and ablations

Writing implications:

- state the formal setup cleanly and early
- avoid hype; make novelty technically precise
- connect experiments directly to the method's mechanism
- use ablations to prove the contribution is not incidental
- keep background concise unless it is needed for the formal contribution

Common successful shapes:

- method paper with crisp algorithmic novelty
- theory or optimization paper with clear implications
- empirical paper organized around a precise ML question

## ICLR

Typical taste:

- representation learning, deep learning, foundation models, reasoning, optimization, generative modeling, and interpretability
- conceptual clarity and intuitive explanation
- strong reviewer sensitivity to overclaiming and weak baselines
- OpenReview discussion makes rebuttal-readiness important

Writing implications:

- make the core insight memorable and easy to debate
- explain why the method or finding changes how readers think
- preempt obvious objections in the main text
- use figures to teach the idea, not only report results
- state limitations clearly because reviewers often probe them in discussion

Common successful shapes:

- method paper centered on a simple but powerful idea
- analysis paper revealing a deep-learning phenomenon
- empirical study with careful controls and a clear lesson

## CVPR / ICCV / ECCV

Typical taste:

- visual evidence, strong benchmarks, and clear task relevance
- method papers with convincing architecture/objective/design explanation
- dataset and benchmark papers with strong qualitative and quantitative inspection
- attention to comparison against current vision baselines

Writing implications:

- make figures carry the claim early
- show qualitative examples that reveal why the method works or fails
- keep method description grounded in the visual task
- ensure table organization highlights the most important comparison

## ACL / EMNLP / NAACL

Typical taste:

- clear task definition, linguistic or NLP relevance, evaluation rigor
- dataset and analysis papers are common when the research question is sharp
- strong concern for data quality, annotation, leakage, ethics, and reproducibility

Writing implications:

- define the task and data assumptions carefully
- explain annotation, evaluation, and possible artifacts
- use error analysis and qualitative examples to support quantitative claims
- avoid claims about language or reasoning that exceed the evidence

## What To Learn From Exemplar Papers

When studying accepted/oral/spotlight papers, extract:

- which archetype the paper uses
- how fast the abstract reaches the contribution
- the introduction move sequence
- the first figure's role
- contribution bullet grammar
- method exposition order
- experiment order
- how limitations are framed
- what appears in appendix rather than main text

Store these observations in project-local memory. Keep them paraphrased and tied to paper metadata.
