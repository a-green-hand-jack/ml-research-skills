# Classification Policy

## Never Publish

Mark as `private-only` when content contains:

- credentials, tokens, API keys, passwords, cookies, private keys, auth headers
- usernames, account IDs, emails, home-directory paths, private project paths
- private hostnames, SSH aliases, internal IPs, VPN details, port-forward details
- unpublished project details, collaborator identities, reviewer notes, or lab-private context
- raw agent trajectories, raw chat logs, or raw private memory excerpts
- data paths, server paths, bucket names, job IDs, or logs that reveal private infrastructure

## Redactable

Mark as `redactable` when the useful part is an operational pattern but the source includes private specifics.

Examples of redactable patterns:

- "Use route inspection to determine whether traffic goes through VPN or local routing"
- "Separate SSH DNS failure, TCP timeout, banner timeout, and auth failure"
- "Convert a private host route into a reusable troubleshooting checklist"
- "Replace local absolute paths with `<project-root>` or `<private-path>`"

## Publishable

Mark as `publishable` only when content is already generic and does not depend on private context:

- abstract workflow steps
- public tool commands with placeholders
- reusable checklists
- skill routing logic
- validation patterns

## Reusable Pattern

Mark as `reusable-pattern` when content should become a public skill, template, or reference after sanitization:

- repeated debugging protocol
- project-management workflow
- validation checklist
- public/private boundary rule
- model routing or sidecar orchestration pattern

## Conservative Default

If the source mixes private facts and generic ideas, classify the raw source as `private-only` and create a separate sanitized candidate as `redactable` or `reusable-pattern`.

If ownership or publication rights are unclear, use `needs-human-review`.
