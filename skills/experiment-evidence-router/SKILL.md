---
name: experiment-evidence-router
description: Route ML experiment planning, execution, debugging, result interpretation, and evidence packaging tasks to the correct skill. Use this when the task involves experiments, compute, results, or evidence — instead of guessing between run-experiment, run-status-monitor, experiment-debugger, result-diagnosis, research-results-auditor, statistical-analysis-planner, or paper packaging skills. Do not solve the task directly.
allowed-tools: Read, Bash
---

# Experiment Evidence Router

You are a **router**. Do not solve the experiment task directly.

Your job: classify the task → read the route table → select one child skill → hand off.

## Before Routing — Mandatory

1. Detect scope: `git rev-parse --git-common-dir` vs `--show-toplevel`.
2. If `memory/BRIEFING.md` exists, read it for active phase and worktree context.
3. This informs whether the task is planning, active execution, or packaging for paper.

## Classification Buckets

| Bucket | Key signals | Route to |
|---|---|---|
| **planning** | design experiment, ablation plan, hypothesis, baselines, metrics, controls | `experiment-design-planner` |
| **baseline-fairness** | are baselines fair, SOTA current, reviewer will object to comparison | `baseline-selection-audit` |
| **compute** | GPU hours, budget, smoke test sizing, how long will it take | `compute-budget-planner` |
| **data** | dataset, split, contamination, preprocessing, train/val/test protocol | `data-pipeline-manager` |
| **launch** | submit new job, create run, SLURM/RunAI/local script, job file | `run-experiment` |
| **status** | existing job, queued, stuck, running, finished, ContainerCreating | `run-status-monitor` |
| **eng-failure** | NaN, OOM, crash, wrong metrics, slow training, reproducibility failure | `experiment-debugger` |
| **sci-surprise** | valid result but negative, surprising, ambiguous, seeds vary, baselines winning | `result-diagnosis` |
| **claim-audit** | confound, claim-drift, protocol integrity, attribution, lock claim into paper | `research-results-auditor` |
| **statistics** | significance test, p-value, confidence interval, effect size, seed variance | `statistical-analysis-planner` |
| **pivot** | direction change, consistent multi-cycle failure, narrow scope, kill project | `project-pivot-planner` |
| **packaging** | evidence board, tables, figures, provenance, experiment report | `paper-result-asset-builder` or `experiment-report-writer` |

## Routing Steps

1. Identify the single most blocking bucket from the table above.
2. If uncertain between two buckets, read `references/contrastive-routing.md`.
3. If still uncertain, ask one narrowing question before routing.
4. Select exactly one child skill.
5. Hand off — state which skill you are routing to and why.

## Hard Constraints

- Do not debug the experiment yourself.
- Do not interpret results yourself.
- Do not submit jobs yourself.
- If a task spans multiple buckets, route to the bucket that blocks progress first.
- If you cannot classify the task, escalate to the user with a clarifying question; do not default to `result-diagnosis` as a catch-all.
