# Final Submission Audit

Use this for final camera-ready readiness. Verify venue-specific rules from official instructions when exact requirements matter.

## Format and Build

- final style file and camera-ready mode
- page limit and allowed appendix/supplement rules
- successful clean compile
- no unresolved references or citations
- final PDF opens and pages render correctly
- figures are not missing, cropped, or low resolution
- tables fit columns/pages
- algorithms, equations, and footnotes are readable
- layout fixes are page/object-specific and visually verified; avoid broad global `\sloppy`, `\emergencystretch`, paragraph, or float-spacing changes unless the whole paper has a documented style problem
- short-line and overfull issues were considered as prose problems first, then local float/page-break problems second

## Text Hygiene

- no TODOs, draft notes, review-response notes, or hidden comments
- no anonymity text remains
- abstract, title, author list, and affiliations are final
- limitations, ethics, broader impact, reproducibility, or checklist sections are final if required
- acknowledgements and funding are complete

## Reference and Link Hygiene

- bibliography is complete and final
- citation metadata is correct
- URL links work or are intentionally archived
- code/data/model/project links point to final destinations or stable placeholders approved by authors

## Upload Package

Check:

- main PDF
- source archive if required
- supplementary PDF or zip
- checklist
- metadata fields in submission system
- copyright/license forms if applicable

## Source Visibility

For camera-ready or publisher-visible source, check:

- no `.agent/`, `AGENTS.md`, `CLAUDE.md`, internal memory, raw CSVs, internal result docs, plotting scripts, notebooks, provenance ledgers, reviewer/rebuttal scratch, or private paths are included
- source files are de-anonymized where required
- source package contains only public-clean LaTeX, paper-facing figures/tables, bibliography, style files, supplement, and approved artifact/release links
- `memory/source-visibility-board.md` records the final visibility tier and audit status when project memory exists

Route detailed LaTeX checks to `citation-audit` and format readiness to `submit-paper`. For screenshot-driven layout work, use `submit-paper/references/layout-debugging.md`: locate the page/object, change one small thing, compile through the configured backend, inspect the affected page, and avoid committing local compile byproducts.
