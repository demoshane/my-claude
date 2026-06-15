# Claude Code — Security Best Practices

Last updated: 2026-06-15

Global security rules and awareness for all projects using Claude Code.

---

## 1. External System Access via MCP

All external MCP calls are proxied through Anthropic's infrastructure.

```
Claude Code (local) → Anthropic API (cloud) → MCP proxy (Anthropic-hosted) → External API
```

### Write-capable systems (highest risk)

1. **Jira** — can create/edit issues, transition status, add comments. Protected by `guard-jira.sh` hook.
2. **Google Calendar** — can create/update/delete events.
3. **Miro** — can create/modify boards, documents, tables, diagrams.
4. **Harvest** — can create/edit/delete time entries, clients, projects, invoices (production time-tracking data). Connected directly via HTTP transport (`https://api.harvestapp.com/mcp`), not the Anthropic MCP proxy. Delete actions blocked by `guard-harvest.sh` hook.

### Read-only systems

- Figma, n8n, Context7, Wunder Quality System

---

## 3. Global Guardrail Hooks

### `guard-jira.sh` (PreToolUse)
- Blocks Jira project deletion
- Blocks HTTP DELETE via fetchAtlassian
- Bulk ticket operations require individual confirmation

### `guard-infra.sh` (PreToolUse)
- SSH: blocks destructive remote commands (rm, shutdown, reboot, kill, systemctl stop)
- kubectl: blocks delete, drain, cordon, scale-to-0
- SCP: allowed (non-destructive)
- Read-only operations always allowed

### `guard-harvest.sh` (PreToolUse)
- Blocks any `mcp__harvest__*` tool whose name contains delete/remove/destroy
- Blocks HTTP DELETE via any generic Harvest request tool
- Read and non-destructive create/edit operations allowed

> **Note:** all three guards read the hook payload as JSON on **stdin** (`tool_name`/`tool_input`), with a fallback to the legacy `CLAUDE_TOOL_NAME`/`CLAUDE_TOOL_INPUT` env vars. The env-var-only form is a silent no-op in current Claude Code — keep new guards on stdin.

---

## 4. Credential Hygiene

| Location | Contains | Security |
|----------|----------|----------|
| macOS Keychain (`Claude Code-credentials`) | OAuth tokens | Keychain ACL |
| `~/.config/second-brain/claude-oauth.json` | Extracted Keychain copy for devcontainer | chmod 600 |
| `~/.config/second-brain/.env.host` | Project env vars | chmod 600 |
| `~/.ssh/` | SSH keys | Never mounted into devcontainers |

**Rules:**
- Never read, log, print, or expose secret values
- Keep production credentials out of home directory and env files
- `detect-secrets` pre-commit hook prevents committing secrets to git

---

## 5. Recommendations

1. Run development in devcontainer by default — guardrail hooks are active there
2. Never use `--dangerously-skip-permissions` when Jira/Calendar/Harvest MCP servers are connected outside devcontainer
3. Review Anthropic's data retention policy quarterly
4. Keep production credentials out of any path accessible to Claude Code
5. Use `sb-forget` two-step token pattern for any destructive operations on brain data
