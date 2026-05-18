# Contrastive Routing Rules

Use this file when two or more buckets seem equally plausible.

---

## `run-experiment` vs `run-status-monitor`

**Use `run-experiment`** when the user needs to:
- Create, configure, or generate a new job script
- Submit a job that does not yet exist
- Choose a compute environment or resource size for a new run

**Use `run-status-monitor`** when:
- A job already exists and the user asks about its current state
- The job is queued, stuck, running, or recently finished
- The user wants to know progress, ETA, or whether to wait or resubmit

**Decision rule**: Has the job been submitted yet?
- No → `run-experiment`
- Yes → `run-status-monitor`

---

## `experiment-debugger` vs `result-diagnosis`

**Use `experiment-debugger`** when the problem is **engineering**:
- Training crashes mid-run (NaN, inf, OOM)
- Metrics are obviously wrong (e.g., accuracy stuck at 0% or 100%)
- The run cannot be reproduced despite identical config
- Data loading is broken, slow, or corrupt
- The training loop has a bug

**Use `result-diagnosis`** when the result is **scientifically valid but surprising**:
- The run completed normally but results don't match expectations
- The baseline is outperforming your method
- Results are inconsistent across seeds in a meaningful (not bug-caused) way
- The user asks "what does this result mean?" or "should I rerun/ablate/pivot?"

**Decision rule**: Did the job finish successfully and produce a valid result?
- No (crashed/wrong/broken) → `experiment-debugger`
- Yes (completed, but surprising) → `result-diagnosis`

---

## `result-diagnosis` vs `research-results-auditor`

**Use `result-diagnosis`** when:
- The user needs to decide what to do next after an unexpected result
- The result is valid but the direction of next action is unclear
- The user asks: debug? rerun? ablate? pivot? write it up? park it?

**Use `research-results-auditor`** when:
- Results are finalized and the user wants to check if they legitimately support a claim
- The question is about **confounds, protocol drift, attribution, or claim validity** before writing
- The user is about to lock results into the paper
- The user asks: "does this ablation really prove X?", "is this a confound?", "am I overclaiming?"

**Decision rule**: Is the user deciding what to do next (diagnosis) or checking if a claim is safe to write (audit)?
- Deciding next action → `result-diagnosis`
- Checking claim validity before writing → `research-results-auditor`

---

## `statistical-analysis-planner` vs `result-diagnosis`

**Use `statistical-analysis-planner`** when:
- The user needs to select or apply a specific statistical test
- The question is about p-values, confidence intervals, effect sizes, or seed variance quantification
- The user asks: "is this difference significant?", "how many seeds do I need?", "how do I report variance?"

**Use `result-diagnosis`** when:
- The user needs to decide *what to do* about a surprising outcome
- The question is about interpretation and next action, not about test selection

**Decision rule**: Is the question about statistical methodology (test selection, reporting) or about scientific interpretation and next action?
- Statistical methodology → `statistical-analysis-planner`
- Scientific interpretation / next action → `result-diagnosis`

---

## `experiment-design-planner` vs `baseline-selection-audit`

**Use `experiment-design-planner`** when designing the experiment itself: what ablations, what metrics, what controls, what stop conditions, what logging.

**Use `baseline-selection-audit`** when reviewing whether the chosen baselines are necessary, fair, current, and reviewer-proof — especially if you already have a set of baselines and want to check them.

**Decision rule**: Is the question about designing your own experiments (design) or validating the comparison set (fairness)?
