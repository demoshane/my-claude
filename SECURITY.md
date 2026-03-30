# Claude Code — Security Best Practices

Last updated: 2026-03-19

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
2. Never use `--dangerously-skip-permissions` when Jira/Calendar MCP servers are connected outside devcontainer
3. Review Anthropic's data retention policy quarterly
4. Keep production credentials out of any path accessible to Claude Code
5. Use `sb-forget` two-step token pattern for any destructive operations on brain data
