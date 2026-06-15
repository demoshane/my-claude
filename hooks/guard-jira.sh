#!/usr/bin/env bash
# guard-jira.sh — PreToolUse hook: block destructive Jira operations
# Prevents: project deletion, bulk ticket deletion, bulk transitions
# Allows: all read ops, single ticket create/edit/comment/transition
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

# Only check Jira MCP tools
case "$TOOL_NAME" in
    mcp__claude_ai_Atlassian__*) ;;
    *) exit 0 ;;
esac

# Block: deleteProject, deleteIssue (these don't exist yet but guard against future)
if echo "$TOOL_NAME" | grep -qiE '(delete|remove).*project'; then
    echo '{"decision": "block", "reason": "BLOCKED: Jira project deletion is forbidden. This is a global safety rule."}'
    exit 2
fi

# Block: bulk operations via JQL that could affect many tickets
# fetchAtlassian with DELETE method
if [ "$TOOL_NAME" = "mcp__claude_ai_Atlassian__fetchAtlassian" ]; then
    if echo "$TOOL_INPUT" | grep -qiE '"method"\s*:\s*"DELETE"'; then
        echo '{"decision": "block", "reason": "BLOCKED: HTTP DELETE via Atlassian fetch is forbidden. This is a global safety rule."}'
        exit 2
    fi
fi

# Block: bulk transition (transitioning more than one issue in a loop)
# This is harder to catch at hook level — we rely on the system prompt for this

exit 0
