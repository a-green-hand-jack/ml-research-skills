# Citation Claim Audit

Use this reference when checking whether a cited paper actually supports the sentence, paragraph, or claim where it appears.

This is a semantic audit. It cannot be fully automated by BibTeX metadata checks.

## Citation Context Extraction

For each citation key, inspect the sentence containing the citation and, when needed, the previous and next sentence.

Classify the citation role:

- `background`: general field context
- `method-existence`: shows that a method or idea exists
- `closest-related-work`: the cited work is a direct comparison point
- `result`: supports a claimed empirical result
- `theory`: supports a theorem, assumption, bound, or proof technique
- `dataset-benchmark`: cites data, benchmark, metric, or evaluation protocol
- `negative-claim`: supports a limitation, failure, impossibility, or gap
- `state-of-the-art`: supports strongest-known or leading-performance language
- `baseline`: justifies a baseline choice
- `implementation`: supports a codebase, tool, hyperparameter, or recipe

## Risk Levels

High-risk contexts require stronger checking:

- novelty claims: "first", "only", "novel", "unlike prior work"
- strength claims: "state-of-the-art", "best", "significantly", "substantially"
- theory claims: "guarantees", "proves", "converges", "consistent", "optimal"
- negative claims: "fails to", "cannot", "does not address"
- direct comparison: "X is more efficient than Y"
- evidence claims in abstract, introduction contribution bullets, or conclusion

Low-risk contexts:

- broad background citations
- citations in lists of related areas
- standard method attribution, when phrased narrowly

## Support Labels

Use these labels:

- `SUPPORTED`: cited work clearly supports the local claim
- `PARTIALLY_SUPPORTED`: cited work supports a narrower version
- `UNSUPPORTED`: cited work does not support the claim
- `WRONG_TARGET`: citation points to a different paper/version
- `NEEDS_BETTER_CITATION`: claim may be true but this citation is not the best support
- `UNVERIFIED`: source could not be accessed

## Audit Method

For each high-risk citation:

1. read the local sentence and identify the exact claim
2. open the cited paper's abstract/introduction
3. inspect the relevant method/result/theory section when needed
4. decide whether the paper supports the local claim
5. propose a minimal correction

Minimal corrections:

- weaken the prose
- replace the citation
- add a second citation
- move the citation to a less specific sentence
- add "e.g." when the citation is illustrative rather than exhaustive
- mark `[AUTHOR VERIFY]` when domain judgment is required

## Claim Audit Row

Use this shape:

```markdown
| Location | Citation | Local claim | Role | Support | Action |
|---|---|---|---|---|---|
| sections/intro.tex:42 | smith2024method | Claims SOTA on X | state-of-the-art | PARTIALLY_SUPPORTED | weaken to "competitive" or add benchmark-specific citation |
```

## Common Failure Patterns

- citation supports a method's existence but not its claimed performance
- citation supports an arXiv version but BibTeX points to a shorter proceedings version
- citation is used for a negative claim that the cited paper never makes
- citation cluster hides which paper supports which claim
- survey citation is used where the original method paper should be cited
- old benchmark citation is used although a newer version changed the task
- self-citation in blind submission uses identifying wording

## Writing Fixes

Bad:

```text
Prior work cannot handle long contexts~\citep{smith2023}.
```

Better:

```text
Prior work primarily evaluates contexts up to 4k tokens~\citep{smith2023}, leaving performance at longer contexts less well characterized.
```

Bad:

```text
Several works prove convergence~\citep{a,b,c}.
```

Better:

```text
Convergence guarantees are known for convex objectives~\citep{a,b}; for nonconvex objectives, existing analyses require bounded variance assumptions~\citep{c}.
```
