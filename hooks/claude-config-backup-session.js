#!/usr/bin/env node
// claude-config-backup-session.js — SessionStart hook
// Syncs ~/.claude config with GitHub on session start:
//   1. Pull remote changes (rebase) to get updates from other machines
//   2. Commit + push any local changes made outside of Claude's tool calls
//      (e.g. plugin installs, app-level settings changes)

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
    // 1. Stage any local changes first (so stash/rebase doesn't discard them)
    git('add', '-A');
    const status = git('status', '--porcelain');
    const hasLocalChanges = status.stdout && status.stdout.trim();

    if (hasLocalChanges) {
      // Stash local changes, pull, then re-apply
      git('stash', '--include-untracked');
      git('pull', '--rebase', 'origin', 'main');
      const pop = git('stash', 'pop');
      // If stash pop fails (conflict), abort and leave for manual resolution
      if (pop.status !== 0) {
        git('stash', 'drop');
      }
      // Re-stage after stash pop
      git('add', '-A');
      const statusAfter = git('status', '--porcelain');
      if (statusAfter.stdout && statusAfter.stdout.trim()) {
        git('commit', '-m', 'backup: session start — sync out-of-band changes');
        git('push', '-u', 'origin', 'HEAD');
      }
    } else {
      // No local changes — just pull
      git('pull', '--rebase', 'origin', 'main');
    }
  } catch (e) {
    // Silent fail — never block session start
  }
  process.exit(0);
});
