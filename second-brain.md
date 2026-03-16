## Second Brain — Rules & Usage

### Always use MCP tools directly
- Use `mcp__second-brain__sb_*` MCP tools — never run `sb-capture` or other sb-* commands as shell commands.
- Shell commands are not on PATH in non-interactive shells and will fail.

### Available MCP tools
- `mcp__second-brain__sb_capture` — save new content
- `mcp__second-brain__sb_search` — search by keyword, semantic, or hybrid
- `mcp__second-brain__sb_read` — read a specific note
- `mcp__second-brain__sb_edit` — edit an existing note
- `mcp__second-brain__sb_forget` — delete a note
- `mcp__second-brain__sb_files` — list files
- `mcp__second-brain__sb_actions` — list pending action items
- `mcp__second-brain__sb_actions_done` — mark action done
- `mcp__second-brain__sb_connections` — find connections between notes
- `mcp__second-brain__sb_digest` — generate digest/summary
- `mcp__second-brain__sb_recap` — recap recent activity
- `mcp__second-brain__sb_anonymize` — anonymize sensitive content

### Proactive capture
When you notice high-value content — a decision made, a person discussed, a meeting described, or project context established — offer once: "I noticed a [decision/meeting/person/project context] — capture it?"

If the user says yes, use `mcp__second-brain__sb_capture` with note_type, title, body, and sensitivity params.

Content types that warrant an offer: decisions, people discussions, meeting notes, project context.
Content types that do NOT warrant an offer: casual chat, code snippets, debugging sessions, transient questions.

Re-offer policy: offer once per topic. Re-offer only if significantly more detail emerges about the same topic in the same session.

### Session context
When starting work in a project, offer: "I noticed you're in `{repo}` — run `sb-recap` to see recent activity?"

### GUI
Start with: `cd /Users/tuomasleppanen/second-brain && /Users/tuomasleppanen/.local/bin/uv run sb-gui`
