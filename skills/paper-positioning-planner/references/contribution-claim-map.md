# Contribution Claim Map

Map what the paper sells to the evidence that can defend it.

## Contribution Levels

`primary`
: The paper's main reason to exist. It should appear in title, abstract, intro thesis, main figure/table, and conclusion.

`secondary`
: Supports the primary story but should not compete with it.

`supporting`
: Useful details, diagnostics, or appendix material.

`cut`
: Interesting but unsupported, distracting, or dangerous.

## Claim Actions

`keep`
: Evidence supports the claim as written.

`narrow`
: Claim is true only for a smaller setting, metric, dataset, model scale, or comparison family.

`revise`
: Claim direction changes because evidence or literature changed.

`block`
: Claim cannot be used until missing evidence arrives.

`cut`
: Remove from paper story.

## Claim Map

```markdown
| Claim | Contribution level | Evidence | Missing evidence | Closest-work distinction | Action |
|---|---|---|---|---|---|
```

## Evidence Standard

Primary claims need:

- direct comparison to closest work
- sufficient baseline fairness
- main figure or main table support
- ablation or diagnostic for mechanism claims
- uncertainty or repeatability when differences are small
- clear relation to target venue expectations

Secondary claims can be weaker, but must not make the paper look overclaimed.

## Closest-Work Boundary

For each major claim, write:

```text
Unlike [closest work], this paper claims [specific distinction] and supports it with [evidence].
```

If the sentence is vague, route to `literature-review-sprint` or narrow the claim.

## Claims to Avoid

Name forbidden claims explicitly:

- too broad for datasets or scales tested
- requires missing baseline
- contradicted by result figure
- only supported by single-seed or diagnostic evidence
- shifts the paper into a different archetype
- invites an unnecessary reviewer attack
