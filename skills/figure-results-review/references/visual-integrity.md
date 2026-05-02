# Visual Integrity

Use this to audit plots for clarity, honesty, and reviewer readability.

## Plot Checks

- For paper figures, inspect both the rendered asset (`figures/*.pdf` or `figures/*.png`) and the LaTeX wrapper (`figures/*.tex`) when available.
- The wrapper includes the intended asset path.
- Wrapper width, crop, subfigure order, caption, and label match the rendered asset.
- Axes have names, units, and directionality.
- Log scales, normalization, smoothing, clipping, or transformations are declared.
- Tick labels are readable at final paper or slide size.
- Legends use stable method names that match the paper.
- Colors and markers remain distinguishable in grayscale.
- Line styles and markers do not imply nonexistent continuity.
- The visual ordering makes the main comparison easy to find.
- Error bars or bands are explained.
- Missing values, failed runs, and censored points are marked.
- Captions and labels match the plotted data.
- Plotting parameters that change the visible result are recorded or explicitly marked unknown.

## Common Fixes

- Split overloaded figures into main result plus diagnostic appendix.
- Replace many similar colors with line style and marker combinations.
- Use direct labels when the legend is too far from the data.
- Add a clear visual anchor for the proposed method.
- Move noisy or secondary diagnostics to appendix.

## Reviewer Readability Test

A reviewer should be able to answer in less than 10 seconds:

- what is being compared?
- which method is ours?
- which baseline is strongest?
- what metric matters?
- which direction is better?
- is the difference large enough to care?
- what caveat changes interpretation?

If not, the visual needs revision before paper use.
