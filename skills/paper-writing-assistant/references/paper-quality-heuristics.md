# Paper Quality Heuristics

Use these checks when drafting or revising an AI conference paper. They are distilled from public writing advice such as hzwer/WritingAIPaper, but rewritten as workflow rules for this skill collection.

Source: https://github.com/hzwer/WritingAIPaper

## Core-Idea Test

Before polishing prose, identify the paper's memorable contribution.

- `insight`: explains a phenomenon, failure mode, principle, or design reason
- `performance`: does something measurably better under a fair protocol
- `capability`: enables something previously unavailable or impractical

Most papers can have supporting contributions, but the reader should remember one primary sell. If the contribution sentence cannot be written without listing many small tricks, route to `paper-positioning-planner`.

## Reader Story

Write the paper as a reader-facing argument, not as the chronological research process.

- Put the valuable finding before implementation history.
- Keep the abstract, introduction, and main body self-contained at increasing detail.
- Make the title, abstract, intro thesis, main figure/table, results, and conclusion sell the same idea.
- Keep closest-work contrast respectful and specific.

## Readability Gates

Run these gates before broad polishing:

`logical-strength`
: Connectives must reflect real logic. Do not use transitions to invent a causal, temporal, or priority relation that the argument has not established.

`defensibility`
: Strong claims need evidence, citations, or explicit scope. If a skeptical reviewer can ask "why is this true?", add support, weaken the claim, or mark a missing-evidence action.

`confusion-time`
: Define a term near first use, resolve ambiguous pronouns, split long sentences when the referent is unclear, and use topic sentences so a reader can recover the paragraph job quickly.

`information-density`
: Remove background that the target audience already knows or that does not support the current claim. Keep setup details close to the figure, table, method object, or claim they interpret.

## Evidence-Integrity Checks

Do not let writing hide experimental or evaluation advantages.

- Report compute, data, training duration, model size, inference cost, hardware, prompts, or tuning budget when they affect the comparison.
- Do not compare methods under different protocols without making the difference visible.
- Do not select only favorable seeds, metrics, datasets, slices, or subjective examples without declaring the selection rule.
- If a trick or hyperparameter materially affects the result, it belongs in the paper, appendix, artifact, or provenance record.
- Small gains need stronger uncertainty, baseline fairness, and claim scope discipline than large qualitative shifts.

## Figure And Table Proximity

Readers often inspect figures and tables before prose.

- Captions should state the setup, comparison, metric direction, and takeaway needed to interpret the evidence.
- Main-text callouts should explicitly name the figure/table and the comparison the reader should inspect.
- If a complex table requires the reader to infer the comparison path, reorder, repeat a key baseline, group columns, or add a short callout.
- Put important interpretation near the relevant visual when layout allows; do not bury the key explanation far away.
