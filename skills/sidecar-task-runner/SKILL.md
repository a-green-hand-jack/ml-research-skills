---
name: sidecar-task-runner
description: Run artifact-driven sidecar agent tasks through one-shot Codex CLI sessions. Use when a main agent should delegate bounded scans, drafts, audits, pre-reviews, or mechanical repo tasks to a fast isolated sidecar model such as gpt-5.3-codex-spark while keeping final decisions with the main agent.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Sidecar Task Runner

Use this skill to run bounded helper tasks from a main agent without sharing the main conversation as the task state. The sidecar produces artifacts; the main agent verifies, integrates, rejects, or escalates them.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
└── scripts/
    └── prepare_sidecar_task.py
```

## Core Contract

- The main agent owns planning, integration, final judgment, and user-facing actions.
- The sidecar gets a small prompt artifact, not the main chat transcript.
- Default to `gpt-5.3-codex-spark` for fast local scans, first drafts, pre-reviews, consistency checks, and other low/medium-risk tasks.
- Prefer deterministic scripts and direct shell commands for facts; use the sidecar for synthesis, ranking, summarization, mismatch detection, and candidate text.
- Default sandbox is `read-only`. Use `workspace-write` only when the sidecar must write its own artifacts or make explicitly bounded edits.
- Keep human gates before external or irreversible actions such as `git tag`, `git push`, release upload, job submission, or public issue creation.
- Do not use a sidecar as the only reviewer for high-risk algorithm design, core correctness, security/privacy, final merge approval, or final submission decisions.

## Artifact Layout

Use a repo-local directory:

```text
.agent/sidecars/<task-id>/
├── prompt.md
├── input-manifest.md
├── output.md
├── findings.md
├── decision.md
├── model.md
└── model.json
```

Meanings:

- `prompt.md`: exact prompt given to the sidecar.
- `input-manifest.md`: files, commands, diffs, or project state the sidecar may inspect.
- `output.md`: raw sidecar final response, usually written with `codex exec -o`.
- `findings.md`: distilled findings if the sidecar writes structured results.
- `decision.md`: main-agent decision after reading the sidecar output.
- `model.md`: human-readable command, model, sandbox, and token notes.
- `model.json`: structured run metadata for token and lifecycle audits.

## Prepare A Task

Create the artifact directory with:

```bash
python3 <installed-skill-dir>/scripts/prepare_sidecar_task.py \
  --repo . \
  --task-id <task-id> \
  --title "<short task title>" \
  --phase tooling \
  --task-type audit \
  --prompt-file <prompt-file>
```

If no prompt file exists, pass `--prompt "<task instructions>"`.

## Run Codex Spark

For a read-only sidecar:

```bash
codex exec --ephemeral \
  -m gpt-5.3-codex-spark \
  -C . \
  -s read-only \
  -o .agent/sidecars/<task-id>/output.md \
  "$(cat .agent/sidecars/<task-id>/prompt.md)"
```

For a sidecar that must write its own `findings.md` or make tightly scoped artifact edits:

```bash
codex exec --ephemeral \
  -m gpt-5.3-codex-spark \
  -C . \
  -s workspace-write \
  -o .agent/sidecars/<task-id>/output.md \
  "$(cat .agent/sidecars/<task-id>/prompt.md)"
```

Avoid `codex resume`, `codex fork`, `claude --continue`, or `claude --resume` for first-pass sidecar work. Those are continuation mechanisms, not clean sidecar boundaries.

## Prompt Requirements

Every sidecar prompt should state:

- task goal and non-goals
- files or directories it may inspect
- whether code edits are allowed
- required output path and format
- escalation criteria for strong reviewer or main-agent judgment
- privacy boundary: do not copy raw private logs or unrelated conversation text into repo artifacts

Keep prompts narrow. If the task needs several independent analyses, create separate sidecar runs rather than one broad prompt.

## Model Routing

Good Spark sidecar tasks:

- first-pass code review before a strong review
- git milestone proposal from recent commits and docs
- README / AGENTS / CLAUDE consistency scan
- test-gap scan after a focused implementation
- experiment log triage and config mismatch inventory
- evidence inventory across CSVs, reports, tables, and figures
- reviewer-comment clustering and action-item extraction
- citation placeholder or TODO scans

Use the main agent or a stronger fresh reviewer for:

- core algorithm design decisions
- final code approval for high-risk changes
- security, privacy, or data-governance decisions
- large refactors with unclear blast radius
- final paper positioning, rebuttal strategy, or submission judgment

## Token Telemetry

Because `--ephemeral` may avoid normal persisted session logs, record run metadata in `model.json`. If Codex CLI reports token usage in the terminal, copy the numeric fields into `model.json` or `model.md` before running `token-usage-auditor`.

If exact usage is unavailable, leave usage values as `null` and record:

```text
Token usage: unavailable from ephemeral run output.
```

Never store raw prompts from private chat logs just to recover token counts.
