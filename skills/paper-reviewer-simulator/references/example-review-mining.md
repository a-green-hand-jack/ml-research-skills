# Example Review Mining

Use this reference when dynamically learning reviewer style from public reviews, OpenReview discussions, official reviewer guidelines, or accepted-paper examples.

The goal is to learn review behavior, not to copy review text.

## Source Priority

Prefer:

1. official reviewer guidelines and review forms
2. OpenReview reviews, meta-reviews, and author discussions for the same venue/year
3. public decision pages for accepted, oral, spotlight, and rejected papers when available
4. accepted papers in the same topic area
5. proceedings and call-for-papers pages

If OpenReview group pages are client-rendered, use OpenReview API/exported data, search results, direct forum URLs, or user-provided review links/PDFs.

## Sampling Strategy

Default sample:

- 3-5 reviews of topically similar papers
- 2-3 reviews of accepted/oral/spotlight papers in the venue
- 1-2 borderline or rejected examples if accessible
- official reviewer form/guidelines

If reviews are not public, inspect accepted papers and official criteria, then mark the review-style inference as weaker.

## Review-Style Matrix

Before simulating reviewers, create:

```markdown
| Source | Venue/year | Paper/topic | Decision/status | Review concern pattern | Score pattern | Useful lesson |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |
```

Keep entries paraphrased.

## What To Extract

From reviews:

- common strength wording
- common weakness categories
- how reviewers discuss novelty
- what baselines or ablations they demand
- how they treat theory assumptions
- how they treat unclear writing
- how confidence affects decision
- what meta-reviewers weigh most
- which issues survive rebuttal

From accepted papers:

- what claims were made acceptable by evidence
- how limitations were handled
- what appendix material supported main claims
- which benchmarks or proof styles were expected

## Output Summary

After mining examples, summarize:

```markdown
## Learned Review Style
- Venue/year:
- Sources checked:
- Dominant acceptance criteria:
- Common rejection triggers:
- Typical reviewer questions:
- Score calibration notes:
- How this applies to the user's paper:
```

## Safety and Copyright

- Do not quote long review text.
- Paraphrase review patterns.
- Include source URLs and access dates.
- Separate observed patterns from inferences.
