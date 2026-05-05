# LaTeX Layout Debugging Protocol

Use this protocol when a paper has layout, float, page-break, short-line, overfull, underfull, or screenshot-driven formatting problems near submission or camera-ready.

## Core Rule

Do not treat layout as a one-shot global parameter problem. Locate the exact page and object first, then make small local, reversible changes and verify the resulting PDF or screenshot.

Layout fixes are usually a joint optimization over:

- prose length and line breaks
- figure/table placement
- float spacing
- page breaks
- caption and callout wording

Do not treat it as only LaTeX engineering or only writing.

## Preferred Workflow

1. Identify the concrete page, screenshot, object, or paragraph.
2. Decide whether the issue is text length, a float/table object, a page break, or a local spacing interaction.
3. Make one small change.
4. Compile through the configured backend, or push to Overleaf/GitHub when that is the project compile backend.
5. Inspect the affected page visually.
6. Continue only if the change helped; otherwise revert or try the next local fix.

Avoid broad edits that make unrelated pages worse.

## Fix Priority

1. Short-line and overfull problems: revise prose first.
   - Shorten or split long sentences.
   - Replace long phrases with shorter terms.
   - Shorten citation or appendix references when safe.
   - Break long compound expressions, long method names, long parenthetical explanations, and dense math sequences.
   - Prefer a local wording edit over global `\sloppy`, `\emergencystretch`, or paragraph setting changes.

2. Figure/table spacing: tune locally.
   - For a specific `figure` or `table`, prefer local `\vspace`, `\FloatBarrier`, `\Needspace`, or local `\textfloatsep` / `\intextsep`.
   - Use `\FloatBarrier` only when `placeins` is available or already accepted by the project; scope `\textfloatsep` / `\intextsep` tweaks in a local group or around one object so they do not become accidental global policy.
   - Do not globally change all float spacing unless the whole paper has a consistent documented style problem.
   - Check the neighboring page after each local spacing change.

3. Avoid fragile wrap floats near page boundaries.
   - `wraptable` and `wrapfigure` often fail at the bottom of a page or before a forced page break.
   - If text flows strangely, a table is cut, or a large blank appears, move the insertion point or add `\Needspace{...}` before the object.
   - Prefer a normal float when wrap behavior is unstable.

4. `[H]` does not eliminate all vertical whitespace.
   - Even when a table is forced in place, the `table` environment can still add vertical skips.
   - If the bottom gap is local to one table, adjust inside or immediately around that table, such as a small bottom `\vspace{...}`, rather than changing global spacing.

5. Iterate on one object at a time.
   - LaTeX is a pagination system; a few words can affect later pages.
   - Change one paragraph, table, figure, or float setting, then inspect the affected page before continuing.

6. Do not submit local compile byproducts.
   - Fast local iteration may create PDFs, aux files, logs, caches, or local TeX artifacts.
   - Commits should contain `.tex` source and required paper-facing assets only.
   - For Overleaf/GitHub workflows, commit and push source changes, then use Overleaf logs/PDF/screenshots as compile evidence.

7. Write prose that serves layout.
   - Technical prose should be accurate and line-break-friendly.
   - Avoid unnecessary long compounds, long citation aliases, consecutive math symbols, and long parenthetical explanations.
   - When needed, split one sentence into two or change "Section H.3 gives ..." to a shorter "App. H.3 gives ...", if the venue/style allows it.

## What To Avoid

- Starting with global `\sloppy`, `\emergencystretch`, `\parskip`, `\textfloatsep`, or paragraph-setting changes.
- Moving many floats at once without screenshot comparison.
- Rewriting large sections only to fix a local line or float.
- Treating a clean local compile as proof that the visual layout is good.
- Committing temporary compile artifacts or local tool state.

## Reporting Format

When reporting layout fixes, include:

- affected page or screenshot
- object or paragraph changed
- exact local change
- compile backend used for verification
- screenshot/PDF inspection status
- whether later pages need rechecking
