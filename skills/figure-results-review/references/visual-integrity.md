# Visual Integrity

Use this to audit plots and tables for clarity, honesty, and reviewer readability.

## Plot Checks

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

## Table Checks

- Rows and columns are grouped by the reader's comparison path.
- The main method and primary baselines are adjacent.
- Bold/underline rules are defined and not misleading.
- Decimal precision matches metric noise.
- Arrows indicate whether higher or lower is better.
- Missing values have footnotes.
- Compute, parameters, data, or NFE columns appear when relevant.
- Main results and ablations are not mixed in a confusing way.
- Appendix tables do not hide essential comparisons.

## Common Fixes

- Reorder rows by baseline family, not by arbitrary run order.
- Split overloaded figures into main result plus diagnostic appendix.
- Replace many similar colors with line style and marker combinations.
- Add a small fairness table when compute or scale affects interpretation.
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
