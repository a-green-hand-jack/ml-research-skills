# Setup Git and GitHub SSH Connection

You are helping the user set up Git configuration and GitHub SSH authentication on a new device.

## User Information

Before starting, **ask the user** for their:
- **Name**: (e.g. `jiekewu`)
- **Email**: (e.g. `you@example.com`)

Use their answers in all subsequent steps.

## Tasks to Complete

### 1. Configure Git Global Settings

Set up the user's global git configuration:

```bash
git config --global user.name "<YOUR_NAME>"
git config --global user.email "<YOUR_EMAIL>"
```

Also configure some recommended settings:
```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.editor "vim"
```

### 2. Check for Existing SSH Keys

Before creating new keys, check if SSH keys already exist:

```bash
ls -la ~/.ssh/id_*
```

If keys exist, ask the user if they want to:
- Use existing keys
- Create new keys (will backup existing ones)

### 3. Generate SSH Key Pair

If needed, generate a new SSH key pair for GitHub:

```bash
ssh-keygen -t ed25519 -C "<YOUR_EMAIL>" -f ~/.ssh/id_ed25519_github -N ""
```

Note:
- Use ed25519 algorithm (modern and secure)
- Save to `~/.ssh/id_ed25519_github` (specific filename for GitHub)
- Empty passphrase for convenience (or ask user if they want one)

### 4. Start SSH Agent and Add Key

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github
```

### 5. Configure SSH Config

**IMPORTANT**: Do NOT overwrite existing SSH config! Check if `~/.ssh/config` exists first.

If config exists, **append** the GitHub configuration to the existing file:
```bash
# Check if github.com host already exists in config
if [ -f ~/.ssh/config ] && grep -q "Host github.com" ~/.ssh/config; then
    echo "GitHub configuration already exists in SSH config"
else
    # Append to existing config
    cat >> ~/.ssh/config << 'EOF'

# GitHub Configuration
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes
EOF
    echo "GitHub configuration added to SSH config"
fi
```

If config doesn't exist, create it:
```bash
cat > ~/.ssh/config << 'EOF'
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes
EOF
chmod 600 ~/.ssh/config
```

### 6. Display Public Key

Show the public key to the user so they can add it to GitHub:

```bash
cat ~/.ssh/id_ed25519_github.pub
```

### 7. Guide User to Add Key to GitHub

Provide clear instructions:

1. Copy the public key displayed above
2. Go to GitHub: https://github.com/settings/keys
3. Click "New SSH key"
4. Title: "[Device Name] - [Date]" (e.g., "MacBook Pro - 2025-10-30")
5. Key type: Authentication Key
6. Paste the public key
7. Click "Add SSH key"

### 8. Test GitHub Connection

After user confirms they've added the key:

```bash
ssh -T git@github.com
```

Expected output: "Hi <YOUR_NAME>! You've successfully authenticated..."

### 9. Display Summary

Show a summary of what was configured:
- Git global config (name, email)
- SSH key location
- SSH config status
- GitHub connection status

## Important Notes

- **Security**: SSH keys provide secure, passwordless authentication
- **Backup**: If generating new keys, back up existing ones first
- **Multiple Keys**: Using a specific filename (id_ed25519_github) allows multiple SSH keys for different services
- **SSH Config**: The config file ensures the correct key is used for GitHub

## Error Handling

- If ssh-keygen fails, check if OpenSSH is installed
- If GitHub connection fails, verify the key was added correctly
- If permission issues occur with .ssh directory, fix with: `chmod 700 ~/.ssh && chmod 600 ~/.ssh/*`

## Execution Flow

1. Ask user for name and email
2. Check current git configuration
3. Check for existing SSH keys
4. Configure git global settings
5. Generate or use existing SSH key
6. Set up SSH config
7. Display public key and instructions
8. Wait for user to add key to GitHub
9. Test the connection
10. Show success summary

Be interactive and guide the user through each step clearly.
