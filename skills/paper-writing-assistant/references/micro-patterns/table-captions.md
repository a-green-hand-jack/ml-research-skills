# Table Captions

Use this file when writing or revising table captions. A table caption should make the comparison question, protocol, metrics, and main takeaway explicit.

Coordinate with `table-results-review` when the question is whether the table values, bolding, row/column semantics, or provenance are correct.

## Main Comparison Table Caption

Pattern:

1. Comparison question: what claim the table tests.
2. Protocol sentence: datasets, splits, metrics, and evaluation setting.
3. Formatting sentence: arrows, bolding, underlining, confidence intervals, or missing values.
4. Takeaway sentence: which comparison supports the claim.
5. Scope sentence when results are mixed or settings are not comparable.

Avoid:

- "Performance comparison" as the full caption.
- hiding important protocol differences only in surrounding prose.
- saying "best" without defining metric direction and comparison set.

## Ablation Table Caption

Pattern:

1. State the mechanism or design question.
2. Define rows as component removals, replacements, or controls.
3. Define columns as metrics or settings.
4. State what change isolates the component's role.

## Efficiency Table Caption

Pattern:

1. State the operational question: latency, memory, throughput, cost, or compute.
2. Define hardware, batch size, model size, or workload if relevant.
3. State the tradeoff rather than only the fastest number.
4. Connect the tradeoff to the systems or method claim.

## Caption Anti-Patterns

Avoid:

- reporting all table entries in the caption
- making a global claim from one dataset column
- omitting whether higher or lower is better
- hiding non-comparable baselines without a note
