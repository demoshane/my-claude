#!/bin/sh
# setup.sh — Run this after cloning on a new machine
# Sets up git hooks and verifies the environment
#
# Usage: sh ~/.claude/setup.sh

set -e

CLAUDE_DIR="$(cd "$(dirname "$0")" && pwd)"
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

ok()   { printf "${GREEN}✓${NC} %s\n" "$1"; }
warn() { printf "${YELLOW}!${NC} %s\n" "$1"; }
fail() { printf "${RED}✗${NC} %s\n" "$1"; }

echo ""
echo "Setting up Claude config at $CLAUDE_DIR"
echo "─────────────────────────────────────────"

# 1. Install pre-commit hook (not tracked by git, must be installed manually)
PRE_COMMIT="$CLAUDE_DIR/.git/hooks/pre-commit"
cat > "$PRE_COMMIT" << 'HOOK'
#!/bin/sh
# Pre-commit hook: block commits containing likely secrets

ASSIGN_PATTERN='(api[_-]?key|secret[_-]?key|access[_-]?token|auth[_-]?token|private[_-]?key|client[_-]?secret|password|passwd)\s*[=:]\s*["'"'"']?[a-zA-Z0-9+/\-_.]{16,}'
TOKEN_PATTERN='(sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{36,}|xoxb-[a-zA-Z0-9\-]{40,}|AKIA[A-Z0-9]{16}|AIza[a-zA-Z0-9\-_]{35})'

STAGED=$(git diff --cached --name-only)

for FILE in $STAGED; do
  CONTENT=$(git show ":$FILE" 2>/dev/null || true)
  if echo "$CONTENT" | grep -Eiq "$ASSIGN_PATTERN"; then
    echo "⛔ Blocked: possible secret (assignment pattern) in $FILE"
    echo "   Remove any API keys, tokens, or passwords before committing."
    exit 1
  fi
  if echo "$CONTENT" | grep -Eq "$TOKEN_PATTERN"; then
    echo "⛔ Blocked: possible secret (token format) in $FILE"
    echo "   Remove any API keys, tokens, or passwords before committing."
    exit 1
  fi
done

exit 0
HOOK
chmod +x "$PRE_COMMIT"
ok "Pre-commit secret scanner installed"

# 2. Verify git remote
REMOTE=$(git -C "$CLAUDE_DIR" remote get-url origin 2>/dev/null || echo "")
if [ -n "$REMOTE" ]; then
  ok "Git remote: $REMOTE"
else
  fail "No git remote configured"
  echo "  Run: git -C ~/.claude remote add origin git@github.com:demoshane/my-claude.git"
fi

# 3. Check Node.js is available (required for hooks)
if command -v node >/dev/null 2>&1; then
  ok "Node.js $(node --version) found"
else
  fail "Node.js not found — hooks will not run"
  echo "  Install Node.js: https://nodejs.org"
fi

# 4. Verify hook scripts exist
for HOOK in claude-config-backup.js claude-config-backup-session.js; do
  if [ -f "$CLAUDE_DIR/hooks/$HOOK" ]; then
    ok "Hook found: hooks/$HOOK"
  else
    fail "Hook missing: hooks/$HOOK"
  fi
done

# 5. Do initial pull to ensure we're up to date
echo ""
echo "Pulling latest config from remote..."
if git -C "$CLAUDE_DIR" pull --rebase origin main 2>/dev/null; then
  ok "Up to date with remote"
else
  warn "Could not pull from remote (check SSH key / network)"
fi

# 6. Remind about plugins
echo ""
echo "─────────────────────────────────────────"
echo "Next steps:"
echo ""
echo "  1. Start Claude Code — it will detect settings.json and prompt to reinstall plugins"
echo "  2. If plugins don't auto-install, check plugins/installed_plugins.json for the list"
echo ""
echo "Plugin marketplaces to register if needed:"
echo "  • claude-plugins-official  → github:anthropics/claude-plugins-official"
echo "  • claude-code-workflows    → github:wshobson/agents"
echo "  • claude-context-mode      → github:mksglu/claude-context-mode"
echo "  • voltagent-subagents      → https://github.com/VoltAgent/awesome-claude-code-subagents.git"
echo ""
ok "Setup complete"
echo ""
