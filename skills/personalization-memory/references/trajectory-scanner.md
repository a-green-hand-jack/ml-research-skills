# Trajectory Scanner Protocol

Use a low-cost sidecar to scan interaction traces without feeding the main agent's whole context back into itself.

## Inputs To Prefer

- recent `git diff` or `git log --stat`
- `memory/current-status.md`, `memory/decision-log.md`, `memory/action-board.md`, and related boards
- `.agent/sidecars/*/decision.md`, `findings.md`, and `model.json`
- `.agent/code-reviews/*/review.md` and `fix-log.md`
- `.agent/layout-issues/*/manifest.md` and issue summaries
- paper/code/slide `.agent/` contracts and ledgers
- sanitized summaries of Codex or Claude Code trajectory logs

Raw agent logs can contain private messages, local paths, collaborator text, and irrelevant context. If they must be scanned, the sidecar prompt must say: summarize derived preferences only; do not quote raw logs; do not copy sensitive material into repo artifacts.

## Sidecar Prompt Shape

Use `sidecar-task-runner` with the `personalization-scanner` preset. Add `--input` items that describe exactly which files or log summaries may be inspected.

The sidecar must output:

- candidate preferences
- scope recommendation: private-user, project, public-skill-candidate, or discard
- confidence: observed, repeated, user-stated, or inferred
- evidence paths or sanitized source summaries
- suggested write target
- reason to defer, if any

The sidecar must not:

- edit memory directly
- ask the user questions
- publish raw logs
- promote public skill rules by itself
- change Git state, submit jobs, tag releases, or push

## Main-Agent Review

The main agent reviews the sidecar output and decides:

- write private memory now
- update project memory now
- create a public skill-maintenance candidate
- discard as noisy or unsafe

Record that decision in the sidecar `decision.md` when the sidecar artifact matters for later audit.

## Good Scan Cadences

- after a substantial writing/layout/figure/code-review session
- before a commit that updates skill behavior
- during weekly project memory closeout
- after repeated user corrections reveal a stable preference
- before a skill-system audit

Do not run a trajectory scan after every tiny command. Use it when the expected memory yield is higher than the scan overhead.
