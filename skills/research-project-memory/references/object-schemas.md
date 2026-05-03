# Object Schemas

Use stable IDs so claims, evidence, figures, risks, actions, reviews, and worktrees can cross-reference each other.

## ID Prefixes

- `CLM-###`: paper or project claim
- `EVD-###`: evidence item
- `EXP-###`: experiment or run family
- `FIG-###`: figure or table
- `PRV-###`: provenance link from source data or analysis to evidence/assets/prose
- `RSK-###`: risk
- `ACT-###`: action
- `DEC-###`: durable decision
- `WTR-###`: worktree or branch
- `REV-###`: reviewer or rebuttal issue
- `HND-###`: cross-module handoff

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
lifecycle_state: idea | planned | evidence-needed | provisional | active | supported | weakened | revised | parked | cut | final
text: ""
paper_location: ""
claim_type: method | theory | empirical | benchmark | system | analysis | application | limitation
required_evidence: ""
supported_by: [EVD-001]
threatened_by: [RSK-001]
actions: [ACT-001]
next_gate: positioning | method | evidence | provenance | writing | review | final
certainty: user-stated
last_updated: YYYY-MM-DD
```

## Evidence

```yaml
id: EVD-001
kind: experiment | analysis | proof | citation | qualitative | figure | review | rebuttal
status: needed | planned | available | verified | provisional | stale | contradictory | cut
summary: ""
source_paths: []
supports: [CLM-001]
weakens: []
traced_by: [PRV-001]
visualized_by: [FIG-001]
limitations: ""
certainty: observed
last_updated: YYYY-MM-DD
```

## Experiment

```yaml
id: EXP-001
status: planned | submitted | running | completed | failed | abandoned
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
traced_by: [PRV-001]
status: planned | draft | current | stale | cut
certainty: observed
last_updated: YYYY-MM-DD
```

## Provenance

```yaml
id: PRV-001
status: planned | available | verified | provisional | stale | cut
source_class: raw-run | csv | report | analysis | citation | asset | prose
source_paths: []
transform: ""
aggregation: ""
produces: [EVD-001, FIG-001]
consumed_by: [CLM-001, "paper/sections/exp.tex"]
checked_by: agent | user | collaborator | unknown
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
linked_handoffs: [HND-001]
status: todo | doing | blocked | done | cancelled
next_step: ""
due: ""
last_updated: YYYY-MM-DD
```

## Handoff

```yaml
id: HND-001
status: proposed | ready | consumed | blocked | stale | cancelled
producer: ""
consumer: ""
from_component: project | paper | code | slides | reviewer | rebuttal | artifact
to_component: project | paper | code | slides | reviewer | rebuttal | artifact
payload: ""
source_paths: []
expected_outputs: []
linked_claims: [CLM-001]
linked_evidence: [EVD-001]
linked_actions: [ACT-001]
acceptance_check: ""
staleness_trigger: ""
certainty: observed
last_updated: YYYY-MM-DD
```

## Phase Dashboard Entry

```yaml
phase: idea | positioning | method-design | implementation | experiment-design | evidence-production | paper-asset-building | drafting | internal-review | submission | rebuttal | camera-ready | artifact-release | maintenance
status: blocked | partial | ready | done
gate: ""
linked_claims: [CLM-001]
linked_evidence: [EVD-001]
blocking_risks: [RSK-001]
active_actions: [ACT-001]
next_phase_trigger: ""
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
