# Result Narrative Patterns

Use these patterns to choose experiment order and paragraph jobs.

## Claim-First Main Results

Best for method papers with one central empirical claim.

Section order:

1. Setup summary and metrics.
2. Main comparison table.
3. Claim interpretation.
4. Ablations explaining the mechanism.
5. Robustness or sensitivity.
6. Efficiency or cost.
7. Qualitative examples or failure cases.

Paragraph job:

- "We first ask whether..."
- "Table X shows..."
- "This supports the claim that..."

## Benchmark Leaderboard Plus Analysis

Best for benchmark, dataset, or evaluation papers.

Section order:

1. Benchmark design recap.
2. Overall leaderboard.
3. Category or slice analysis.
4. Model behavior findings.
5. Human or annotation quality checks.
6. Implications for future evaluation.

Writing pressure:

- Treat scores as evidence for benchmark usefulness, not only model ranking.

## Study Findings Sequence

Best for empirical studies.

Section order:

1. Study design and controls.
2. Finding 1.
3. Finding 2.
4. Finding 3.
5. Cross-finding synthesis.
6. Practical recommendation.

Writing pressure:

- Each subsection should read like an answer to a research question.

## Mechanism-First Ablations

Best when the paper's novelty is a design insight.

Section order:

1. Main result.
2. Ablation by component.
3. Ablation by training/inference condition.
4. Sensitivity or robustness.
5. Mechanism interpretation.

Writing pressure:

- Do not treat ablations as an appendix dump. They should explain why the method works.

## Systems Performance Stack

Best for systems/tooling papers.

Section order:

1. Experimental environment.
2. End-to-end performance.
3. Component contribution.
4. Scalability.
5. Cost/resource profile.
6. Reliability or usability.

Writing pressure:

- Tie each number to the system design principle it validates.

## Diagnostic or Failure-Mode Sequence

Best for analysis or limitation papers.

Section order:

1. Phenomenon reproduction.
2. Controlled factor analysis.
3. Boundary conditions.
4. Failure cases.
5. Recommendation or revised interpretation.

Writing pressure:

- Keep the constructive implication visible.
