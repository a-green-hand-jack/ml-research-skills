# Draft Consistency Rules

Use this checklist to audit whether a paper draft tells one coherent story.

## Story-Level Consistency

Check:

- Title promise matches abstract and introduction.
- Abstract's main claim appears in the introduction thesis.
- Introduction contribution bullets map to sections, figures, tables, theorem, artifact, or appendix evidence.
- Conclusion does not introduce a broader claim than abstract/results.
- Limitations narrow the same claims that evidence cannot fully support.

Common issues:

- title sells a method while the evidence supports an empirical study
- abstract claims broad generality but experiments cover one setting
- introduction promises an ablation that results do not discuss
- conclusion adds deployment or causal claims not supported earlier

## Claim Strength Consistency

Track whether each claim is stated as:

- `proven` / `shown` / `demonstrated`
- `suggested` / `consistent with`
- `motivated`
- `preliminary`
- `scoped`

Fix drift:

- If abstract says "demonstrates" but results are preliminary, weaken abstract.
- If results are mixed, make intro and conclusion scope explicit.
- If limitations state a missing condition, do not leave the abstract claiming it.

## Evidence Mapping

For each main claim, identify:

- paper locations
- evidence artifact
- figure/table/proof/citation
- status: verified, user-stated, provisional, missing, stale, contradicted

Flag:

- claim without evidence
- evidence not discussed in prose
- table/figure without claim
- stale result after updated experiments
- provisional placeholder not tracked

## Result Consistency

Check:

- numbers match between tables, captions, and prose
- metric direction is consistent
- dataset/task names match
- baseline names match
- statistical language matches reported uncertainty
- "best", "outperforms", "improves", and "state of the art" are justified by the comparison set

Flag:

- "higher is better" omitted where ambiguity matters
- bolding contradicts prose
- mixed wins described as uniform dominance
- result prose describes an old table

## Figure and Table Consistency

For each figure/table:

- Does the caption state the intended takeaway?
- Does the main text callout match the caption?
- Does the visual/table support the claim assigned in the writing contract?
- Are colors, markers, method labels, and abbreviations consistent?
- Are appendix references and labels correct?

Flag:

- caption only describes axes
- main text overclaims beyond visual evidence
- figure/table appears before the reader knows why it matters
- table row/column semantics conflict with prose

## Terminology and Notation Consistency

Check:

- method name and abbreviation
- dataset/task names
- baseline names
- metric names and capitalization
- symbols and notation
- section names
- figure/table labels
- claim terminology, such as "robustness", "generalization", "truthfulness", "efficiency"

Flag:

- same object has multiple names
- same term means different things
- notation changes between setup and method
- baseline abbreviation is introduced more than once or never defined

## Related Work and Novelty Boundary

Check:

- closest work mentioned in intro appears in related work
- related work acknowledges strongest adjacent work
- novelty boundary matches contribution claims
- "first", "novel", "unlike prior work", and "orthogonal" claims are supported
- related work does not undermine the intro by implying a different contribution

## Provisional and TODO Hygiene

Search for:

- `PROVISIONAL-RESULT`
- `PR-###`
- `TODO`
- `TBD`
- `??`
- placeholder brackets
- comments that should not remain in public source

Flag every unresolved placeholder with location and required action.
