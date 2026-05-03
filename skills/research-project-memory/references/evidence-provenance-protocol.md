# Evidence Provenance Protocol

Evidence provenance records how a project fact moves from raw computation or analysis into paper-facing assets and prose. It prevents tables, captions, and claims from floating away from their source data.

## Provenance Chain

Use this chain when possible:

```text
EXP-### / raw run
  -> CSV / report / analysis artifact
  -> EVD-###
  -> FIG-### table or figure asset
  -> paper section, caption, abstract, or slide
  -> CLM-###
```

Not every evidence item needs every step. A citation may skip experiment IDs; a proof may point to a theorem file. But every paper-facing result should have enough source pointers to be checked later.

## Source Classes

Use these source classes in `memory/provenance-board.md` and `memory/evidence-board.md`:

| Source class | Examples | Required pointer |
|---|---|---|
| `raw-run` | checkpoint, log dir, wandb run, tensorboard event, scheduler job | run ID, command/config pointer, code commit if known |
| `csv` | aggregated metric table, seed-level result table | path, schema/columns, aggregation rule |
| `report` | experiment report, diagnosis report, advisor result note | path and section |
| `analysis` | proof, diagnostic notebook, qualitative annotation | path and method summary |
| `citation` | paper or benchmark reference | citation key and claim role |
| `asset` | paper table, figure PDF/PNG, LaTeX wrapper | path, generation command or script when available |
| `prose` | section sentence, caption, abstract result phrase | section or file location |

## Evidence Status

Use these statuses:

| Status | Meaning |
|---|---|
| `needed` | Evidence required for a claim but not found yet |
| `planned` | Experiment or analysis is designed but not produced |
| `available` | Source exists but has not been audited for paper use |
| `verified` | Source, aggregation, and claim interpretation were checked |
| `provisional` | Temporary result used for drafting and must be replaced |
| `stale` | Older evidence may no longer match current code, claim, or paper text |
| `contradictory` | Evidence weakens or contradicts a claim |
| `cut` | Evidence no longer used in the active story |

## Paper-Facing Asset Requirements

For each paper-facing figure or table, record:

- source evidence IDs
- source CSV/report paths
- transformation or aggregation rule
- script/notebook path when available
- paper asset path
- paper location and caption status
- supported claim IDs
- reviewer risk if provenance is incomplete

## Provisional Results

Temporary numbers are allowed during drafting only if they are explicit:

- mark evidence `provisional`
- record the placeholder value and intended replacement source
- add an action to verify or replace it
- mark dependent prose, caption, table, or figure as provisional or stale

Never promote provisional evidence to `verified` without checking the source path and aggregation.

## Minimal Entry Shape

```yaml
id: PRV-001
status: verified | provisional | stale
source_class: csv
source_paths: []
transform: ""
produces: [EVD-001, FIG-001]
consumed_by: [CLM-001, "paper/sections/exp.tex"]
aggregation: ""
checked_by: agent | user | collaborator
certainty: observed
last_updated: YYYY-MM-DD
```
