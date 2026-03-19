# Claude Code — Security Best Practices

Last updated: 2026-03-19

Global security rules and awareness for all projects using Claude Code.

---

## 1. Data Flows to Anthropic

Running under **Anthropic Max plan** (OAuth, no API key). All AI interaction goes through Anthropic's cloud API.

### What gets sent

| Data type | When |
|-----------|------|
| **Conversation context** | Every user message, assistant response, tool call/result in the session |
| **File contents** (Read tool) | When Claude reads source files, configs, docs |
| **Code diffs** (Edit tool) | old_string/new_string pairs |
| **Bash output** | stdout/stderr from Bash tool calls |
| **MCP tool results** | All return values from connected MCP servers |

**Key implication**: Any file read or MCP result becomes part of the conversation and is sent to Anthropic. There is no local-only mode for Claude Code.

**Anthropic's data policy** (Max plan): conversation data is not used for training. Review Anthropic's Terms of Service for current retention and access policies.

---

## 2. External System Access via MCP

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

## 5. Risk Summary

| Risk | Protections | Gaps |
|------|-------------|------|
| **Customer data to Anthropic** | PII-flagged notes routed through local Ollama; Max plan no-training policy | Most notes are `sensitivity: public` by default; no auto-PII classification |
| **AI accessing production** | No SSH keys in devcontainer; `guard-infra.sh` blocks destructive commands | Host Claude Code has full user permissions; no network-level firewall |
| **AI damaging Jira/Calendar** | `guard-jira.sh` blocks project/bulk deletion; permission prompts on write ops | `editJiraIssue` can overwrite fields; no undo for Jira edits via MCP |

---

## 6. Recommendations

1. Run development in devcontainer by default — guardrail hooks are active there
2. Never use `--dangerously-skip-permissions` when Jira/Calendar MCP servers are connected outside devcontainer
3. Review Anthropic's data retention policy quarterly
4. Keep production credentials out of any path accessible to Claude Code
5. Use `sb-forget` two-step token pattern for any destructive operations on brain data
