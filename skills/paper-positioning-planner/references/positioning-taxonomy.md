# Positioning Taxonomy

Choose the paper archetype that best matches evidence and reviewer expectations.

## Archetypes

`method-paper`
: A new algorithm, model, objective, training recipe, inference procedure, or architecture. Requires strong baselines, ablations, and clear novelty against closest methods.

`theory-guided-method`
: A method motivated by a theorem, principle, bound, or formal diagnostic. Requires both method evidence and a measured link to the theory.

`empirical-analysis`
: A careful study explaining behavior, tradeoffs, scaling, failure modes, or evaluation gaps. Requires controlled comparisons and clear analysis questions.

`benchmark-or-dataset`
: A new benchmark, dataset, protocol, metric, or evaluation suite. Requires task motivation, coverage, baseline suite, and community need.

`systems-or-tooling`
: A practical system, library, infrastructure, compiler, training stack, or workflow. Requires usability, reliability, performance, and adoption argument.

`application-paper`
: Applying methods to a meaningful domain problem. Requires domain relevance, realistic evaluation, and comparison to domain baselines.

`diagnostic-or-mechanistic-study`
: Explains why methods work or fail. Requires diagnostics, interventions, and controlled evidence rather than headline performance.

`negative-result-or-limitation`
: Shows a plausible approach fails or has important limits. Requires careful controls and clear lesson value.

`position-or-perspective`
: Argues for a conceptual reframing. Requires strong synthesis and persuasive examples, usually not enough for standard ML conference main track unless invited or workshop-fit.

`hybrid`
: Combines two archetypes only when the secondary archetype directly strengthens the primary one.

## Selection Questions

- What would a reviewer say is the contribution after reading only the abstract?
- Which result is strongest and most defensible?
- Which closest work defines novelty?
- Which audience has the strongest reason to care?
- What evidence would be fatal if missing?
- Does the current draft sell a contribution that the figures do not support?

## Archetype Fit Table

```markdown
| Archetype | Fit | Evidence available | Missing evidence | Risk |
|---|---|---|---|---|
```

Use `strong`, `medium`, `weak`, or `not-fit`.
