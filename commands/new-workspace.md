# Create New Git Workspace (Branch or Worktree)

You are helping the user create a new Git branch or worktree for experiments or features.

## Workflow

### 1. Ask User for Workspace Type

Ask the user to choose:
- **branch**: Create a new branch in the current working directory
- **worktree**: Create a new worktree in a separate directory

### 2. Ask for Branch Type and Name

Ask the user to choose the branch type:
- **feature**: For new features (creates `feature/<name>`)
- **exp**: For experiments (creates `exp/<name>`)

Then ask for the branch name (without prefix). For example:
- User inputs: `authentication`
- Result: `feature/authentication` or `exp/authentication`

### 3. Verify Current Git State

Before creating anything, check:
```bash
# Ensure we're in a git repository
git rev-parse --git-dir

# Check for uncommitted changes
git status --porcelain
```

If there are uncommitted changes, warn the user and ask if they want to:
- Stash changes and continue
- Commit changes first
- Cancel operation

### 4. Create Branch or Worktree

#### Option A: Create Branch Only

```bash
# Create and checkout new branch
git checkout -b <branch-type>/<branch-name>
```

Show success message and current branch.

#### Option B: Create Worktree

**Steps:**

1. **Get project root directory:**
```bash
git rev-parse --show-toplevel
```

2. **Create worktree directory structure:**
```bash
# Worktrees will be at: <project-root>/../worktrees/<branch-name>/
PROJECT_ROOT=$(git rev-parse --show-toplevel)
WORKTREE_DIR="$PROJECT_ROOT/../worktrees/<branch-type>-<branch-name>"

# Create worktree
git worktree add "$WORKTREE_DIR" -b <branch-type>/<branch-name>
```

3. **Sync IDE configuration directories:**

Automatically copy IDE configuration folders from project root to worktree:

```bash
# Copy IDE configuration directories
for config_dir in .vscode .cursor .claude; do
    if [ -d "$PROJECT_ROOT/$config_dir" ]; then
        echo "Copying $config_dir configuration..."
        cp -r "$PROJECT_ROOT/$config_dir" "$WORKTREE_DIR/"
        echo "✓ $config_dir synced"
    fi
done
```

**Important**: These directories are **copied** (not symlinked) so that:
- Each worktree can have independent IDE settings if needed
- Changes in one worktree don't affect others
- You can customize settings per experiment/feature

4. **Check for .worktree-links configuration:**

Look for `.worktree-links` file in the project root:
```bash
LINKS_CONFIG="$PROJECT_ROOT/.worktree-links"
if [ -f "$LINKS_CONFIG" ]; then
    # Read and process links
    while IFS= read -r line; do
        # Skip empty lines and comments
        [[ -z "$line" || "$line" =~ ^#.* ]] && continue

        # Create symlink from worktree to original location
        SOURCE="$PROJECT_ROOT/$line"
        TARGET="$WORKTREE_DIR/$line"

        if [ -e "$SOURCE" ]; then
            # Create parent directory if needed
            mkdir -p "$(dirname "$TARGET")"
            ln -s "$SOURCE" "$TARGET"
            echo "Linked: $line"
        else
            echo "Warning: Source not found: $line"
        fi
    done < "$LINKS_CONFIG"
fi
```

**Format of `.worktree-links` file:**
```
# Lines starting with # are comments
# List relative paths from project root to link

data/
models/
.env
configs/local_settings.yaml
```

4. **Sync UV environment in the new worktree:**

```bash
cd "$WORKTREE_DIR"

# Check if pyproject.toml exists (indicating a Python project with uv)
if [ -f "pyproject.toml" ]; then
    echo "Syncing UV environment..."
    uv sync
    echo "UV environment synced successfully"
else
    echo "No pyproject.toml found, skipping UV sync"
fi
```

5. **Display summary:**
```
✓ Worktree created at: <worktree-path>
✓ Branch created: <branch-type>/<branch-name>
✓ Symlinks created: <count> items
✓ UV environment synced

To start working:
  cd <worktree-path>
```

### 5. Error Handling

Handle common errors:

- **Not in a git repository**: Show clear error message
- **Branch already exists**: Ask if user wants to:
  - Create worktree from existing branch (if applicable)
  - Choose a different name
  - Cancel
- **Worktree directory already exists**: Ask to remove or choose different name
- **UV sync fails**: Show error but don't rollback worktree creation
- **.worktree-links not found**: Continue without creating symlinks (this is optional)

### 6. Additional Features

**Optional: List existing worktrees**

If user chooses worktree option, first show existing worktrees:
```bash
git worktree list
```

This helps user see what already exists.

## Configuration File Template

If `.worktree-links` doesn't exist in the project, you can offer to create it with common defaults:

```
# .worktree-links
#
# Symlinks to create in new worktrees
# List paths relative to project root
# Lines starting with # are ignored

# Example entries:
# data/
# models/
# .env
# configs/production.yaml
```

## Best Practices

1. **Always show a summary** of what will be created before executing
2. **Validate branch names** (no spaces, special characters except `-` and `_`)
3. **Check disk space** before creating worktree (optional, for large repos)
4. **Clean up on failure**: If worktree creation fails midway, remove partial worktree
5. **Preserve user context**: After creating worktree, suggest next steps (cd to worktree, open in editor, etc.)

## Important Notes

- **Worktree isolation**: Each worktree has its own working directory but shares the same Git object database
- **UV environment**: Each worktree gets its own `.venv/` (not symlinked) to avoid conflicts
- **Symlinks are absolute paths**: Use absolute paths in symlinks to ensure they work from the worktree location
- **Branch tracking**: New branches are created as local branches (not tracking remote)

## Security Considerations

- Validate all user inputs (branch names, paths)
- Don't execute arbitrary commands from config files
- Ensure symlinks point within expected directories
- Warn if symlink targets are outside project root

## Troubleshooting

**Issue: "uv sync fails in new worktree"**
- Check if symlinked files/dirs are causing issues
- Ensure `pyproject.toml` and `uv.lock` are not symlinked
- Try running `uv sync --reinstall`

**Issue: "Symlinks not working"**
- Verify source paths exist in original location
- Check file permissions
- Ensure proper path resolution

**Issue: "Git worktree add fails"**
- Check if branch name conflicts with existing branches
- Verify worktree path is valid and accessible
- Ensure no existing worktree at that location

## Example Interaction Flow

**Example 1: Creating a worktree for a new feature**

```
User: /new-workspace