# Citation Coverage Audit Report Template

Use this template for saved reports or substantial chat reports.

```markdown
# Citation Coverage Audit

Date: YYYY-MM-DD
Paper root:
Target venue:
Topic:
Search horizon:

## Summary
- Overall coverage status:
- Must-cite missing:
- Should-cite missing:
- Recent/concurrent work checked:
- Highest novelty risk:

## Paper Citation Map
- Main claim:
- Core method/theory:
- Closest related work currently cited:
- Classic foundations currently cited:
- Recent/concurrent work currently cited:
- Datasets/benchmarks currently cited:
- Baselines currently cited:
- Sections with thin citation coverage:

## Search Log

| Query | Source | Date | Useful hits | Notes |
|---|---|---|---|---|

## Missing Citation Candidates

| Priority | Paper | Year | Role | Why it matters | Where to cite | Novelty impact | Action |
|---|---|---|---|---|---|---|---|

Priority values:

- `must-cite`
- `should-cite`
- `optional`
- `needs-author-review`
- `do-not-cite`

## Classic Work Coverage

## Closest Work Coverage

## Recent / Concurrent Work Coverage

## Benchmark, Dataset, and Baseline Coverage

## Novelty Claim Risk

| Claim | Current citation support | Missing work | Risk | Recommended change |
|---|---|---|---|---|

## Suggested Insertion Points

```latex
% Example only; verify BibTeX keys with citation-audit after editing.
...
```

## BibTeX Needed

## Papers Considered But Not Recommended

## Unresolved Author Decisions

## Next Steps
1. Add must-cite papers and adjust novelty wording.
2. Add should-cite papers if space allows.
3. Run `citation-audit` to verify BibTeX metadata and citation keys.
```

## Overall Status

- `GOOD_COVERAGE`: no must-cite gaps found
- `NEEDS_CITATIONS`: must-cite or high-risk should-cite gaps found
- `NEEDS_TOPIC_EXPERT_REVIEW`: several plausible gaps need author judgment
- `INCOMPLETE_SCAN`: search sources were unavailable or the paper was too incomplete
