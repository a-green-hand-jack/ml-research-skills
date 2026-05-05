---
name: add-git-tag
description: Create annotated Git milestone tags. Use when completing a phase, releasing a version, marking a research checkpoint, or generating a milestone summary from git history before tagging.
allowed-tools: Read, Write, Bash
---

# Add Git Tag Workflow

Use this workflow whenever the user wants to mark a milestone in the current Git repository with a tag. The agent may use a read-only sidecar to draft milestone content from git history, but the main agent must keep the human gates before creating or pushing a tag.

## Execution Contract

- Default runner: main agent.
- Sidecar eligible: yes, for read-only milestone proposal generation.
- Suggested sidecar model: `gpt-5.3-codex-spark` through `codex exec --ephemeral`.
- Sidecar permissions: `read-only`.
- Human gates: before `git tag -a`; before `git push origin <tag>`.
- Final actions: only the main agent creates and pushes tags.
- Required artifacts when using a sidecar: `.agent/sidecars/<task-id>/prompt.md`, `output.md`, `model.json`, and `decision.md`.

## Step 1 — Gather or Propose Milestone Information

If the user already supplied all three items, use them directly:

1. **Tag version**: What should the tag name be? (e.g. `v0.1.3`)
2. **Achievements**: What was accomplished in this phase? (provide a short bullet-point list of features/fixes completed)
3. **Next plans**: What is planned for the next phase? (provide a short bullet-point list of upcoming goals)

If one or more items are missing, do not force the user to fill the whole form from scratch. First inspect the repo state and, when available, use `sidecar-task-runner` to draft a proposal from recent commits, tags, README or changelog snippets, and project memory.

Read-only context command:

```bash
REPO=$(git rev-parse --show-toplevel 2>/dev/null) && \
git -C "$REPO" log --oneline --decorate -30 && \
git -C "$REPO" status --short && \
git -C "$REPO" tag --sort=-version:refname | head -10
```

Suggested sidecar prompt:

```text
Use recent git history and visible project docs to propose an annotated milestone tag.
Do not create a tag, commit, push, or edit production files.

Return:
- suggested tag name
- achievements as concise bullets with commit evidence
- next plans as concise bullets inferred from docs or TODOs
- uncertainty notes where the evidence is weak
```

If sidecar execution is not available, use the read-only git context yourself and ask the user only for the missing or uncertain fields.

## Step 2 — Confirm the tag message (Show a preview)

After collecting user input or a sidecar proposal, **compose and display** the full annotated tag message for the user to review. The format should be:

```
Tag: <version>
Date: <current date, YYYY-MM-DD>

## ✅ This Phase — What Was Achieved
- <bullet 1>
- <bullet 2>
...

## 🚀 Next Phase — What's Planned
- <bullet 1>
- <bullet 2>
...
```

Ask the user: **"Does this look good? Should I go ahead and create the tag?"**

Wait for confirmation before proceeding.

## Step 3 — Verify the repository state

// turbo
Detect the current Git project root and check status:

```bash
REPO=$(git rev-parse --show-toplevel 2>/dev/null) && \
git -C "$REPO" log --oneline -5 && \
git -C "$REPO" status --short && \
git -C "$REPO" tag --sort=-version:refname | head -5
```

This gives the last 5 commits, any uncommitted changes, and the 5 most recent existing tags.

## Step 4 — Create the annotated tag

// turbo
Only after user confirmation, detect the repo root and create the tag:

```bash
REPO=$(git rev-parse --show-toplevel)
git -C "$REPO" tag -a "<version>" -m "<full_tag_message>"
```

Where:

- `<version>` is the tag name from the user (e.g. `v0.1.3`)
- `<full_tag_message>` is the full formatted message from Step 2

## Step 5 — Push the tag to remote (ask first)

Ask the user: **"Would you like to push the tag `<version>` to the remote repository (origin)?"**

If yes:
// turbo

```bash
REPO=$(git rev-parse --show-toplevel)
git -C "$REPO" push origin "<version>"
```

If no, inform the user that the tag was created locally and can be pushed later with:

```bash
git push origin <version>
```

## Step 6 — Confirm success

```bash
REPO=$(git rev-parse --show-toplevel)
git -C "$REPO" tag -n1 <version>
```

Report the outcome to the user:

- Show the tag that was created
- Confirm whether it was pushed to remote
- Remind the user they can view all tags with `git tag -n1 --sort=-version:refname`
