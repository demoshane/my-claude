#!/usr/bin/env bash
# guard-infra.sh — PreToolUse hook: block destructive infra commands
# Prevents: destructive ssh/scp/kubectl commands by AI
# Allows: read-only and non-destructive operations
set -euo pipefail

TOOL_NAME="${CLAUDE_TOOL_NAME:-}"
TOOL_INPUT="${CLAUDE_TOOL_INPUT:-}"

# Only check Bash tool
[ "$TOOL_NAME" = "Bash" ] || exit 0

# Extract the command from input
CMD="$TOOL_INPUT"

# --- SSH: block destructive remote commands ---
if echo "$CMD" | grep -qE '\bssh\b'; then
    # Block: rm, rmdir, drop, delete, shutdown, reboot, systemctl stop/disable, kill
    if echo "$CMD" | grep -qE 'ssh\s+\S+.*\b(rm|rmdir|drop|delete|shutdown|reboot|kill|systemctl\s+(stop|disable|restart)|service\s+\S+\s+(stop|restart)|docker\s+(rm|stop|kill|system\s+prune))\b'; then
        echo '{"decision": "block", "reason": "BLOCKED: Destructive command via SSH is forbidden. Read-only SSH operations are allowed. This is a global safety rule."}'
        exit 2
    fi
fi

# --- SCP: allow (file transfer is non-destructive) ---
# scp itself is fine — it copies files, doesn't delete

# --- kubectl: block destructive operations ---
if echo "$CMD" | grep -qE '\bkubectl\b'; then
    # Block: delete, drain, cordon, taint, scale to 0, rollout undo
    if echo "$CMD" | grep -qE 'kubectl\s+(delete|drain|cordon|taint)\b'; then
        echo '{"decision": "block", "reason": "BLOCKED: Destructive kubectl command is forbidden. Read-only kubectl operations (get, describe, logs) are allowed. This is a global safety rule."}'
        exit 2
    fi
    # Block: scale to 0 replicas
    if echo "$CMD" | grep -qE 'kubectl\s+scale\b.*--replicas\s*=?\s*0'; then
        echo '{"decision": "block", "reason": "BLOCKED: kubectl scale to 0 replicas is forbidden. This is a global safety rule."}'
        exit 2
    fi
fi

exit 0
