# Quality Gates

Run these checks before finalizing a rewrite plan, paragraph blueprint, or rewritten section. The gates make the skill behave less like a generic writing assistant and more like a venue-aware paper editor.

## Gate 1 - Venue Fit

Pass criteria:

- target venue and year are explicit
- current official rules are verified when relevant
- rewrite choices reflect the target venue, not generic ML style
- exemplar-derived patterns are named when exemplars were studied

Fail examples:

- NeurIPS, ICML, and ICLR receive the same method-section plan
- page budget or mandatory statements are asserted from memory without verification
- the rewrite sounds polished but not venue-specific

## Gate 2 - Archetype Fit

Pass criteria:

- primary paper archetype is stated
- section order follows that archetype
- the structure matches the real contribution and evidence

Fail examples:

- a theory-driven method paper is written like a pure benchmark paper
- an empirical study is forced into a novelty-first method narrative
- a paper with weak experiments is written as if the evidence is complete

## Gate 3 - Reviewer Promise

Pass criteria:

- the introduction implies a clear reviewer promise
- the promise names problem, contribution, and evidence
- the first page makes the paper's value legible

Template:

```text
This paper matters because [problem], and it deserves acceptance because [specific contribution] is supported by [specific evidence].
```

## Gate 4 - Claim-Evidence Alignment

Pass criteria:

- each major claim maps to an experiment, theorem, proof sketch, figure, dataset, ablation, or citation
- unsupported claims are weakened or marked as missing evidence
- contribution bullets are not vague novelty statements

Fail examples:

- "significantly improves" without metric, baseline, or setting
- "principled" without formal result or clearly stated design principle
- "general" after evaluation on one narrow setup

## Gate 5 - Paragraph Function

Pass criteria:

- each important paragraph has one primary function
- the opening sentence orients the reviewer
- the closing sentence advances the argument or transitions
- paragraphs do not mix motivation, method detail, and result interpretation without control

Use the paragraph blueprint from `paragraph-protocol.md` for high-risk sections.

## Gate 6 - Rebuttal Readiness

Pass criteria:

- obvious reviewer objections are anticipated in the main text
- assumptions are named and scoped
- limitations are specific rather than generic
- related work distinguishes the contribution from close alternatives

For OpenReview-heavy venues such as ICLR, this gate is especially important because public discussion often probes assumptions, baselines, and overclaims.

## Gate 7 - Reproducibility and Appendix Strategy

Pass criteria:

- main text includes enough detail to understand the method
- appendix promises are explicit and credible
- proofs, derivations, hyperparameters, and extra ablations are placed intentionally
- code/data/supplementary availability is handled according to venue rules

Fail examples:

- core evidence appears only in appendix
- the main algorithm cannot be implemented from the paper
- proof obligations are hidden behind "details omitted"

## Gate Report Template

Use this when returning a substantial rewrite plan:

```markdown
## Quality Gate Report
| Gate | Status | Notes |
|---|---|---|
| Venue fit | PASS/FAIL | ... |
| Archetype fit | PASS/FAIL | ... |
| Reviewer promise | PASS/FAIL | ... |
| Claim-evidence alignment | PASS/FAIL | ... |
| Paragraph function | PASS/FAIL | ... |
| Rebuttal readiness | PASS/FAIL | ... |
| Reproducibility / appendix | PASS/FAIL | ... |
```

If one or more gates fail because paper evidence is missing, do not hide the failure. Return a concise blocker list and the smallest revision needed to pass.
