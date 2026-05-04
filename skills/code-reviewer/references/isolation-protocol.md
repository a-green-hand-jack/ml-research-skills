# Fresh-Context Code Review Protocol

Use this protocol to keep code-writer and code-reviewer roles independent.

## Isolation Contract

The reviewer may read:

- original task contract
- writer summary
- git diff or commit range
- test output
- relevant source files needed to verify the diff
- project guidance such as `AGENTS.md`, `CLAUDE.md`, or component docs

The reviewer must not read:

- the writer's chat transcript
- writer chain-of-thought or private reasoning
- prior reviewer conclusions unless doing an explicit follow-up review
- unrelated project history that is not needed to judge the change

## Context Boundary

Prefer a fresh agent session for review. If using an orchestration system that can spawn subagents, do not fork the writer context for the reviewer. Pass only the review bundle path and the review instructions.

Useful fresh reviewer prompt:

```text
You are the code-reviewer.

Review only the bundle at .agent/code-reviews/<change-id>/.
Do not modify production code.
Read request.md, writer-summary.md, diff.patch, and test-output.md.
Open only files needed to verify the diff.
Write the review to review.md.

Prioritize correctness, edge cases, tests, design risk, and maintainability.
Use severity High / Medium / Low.
End with verdict: request changes, acceptable with nits, or approve.
```

## Reviewer Output

Write findings to `review.md`; do not leave only chat comments. A review finding is actionable only if it identifies a concrete risk and a required fix or test.

Good finding:

```markdown
### Medium: Missing test for empty-batch path

- File: `src/train/loss.py:87`
- Problem: the new reduction assumes `batch_size > 0`.
- Why it matters: filtered datasets can produce empty batches in evaluation.
- Required fix: handle empty tensors before reduction or skip the batch.
- Suggested test: add an empty-batch unit test for the loss wrapper.
```

Weak finding:

```markdown
Maybe improve this function.
```

## Writer Response

The writer reads `review.md`, fixes the code, and writes `fix-log.md`. The fix log should be explicit enough that a second reviewer can check whether each finding was handled without reading the writer's chat.

If the reviewer asks for a change that expands scope, the writer should either:

- implement it and update the task contract, or
- record why it is out of scope in `fix-log.md`.

## GitHub Issues

Use local review artifacts by default. GitHub issues are optional and should be reserved for collaborator-visible follow-up work, long-lived risks, or items that must survive outside the branch.

Avoid `git notes` for the first-line workflow; notes are less visible in normal repo browsing and require explicit refs syncing.
