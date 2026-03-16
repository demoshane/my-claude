# My Claude Config

Personal configuration, rules, agents, and hooks for [Claude Code](https://claude.ai/code).

Automatically backed up via git hooks on every change.

---

## What's in here

| Path | What it is |
|---|---|
| `CLAUDE.md` | Global instructions Claude follows in every session |
| `jira.md` | Jira-specific rules (referenced from CLAUDE.md) |
| `second-brain.md` | Second Brain MCP tool usage rules (referenced from CLAUDE.md) |
| `settings.json` | Claude Code settings — enabled plugins, hooks, model |
| `policy-limits.json` | Security policy (e.g. remote control disabled) |
| `agents/` | 100+ custom agent definitions |
| `hooks/` | Automation hooks (context monitor, GSD, auto-backup) |
| `commands/gsd/` | GSD slash command definitions |
| `get-shit-done/` | GSD plugin workflows, templates, and tooling |
| `plugins/installed_plugins.json` | Installed plugin list with versions |
| `plugins/known_marketplaces.json` | Plugin marketplace sources |
| `plugins/blocklist.json` | Blocked plugins |

---

## How to restore on a new machine

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Clone this repo into ~/.claude

```bash
# Back up any existing config first
mv ~/.claude ~/.claude.bak 2>/dev/null || true

# Clone
git clone git@github.com:demoshane/my-claude.git ~/.claude
```

### 3. Run the setup script

```bash
sh ~/.claude/setup.sh
```

This will:
- Install the pre-commit secret scanner (not tracked by git, must be installed per machine)
- Verify git remote, Node.js, and hook scripts
- Pull latest config from remote
- Print plugin reinstall instructions

### 4. Start Claude Code

Claude Code will auto-detect `settings.json` and prompt to reinstall plugins.
If not, check `plugins/installed_plugins.json` for the full list and reinstall manually.

---

## How auto-backup and sync works

Two hooks keep all machines in sync automatically:

### SessionStart (`hooks/claude-config-backup-session.js`)
Runs when Claude Code starts. Syncs in this order:
1. Detects any local out-of-band changes (plugin installs, app updates)
2. If local changes exist: stash → pull --rebase → pop stash → commit → push
3. If no local changes: just pull

### PostToolUse (`hooks/claude-config-backup.js`)
Fires after every Write/Edit on a tracked config file:
1. Commits the changed file immediately
2. Pulls with rebase (to pick up any changes from other machines)
3. Pushes

You never need to manually commit — changes are pushed within seconds and pulled at the start of every session.

### Multi-machine workflow
- **Machine A** makes a change → auto-committed and pushed immediately
- **Machine B** starts a session → SessionStart hook pulls the change automatically
- No manual `git pull` needed ever

---

## Adding new tool-specific rules

1. Create `~/.claude/<tool>.md` with the rules
2. Add a one-liner to `CLAUDE.md` under **Tool-specific rules**:
   ```
   When working with <Tool>: @~/.claude/<tool>.md
   ```
The new file will be auto-backed up on first save.
