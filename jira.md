## Jira — Rules & Knowledge

### Formatting
- Always use `contentFormat: adf` with a proper ADF JSON document when creating or editing issue descriptions.
- Markdown format causes literal `\n` characters and broken rendering — never use it for descriptions.

### Scope discipline
- Never perform actions beyond what the user explicitly asked for. When in doubt, ask first.
- "Enhance a ticket" = improve content/structure only — not transition status, reassign, or make workflow decisions.

### Wunder service desk workflow
Open → Provide Estimation → In Progress → Peer Review → Customer Testing → Pending for Release → Closed
Side states: Waiting for Customer, Postponed, Rejected

- **Customer Testing** = work is done, client needs to UAT/verify
- **Waiting for Customer** = waiting for client information or input
- These are different — always clarify intent when searching for pending client action.

### Destructive operations — NEVER allowed
- **NEVER delete Jira projects** — not single, not bulk, not via API
- **NEVER bulk-delete tickets** — individual ticket deletion only with explicit user confirmation
- **NEVER bulk-transition tickets** — transition one at a time, confirm each
- **NEVER use HTTP DELETE via fetchAtlassian** — this is enforced by a PreToolUse hook
- These rules are non-negotiable and enforced by `guard-jira.sh` hook globally.

### cloudId
Wunder Jira: `560ee6d8-523e-4fdc-939f-b1e3843d240a` (https://wunder.atlassian.net)
