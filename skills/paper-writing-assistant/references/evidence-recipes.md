# Evidence Recipes

Use this file after selecting the paper archetype. It defines which experiments, analyses, proofs, figures, and tables are needed for each paper type, and how missing evidence should constrain writing.

The recipe is not a substitute for experiment design. It tells the writing assistant which evidence slots a claim needs, which missing slots should become provisional placeholders or actions, and which claims must be narrowed.

## Evidence Slot Status

Use these statuses when mapping evidence:

- `filled`: verified result/proof/artifact exists and can be cited in prose
- `user-stated`: user reported the evidence but source artifact is not yet checked
- `planned`: experiment or proof is planned but not run
- `running`: experiment is in progress
- `provisional`: temporary writing placeholder, must use `PR-###`
- `missing`: no credible evidence yet
- `contradicted`: available evidence weakens or refutes the claim
- `not-needed`: slot does not apply because the claim is not made

## Output Shape

When using this reference, create a compact map:

```markdown
## Evidence Recipe
- Archetype:
- Primary claim:
- Must-have slots:
- Should-have slots:
- Optional slots:
- Filled evidence:
- Missing or provisional evidence:
- Claims to narrow or avoid:
- Follow-up actions:
```

## Method Paper

Sells a new algorithm, model, objective, training recipe, inference procedure, or architecture.

### Must Have

- `main_comparison`: strong baselines on accepted tasks/datasets with fair protocol.
- `mechanism_ablation`: remove, replace, or vary the core component.
- `baseline_fairness`: same data, metric, tuning budget, compute, and evaluation protocol unless differences are stated.
- `scope_check`: at least one test beyond the easiest or original setting.

### Should Have

- `robustness`: seeds, dataset shift, model size, noise, hyperparameter sensitivity, or domain variation.
- `efficiency`: runtime, memory, parameters, training cost, or inference cost if the method implies efficiency.
- `qualitative_examples`: only when qualitative behavior supports a claim that metrics do not capture.

### Blocker If Missing

- no strong baseline while claiming superiority
- no ablation for the core mechanism
- only one narrow dataset while claiming generality
- efficiency claim without cost measurement

### Writing Consequences

- If `main_comparison` is missing, do not claim performance improvement; write the section as planned evaluation.
- If `mechanism_ablation` is missing, phrase mechanism as motivation, not demonstrated cause.
- If `scope_check` is weak, scope the claim to the tested regime.

## Theory-Guided Method Paper

Sells a theoretical insight that motivates a practical method.

### Must Have

- `formal_result`: theorem, proposition, derivation, or precise analytical claim.
- `assumption_explanation`: assumptions stated and defended in plain language.
- `theory_to_design`: method component derived from the formal result.
- `theory_validation`: experiment or analysis where the theory predicts a behavior.
- `main_task_performance`: evidence the method works on the real task.

### Should Have

- `assumption_stress_test`: vary settings where assumptions hold or break.
- `heuristic_comparison`: compare theory-derived design against a plausible heuristic.
- `mechanism_ablation`: remove the theory-motivated component.

### Blocker If Missing

- theory does not affect method design
- experiments do not test any theory-derived prediction
- assumptions are too remote from the empirical setting and not acknowledged

### Writing Consequences

- If `theory_validation` is missing, do not write that experiments confirm the theory; write that the theory motivates the design.
- If `main_task_performance` is weak, position as analysis or diagnostic paper rather than method paper.

## Empirical Study

Sells a finding about models, data, scaling, evaluation, or training behavior.

### Must Have

- `research_question`: one clear question or misconception.
- `controlled_comparison`: isolate variables rather than changing many factors together.
- `breadth`: multiple models, datasets, tasks, domains, or conditions.
- `confounder_checks`: alternative explanations and sensitivity analysis.
- `finding_replication`: key finding appears across more than one setting.

### Should Have

- `effect_size_or_uncertainty`: confidence intervals, variance, seeds, or practical magnitude.
- `decision_implication`: recommendation for model design, evaluation, or future work.
- `negative_controls`: cases where the effect should not appear.

### Blocker If Missing

- observations are not tied to a central finding
- no controls for the main alternative explanation
- results are organized by dataset/model instead of finding

### Writing Consequences

- If `confounder_checks` are missing, write "associated with" or "consistent with," not causal language.
- If `breadth` is narrow, write a case study or diagnostic framing rather than a field-level finding.

## Benchmark or Dataset Paper

Sells a new task, dataset, benchmark, protocol, or evaluation suite.

### Must Have

- `evaluation_gap`: clear capability or failure mode existing benchmarks miss.
- `construct_definition`: what the benchmark measures and what it does not.
- `data_protocol`: construction, filtering, annotation, validation, and splits.
- `quality_checks`: annotation quality, agreement, contamination, diversity, coverage, or difficulty.
- `baseline_suite`: simple baselines plus strong current methods.
- `diagnostic_slices`: categories or subgroups showing what the benchmark reveals.

### Should Have

- `human_or_oracle_reference`: where applicable.
- `adoption_protocol`: metric definitions, leaderboards, licenses, documentation, and reproducible evaluation.
- `failure_examples`: examples that clarify the measured capability.

### Blocker If Missing

- dataset is presented as valuable only because of size
- no validity evidence for the measured construct
- baselines too weak to reveal meaningful differences
- unclear licensing, data rights, or maintenance for a released artifact

### Writing Consequences

- If `quality_checks` are missing, do not claim high-quality data.
- If `diagnostic_slices` are missing, do not claim the benchmark reveals fine-grained model behavior.
- If `baseline_suite` is weak, frame results as preliminary.

## Systems or Tooling Paper

Sells a system, infrastructure, compiler, serving/training pipeline, or tool.

### Must Have

- `workload_bottleneck`: real workload and measured bottleneck.
- `design_goals`: latency, throughput, memory, cost, reliability, usability, or scale.
- `end_to_end_performance`: comparison against existing systems or common practice.
- `component_breakdown`: ablation of design components.
- `scaling_study`: scale users, devices, data, model size, requests, or workload.
- `hardware_workload_details`: enough detail to interpret results.

### Should Have

- `stress_test`: tail latency, failure modes, reliability, fault tolerance, or degraded conditions.
- `cost_analysis`: resource and operational cost.
- `usability_or_integration`: adoption friction, API compatibility, or migration cost.

### Blocker If Missing

- no end-to-end comparison
- no component breakdown
- hardware/workload hidden or under-specified
- improvement may be cherry-picked workload-specific behavior

### Writing Consequences

- Captions must include hardware, workload, metric, and units.
- If `component_breakdown` is missing, describe the design as a plausible system, not proven cause of improvement.
- If `scaling_study` is narrow, avoid "scales to" claims.

## Analysis / Interpretability / Diagnostic Paper

Sells an explanation of a model behavior or phenomenon.

### Must Have

- `phenomenon_demo`: show the phenomenon exists.
- `analysis_method`: define the diagnostic tool and scope.
- `converging_evidence`: multiple analyses pointing to the explanation.
- `alternative_explanations`: explicit tests against plausible alternatives.
- `controls_or_interventions`: negative controls, interventions, cross-model checks, or synthetic controls.

### Should Have

- `cross_model_or_dataset`: not tied to one model or dataset artifact.
- `failure_cases`: where the explanation breaks.
- `practical_implication`: what changes in design, evaluation, or interpretation.

### Blocker If Missing

- visually compelling evidence without controls
- correlation written as causation
- no alternative explanation handling

### Writing Consequences

- Without intervention/control evidence, write "suggests" or "is consistent with," not "shows that X causes Y."
- If evidence is one-model only, scope all claims to that model family.

## Application Paper

Sells a technically meaningful adaptation to a consequential domain problem.

### Must Have

- `domain_problem`: precise domain pain and why it matters.
- `generic_method_failure`: why off-the-shelf methods are insufficient.
- `technical_adaptation`: method, data, objective, interface, or evaluation change specific to the domain.
- `domain_metric`: metric meaningful to domain users.
- `credible_baselines`: prior ML, non-ML, expert, or standard-practice baselines.
- `realistic_split_or_setting`: deployment-like split, site, time, subgroup, or operating condition.

### Should Have

- `expert_or_case_analysis`: examples judged by domain criteria.
- `subgroup_robustness`: sites, cohorts, conditions, devices, time periods, or demographic groups.
- `constraint_analysis`: cost, latency, safety, interpretability, annotation burden, or workflow impact.

### Blocker If Missing

- reads as "apply existing model to domain"
- metric does not reflect domain utility
- no credible expert or domain baseline
- deployment readiness claimed without deployment-like evidence

### Writing Consequences

- If `technical_adaptation` is weak, position as application study or benchmark, not method novelty.
- If `realistic_split_or_setting` is missing, avoid deployment claims.

## Negative Result or Limitation Paper

Sells a carefully supported failure, non-result, limitation, or correction of a common belief.

### Must Have

- `target_belief`: the claim or assumption being tested.
- `faithful_reproduction`: credible implementation or reproduction of the tested method/belief.
- `controlled_failure`: conditions where the claim breaks.
- `robustness`: seeds, settings, implementations, or datasets.
- `alternative_explanations`: rule out bad tuning, bad baseline, bad implementation, or metric artifact.
- `implication`: why the negative result matters.

### Should Have

- `positive_control`: setting where the method or belief does work.
- `recommendation`: how future papers should evaluate or phrase claims.
- `release_artifact`: code/configs to make the negative result inspectable.

### Blocker If Missing

- failure may be implementation error
- tuning effort is not credible
- implication is too narrow or obvious

### Writing Consequences

- Do not write accusatory language toward prior work.
- State exactly what fails, under what condition, and what remains unresolved.

## Hybrid Papers

Most papers have secondary aspects. Choose one primary recipe and at most one secondary recipe.

Common hybrids:

- method + benchmark: method claim still needs ablations; benchmark claim still needs validity checks.
- theory + method: theory must influence design and experiments must test theory-derived behavior.
- systems + method: system metrics must be primary if the venue/audience evaluates systems.
- application + method: domain evidence must be strong enough to justify the application claim.
- benchmark + empirical study: benchmark quality plus findings must both be supported.

Rule:

- If two recipes require incompatible evidence, narrow the secondary claim.
- If the primary recipe's must-have slots are missing, change archetype or create actions before writing final claims.
