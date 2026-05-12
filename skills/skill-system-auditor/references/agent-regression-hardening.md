# Agent Regression Hardening

Use this reference when a skill technically exists but agents keep doing the wrong thing in live sessions. The goal is to turn observed regressions into behavior that activates earlier, costs fewer tokens, and survives installation into future projects.

## Regression Pattern

Common signs that a skill needs hardening rather than a new skill:

- The user says "we already fixed this" or "isn't there a skill for this?"
- Agents use the old command shape after a helper or wrapper exists.
- Agents perform a long action in the main transcript that should be artifact-bounded.
- Agents retry the same failing tool/API call without a new recovery path.
- Agents choose a resource, environment, or backend without checking task intent and startup cost.
- A rule exists in prose but not in routing metadata, core contracts, templates, or installed runtime copies.

## Hardening Ladder

Promote a lesson through the smallest layer that will actually change behavior:

1. `description`: add trigger phrases so the skill activates before the mistake is made.
2. `Core Contract`: state the required behavior, prohibited loop, stop condition, and fallback.
3. `references/`: explain edge cases, classification rules, examples, and failure modes.
4. `templates/`: make new projects inherit the behavior without rereading the repo history.
5. `scripts/` or wrappers: stabilize repeated command shapes when approvals, quoting, or shell behavior are the failure source.
6. `memory/`: record the decision, risk, action, evidence, and provenance so later maintenance does not rediscover the lesson.
7. Runtime reinstall: refresh installed skills after push and verify the installed copy contains the rule.

Do not stop at step 3 when the regression is caused by missed activation or stale project guidance. In those cases, update the description and templates too.

## Design Checks

For each user-observed regression, ask:

- What did the agent do that wasted context, time, compute, or trust?
- Which skill should have owned the situation earlier?
- Was the trigger missing from `description`, hidden too deep in references, or absent from generated project guidance?
- Is this a preference, a project contract, a public reusable rule, or a private environment fact?
- What is the first failure signal that should stop retries?
- What bounded artifact should replace raw transcript output?
- What command shape or wrapper would make sandbox approvals and quoting stable?
- What validation or installed-copy check proves the fix is live?

## Patterns From Recent Hardening

Stable command shapes:

- If equivalent command forms cause approval churn, ship or prefer one wrapper command.
- Document the wrapper in the owning skill, root/project guidance, and templates.
- Keep normal preflight; wrappers reduce command drift but do not replace safety checks.

Earlier routing:

- If agents miss a protocol, add concrete trigger phrases to the skill description and user-facing project guidance.
- Include the failure vocabulary the agent will actually see, such as `invalid_grant`, raw SSH one-liners, `ContainerCreating`, image pull, or transcript-visible polling.

Circuit breakers:

- Repeated failures need a stop rule, not just a retry limit.
- Classify auth, scheduler, image startup, resource pending, and environment setup separately from code failure.
- After the first unrecoverable-in-context signal, switch to a fallback or record one explicit recovery action.

Artifact-bounded work:

- Long-lived observation, noisy logs, source reading, reviews, and audits should produce short artifacts.
- The main agent should read compressed fields and paths, not raw logs or repeated probe output.
- Status artifacts should include the next useful check condition, suggested cadence, and stop condition.

Resource-aware execution:

- Distinguish smoke/debug/formal tasks before changing compute.
- For smoke/debug, prefer the fastest compatible resource that can validate the code path.
- For formal runs, preserve the experimental resource contract unless the user explicitly changes it.
- Treat environment creation, image startup, and hardware/software compatibility as scheduling costs.

Public/private split:

- General workflow rules belong in public skills.
- Cluster names, paths, user accounts, job IDs, and unpublished project context belong in private memory or project-local ignored artifacts.
- If a private lesson looks reusable, sanitize it before promoting it into public skills.

## Closeout Checklist

Before considering the hardening done:

- The owning skill's `description` can route the next similar request.
- The core contract names the prohibited behavior and the replacement path.
- References cover failure classification and stop conditions.
- Templates or project guidance inherit the rule when relevant.
- Public memory records the durable decision without private facts.
- Validation passed.
- Changed skills were reinstalled, or the final report says why not.
- The installed copy was checked for the new trigger or rule.
