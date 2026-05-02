# Search Protocol

Use this protocol to turn a broad topic into a traceable search plan.

## Inputs

Capture:

- target claim or topic
- seed papers or known baselines
- venues and communities
- time budget
- desired decision: novelty, baseline, positioning, or general field map

## Query Families

Build queries across these axes:

- exact method name and common abbreviations
- older terminology for the same idea
- task/domain terms
- objective/loss/architecture/inference terms
- benchmark, dataset, or metric terms
- theoretical concept names
- competing family names
- venue names plus the topic

For each family, write at least one broad query and one narrow query.

## Sources

Prefer primary or near-primary sources:

- arXiv for recent preprints and concurrent work
- OpenReview for ICLR, NeurIPS, ICML workshops, reviews, and discussion traces
- PMLR for ICML and AISTATS proceedings
- NeurIPS, ICML, ICLR, ACL Anthology, CVF, ACM, IEEE, and journal proceedings pages
- DBLP, Semantic Scholar, and Google Scholar for citation chaining
- authors' project pages only as pointers to papers, code, or updates

Use secondary sources only to discover paper names, not as evidence.

## Search Order

1. Seed-paper backward references for canonical roots.
2. Seed-paper forward citations for recent descendants.
3. Venue/proceedings search for the target community.
4. arXiv and OpenReview search for recent and concurrent work.
5. Baseline and benchmark search from evaluation protocols.
6. Terminology expansion after seeing new keywords.

## OpenReview and Venue Search

When venue culture or reviewer expectations matter:

- inspect accepted, spotlight, oral, or high-scoring papers in the relevant venue/year
- inspect reviews only to learn reviewer concerns, not to copy wording
- record whether a paper is accepted, rejected, withdrawn, workshop-only, or under review
- separate paper quality from relevance to the user's project

## Stopping Criteria

Stop when:

- the closest-work candidates have stabilized
- additional papers repeat the same method family
- baseline implications are clear enough for experiment design
- novelty risk is resolved or explicitly marked unresolved
- the sprint time budget is reached

Do not stop just because the first search query returns no direct match. Expand terminology before concluding novelty.

## Search Log Format

```markdown
| Date | Source | Query / path | Useful hits | Notes |
|---|---|---|---|---|
```

Mark facts as `verified`, `user-stated`, `inferred`, or `unverified`.
