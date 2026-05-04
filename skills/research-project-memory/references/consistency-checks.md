# Consistency Checks

Use these checks before writing, review simulation, rebuttal, submission, camera-ready work, or any major project transition.

## Claim Checks

- Does every active major paper claim have at least one linked evidence item?
- Are unsupported claims marked `planned`, `evidence-needed`, `provisional`, `parked`, or `cut`?
- Did new results weaken any existing claim?
- Is the paper still using stale claims from an abandoned worktree?
- Are provisional claims still clearly marked and linked to replacement actions?
- Does each active claim have a next gate?

## Evidence Checks

- Does every evidence item link to a claim?
- Does every completed experiment have source paths, run IDs, or logs?
- Are results marked with certainty?
- Are negative or failed experiments captured if they changed project direction?
- Are figures and tables traceable to evidence?
- Does every paper-facing table, figure, caption, or result sentence have provenance or a missing-provenance action?
- Are provisional results still visible before submission or internal review?

## Provenance Checks

- Can each `EVD-###` be traced to raw-run, CSV, report, citation, analysis, asset, or prose sources as appropriate?
- Do aggregation rules exist for paper-facing numbers?
- Are generated assets linked to the CSV/report/script that produced them?
- Are stale provenance entries reflected in claim, figure/table, writing-memory, or action state?

## Risk Checks

- Does every high or fatal risk have an action, accepted-risk decision, or reason it is out of scope?
- Did reviewer simulation create actions?
- Did rebuttal promises create paper/code actions?
- Are novelty and baseline risks reflected in related work and experiment plans?

## Phase and Handoff Checks

- Does `memory/phase-dashboard.md` match the current claim/evidence/provenance/risk/action/handoff boards?
- Is the active phase gate blocked, partial, ready, or done with a concrete reason?
- Does every ready handoff have a consumer and acceptance check?
- Does every blocked handoff have an action or accepted reason?
- Are stale handoffs marked stale rather than silently reused?

## Worktree Checks

- Does every worktree have a purpose?
- Does it link to a claim, experiment, risk, or action?
- Does it have an exit condition?
- Is any stale worktree still influencing paper text or slides?
- Has a merged/killed worktree updated project memory?
- Does every paper worktree have a source visibility tier, audience, sync target, cleanup gate, and forbidden-file policy?

## Source Visibility Checks

- If `paper/main` is linked to Overleaf or visible to coauthors, is it marked `author-visible` rather than private?
- Do author-visible, anonymous, arXiv, camera-ready, or publisher source surfaces exclude `.agent/`, `AGENTS.md`, `CLAUDE.md`, raw CSVs, internal result docs, plotting scripts, reviewer/rebuttal notes, private paths, and provenance ledgers?
- Are internal result inventories, writing memory, and paper asset provenance stored in root/private memory or agent-private worktrees rather than visible source?
- Does every visible paper source surface have a cleanup gate before push, submission, arXiv, camera-ready, or release?
- Are public-source audits recorded in `memory/source-visibility-board.md`?

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
- Did rebuttal or camera-ready work update provenance, handoffs, and phase status?
- Did rebuttal, submission, arXiv, or camera-ready work update source visibility and cleanup status?

## Volatility Checks

Do not trust memory alone for:

- git branch, commit, or dirty state
- active job or queue status
- whether output files exist
- latest metric values not yet copied into a stable report
- remote paths and environment availability

Create a verification action when stale volatile state matters.
