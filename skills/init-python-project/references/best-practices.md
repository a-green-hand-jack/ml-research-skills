# Best Practices

## Error Handling

- Directory already exists:
  - For new project: ask to choose a different name or cancel.
  - For fork: confirm before cloning into an existing directory.
- Git already initialized:
  - Skip `git init`.
  - Check for existing remotes.
  - Offer to add a different remote name if needed.
- Package name conflict:
  - Flag likely conflicts and suggest alternatives.
- `uv` not installed:
  - Provide installation instructions.
  - Use `pip` only as a fallback if the user wants that.
- GitHub SSH authentication fails:
  - Suggest checking SSH key setup.
  - Offer to continue without a remote.

## Working Principles

1. Prefer editable installs: `uv pip install -e .`
2. Keep tests isolated from project data and outputs.
3. Mirror `src/` in `tests/` where practical.
4. Keep docs proportional to project size.
5. Never hardcode secrets or machine-specific paths in source code.
6. Ask before pushing to a remote.

## Security Notes

- Never commit `.env`.
- Always provide `.env.example`.
- Validate target paths before writing.
- Check for existing sensitive files before initializing git.
