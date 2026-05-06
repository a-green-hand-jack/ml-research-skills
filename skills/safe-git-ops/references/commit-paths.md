# Commit Path Policy

Use this policy when the user asks for a commit, push, quick save, or says the Git closeout process feels too slow.

The goal is to keep routine commits fast without weakening safety for risky repository operations.

## Path Selection

Choose the highest-risk applicable path:

`Risk Path` > `Code Path` > `Skill Path` > `Fast Path`.

### Fast Path

Use for small prose, README, paper text, memory, comments, or narrow docs changes.

Do not use when helper scripts, tests, generated templates, skill behavior, lockfiles, CI, branch structure, secrets, or release artifacts changed.

Minimal flow:

```bash
git status --short
git diff --check
git add <explicit-files>
git diff --cached --stat
git commit -m "<message>"
git push
```

No default tests. No default reinstall.

### Skill Path

Use when installed agent behavior changes but executable helper scripts do not, such as:

- `skills/*/SKILL.md`
- `skills/*/references/`
- `skills/*/templates/` that are instruction or documentation templates only
- `README.md`, `AGENTS.md`, or `CLAUDE.md` updates caused by skill behavior changes

Minimal flow:

```bash
python3 scripts/validate_skills.py
git diff --check
git add <explicit-files>
git diff --cached --stat
git commit -m "<message>"
git push
```

After push, reinstall only the changed skill names when practical:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s <skill-name> -y
```

Use full reinstall only when inventory, shared docs, installation layout, or many skills changed.

### Code Path

Use when executable behavior changes, such as:

- helper scripts
- validators
- tests
- executable templates
- package, lockfile, or CI/config changes

Minimal flow:

```bash
python3 scripts/validate_skills.py
git diff --check
python3 -m unittest -v <targeted-tests>
git add <explicit-files>
git diff --cached --stat
git commit -m "<message>"
git push
```

Run full smoke tests only for shared infrastructure, runner, reviewer, telemetry, or validation changes.

### Risk Path

Use for:

- merge, rebase, cherry-pick, branch deletion, reset, checkout over local changes, clean, force push
- branch/worktree ambiguity
- unresolved conflicts or dirty-state blockers
- release/tag/publication operations
- credential, secret, source-visibility, or privacy-sensitive changes
- broad changes where scope is unclear

Use the full `safe-git-ops` orientation and failure-mode protocol before state-changing commands. Ask before destructive operations.

## Sidecar-Assisted Classification

For non-trivial closeouts, use `sidecar-task-runner` with the `precommit-classifier` preset. The sidecar may inspect read-only `git status` and `git diff`, then recommend a path, minimal validation, and reinstall scope.

The main agent keeps responsibility for:

- deciding whether to accept the sidecar recommendation
- staging files
- committing
- pushing
- reinstalling skills
- reporting the result to the user

Do not let a sidecar commit, push, tag, release, submit jobs, or publish issues.

Suggested preparation:

```bash
python3 <sidecar-task-runner-skill-dir>/scripts/prepare_sidecar_task.py \
  --repo . \
  --title "Precommit classifier" \
  --phase maintenance \
  --task-type audit \
  --preset precommit-classifier \
  --input "git status --short" \
  --input "git diff"
```
