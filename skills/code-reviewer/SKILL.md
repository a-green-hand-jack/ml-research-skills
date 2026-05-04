---
name: code-reviewer
description: Run isolated code reviews for core algorithm or production code changes. Use when the user asks for a fresh-context reviewer, writer/reviewer separation, code review, implementation audit, review bundle, independent review, or review artifacts under `.agent/code-reviews/`.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Code Reviewer

Run code review as an isolated artifact-driven workflow. The reviewer should judge the implemented change from the task contract, diff, writer summary, tests, and relevant files, not from the writer's conversation history.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── scripts/
│   └── prepare_review_bundle.py
├── references/
│   └── isolation-protocol.md
└── templates/
    ├── review.md
    └── fix-log.md
```

## Core Rule

The reviewer must not inherit the writer's chat context. Use one of these patterns:

- Strong isolation: start a new Codex or Claude Code session and give it only the review bundle path.
- Cross-agent isolation: Codex writes and Claude Code reviews, or Claude Code writes and Codex reviews.
- Subagent isolation: use a fresh subagent only if it does not fork the current writer context.

The reviewer input is the bundle, not the writer conversation.

## Bundle Workflow

1. Create a review bundle after implementation:

```bash
python3 <installed-skill-dir>/scripts/prepare_review_bundle.py \
  --repo . \
  --base main \
  --request "Implement <feature> with <acceptance criteria>" \
  --writer-summary "Changed <files>; ran <tests>; known risks: <risks>"
```

2. For uncommitted work, include the working tree:

```bash
python3 <installed-skill-dir>/scripts/prepare_review_bundle.py \
  --repo . \
  --working-tree \
  --request-file .agent/code-reviews/<change-id>/request.md
```

3. Launch a fresh reviewer with only:

```text
Use code-reviewer.
Review the bundle at .agent/code-reviews/<change-id>/.
Do not modify production code.
Write findings to .agent/code-reviews/<change-id>/review.md.
```

4. The writer then reads `review.md`, fixes the code, and records responses in `fix-log.md`.

5. For high-risk changes, run a second fresh review after fixes.

## Reviewer Behavior

Read `references/isolation-protocol.md` before reviewing.

Review only the change described by the bundle:

- `request.md`: task contract and acceptance criteria
- `writer-summary.md`: what changed, tests run, known risks
- `diff.patch`: stat and patch
- `test-output.md`: test commands and outputs
- `reviewer-prompt.md`: ready-to-use fresh reviewer prompt

Focus on:

- correctness and algorithmic assumptions
- edge cases, invariants, and data shape assumptions
- tests that would fail if the implementation were wrong
- maintainability and integration risk
- mismatch between request, writer summary, diff, and tests

Do not rewrite the implementation unless the user explicitly asks for reviewer-as-fixer mode. Default reviewer output is `review.md`.

## Findings Format

Use this severity order:

- `High`: likely correctness bug, data corruption, invalid experiment result, security/privacy issue, or broken public API
- `Medium`: edge-case bug, missing test for risky behavior, fragile design, or confusing integration
- `Low`: maintainability nit, naming issue, small docs mismatch

Each finding must include:

- file and line when possible
- problem
- why it matters
- required fix
- suggested test

End with one verdict:

- `request changes`
- `acceptable with nits`
- `approve`

## Handoff Back To Writer

The writer should update `fix-log.md` with:

- each review item
- action taken
- commit or file reference
- tests rerun
- items intentionally not fixed and why

If review findings change the task scope or algorithm contract, update the project memory or design docs before continuing.
