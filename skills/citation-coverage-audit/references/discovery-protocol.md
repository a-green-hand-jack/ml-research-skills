# Discovery Protocol

Use this protocol to find missing citations systematically.

## Search Sources

Prefer primary or reliable scholarly sources:

- arXiv
- OpenReview
- Google Scholar, if available through browser/search snippets
- Semantic Scholar
- DBLP
- ACL Anthology
- PMLR
- NeurIPS proceedings
- CVF Open Access
- ACM Digital Library
- IEEE Xplore
- Springer
- project pages and GitHub repos linked from papers

Use venue pages and OpenReview for concurrent work when possible.

## Query Families

Run searches in several families:

### Claim Queries

Use the paper's novelty claim:

```text
"[core phrase]" machine learning
"[problem]" "[method family]"
"[task]" "[claimed property]"
```

### Component Queries

Search method components:

```text
"[component]" "[task]"
"[theory object]" "[model family]"
"[loss/objective/sampler]" "[domain]"
```

### Baseline Queries

Search benchmark and baseline terms:

```text
"[dataset]" "[metric]" "[task]" state of the art
"[benchmark]" "[method family]" arxiv
```

### Recent Work Queries

Search by time and venue:

```text
site:openreview.net "[topic]" ICLR 2026
site:openreview.net "[topic]" NeurIPS 2025
site:arxiv.org "[topic]" "[method]" 2025
"[topic]" "ICML 2025"
```

Adjust years to the current date and target venue. Always record the exact date searched.

### Citation Graph Queries

For each closest cited paper:

- search for the title plus "cited by"
- inspect related papers in Semantic Scholar or Google Scholar
- search the paper title with the target topic
- inspect the paper's references for classics

## Candidate Screening

For each candidate, inspect at least:

- title
- abstract
- venue/year
- method or contribution summary
- relationship to the user's claim

For high-risk candidates, inspect introduction, method, experiments, or theorem statements.

## Relevance Test

A candidate is relevant only if it maps to one or more roles:

- foundation
- closest prior work
- direct competitor
- baseline
- concurrent work
- dataset/benchmark/metric
- method component
- theory/proof technique
- negative claim support
- survey/taxonomy

If it does not map to a role, do not recommend it.

## Recency Policy

For "recent" or "concurrent", verify with browsing. The current date matters.

Default windows:

- current year and previous year for most ML topics
- last 6-9 months for very fast-moving topics
- last 24 months for theory or slower-moving areas

If the submission is to a specific conference, include papers from:

- previous year's same conference
- current OpenReview submissions if public
- recent arXiv papers before the submission deadline

## Search Log

Record:

```markdown
| Query | Source | Date | Useful hits | Notes |
|---|---|---|---|---|
```

This makes the audit reproducible and lets future agents update the scan.
