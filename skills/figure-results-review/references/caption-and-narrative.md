# Caption and Narrative

Captions and result prose should make figure evidence interpretable without overclaiming.

## Separate the Artifacts

Keep these artifacts separate:

- `visual description`: an audit record of what the rendered figure actually shows
- `provenance`: plotting parameters and experiment parameters needed to reproduce or interpret the figure
- `caption`: paper-facing explanation under the figure
- `main-text callout`: the sentence or paragraph that tells the reader why to look at the figure now

The visual description can be longer and more literal than the caption. It should mention panels, axes, visible trends, missing uncertainty, labels, colors, and anything a reviewer could see. The caption should not become an alt-text dump. It should give enough setup, comparison, metric, and takeaway for the figure to work as evidence.

## Visual Description Contents

A visual description should include:

- rendered asset path and wrapper `.tex` path, if applicable
- figure type and panel layout
- axes, units, scales, and direction
- methods, datasets, variables, colors, markers, and legends
- visible trend, comparison, outlier, missing value, or uncertainty
- whether the caption and labels match what is visible
- certainty source: inspected asset, wrapper, logs, config, caption, filename, or user statement

## Provenance Contents

For experiment figures, record the parameters that determine what the figure means:

- dataset, split, subset, filtering, and preprocessing
- model/checkpoint and baseline versions
- metric definition and aggregation
- seeds or number of repeated runs
- sampling budget, compute budget, NFE, step count, temperature, threshold, or other method-specific knobs
- plotting filters, smoothing, normalization, axis range, colormap, panel ordering, and annotation rules
- source code, config, result table, log, or report path when available

Do not hide unknown provenance. Mark it as `unknown` or `needs-author-confirmation`.

## Caption Contents

A strong caption includes:

- task or dataset
- model or method family
- metric and direction
- comparison set
- key setup or budget constraint
- uncertainty convention, if any
- one factual takeaway
- caveat when needed

## Caption Pattern

```text
[What is plotted.] We compare [methods] on [task/dataset] using [metric; direction].
[Setup/fairness detail.] [Takeaway tied to the claim]. Error bars show [uncertainty].
```

For figures with important method or plotting parameters:

```text
[What is plotted.] We compare [methods] on [task/dataset] using [metric; direction] under [key experiment parameters].
[Plotting convention or budget detail.] [Takeaway tied to the claim]. Error bars show [uncertainty].
```

Do not put every hyperparameter in the caption. Include the parameters needed to interpret the claim. Put the full provenance in the figure review report, appendix, artifact, or `paper/.agent/` record.

## Caption-Image Alignment

Before accepting a caption, check:

- every captioned method, dataset, metric, and parameter appears in the figure or is necessary setup
- the caption's takeaway is visually supported by the rendered asset
- panel references match panel labels and order
- the caption does not describe an older asset after the figure was regenerated
- missing uncertainty, seeds, or provenance are either stated or routed to a fix
- the wrapper `.tex` includes the intended asset and label

## Result Prose Pattern

Use one sentence for each function:

1. State the comparison.
2. State the observed result.
3. Interpret only within the supported scope.
4. Mention the caveat or route to appendix if needed.

Example:

```text
Under a matched training budget, our consistency objective improves the MDLM speed-quality curve at low denoising-step counts. The gain is largest at 8-16 steps and narrows at 64 steps, suggesting that the method primarily helps fast sampling rather than final likelihood.
```

## Claims to Avoid

Avoid:

- claiming causality from a correlation plot
- claiming robustness from one dataset
- claiming efficiency without compute or latency
- claiming SOTA without current baselines
- claiming theory validation from a weak diagnostic
- using "significant" without statistical support

## Figure Callout

Every main-text callout should answer:

- why should the reader look at this figure now?
- what should they notice?
- how does it support the paper's claim?
- what caveat should they keep in mind?

If the answer is not clear, revise the surrounding prose, not only the caption.
