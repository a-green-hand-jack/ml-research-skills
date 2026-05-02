# Figure Captions

Use this file when writing or revising figure captions. A paper figure caption should let a skimming reader understand the claim, setup, visual encoding, and takeaway.

Coordinate with `figure-results-review` when the question is whether the figure itself supports the claim or whether visual encodings are correct.

## Claim-First Figure Caption

Use for a main figure that supports a central claim.

Pattern:

1. Takeaway sentence: what the reader should learn.
2. Setup sentence: task, dataset, metric, or experimental condition.
3. Visual encoding sentence: panels, axes, colors, markers, or grouping.
4. Evidence sentence: what comparison supports the claim.
5. Caveat sentence if the result is scoped or mixed.

Avoid:

- captions that only describe axes
- unexplained colors, panels, markers, or error bars
- claiming more than the plotted comparison supports

## Mechanism Figure Caption

Use for diagrams, method overviews, or ablation visuals.

Pattern:

1. State the mechanism or design principle.
2. Walk through the figure in the order the reader should inspect it.
3. Name each module or panel by function, not only label.
4. Explain what later experiment or ablation tests the mechanism.

## Qualitative Figure Caption

Use for examples, generated outputs, failure cases, or case studies.

Pattern:

1. State the qualitative phenomenon.
2. Define rows, columns, examples, prompts, or conditions.
3. Explain what visual/textual difference matters.
4. Mark cherry-picking, representative sampling, or failure mode if relevant.

## Caption Openers

Good:

- "The figure shows that [takeaway] under [setting]."
- "[Method/artifact] changes [behavior], especially when [condition]."
- "Ablating [component] reveals [mechanism-facing result]."

Weak:

- "Visualization of our method."
- "Results on [dataset]."
- "More examples are shown."
