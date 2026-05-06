# Style Memory

Use this when a figure, table, wrapper, or plotting script exposes a reusable style lesson.

Style memory should evolve gradually. Do not turn one local preference into a universal rule too early.

## Promotion Ladder

Record style knowledge at the lowest durable level that fits the evidence:

1. `lesson`: one observed issue and fix, often from a screenshot, PDF page, or reviewer comment.
2. `preference`: a repeated habit or user/project taste that should guide future edits but may have exceptions.
3. `project contract`: a paper-local rule that plotting scripts and LaTeX wrappers should follow.
4. `reusable skill rule`: a general rule that belongs in a public skill reference after repeated use across projects.

Promotion rule:

- One incident usually becomes a `lesson`.
- Repeated incidents in the same paper become a `preference`.
- A preference that affects generated assets becomes a `project contract`.
- A contract that proves generally useful across papers becomes a reusable skill rule.

## Recommended Files

Use these paper-local files when they exist:

```text
paper/.agent/visual-style.md       # paper-facing style contract and lessons
paper/.agent/style-lessons.md      # optional append-only lesson log for noisy iteration
code/config/plot_style.yaml        # machine-readable plotting contract
```

If the current repo is the paper repo, use:

```text
.agent/visual-style.md
.agent/style-lessons.md
../code/config/plot_style.yaml
```

Use `.agent/conference-writing/project-style.md` when venue adaptation owns the style decisions.

## Figure Typography Contract

Final-size typography should be specified relative to the paper, not the notebook preview.

Record:

- body font size and, when known, baseline skip
- final one-column and full-width figure sizes in inches
- LaTeX insertion width, such as `\linewidth`, `\columnwidth`, or `\textwidth`
- figure export size in inches
- axis label, tick label, legend, annotation, and panel-label sizes in points
- line width, marker size, hatch density, and minimum whitespace rules
- whether LaTeX text rendering is used and whether local TeX availability is required

Default starting point for 10pt ML papers:

```yaml
body_font_pt: 10
axis_label_pt: 8.5
tick_label_pt: 7
legend_pt: 7
annotation_pt: 7
panel_label_pt: 9
line_width_pt: 1.1
marker_size_pt: 3.5
```

These are starting points, not universal law. Adjust by final PDF inspection.

## Conversion Rule

Generate plots at the final inserted size whenever practical:

```text
final_width_in = LaTeX includegraphics width in inches
figsize = (final_width_in, final_height_in)
```

Avoid generating a large plot and then shrinking it heavily in LaTeX; fonts, lines, markers, and legend spacing shrink with the asset.

Use vector outputs (`pdf` or `svg`) for line plots, bar plots, scatter plots, diagrams, and most paper figures. Use raster outputs for screenshots, image grids, heatmaps, or qualitative examples, with an explicit DPI.

## Writeback Entry

When a new lesson appears, append a short entry:

```markdown
## YYYY-MM-DD - <short issue>

- Level: lesson | preference | project contract | reusable skill rule candidate
- Context: venue, figure, final placement, and source path
- Problem:
- Fix:
- Applies to:
- Exceptions:
- Promote when:
- Certainty: user-stated | observed | inferred | unverified
```

Keep entries small. A style memory should help the next plotting or review action, not become a long diary.

## Review Questions

Before marking a figure style-ready, ask:

- Does the rendered asset use the same final width assumed by LaTeX?
- Are axis labels, ticks, legend, annotations, and panel labels smaller than or comparable to body text at final size?
- Does the legend compete with the plotted result?
- Are method colors and markers consistent with prior figures?
- Are metric direction arrows, units, and notation aligned with captions and prose?
- Is this issue a one-off lesson, a repeated preference, or a project contract?
