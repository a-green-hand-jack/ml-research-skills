# Writing Contract Schema

Use this reference to instantiate the structure of a paper writing contract. The contract should describe how the paper will be written before `paper-writing-assistant` drafts prose.

## Core Contract Fields

Every contract should include:

- target venue and year
- primary audience
- primary archetype and optional secondary archetype
- one-sentence paper thesis
- primary and secondary claims
- claims to avoid
- section order
- paragraph recipes for core sections
- evidence slots and current status
- figure/table jobs
- related-work boundary
- limitation policy
- provisional result policy
- exemplar patterns
- open actions

## Archetype Structure Recipes

### Method Paper

Section order:

1. Introduction
2. Problem Setup / Background
3. Method
4. Experiments
5. Analysis / Ablation
6. Related Work
7. Limitations / Conclusion

Intro recipe:

- P1: task or setting importance
- P2: current method failure mode
- P3: key insight
- P4: method preview
- P5: evidence preview
- P6: contributions

Evidence slots:

- main comparison
- mechanism ablation
- fair baseline
- scope or robustness
- efficiency if claimed

Main visual:

- method overview figure or mechanism diagram

Main table:

- benchmark comparison table

### Theory-Guided Method Paper

Section order:

1. Introduction
2. Background / Formal Setup
3. Theory / Analysis
4. Algorithm or Design Derived from Theory
5. Experiments
6. Discussion / Limitations

Intro recipe:

- P1: phenomenon or modeling problem
- P2: missing principle or explanation
- P3: theory perspective
- P4: theory-derived method
- P5: theory validation and task evidence preview

Evidence slots:

- formal result
- assumption explanation
- theory-to-design bridge
- theory validation
- main task performance

Main visual:

- theory-to-method bridge diagram or assumption/regime diagram

### Empirical Study

Section order:

1. Introduction
2. Study Design
3. Finding 1
4. Finding 2
5. Finding 3
6. Implications / Recommendations
7. Related Work
8. Limitations

Intro recipe:

- P1: important unresolved question
- P2: why current evidence is incomplete or confounded
- P3: controlled study design
- P4: preview 3-5 findings
- P5: implication for practice or understanding

Evidence slots:

- research question
- controlled comparison
- breadth
- confounder checks
- finding replication

Main visual:

- study design map or finding summary figure

### Benchmark or Dataset Paper

Section order:

1. Introduction
2. Task Definition / Benchmark Goals
3. Data or Protocol Construction
4. Quality / Validity Analysis
5. Baselines and Main Results
6. Diagnostic Analysis
7. Ethics / Licensing / Limitations

Intro recipe:

- P1: current evaluation misses an important capability or failure mode
- P2: existing benchmarks are saturated, narrow, biased, or misaligned
- P3: new task or protocol
- P4: construction and validation principle
- P5: baseline results reveal new behavior

Evidence slots:

- evaluation gap
- construct definition
- data protocol
- quality checks
- baseline suite
- diagnostic slices

Main visual:

- benchmark/task schematic or data example panel

Main table:

- baseline suite with diagnostic categories

### Systems or Tooling Paper

Section order:

1. Introduction
2. Workload / Bottleneck
3. Design Goals
4. System Architecture
5. Implementation
6. Evaluation
7. Breakdown / Ablation
8. Limitations

Intro recipe:

- P1: real workload bottleneck
- P2: why existing systems/tools fail
- P3: design goals
- P4: system mechanism
- P5: evaluation preview with scale, speed, cost, or reliability

Evidence slots:

- workload bottleneck
- design goals
- end-to-end performance
- component breakdown
- scaling study
- hardware/workload details

Main visual:

- system architecture and critical path

Main table:

- end-to-end comparison with workload and hardware details

### Analysis / Interpretability / Diagnostic Paper

Section order:

1. Introduction
2. Phenomenon and Scope
3. Analysis Method
4. Evidence Chain / Findings
5. Controls / Interventions
6. Implications
7. Limitations

Intro recipe:

- P1: observed phenomenon
- P2: existing explanation is incomplete
- P3: diagnostic method or analysis frame
- P4: converging evidence and controls
- P5: implication for model understanding or design

Evidence slots:

- phenomenon demonstration
- analysis method
- converging evidence
- alternative explanations
- controls or interventions

Main visual:

- phenomenon figure plus control/intervention figure

### Application Paper

Section order:

1. Introduction
2. Domain Problem
3. Why Generic ML Fails
4. Method / Adaptation
5. Domain Evaluation
6. Case Study / Expert Analysis
7. Deployment / Limitations

Intro recipe:

- P1: precise domain pain
- P2: generic methods fail under domain constraints
- P3: technical adaptation
- P4: domain-relevant evaluation
- P5: case or deployment implication

Evidence slots:

- domain problem
- generic method failure
- technical adaptation
- domain metric
- credible baselines
- realistic split or setting

Main visual:

- domain workflow or case example

### Negative Result / Limitation Paper

Section order:

1. Introduction
2. Target Belief / Common Assumption
3. Experimental Design
4. Negative Findings
5. Robustness / Alternative Explanations
6. Implications
7. Recommendations / Limitations

Intro recipe:

- P1: widely held belief or common claim
- P2: why the claim matters
- P3: controlled test design
- P4: negative finding preview
- P5: implication for future evaluation or claim wording

Evidence slots:

- target belief
- faithful reproduction
- controlled failure
- robustness
- alternative explanations
- implication

Main visual:

- failure condition map or robustness matrix

## Hybrid Rule

Choose one primary recipe and at most one secondary recipe. If the primary recipe's blocker evidence is missing, change the archetype, narrow the claim, or create evidence actions before final writing.

Common hybrids:

- method + benchmark
- theory + method
- systems + method
- application + method
- benchmark + empirical study

## Contract Strength Labels

Use these labels for claims:

- `final-supported`: evidence is verified and sufficient
- `draft-supported`: evidence is user-stated or not fully verified
- `provisional`: intended evidence is pending
- `narrowed`: evidence supports a smaller claim
- `blocked`: blocker evidence is missing
- `cut`: do not write this claim

## Figure and Table Job Labels

Figure jobs:

- `main-story`
- `method-mechanism`
- `data-or-task-example`
- `result-summary`
- `ablation-or-control`
- `qualitative-evidence`
- `scope-or-limitation`

Table jobs:

- `main-comparison`
- `ablation`
- `benchmark-suite`
- `efficiency`
- `dataset-statistics`
- `system-scaling`
- `error-analysis`

Each figure/table should name the claim it supports and the section where it will be discussed.
