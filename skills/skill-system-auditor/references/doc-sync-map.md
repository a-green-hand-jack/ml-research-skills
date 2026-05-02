# Documentation Sync Map

When the skill inventory changes, check these files first:

- `README.md`: public inventory, lifecycle categories, role categories, typical workflow, capability sections.
- `AGENTS.md`: agent-facing repo instructions and current skill set table.
- `CLAUDE.md`: Claude Code-facing inventory and design patterns.
- `skills/research-project-memory/references/writeback-protocol.md`: writeback expectations for new state-changing skills.
- `docs/audits/`: previous audit reports that mention future gaps.

Useful searches:

```bash
rg -n "future|planned|not implemented|TODO|artifact-evaluation-prep|advisor-update-writer|skill-system-auditor" README.md CLAUDE.md AGENTS.md skills docs
rg -n "Pair this skill with|writeback|memory" skills/*/SKILL.md skills/*/references
python3 scripts/validate_skills.py
```

Keep historical reports factual. If updating an old report, prefer adding a short follow-up status rather than pretending the original audit happened later.
