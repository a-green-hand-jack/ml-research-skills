# Phase Dashboard Protocol

The phase dashboard gives a global project-cycle view. It should answer: where is the project now, what phase gate is blocking progress, and which claim/evidence/writing/review objects need attention next.

## Location

Use:

```text
memory/phase-dashboard.md
```

## Phase Model

Use these phases:

| Phase | Goal | Main gate |
|---|---|---|
| `idea` | Decide whether the project direction is worth pursuing | pursue/revise/park/kill decision |
| `positioning` | Decide what the paper sells and to whom | primary contribution and forbidden claims |
| `method-design` | Specify method, assumptions, and ablations | implementable design and experiment implications |
| `implementation` | Build reliable code path | runnable method and baseline setup |
| `experiment-design` | Plan evidence against claims | experiment matrix and baseline policy |
| `evidence-production` | Produce and diagnose results | verified evidence or revised claims |
| `paper-asset-building` | Convert results into paper tables/figures | provenance-tracked assets |
| `drafting` | Write sections from contract and evidence | section completeness and provisional result tracking |
| `internal-review` | Simulate reviewers and check consistency | must-fix risk list |
| `submission` | Prepare the final submission package | compile/readiness/anonymity/citation gates |
| `rebuttal` | Respond to real reviews | promised actions and response strategy |
| `camera-ready` | Finalize accepted paper | fulfilled promises and final evidence lock |
| `artifact-release` | Package artifact/code/reproduction | reproducible artifact and public release |
| `maintenance` | Keep docs, memory, tags, and timeline current | clean handoff to next milestone |

## Dashboard Fields

The dashboard should track:

- current phase
- phase objective
- active gate
- readiness: `blocked | partial | ready | done`
- linked claim IDs
- linked evidence IDs
- linked risks
- linked actions
- stale objects
- next phase trigger

## Update Rules

- Update after project initialization, major result changes, writing milestones, review arrival, rebuttal submission, acceptance, artifact release, or milestone tag.
- If a phase regresses, record why rather than pretending the project only moves forward.
- Use the dashboard for orientation; use claim/evidence/provenance/risk/action/handoff boards for details.
- If the user asks "where are we?", answer from the dashboard plus live verification of volatile state.

## Readiness Gates

Before moving forward:

- `positioning` -> paper has a primary contribution and claim boundaries.
- `method-design` -> method spec has implementation and experiment handoffs.
- `evidence-production` -> important claims have verified or explicitly provisional evidence.
- `drafting` -> writing contract and writing memory exist for active sections.
- `internal-review` -> consistency editor and reviewer simulator issues have actions or accepted-risk decisions.
- `submission` -> citation, anonymity, formatting, and evidence checks have no fatal blocker.
- `camera-ready` -> rebuttal promises are fulfilled or explicitly resolved.
- `artifact-release` -> reproduction path and release obligations are clear.
