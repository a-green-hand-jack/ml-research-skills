# Precommit Classifier Sidecar

## Goal

Classify the current unstaged and staged repository changes so the main agent can choose the fastest safe commit path.

## Non-Goals

- Do not edit files.
- Do not stage files.
- Do not commit, push, tag, reinstall skills, submit jobs, or call external services.
- Do not inspect private logs, raw chat transcripts, credentials, or files outside this repository.
- Do not perform final approval for high-risk code, release, or publication decisions.

## Allowed Inspection

Use read-only local inspection only:

```bash
git status --short
git diff --name-only
git diff --stat
git diff
git diff --cached --name-only
git diff --cached --stat
git diff --cached
```

You may also read directly affected public repo files when needed to decide documentation or skill inventory impact.

## Classification Rules

Choose exactly one primary path:

- `Fast Path`: small prose, README, paper text, memory, comments, or narrow docs changes with no helper scripts, templates, schemas, tests, lockfiles, or cross-skill behavior changes.
- `Skill Path`: changes under `skills/*/SKILL.md`, `skills/*/references/`, skill metadata, skill templates, `README.md`, `AGENTS.md`, or `CLAUDE.md` that affect installed agent behavior but do not change executable helper scripts.
- `Code Path`: changes to Python/shell/JS/TS/R scripts, templates that generate executable code, tests, validators, lockfiles, configs, CI, or behavior that needs targeted tests.
- `Risk Path`: branch/worktree operations, merge/rebase/cherry-pick conflicts, destructive operations, release/tag/publication actions, security/privacy-sensitive changes, credential handling, or broad changes with unclear scope.

If multiple paths apply, choose the highest-risk applicable path:

`Risk Path` > `Code Path` > `Skill Path` > `Fast Path`.

## Output Format

Write a concise Markdown report with these exact headings:

```markdown
# Precommit Classification

- Path: Fast Path | Skill Path | Code Path | Risk Path
- Confidence: high | medium | low
- Changed files:
- Why this path:
- Minimal validation:
- Reinstall needed: no | yes, specific skills: <names> | yes, full install
- Commit scope risk:
- Blockers:
- Suggested commit message:
```

Keep recommendations minimal. Prefer targeted validation over full test suites and targeted skill reinstall over reinstalling all skills.
