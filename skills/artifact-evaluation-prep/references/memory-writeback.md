# Memory Writeback

When project memory exists, write only durable artifact state.

## Recommended Updates

- `memory/evidence-board.md`: artifact-backed evidence, reproduction commands, generated outputs, and claim coverage labels.
- `memory/risk-board.md`: artifact risks such as missing data, fragile dependencies, runtime over budget, license uncertainty, or unsupported claims.
- `memory/action-board.md`: packaging, smoke-test, upload, release, and reviewer-instruction tasks.
- `memory/decision-log.md`: durable choices about artifact scope, reduced runs, cached outputs, or excluded claims.
- `paper/.agent/`: artifact appendix, supplement, camera-ready, or submission-package links.
- `code/.agent/`: artifact commit, package layout, environment, command entry points, and smoke-test status.

## Entry Style

Use stable IDs when available:

```markdown
### EVD-ART-001 - Artifact support for Table 1
- Status: ready-with-caveats
- Command: `scripts/reproduce_table1.sh --quick`
- Output: `outputs/table1_main.csv`
- Related claims: CLM-001
- Risks: RSK-ART-002
- Last checked: YYYY-MM-DD
```

Do not store full logs or large output tables in memory; link to files instead.
