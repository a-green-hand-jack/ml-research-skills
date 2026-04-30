# Risk Register

Use the risk register to turn reviewer criticism into a revision plan.

## Risk Fields

Each risk should include:

- ID
- reviewer concern
- category: novelty, correctness, theory, experiments, baselines, ablation, clarity, related work, reproducibility, ethics, scope
- evidence from paper
- severity: critical, high, medium, low
- probability: high, medium, low
- fix effort: small, medium, large, cannot-fix-before-deadline
- recommended action
- owner, if known
- rebuttal fallback

## Severity

- `critical`: likely rejection if not addressed
- `high`: could drive weak reject or reject if multiple reviewers notice
- `medium`: likely reviewer complaint but probably fixable
- `low`: polish or convenience issue

## Probability

- `high`: likely at least one reviewer will notice
- `medium`: plausible given venue/topic
- `low`: possible but not central

## Fix Effort

- `small`: wording, figure, citation, clarification, moving text
- `medium`: new analysis, stronger explanation, additional ablation using existing runs/data
- `large`: new experiments, new proof, new dataset annotation, major rewrite
- `cannot-fix-before-deadline`: prepare rebuttal and scope claims

## Priority Buckets

### Must-Fix

Risks that could independently cause rejection:

- unsupported central claim
- missing closest baseline
- incorrect theorem or unclear assumption
- unaddressed fatal limitation
- unclear novelty relative to close prior work

### Should-Fix

Risks that materially improve acceptance odds:

- weak ablation
- unclear contribution framing
- insufficient limitation discussion
- incomplete implementation detail
- poor figure/table readability

### Nice-To-Fix

Useful but less decision-critical:

- minor wording
- bibliography cleanup
- small appendix organization issue
- additional qualitative examples

### Rebuttal-Only

Issues unlikely to be fixable before submission:

- compute-heavy additional benchmark
- new theorem
- new dataset collection
- unavailable proprietary baseline

## Register Template

```markdown
| ID | Priority | Concern | Category | Evidence | Severity | Probability | Effort | Action | Rebuttal fallback |
|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | must-fix | ... | experiments | Section 4 lacks ... | critical | high | medium | ... | ... |
```

## Action Quality

Good actions are specific:

- "Add ablation removing the calibration loss on datasets A/B and report delta in Table 2."
- "Rewrite intro P3 to distinguish from Smith et al. 2024 on objective, not architecture."
- "Move proof sketch of Theorem 1 into main text and state Assumption 2 before the theorem."

Bad actions are vague:

- "Improve experiments."
- "Clarify novelty."
- "Discuss limitations more."
