#!/usr/bin/env node
// claude-config-backup-session.js — SessionStart hook
// Syncs ~/.claude config with GitHub on session start:
//   1. Commit any local out-of-band changes (plugin installs, etc.)
//   2. Check if remote has changes — INFORM user, don't auto-pull
//   3. Push local commits if any

const { spawnSync } = require('child_process');

const CLAUDE_DIR = '/Users/tuomasleppanen/.claude';
const GIT = '/usr/bin/git';

function git(...args) {
  return spawnSync(GIT, ['-C', CLAUDE_DIR, ...args], {
    encoding: 'utf8',
    timeout: 15000,
  });
}

let input = '';
const stdinTimeout = setTimeout(() => process.exit(0), 3000);
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
  clearTimeout(stdinTimeout);
  try {
    // 1. Commit any local changes first — never lose out-of-band work
    git('add', '-A');
    const status = git('status', '--porcelain');
    const hasLocalChanges = status.stdout && status.stdout.trim();

    if (hasLocalChanges) {
      git('commit', '-m', 'backup: session start — sync out-of-band changes');
    }

    // 2. Fetch remote (don't merge/pull)
    const fetch = git('fetch', 'origin', 'main');
    if (fetch.status !== 0) {
      // Offline or fetch failed — just push local if we have changes
      if (hasLocalChanges) git('push', '-u', 'origin', 'HEAD');
      process.exit(0);
    }

    // 3. Check if remote is ahead
    const behind = git('rev-list', '--count', 'HEAD..origin/main');
    const behindCount = parseInt((behind.stdout || '').trim(), 10) || 0;

    // 4. Push local commits if any
    if (hasLocalChanges) {
      git('push', '-u', 'origin', 'HEAD');
    }

    // 5. If remote has changes, inform via stderr (shows in hook output)
    if (behindCount > 0) {
      const remoteLog = git('log', '--oneline', 'HEAD..origin/main');
      const changes = (remoteLog.stdout || '').trim();
      process.stderr.write(
        `\n⚠️  ~/.claude remote has ${behindCount} new commit(s):\n` +
        `${changes}\n\n` +
        `Run: git -C ~/.claude pull --rebase origin main\n` +
        `(Check for local changes first with: git -C ~/.claude status)\n\n`
      );
    }
  } catch (e) {
    // Silent fail — never block session start
  }
  process.exit(0);
});
