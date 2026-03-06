# Sync Claude Configuration

You are helping the user synchronize their Claude Code configuration across multiple devices.

## Configuration to sync

Sync the following files and directories from `~/.claude/`:
- `CLAUDE.md` - User instructions and principles
- `settings.json` - Basic settings
- `settings.local.json` - Permissions configuration
- `skills/` - Custom skills directory
- `commands/` - Custom slash commands directory
- `plugins/config.json` - Plugin configuration (if exists)

**Exclude** the following (temporary/session data):
- `debug/`
- `file-history/`
- `history.jsonl`
- `session-env/`
- `shell-snapshots/`
- `todos/`
- `statsig/`
- `projects/`
- `.credentials.json`

## Target servers

**Before running**, ask the user which SSH servers to sync with, for example:
- `my-remote-server`
- `work-laptop`

Or edit this file to pre-fill your servers:
```
# Example:
# - server-alias-1
# - server-alias-2
```

The server aliases must be configured in `~/.ssh/config`.

## Sync strategy (Smart sync)

1. **Check modification times**: For each key file (CLAUDE.md, settings.local.json), compare the modification time between local and remote servers.

2. **Determine sync direction**:
   - If local is newer: Push to servers
   - If any server is newer: Ask user which version to use
   - If timestamps are same: Report no changes needed

3. **Execute sync**: Use `rsync` with appropriate flags to sync the configuration.

## Instructions

1. First, ask the user for their target server(s) if not already configured above
2. Check the modification times of key configuration files on local and all remote servers
3. Show a summary of which files differ and their timestamps
4. Recommend a sync direction based on timestamps
5. Ask for user confirmation before syncing
6. Execute the sync using rsync with `--exclude` flags for temporary files
7. Verify the sync completed successfully by checking file sizes or timestamps
8. Report the results to the user

## Example commands

```bash
# Check local file timestamp
stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" ~/.claude/CLAUDE.md

# Check remote file timestamp
ssh <SERVER> "stat -c '%y' ~/.claude/CLAUDE.md 2>/dev/null || echo 'File not found'"

# Sync from local to remote (excluding temp files)
rsync -avz --exclude='debug' --exclude='file-history' --exclude='history.jsonl' \
  --exclude='session-env' --exclude='shell-snapshots' --exclude='todos' \
  --exclude='statsig' --exclude='projects' --exclude='.credentials.json' \
  ~/.claude/ <SERVER>:~/.claude/

# Sync from remote to local
rsync -avz --exclude='debug' --exclude='file-history' --exclude='history.jsonl' \
  --exclude='session-env' --exclude='shell-snapshots' --exclude='todos' \
  --exclude='statsig' --exclude='projects' --exclude='.credentials.json' \
  <SERVER>:~/.claude/ ~/.claude/
```

Be helpful and clear in your communication. Show the user exactly what will be synced before executing.
