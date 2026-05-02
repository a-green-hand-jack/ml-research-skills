# Result Interpretation and Claim Bridges

Use this file when converting results into prose. The purpose is to connect evidence to claims without overclaiming.

## Main Result Bridge

Pattern:

1. "Table/Figure X evaluates [claim] by measuring [metric] on [setting]."
2. "Compared with [baseline/control], [method/artifact] [observed change]."
3. "This supports [claim] because [mechanistic or evaluation reason]."
4. "The effect is strongest/weaker under [condition], suggesting [scope]."

## Mechanism Bridge

Use for ablations, diagnostics, or analysis.

Pattern:

- "If [alternative explanation] were responsible, we would expect [counterfactual]. Instead, [observed result], which indicates [mechanism]."
- "Removing [component] changes [metric/behavior], showing that [component role] is not merely an implementation detail."

## Scope Bridge

Use when results are mixed.

Pattern:

- "These results support [narrow claim] rather than [broader claim]."
- "The gain does not appear in [setting], which suggests that [boundary condition]."
- "We therefore state the claim as [scoped claim]."

## Provisional Result Bridge

Use only when a missing result is allowed as a writing scaffold.

Pattern:

- "The intended test is whether [claim] holds on [setting]. % PROVISIONAL-RESULT PR-###"
- "[PR-###: pending verified result comparing METHOD to BASELINE on DATASET for METRIC]"

Never write a provisional number as observed evidence.

## Result Sentence Anti-Patterns

Avoid:

- "Our method significantly outperforms all baselines" without dataset, metric, baseline, and statistical meaning.
- "This proves that..." for empirical evidence unless the paper truly provides a proof.
- "The results validate our approach" without explaining what alternative was ruled out.
- "We achieve state of the art" when the baseline set or protocol is incomplete.
