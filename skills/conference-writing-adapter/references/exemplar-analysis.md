# Exemplar Analysis

Use this reference when the user wants to learn from successful papers at a target conference or when a rewrite should be shaped by accepted, oral, spotlight, best-paper, or highly discussed examples.

The goal is not to imitate wording. The goal is to infer reusable writing moves: how successful papers at the venue make claims, allocate space, introduce theory, stage experiments, and preempt reviewer concerns.

## Sampling Strategy

Default sample size:

- 3-5 close exemplars: same topic, method family, or application area
- 3-5 venue taste exemplars: accepted/oral/spotlight/best-paper papers that may be topically farther away but reveal venue style
- 1-2 contrast examples when useful: papers in the same area with a different archetype

Selection priority:

1. target venue and target year
2. recent adjacent years if the current year has few relevant examples
3. oral, spotlight, award, notable, or highly discussed status
4. archetype diversity, not just popularity
5. availability of PDF, abstract, review discussion, or proceedings page

For OpenReview pages, static HTML may not contain paper data. Use API/exported data, official proceedings, search results, or user-provided PDFs/links when needed.

## Exemplar Style Matrix

Create a compact matrix before making rewrite recommendations:

```markdown
| Paper | Status | Archetype | Opening move | Core claim placement | Method style | Evidence order | Limitation handling | Relevance |
|---|---|---|---|---|---|---|---|---|
| [Title] | oral/spotlight/accepted | method/theory/... | ... | ... | ... | ... | ... | ... |
```

Keep entries short and paraphrased.

## What To Extract

For each exemplar, record:

- title and source URL
- venue status
- paper archetype
- one-sentence reviewer promise
- abstract move sequence
- introduction paragraph sequence
- method section shape
- theory/explanation balance
- role of the first figure
- where the main claim appears
- where assumptions and limitations appear
- how experimental evidence is ordered
- what material is pushed to appendix

## Cross-Paper Pattern Summary

After the matrix, synthesize:

```markdown
## Cross-Paper Patterns
- Pattern 1:
- Pattern 2:
- Pattern 3:

## Patterns Suitable For This Paper
- ...

## Patterns To Avoid
- ...
```

Patterns must be tied to the user's paper archetype. For example, do not recommend a benchmark-paper structure for a theory-driven method paper unless the user's real contribution is evaluation infrastructure.

## Theory-Driven Method Papers

When the user's paper applies a new theory to a concrete ML model family, such as MDLMs:

- learn how exemplars introduce a phenomenon before formalization
- check whether the venue favors theorem-first, intuition-first, or algorithm-first exposition
- inspect how much proof detail stays in the main text
- identify how the method section translates theory into an objective, diagnostic, sampler, schedule, or algorithm
- track how assumptions are defended in the main text

The final recommendation should say which style is being borrowed:

```markdown
Borrowed style:
- From close exemplars: [pattern]
- From venue taste exemplars: [pattern]
- Not borrowed: [pattern], because [reason]
```

## Copyright Safety

- Do not copy exemplar prose.
- Do not store long quotes.
- Keep notes paraphrased.
- Store titles, URLs, statuses, and short observations only.
