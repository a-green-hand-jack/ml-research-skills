# Statistical Test Selection Guide for ML Papers

## Decision Tree

```
Are you comparing two methods on the same data (paired)?
├── Yes → Are the differences normally distributed?
│         ├── Yes, N ≥ 30 → Paired t-test
│         ├── Unknown or N < 30 → Wilcoxon signed-rank test
│         └── Binary outcomes (correct/incorrect per sample) → McNemar's test
└── No → Are you comparing more than 2 groups?
          ├── No (2 groups, independent) → Two-sample t-test or Mann-Whitney U
          └── Yes (> 2 groups) → Kruskal-Wallis + post-hoc (Dunn's test)

For comparing accuracy/BLEU/F1 averaged over multiple test instances?
→ Bootstrap confidence intervals are usually the safest choice

For comparing over multiple datasets or seeds?
→ Use the test above per dataset/seed comparison, then apply multiple-comparison correction
```

## Test Reference

### Paired t-test
- Use when: same test set, different models; N ≥ 10 paired observations; differences are approximately normal
- Assumption: pairs are independent; differences are normally distributed
- Limitation: sensitive to outliers; requires normality
- Effect size: Cohen's d = mean_diff / std_diff

### Wilcoxon Signed-Rank Test
- Use when: paired data, non-normal distribution, or small N (< 30)
- Assumption: pairs are independent; symmetric differences (but not necessarily normal)
- Effect size: Cliff's delta (r = Z / sqrt(N))
- Note: preferred for most ML comparisons where normality cannot be assumed

### McNemar's Test
- Use when: binary outcomes per sample (correct/incorrect) and two models are compared on the same test set
- Best for: sequence labeling, classification where per-sample correctness is available
- Effect size: odds ratio or relative risk

### Bootstrap Confidence Intervals
- Use when: normality is unknown, distribution is complex, or you want a distribution-free CI
- Method: resample with replacement N_bootstrap=10000 times; compute the statistic; take the 2.5th and 97.5th percentiles
- Use for: means, BLEU, F1, AUC, and any aggregate metric
- Advantage: works for any statistic; honest about uncertainty

### Permutation Test
- Use when: you want to test whether an observed difference is larger than expected by chance
- Method: randomly reassign labels N_perm=10000 times; compute the statistic; compare observed to permutation distribution
- Use for: situations where bootstrap assumptions may not hold

## Effect Size Conventions

### Cohen's d (continuous)
- Small: d ≈ 0.2
- Medium: d ≈ 0.5
- Large: d ≈ 0.8

### Relative improvement %
- More intuitive for ML audiences: "(Method A improves accuracy from 78.3 to 82.1, a 4.9% relative gain)"
- Always report the absolute baseline value alongside the percentage

### Cliff's delta (ordinal / non-parametric)
- Range: [-1, 1]
- Small: |δ| < 0.15
- Medium: 0.15 ≤ |δ| < 0.33
- Large: |δ| ≥ 0.33

## Multiple Comparison Corrections

When running K comparisons on the same data:

### Bonferroni Correction
- Adjust α to α/K
- Most conservative; use when false positives are very costly
- Example: 5 comparisons at α=0.05 → test at α=0.01

### Holm-Bonferroni Correction
- Sort p-values ascending: p(1) ≤ p(2) ≤ ... ≤ p(K)
- Reject p(i) if p(i) ≤ α / (K - i + 1)
- Less conservative than Bonferroni; recommended default

### Benjamini-Hochberg (FDR Control)
- Controls the expected proportion of false positives among rejected hypotheses
- More powerful than Bonferroni for large numbers of tests
- Appropriate for exploratory ablation batteries

## Seed Variance Reporting

For N seeds:

| N seeds | What to report | Caveat |
|---|---|---|
| 1 | Value only | "Single run; variance not characterized" |
| 2–4 | Mean and range [min, max] | "Limited seeds; std may be unreliable" |
| 5–9 | Mean ± std | Standard ML paper reporting |
| ≥ 10 | Mean ± std + 95% CI | Preferred for high-stakes claims |

## Power Analysis (Planning Mode)

To detect an effect of size d with power 0.8 and α=0.05 (two-tailed):

| Effect size (Cohen's d) | Required N (per group) |
|---|---|
| Large (0.8) | 26 |
| Medium (0.5) | 64 |
| Small (0.2) | 394 |

For ML comparisons where the effect is typically medium-to-large, 5–10 seeds per method is the practical minimum. For small expected effects, report the limitation explicitly.

## Common Mistakes to Avoid

- **Cherry-picking seeds**: always report all seeds, not just the best-performing ones
- **Significance theater**: reporting p < 0.05 with d = 0.05 — statistically significant but practically meaningless
- **Test-set snooping**: running many variants and reporting only the significant one inflates the type-I error
- **Ignoring paired structure**: if two models share a test set, always use paired tests — not independent sample tests
- **Non-corrected multiple comparisons**: 10 ablations at α=0.05 → expected ~0.5 false positives
