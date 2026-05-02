# Audience and Venue Fit

Use this to decide who the paper should primarily serve.

## Audience Types

`method-researchers`
: Care about algorithmic novelty, performance, baselines, ablations, and usable implementation.

`theory-readers`
: Care about assumptions, formal statements, proof relevance, and whether theory predicts observed behavior.

`empirical-analysts`
: Care about controlled comparisons, diagnostics, scaling, failure modes, and causal interpretation.

`benchmark-users`
: Care about protocol design, coverage, reproducibility, and whether the benchmark changes evaluation practice.

`systems-builders`
: Care about efficiency, reliability, deployment constraints, and engineering tradeoffs.

`domain-users`
: Care about domain validity, practical impact, and realistic baselines.

## Venue Fit Questions

- Does the venue reward this archetype?
- What evidence does this venue expect for the claim?
- Which reviewer pool will judge novelty?
- Is the paper too engineering-heavy, too theoretical, too narrow, or too empirical for the venue?
- Would another venue make the same evidence look stronger?

## Target-Audience Statement

Write:

```text
The paper primarily targets [audience] because [reason]. It should not primarily target [audience] because [risk].
```

## Related-Work Boundary

Define:

- closest work to compare against
- adjacent work to cite but not compete with
- communities not being claimed over
- terms that may confuse reviewers
- papers that must be distinguished in the intro

## Venue Caution

If current venue expectations are important or may have changed, verify with official guidelines, recent accepted papers, OpenReview patterns, or user-provided exemplars before making a strong venue-specific claim.
