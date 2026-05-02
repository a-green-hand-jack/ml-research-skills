# Claim Evidence Final Lock

Use this to ensure the final paper does not drift after acceptance.

## Claim Lock Table

```markdown
| Claim | Paper location | Evidence | Final status | Required edit |
|---|---|---|---|---|
```

Final statuses:

- `supported`
- `narrowed`
- `moved-to-appendix`
- `limitation`
- `cut`
- `needs-author-decision`

## Check Each Claim

- Does the final figure/table/theorem still support the wording?
- Did rebuttal experiments change the number, trend, or scope?
- Did a new citation or related-work edit narrow novelty?
- Does the abstract overstate what final evidence shows?
- Do captions match final table/plot values?
- Does the supplement contradict the main paper?
- Does the code release support reproducibility claims?

## Final Claim Rules

- Keep claims that are supported by final evidence.
- Narrow claims that depend on limited settings, seeds, baselines, or datasets.
- Move secondary diagnostics to appendix when they are not central.
- Convert unresolved weaknesses into limitations.
- Cut claims that require missing evidence.

Final papers should not become more ambitious after acceptance unless the evidence was actually added.
