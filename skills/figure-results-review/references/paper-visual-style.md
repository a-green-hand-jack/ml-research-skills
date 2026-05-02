# Paper Visual Style

Use this when figures are being prepared for a paper, slide deck, rebuttal, or camera-ready version. This is a writing and presentation concern: visual style controls the reader's attention and should match the paper's narrative.

## Style Policy

Create a compact style policy when the paper has more than one figure:

```markdown
# Paper Visual Style Policy

## Palette
- Proposed method:
- Main baseline:
- Secondary baselines:
- Ablations:
- Diagnostics:

## Encodings
- Method -> color:
- Method -> marker:
- Method -> line style:
- Condition -> hatch or symbol:

## Typography
- Axis label size:
- Tick label size:
- Legend size:
- Caption dependency:

## Layout
- One-column figures:
- Two-column figures:
- Appendix figures:

## Rules
- What should be visually salient:
- What should never rely on color alone:
- Which symbols must match paper notation:
```

Save project-local policy in `paper/.agent/visual-style.md` or `.agent/conference-writing/project-style.md` when venue adaptation is active.

## Visual Language Checks

- The same method uses the same color, marker, and line style across all figures.
- The proposed method is visually findable but not misleadingly overemphasized.
- Baseline families are grouped visually, not assigned arbitrary colors.
- Ablations use a secondary visual encoding rather than competing with the main method.
- Diagnostic plots use restrained styling so they do not look like main claims.
- Color choices survive colorblind and grayscale viewing.
- No figure relies on red/green contrast alone.
- Markers, hatches, direct labels, or line styles make black-and-white print readable.

## Typography and Sizing

Check final rendered size, not only the plotting notebook:

- Axis labels are readable in final one-column or two-column placement.
- Tick labels do not collide or require rotation unless necessary.
- Legends do not cover data and are not far from the relevant curve.
- Panel labels use stable ordering and match the caption.
- Line widths and marker sizes remain visible after PDF scaling.

## Symbol and Notation Consistency

- Plot labels use the same method names as the paper text.
- Mathematical symbols match the method section.
- Dataset, metric, and baseline names match captions and related work.
- Units and arrows match the metric definition.
- The same color is not reused for different meanings across figures.

## Venue and Archetype Fit

Different paper archetypes need different visual emphasis:

- `method`: one main figure should teach the method or mechanism, not only show final scores.
- `theory-guided method`: plots should connect empirical behavior to the theoretical quantity or diagnostic.
- `benchmark`: figures need clear grouping, protocol labels, and fair comparison cues.
- `analysis`: visual encodings should make patterns, regimes, or failure modes visible.
- `systems`: latency, memory, throughput, and scale axes must be readable and units explicit.

When adapting to a venue, inspect strong accepted papers for figure density, caption style, and main-figure role. Borrow conventions, not content.

## Common Fixes

- Define a method-to-color/marker map before restyling individual plots.
- Replace overloaded legends with direct labels or grouped legends.
- Use one visual encoding for method identity and another for experimental condition.
- Split a crowded figure into main claim plus appendix diagnostics.
- Convert a rainbow palette into a small semantic palette plus markers/hatches.
- Use consistent figure aspect ratios across related results.
