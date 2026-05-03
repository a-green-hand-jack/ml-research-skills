# Impact Propagation

Use this guide when a change may affect multiple parts of the paper.

## Claim Change

Check:

- title
- abstract
- contribution bullets
- introduction gap and contribution paragraphs
- results narrative
- captions
- limitations
- conclusion
- related-work boundary

If claim strength decreases, mark strong phrases stale: `general`, `robust`, `state-of-the-art`, `first`, `solves`, `demonstrates`, `guarantees`.

## Result or Evidence Change

Check:

- paper-evidence-board entry
- result table
- result figure
- caption
- main-text callout
- abstract result sentence
- introduction evidence paragraph
- limitation or scope paragraph
- conclusion

Route:

- existing CSV may fill gap -> `paper-evidence-gap-miner`
- table/figure needs rebuild -> `paper-result-asset-builder`
- surprising result -> `result-diagnosis`
- prose update -> `experiment-story-writer`

## Table or Figure Change

Check:

- source CSV/provenance
- caption
- main-text callout
- result paragraph
- abstract or intro if it mentions the number
- visual/table review status
- evidence board

Route to `figure-results-review` or `table-results-review` before final prose if the asset changed materially.

## Caption Change

Check:

- figure/table job
- claim supported
- metric/dataset/method naming
- result paragraph
- style rules

Caption edits often require dependency-map updates because captions carry claim wording.

## Method or Notation Change

Check:

- method section
- overview figure caption
- algorithm box
- experiment setup
- result labels
- related work terminology
- abstract method sentence

Route to `method-section-explainer` when explanation order or notation flow changes.

## Related-Work Boundary Change

Check:

- introduction gap paragraph
- related work section
- title/abstract novelty wording
- contribution bullets
- limitations if novelty scope narrows

Route to `related-work-positioning-writer` and possibly `citation-coverage-audit`.

## Limitation or Scope Change

Check:

- title scope
- abstract claim strength
- introduction contribution bullets
- results interpretation
- conclusion
- ethics/broader impact

Route to `limitations-scope-writer` and `abstract-title-contribution-writer` when top-level wording changes.

## Style or Terminology Change

Check:

- all section headings
- method names
- figure/table legends
- captions
- contribution bullets
- related work names
- appendix labels

Record in `style-and-terminology.md` and mark affected locations `verify`.
