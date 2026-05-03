# Claim Lifecycle Protocol

Claims are the central objects of a research project. A claim should not jump from "idea" to "paper text" without passing through evidence, risk, and writing gates.

## Lifecycle States

Use these states in `memory/claim-board.md`:

| State | Meaning | Allowed next states |
|---|---|---|
| `idea` | Possible claim, not yet committed to the project story | `planned`, `parked`, `cut` |
| `planned` | Claim is intended but required evidence is not yet specified | `evidence-needed`, `active`, `cut` |
| `evidence-needed` | Claim has a clear evidence requirement but insufficient support | `provisional`, `supported`, `weakened`, `cut` |
| `provisional` | Claim is written or planned using placeholder or incomplete evidence | `supported`, `weakened`, `revised`, `cut` |
| `active` | Claim is part of the current paper/project story | `supported`, `evidence-needed`, `weakened`, `revised`, `cut` |
| `supported` | Evidence is verified enough for current paper scope | `final`, `weakened`, `revised` |
| `weakened` | New evidence or review pressure reduced claim strength | `revised`, `evidence-needed`, `cut` |
| `revised` | Claim wording, scope, or target changed | `active`, `supported`, `evidence-needed`, `cut` |
| `parked` | Claim is useful but outside the current paper or milestone | `planned`, `cut` |
| `cut` | Claim should not appear in the active paper/story | none, except a new claim ID if revived |
| `final` | Accepted/camera-ready claim locked against final evidence | `revised` only if a post-acceptance correction is needed |

## Required Fields Per Claim

Every non-cut claim should have:

- stable ID: `CLM-###`
- lifecycle state
- one-sentence claim text
- claim type
- target paper location or project component
- required evidence slot
- current supporting evidence IDs
- main risk IDs
- next gate
- certainty label
- last updated date

## Gates

Use gates to prevent hidden overclaiming:

| Gate | Question | Usual owner |
|---|---|---|
| `positioning` | Is this claim part of the paper we are selling? | `paper-positioning-planner` |
| `method` | Does the method actually imply this claim? | `algorithm-design-planner` |
| `evidence` | What result, proof, analysis, or citation would support it? | `experiment-design-planner`, `paper-evidence-board` |
| `provenance` | Can the evidence source be traced to files, runs, CSVs, or paper assets? | `paper-result-asset-builder`, `project-sync` |
| `writing` | Is the claim stated with the right strength in the right section? | `paper-writing-assistant`, section writers |
| `review` | Would a reviewer accept the evidence for this claim? | `paper-reviewer-simulator` |
| `final` | Is this still true in the submitted or camera-ready paper? | `submit-paper`, `camera-ready-finalizer` |

## Transition Rules

- When evidence strengthens a claim, update both `memory/claim-board.md` and `memory/evidence-board.md`.
- When evidence weakens a claim, mark the claim `weakened` or `revised`; do not silently keep old wording.
- When writing uses a temporary number or result, mark the claim `provisional` and link the placeholder in paper-local memory.
- When a claim is cut, record why and remove or mark stale dependent prose, figures, tables, slides, and rebuttal promises.
- When a claim reaches `final`, its evidence, paper location, and provenance must be traceable.

## Closeout Checklist

Before ending a substantial session, ask:

- Did any claim change state?
- Did any new evidence support, weaken, or contradict a claim?
- Did any draft prose use a claim whose state is not `supported` or `final`?
- Did any reviewer, advisor, or result change the next gate?
- Are cut or parked claims still visible in paper text, captions, slides, or contribution bullets?
