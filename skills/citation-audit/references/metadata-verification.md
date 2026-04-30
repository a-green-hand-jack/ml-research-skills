# Metadata Verification

Use this reference when checking whether BibTeX metadata matches the real cited work.

## Preferred Sources

Choose the most authoritative source available:

1. publisher or conference proceedings page
2. DOI resolver and CrossRef metadata
3. official repository such as arXiv, OpenReview, ACL Anthology, PMLR, CVF, ACM, IEEE, Springer, or NeurIPS proceedings
4. Semantic Scholar, DBLP, Google Scholar, or personal/project pages as secondary evidence

Use at least two sources for high-risk entries when possible.

## Field Checks

For every cited BibTeX entry, check:

- `title`: exact or publication-normalized title
- `author`: first author and approximate author list/order
- `year`: publication year or preprint year, clearly labeled
- `venue`: conference, journal, workshop, preprint server, or proceedings
- `doi`: resolves and belongs to the same work
- `url`: resolves and is not a stale personal copy when official URL exists
- `arxiv`: ID matches the paper and version if version matters
- `openreview`: forum URL or note URL matches the target paper

## Version Policy

Many ML papers have multiple versions:

- arXiv preprint
- OpenReview submission
- accepted conference version
- proceedings PDF
- journal extension

For submission references, prefer the accepted/proceedings version when it exists and is relevant. Keep arXiv when:

- no peer-reviewed version exists
- the paper is concurrent work
- the arXiv version contains material not in proceedings and the paper text explicitly needs that version

If the BibTeX cites arXiv but a peer-reviewed version exists, report it as `important`, not automatically blocking.

## DOI Checks

A DOI issue is blocking when:

- DOI does not resolve
- DOI resolves to a different title
- DOI resolves to a different work by different authors
- DOI belongs to an old conference abstract while the paper cites a full article

A DOI issue is a warning when:

- DOI is missing but the entry has an authoritative proceedings URL
- DOI is missing for arXiv/OpenReview-only work
- DOI metadata has minor punctuation/capitalization differences

## Venue Normalization

Normalize common ML venues consistently:

- NeurIPS: `Advances in Neural Information Processing Systems`
- ICML: `Proceedings of the International Conference on Machine Learning`
- ICLR: `International Conference on Learning Representations`
- ACL/EMNLP/NAACL: use ACL Anthology venue strings when available
- CVPR/ICCV/ECCV: use official proceedings names
- PMLR: include volume when available

Do not invent page numbers or volume numbers.

## Metadata Report Row

Use this shape for each checked entry:

```markdown
| Key | Status | Source checked | Issue | Action |
|---|---|---|---|---|
| smith2024method | PASS | DOI + proceedings | Metadata matches | none |
```

Status values:

- `PASS`
- `BLOCKING`
- `IMPORTANT`
- `WARNING`
- `UNVERIFIED`
