# Paper Archetypes

Use this reference to decide which successful-paper shape the user's draft should follow. Most papers are hybrids, but the rewrite should choose one primary archetype so the reviewer knows how to evaluate the work.

## Method Paper

Reviewer expectation:

- a concrete technical novelty
- a clean problem setup
- intuition before machinery
- implementation details sufficient for reproduction
- experiments proving the method matters, not just that it works once

Best structure:

1. introduce the task and the failure of current methods
2. state the key insight in non-technical language
3. preview the method as a small number of components
4. define the formal setup
5. describe the method in the same order as the insight
6. evaluate on strong baselines and ablations
7. analyze when and why it works

Common writing failure:

- the introduction sells novelty before making the problem painful
- the method section is a code walk-through
- experiments are ordered by when they were run rather than by reviewer questions

## Empirical Study

Reviewer expectation:

- a crisp question
- principled experimental design
- breadth without appearing like a random survey
- careful controls
- findings that change what readers believe or do

Best structure:

1. state the misconception, open question, or practical decision
2. define the study axes and controls
3. preview 3-5 findings
4. organize sections by findings, not by datasets or model names
5. connect each finding to a design recommendation or scientific implication

Common writing failure:

- too many tables without a central thesis
- treating observations as explanations
- weak discussion of confounders

## Benchmark or Dataset Paper

Reviewer expectation:

- a gap in existing evaluation
- clear construction protocol
- evidence of quality, coverage, difficulty, and relevance
- baselines that reveal meaningful differences
- enough documentation for adoption

Best structure:

1. show why existing benchmarks are saturated, narrow, biased, or misaligned
2. define what the new benchmark measures
3. explain data/task construction and validation
4. demonstrate quality and difficulty
5. show baseline results and analysis
6. discuss maintenance, ethics, licensing, and limitations

Common writing failure:

- presenting a dataset as inherently valuable without showing what it reveals
- hiding annotation quality or contamination issues
- insufficient comparison with existing benchmarks

## Theory Paper

Reviewer expectation:

- a precise problem and assumption set
- theorem statements that are readable before proof details
- connection between formal result and ML relevance
- proof sketch in the main text when possible
- examples that make the assumptions concrete

Best structure:

1. motivate the formal question from a real modeling or learning issue
2. define the setup with minimal notation
3. state the main theorem and interpretation
4. explain proof intuition
5. compare with prior bounds or assumptions
6. include synthetic or illustrative experiments only when they clarify the theorem

Common writing failure:

- notation appears before motivation
- theorem statements are correct but not interpretable
- assumptions are not defended

## Systems Paper

Reviewer expectation:

- a real bottleneck or deployment pain
- design choices tied to constraints
- reproducible performance comparison
- ablation of system components
- clarity about scope, hardware, and workload

Best structure:

1. name the bottleneck and why common tools fail
2. state design goals
3. explain architecture through the critical path
4. evaluate latency, throughput, memory, cost, reliability, or usability
5. analyze tradeoffs and failure modes

Common writing failure:

- unclear novelty relative to engineering integration
- benchmark settings that look cherry-picked
- missing operational constraints

## Analysis or Interpretability Paper

Reviewer expectation:

- a focused phenomenon or question
- careful definitions
- multiple converging analyses
- negative controls and alternative explanations
- conclusions that do not overclaim causality

Best structure:

1. introduce the phenomenon and why it matters
2. define analysis tools and scope
3. organize by claims/findings
4. validate findings with interventions, controls, or cross-model checks
5. discuss limits of interpretation

Common writing failure:

- visually compelling but causally weak figures
- excessive speculation
- methods that cannot be reproduced

## Application Paper

Reviewer expectation:

- a consequential domain problem
- a real technical adaptation, not just applying an off-the-shelf model
- rigorous domain-specific evaluation
- comparison against credible non-ML or prior ML baselines
- clear deployment, annotation, or data constraints

Best structure:

1. motivate the domain pain precisely
2. explain why generic ML methods fail
3. describe the adaptation or modeling insight
4. evaluate with domain-relevant metrics and expert baselines
5. analyze cases that matter to domain users

Common writing failure:

- domain motivation is strong but ML novelty is weak
- evaluation uses convenient rather than meaningful metrics
- overclaiming deployment readiness
