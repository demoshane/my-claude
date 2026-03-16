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

### 3. Reinstall plugins

Claude Code will auto-detect `settings.json` and prompt to reinstall plugins on first launch.
If not, reinstall manually from `plugins/installed_plugins.json` — each entry has the marketplace and plugin name.

Key marketplaces:
- `claude-plugins-official` → `github:anthropics/claude-plugins-official`
- `claude-code-workflows` → `github:wshobson/agents`
- `claude-context-mode` → `github:mksglu/claude-context-mode`
- `voltagent-subagents` → `https://github.com/VoltAgent/awesome-claude-code-subagents.git`

### 4. Verify hooks work

```bash
node ~/.claude/hooks/claude-config-backup.js <<< '{}'
node ~/.claude/hooks/claude-config-backup-session.js <<< '{}'
```

Both should exit silently (no errors).

### 5. Set up git remote (if restoring from scratch)

The repo is already cloned with the correct remote, so auto-backup will work immediately.
Verify with:

```bash
git -C ~/.claude remote -v
```

---

## How auto-backup works

Two hooks keep this repo in sync automatically:

- **PostToolUse** (`hooks/claude-config-backup.js`) — fires after every file write/edit in `~/.claude/`, commits and pushes the changed file immediately.
- **SessionStart** (`hooks/claude-config-backup-session.js`) — fires when Claude Code starts, catches any changes made by the app itself (plugin installs, updates) between sessions.

You never need to manually commit — changes are pushed to GitHub within seconds.

---

## Adding new tool-specific rules

1. Create `~/.claude/<tool>.md` with the rules
2. Add a one-liner to `CLAUDE.md` under **Tool-specific rules**:
   ```
   When working with <Tool>: @~/.claude/<tool>.md
   ```
The new file will be auto-backed up on first save.
