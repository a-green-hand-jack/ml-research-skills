# Caption and Narrative

Captions and result prose should make the evidence interpretable without overclaiming.

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
