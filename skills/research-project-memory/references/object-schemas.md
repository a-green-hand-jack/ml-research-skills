# Object Schemas

Use stable IDs so claims, evidence, figures, risks, actions, reviews, and worktrees can cross-reference each other.

## ID Prefixes

- `CLM-###`: paper or project claim
- `EVD-###`: evidence item
- `EXP-###`: experiment or run family
- `FIG-###`: figure or table
- `RSK-###`: risk
- `ACT-###`: action
- `DEC-###`: durable decision
- `WTR-###`: worktree or branch
- `REV-###`: reviewer or rebuttal issue

## Certainty Labels

Use:

- `observed`: directly verified from files, logs, command output, paper text, or review text
- `user-stated`: stated by the user
- `inferred`: inferred by the agent and should be treated cautiously
- `stale`: was true at some earlier point but may have changed
- `needs-verification`: required before acting

## Claim

```yaml
id: CLM-001
status: planned | active | revised | supported | weakened | cut
text: ""
paper_location: ""
claim_type: method | theory | empirical | benchmark | system | analysis | application | limitation
supported_by: [EVD-001]
threatened_by: [RSK-001]
actions: [ACT-001]
certainty: user-stated
last_updated: YYYY-MM-DD
```

## Evidence

```yaml
id: EVD-001
kind: experiment | analysis | proof | citation | qualitative | figure | review | rebuttal
summary: ""
source_paths: []
supports: [CLM-001]
weakens: []
visualized_by: [FIG-001]
limitations: ""
certainty: observed
last_updated: YYYY-MM-DD
```

## Experiment

```yaml
id: EXP-001
status: planned | running | completed | failed | abandoned
hypothesis: ""
branch_or_worktree: WTR-001
run_ids: []
metrics: []
supports: [CLM-001]
outputs: []
decision: continue | rerun | write | revise-method | park | kill
certainty: observed
last_updated: YYYY-MM-DD
```

## Figure or Table

```yaml
id: FIG-001
kind: figure | table
paper_location: ""
source_paths: []
shows: [EVD-001]
supports: [CLM-001]
status: planned | draft | current | stale | cut
certainty: observed
last_updated: YYYY-MM-DD
```

## Risk

```yaml
id: RSK-001
kind: novelty | baseline | mechanism | evaluation | writing | execution | reproducibility | reviewer | rebuttal
summary: ""
threatens: [CLM-001]
severity: low | medium | high | fatal
probability: low | medium | high
mitigation: ""
actions: [ACT-001]
status: open | mitigated | accepted | closed
certainty: inferred
last_updated: YYYY-MM-DD
```

## Action

```yaml
id: ACT-001
summary: ""
owner: user | agent | collaborator | unknown
component: project | paper | code | slides | reviewer | rebuttal
linked_claims: [CLM-001]
linked_evidence: [EVD-001]
linked_risks: [RSK-001]
status: todo | doing | blocked | done | cancelled
next_step: ""
due: ""
last_updated: YYYY-MM-DD
```

## Worktree

```yaml
id: WTR-001
path: ""
branch: ""
purpose: ""
linked_claims: [CLM-001]
linked_experiments: [EXP-001]
latest_result: ""
exit_condition: merge | continue | park | kill | unknown
status: active | merged | parked | killed | stale
certainty: observed
last_updated: YYYY-MM-DD
```

## Decision

```yaml
id: DEC-001
date: YYYY-MM-DD
decision: ""
why: ""
alternatives_considered: []
affects: [CLM-001, ACT-001]
revisit_when: ""
certainty: user-stated
```
