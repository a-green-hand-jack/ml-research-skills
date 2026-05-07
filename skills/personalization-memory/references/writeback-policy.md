# Personalization Writeback Policy

Use this policy to decide where an observed preference or lesson belongs.

## Visibility Routing

| Scope | Write target | Use for | Do not store |
|---|---|---|---|
| `private-user` | Agent-private memory such as `~/.codex/memories/` | local tool paths, aliases, workstation facts, personal interaction preferences, personal writing habits | public project policy, collaborator-visible requirements |
| `project` | `memory/`, `paper/.agent/`, `code/.agent/`, `slides/.agent/` | project contracts, paper-specific writing/style rules, code workflow defaults, compute environment policy | raw chats, local paths, credentials, private collaborator comments |
| `public-skill-candidate` | candidate note in project memory or skill-maintenance TODO | cross-project lessons that may improve this skill repo | direct public edits without a skill-maintenance task |
| `discard` | no writeback | one-off preferences, already captured facts, low-confidence guesses | anything sensitive or ambiguous |

## Promotion Ladder

| Level | Meaning | Typical action |
|---|---|---|
| observation | one event may matter later | write only if cheap and safe, usually as a lesson |
| candidate | plausible reusable preference | record in a preference ledger or sidecar findings |
| preference | repeated or user-stated default | write to private or project memory |
| project contract | stable rule for this project | link from `memory/project.yaml` or component `.agent/` files |
| public skill-rule candidate | likely useful across projects | record as a maintainer task; edit public skills only when requested |

## Automatic Writeback Rules

- `user-stated` preferences may be written automatically if the target is private or project-local and the summary is non-sensitive.
- `repeated` preferences may be written automatically when two or more independent artifacts support the same behavior.
- `observed` one-off lessons may be written as lessons, not as hard rules.
- `inferred` candidates should stay in a ledger until another artifact supports them.
- Public skill edits require normal repo maintenance, validation, commit, push, and reinstall.

## Conflict Handling

When a new preference conflicts with existing memory:

1. Keep both entries if they apply to different scopes or phases.
2. Mark the newer entry as `candidate` when the scope is unclear.
3. Prefer user-stated instructions over inferred observations.
4. Prefer project-local contracts over public defaults for a specific project.
5. Do not ask the user unless acting on the conflict would cause external or irreversible behavior.

## Minimal Entry Standard

Every stored preference should include:

- a short reusable rule
- scope
- confidence
- source artifact or summarized source
- date
- target skill/workflow affected
- promotion status

Avoid transcript excerpts. Use paraphrases.
