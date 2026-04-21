# Validation Scripts

Run the local skill validator from the repository root:

```bash
python3 scripts/validate_skills.py
```

The validator checks:

- YAML frontmatter parses correctly
- `name` matches the skill directory
- common helper-file references in `SKILL.md` exist
- `SKILL.md` does not hardcode Claude-only install paths
