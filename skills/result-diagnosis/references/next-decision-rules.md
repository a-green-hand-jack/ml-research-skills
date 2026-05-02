# Next Decision Rules

Choose one primary decision and list secondary actions if needed.

## Debug

Use when:

- provenance is broken
- metric computation is suspicious
- method flag or code path is uncertain
- logs show NaNs, crashes, or impossible values
- results are too good to be plausible

Next action: smallest sanity check that can confirm or rule out the bug.

## Rerun

Use when:

- result is plausible but underpowered
- seeds are insufficient
- baseline comparison is unfair but fixable
- output is missing required logs
- checkpoint rule was wrong

Next action: rerun with corrected controls and explicit stop condition.

## Ablate

Use when:

- effect exists but mechanism is unclear
- multiple variables changed
- metric conflict needs isolation
- generic regularization or tuning may explain gains

Next action: one-variable ablation or diagnostic.

## Revise Method

Use when:

- mechanism diagnostic fails
- optimization repeatedly fails under reasonable settings
- method only works with unacceptable cost or brittleness
- failure points to a design flaw

Next action: use `algorithm-design-planner` to revise the mechanism.

## Narrow Claim

Use when:

- method works only in a specific regime
- only one metric or dataset supports the claim
- mechanism claim is unsupported but empirical claim remains
- result is useful but weaker than original story

Next action: update paper claim and evidence board.

## Write

Use when:

- provenance is clear
- comparison is fair enough for intended audience
- result supports a claim or useful negative conclusion
- limitations are understood

Next action: use `experiment-report-writer` or update paper.

## Park

Use when:

- result is inconclusive
- next check is expensive and lower priority
- prerequisites are missing
- another project path has higher expected value

Next action: record what would reopen the direction.

## Kill

Use when:

- fair controls repeatedly falsify the claim
- mechanism and performance evidence both fail
- strong baseline closes the gap under matched tuning
- success would still not support a meaningful paper claim

Next action: preserve lessons, cut claims, and close or park worktree.

## Decision Confidence

Use:

- `high`: evidence clearly supports the decision.
- `medium`: enough to act, but some uncertainty remains.
- `low`: next action should reduce uncertainty before major commitment.
