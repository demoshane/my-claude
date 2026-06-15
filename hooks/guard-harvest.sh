#!/usr/bin/env bash
# guard-harvest.sh — PreToolUse hook: block destructive Harvest MCP operations
# Prevents: any delete/remove/destroy action via the Harvest MCP server,
#           plus any HTTP DELETE issued through a generic Harvest request tool.
# Allows: all read ops and non-destructive create/edit operations.
set -euo pipefail

# Current Claude Code passes hook payload as JSON on stdin. Older convention
# used CLAUDE_TOOL_NAME / CLAUDE_TOOL_INPUT env vars — honour both.
INPUT="$(cat 2>/dev/null || true)"

TOOL_NAME="${CLAUDE_TOOL_NAME:-}"
if [ -z "$TOOL_NAME" ] && [ -n "$INPUT" ]; then
    TOOL_NAME="$(printf '%s' "$INPUT" \
        | grep -oE '"tool_name"[[:space:]]*:[[:space:]]*"[^"]*"' \
        | head -1 \
        | sed -E 's/.*:[[:space:]]*"([^"]*)"/\1/')"
fi

TOOL_INPUT="${CLAUDE_TOOL_INPUT:-$INPUT}"

# Only check Harvest MCP tools
case "$TOOL_NAME" in
    mcp__harvest__*) ;;
    *) exit 0 ;;
esac

# Block: any delete/remove/destroy/unassign operation by tool name.
# 'unassign' is destructive in effect (tears down a project assignment) but
# its name avoids the delete/remove/destroy substrings — match it explicitly.
if printf '%s' "$TOOL_NAME" | grep -qiE '(delete|remove|destroy|unassign)'; then
    echo '{"decision": "block", "reason": "BLOCKED: Delete actions via the Harvest MCP are forbidden. Harvest holds production time-tracking data. Read and non-destructive create/edit operations are allowed. This is a global safety rule."}'
    exit 2
fi

# Block: HTTP DELETE via any generic Harvest request/fetch tool
if printf '%s' "$TOOL_INPUT" | grep -qiE '"method"[[:space:]]*:[[:space:]]*"DELETE"'; then
    echo '{"decision": "block", "reason": "BLOCKED: HTTP DELETE via the Harvest MCP is forbidden. This is a global safety rule."}'
    exit 2
fi

exit 0
