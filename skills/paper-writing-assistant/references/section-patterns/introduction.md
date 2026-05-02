# Introduction Patterns

Use this file when drafting or revising the introduction. The introduction should let a reviewer understand the paper's promise, why it matters, what must be believed, and what evidence will be used to evaluate it.

## Default Paragraph Sequence

### P1 - Problem in Context

Job: make the reader care about the concrete problem.

- Name the setting, not only the field.
- State the practical, scientific, or evaluation consequence.
- Avoid starting with an overly broad sentence that could begin any paper.

### P2 - Gap or Failure Mode

Job: explain why existing methods, evaluations, theories, or analyses are insufficient.

- Identify the condition where current approaches fail or current knowledge is incomplete.
- Be specific about whether the gap is empirical, methodological, theoretical, dataset-related, or systems-related.

### P3 - Insight or Hypothesis

Job: introduce the paper's central idea.

- State the mechanism, study hypothesis, benchmark design principle, or theorem intuition.
- Tie the idea to the gap from P2.

### P4 - Approach

Job: explain what the paper does.

- For methods, describe the method components in causal order.
- For studies, describe the comparison design.
- For benchmarks, describe task/protocol/data design.
- For theory, describe assumptions and result type.

### P5 - Evidence Preview

Job: preview the evidence that supports the main claim.

- Mention the main experimental setting, theorem, diagnostic, or benchmark result.
- Use exact numbers only if verified.
- If not verified, use a marked provisional placeholder.

### P6 - Contributions

Job: make the paper easy to evaluate.

- Each contribution should be claim plus evidence or artifact.
- Avoid contribution bullets that are only implementation descriptions.

## Opening Risks

Avoid:

- field-generic openings such as "Deep learning has achieved remarkable success"
- writing a literature review before the gap is defined
- introducing a method name before the failure mode
- promising broad generality before the evidence scope is established

## Contribution Bullet Pattern

Use:

- "We identify [failure/gap] in [setting] and show [evidence]."
- "We introduce [method/artifact], which [mechanism/design principle]."
- "We evaluate [claim] through [evidence type], finding [verified or provisional result]."
- "We provide [analysis/resource] that enables [specific future comparison or diagnosis]."

Avoid:

- "We are the first to..." unless the novelty claim has been checked.
- "Extensive experiments demonstrate..." without saying what they test.
- bullets that repeat section titles rather than claims.
