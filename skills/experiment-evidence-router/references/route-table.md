# Experiment Evidence Route Table

Use this table when the classification bucket from the main SKILL.md is not immediately obvious.

| Task type | Concrete signals | Correct skill | Wrong choices to avoid |
|---|---|---|---|
| Design experiment | "what ablations do I need", "how many seeds", "what metrics to log", "what are my controls" | `experiment-design-planner` | `baseline-selection-audit` (different: that's about fairness, not design) |
| Audit baselines | "is this baseline fair", "is this SOTA current", "reviewers will ask why I didn't compare to X" | `baseline-selection-audit` | `experiment-design-planner` (different: that's about your own design) |
| Size compute | "how many GPU hours", "will this fit in my allocation", "smoke test budget", "cost of 8 ablations" | `compute-budget-planner` | `run-experiment` (different: budgeting comes before submission) |
| Prepare data | "preprocess dataset", "design train/val/test split", "check for contamination", "data quality" | `data-pipeline-manager` | `experiment-design-planner` (different: data prep is not experiment design) |
| Submit new job | "run this config", "generate job script", "submit to SLURM/RunAI", "create local training run" | `run-experiment` | `run-status-monitor` (different: status is for existing jobs) |
| Check existing job | "is my job running", "it's stuck in queue", "ContainerCreating", "how long left", "job finished?" | `run-status-monitor` | `run-experiment` (different: launching is for new jobs) |
| Debug crash/NaN/OOM | "training crashed", "NaN loss", "GPU out of memory", "metric looks wrong", "can't reproduce" | `experiment-debugger` | `result-diagnosis` (different: debugging is engineering, diagnosis is science) |
| Interpret valid result | "baseline is winning", "surprising negative result", "what should I do next", "seeds vary a lot" | `result-diagnosis` | `experiment-debugger` (different: valid results aren't bugs) |
| Audit claim before writing | "does this ablation prove X", "confound risk", "claim-drift", "protocol integrity" | `research-results-auditor` | `result-diagnosis` (different: auditing is about claim validity, not deciding what to do) |
| Statistical rigor | "is this significant", "effect size", "confidence interval", "how many seeds needed" | `statistical-analysis-planner` | `result-diagnosis` (different: stats planning is about test selection, not diagnosis) |
| Multi-cycle failure | "core claim hasn't held after 3 rounds", "should I pivot", "narrow scope or change direction" | `project-pivot-planner` | `result-diagnosis` (different: pivot is after multiple cycles, not one experiment) |
| Build paper assets | "generate table from CSV", "create figure wrappers", "provenance records" | `paper-result-asset-builder` | `experiment-report-writer` (different: asset builder produces LaTeX artifacts, report writer produces narrative) |
| Write experiment report | "write up what happened", "experiment summary for advisor", "document this run" | `experiment-report-writer` | `paper-result-asset-builder` (different: report is prose, assets are LaTeX) |
