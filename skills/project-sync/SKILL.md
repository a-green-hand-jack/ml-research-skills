---
name: project-sync
description: Sync verified experiment results from the code repo or a code worktree into the paper's daily experiments log and project memory. Use when results in code/docs/results, code/docs/reports, code/docs/runs, worktree docs, logs, or user-confirmed metrics should be promoted into paper-facing evidence.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Project Sync Workflow

Use this workflow when you have new experiment results in the code repo or a code worktree and want to record them in the paper's `daily_experiments.tex`.

This is a **manual, human-triggered** workflow — run it whenever you want to checkpoint results into the paper.

Pair this skill with `research-project-memory` when the logged result should update evidence, claims, risks, actions, or paper status.

---

## Step 1 — Locate the Project

// turbo
Auto-detect the project structure. Run:

```bash
# Find the git root of the current repo
git rev-parse --show-toplevel 2>/dev/null

# Check if we're in code/ or paper/ and find sibling
ls "$(git rev-parse --show-toplevel)/../"
```

Determine:
- `$CODE_ROOT` - the code repo root or active code worktree root
- `$PAPER_ROOT` - the paper repo root
- `$PROJECT_ROOT` - the project control root, if present

In a project-init project, `paper/` and `code/` are component repos under the project control root, and code worktrees usually live under `code-worktrees/`. If the paper repo cannot be inferred, ask the user:
> "Where is the paper repo? Please provide its path."

---

## Step 2 — Gather New Results

Ask the user **in a single message**:

1. **Date**: What date are these experiments? (default: today's date, YYYY-MM-DD)
2. **Short title**: A brief label for this experiment batch (e.g. "Baseline on CIFAR-10", "Ablation: remove attention layer")
3. **Setup**: What method variant / config / dataset was used?
4. **Results**: What are the key numbers? (paste metrics, accuracy, loss, etc.)
5. **Observation**: What do the results mean? What worked, what didn't?
6. **Next**: What follow-up experiment is planned?

Optionally, also check if there are existing result files to pull from:

```bash
# Stable code-side evidence
find "$CODE_ROOT/docs/results" "$CODE_ROOT/docs/reports" "$CODE_ROOT/docs/runs" -maxdepth 2 -type f 2>/dev/null | sort | tail -20

# Raw or ignored outputs, if present
find "$CODE_ROOT/outputs" "$CODE_ROOT/logs" "$CODE_ROOT/checkpoints" -maxdepth 2 -type f 2>/dev/null | sort | tail -20
```

If relevant result summaries or reports exist, read them and pre-fill the answers for the user to confirm. Treat raw logs as supporting material, not paper-facing evidence, unless the user confirms the numbers.

---

## Step 3 — Preview the Entry

Compose and display the LaTeX entry for the user to review:

```latex
\subsection*{<DATE> — <SHORT TITLE>}
\textbf{Setup:} <setup>\\
\textbf{Result:} <results>\\
\textbf{Observation:} <observation>\\
\textbf{Next:} <next>
```

Ask: **"Does this look correct? Should I add it to the paper?"**

Wait for confirmation.

---

## Step 4 — Insert into daily_experiments.tex

// turbo
Read the current contents of `$PAPER_ROOT/sections/daily_experiments.tex`.

Insert the new entry **at the top** (below the comment header), so the log is in reverse chronological order (newest first).

After inserting, show the user the updated top of the file to confirm it looks right.

---

## Step 5 — Commit to Paper Repo (optional)

Ask: **"要把这条实验记录提交到 paper repo 的 Git 吗？(Y/n)"**

If yes:

```bash
git -C "$PAPER_ROOT" add sections/daily_experiments.tex
git -C "$PAPER_ROOT" commit -m "exp: add <DATE> — <SHORT TITLE>"
```

If no, inform the user the file is saved and can be committed later.

---

## Step 6 — Confirm

Report:

```
Experiment logged:
  Date:   <DATE>
  Title:  <SHORT TITLE>
  File:   <PAPER_ROOT>/sections/daily_experiments.tex

To view all logged experiments:
  cat <PAPER_ROOT>/sections/daily_experiments.tex
```

## Step 7 — Update Project Memory When Present

If the parent project has `memory/`, update:

- `memory/evidence-board.md`: add the logged result as an `EVD-###` or link it to an existing `EXP-###`
- `memory/provenance-board.md`: record the source path, confirmation status, and daily-log/paper-facing consumer path
- `memory/claim-board.md`: move affected claims to `supported`, `weakened`, `provisional`, or `evidence-needed`
- `memory/risk-board.md`: add or close risks exposed by the result
- `memory/action-board.md`: add the next experiment/report/writing action from the log entry
- `memory/handoff-board.md`: create a handoff to `paper-evidence-board`, `paper-result-asset-builder`, or `experiment-story-writer` when the synced result needs paper consumption
- `memory/phase-dashboard.md`: update the active evidence or drafting gate if this sync changes project readiness
- `paper/.agent/paper-status.md`: note that `sections/daily_experiments.tex` now contains the result
- `code/.agent/` or `<code-worktree>/.agent/worktree-status.md`: mark that the result was promoted to paper-facing evidence

Treat the daily experiment log as evidence only if the numbers are source-linked or user-confirmed. Otherwise mark certainty as `user-stated` or `needs-verification`.
