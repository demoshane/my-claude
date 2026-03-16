#!/usr/bin/env node
// claude-config-backup-session.js — SessionStart hook
// Commits and pushes any config changes that happened outside of Claude's
// tool calls (e.g. plugin installs, app-level settings changes).

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
    // Stage all tracked files (respects .gitignore)
    git('add', '-A');

    // Only commit if there are staged changes
    const status = git('status', '--porcelain');
    if (!status.stdout || !status.stdout.trim()) process.exit(0);

    git('commit', '-m', 'backup: session start — sync out-of-band changes');
    git('push', '-u', 'origin', 'HEAD');
  } catch (e) {
    // Silent fail — never block session start
  }
  process.exit(0);
});
