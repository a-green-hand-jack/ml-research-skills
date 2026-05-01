# Consistency Checks

Use these checks before writing, review simulation, rebuttal, submission, camera-ready work, or any major project transition.

## Claim Checks

- Does every active major paper claim have at least one linked evidence item?
- Are unsupported claims marked `planned`, `unsupported`, or `cut`?
- Did new results weaken any existing claim?
- Is the paper still using stale claims from an abandoned worktree?

## Evidence Checks

- Does every evidence item link to a claim?
- Does every completed experiment have source paths, run IDs, or logs?
- Are results marked with certainty?
- Are negative or failed experiments captured if they changed project direction?
- Are figures and tables traceable to evidence?

## Risk Checks

- Does every high or fatal risk have an action, accepted-risk decision, or reason it is out of scope?
- Did reviewer simulation create actions?
- Did rebuttal promises create paper/code actions?
- Are novelty and baseline risks reflected in related work and experiment plans?

## Worktree Checks

- Does every worktree have a purpose?
- Does it link to a claim, experiment, risk, or action?
- Does it have an exit condition?
- Is any stale worktree still influencing paper text or slides?
- Has a merged/killed worktree updated project memory?

## Paper/Slide Checks

- Do paper sections reflect the latest evidence board?
- Are figures/tables current rather than stale?
- Do slides tell the same story as the current paper positioning?
- Are advisor or audience feedback items converted into actions?

## Review/Rebuttal Checks

- Do simulated reviewer risks link to claims and actions?
- Do real review issues link to rebuttal responses and promised revisions?
- Are promised revisions tracked until completed?
- Did rebuttal experiments update evidence and paper claims?

## Volatility Checks

Do not trust memory alone for:

- git branch, commit, or dirty state
- active job or queue status
- whether output files exist
- latest metric values not yet copied into a stable report
- remote paths and environment availability

Create a verification action when stale volatile state matters.
