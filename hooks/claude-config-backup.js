#!/usr/bin/env node
// claude-config-backup.js — PostToolUse hook
// Auto-commits and pushes ~/.claude config files to git when they change.
// Pulls with rebase before pushing to stay in sync across multiple machines.
//
// Watched: CLAUDE.md, *.md, settings.json, hooks/*.js, package.json, .gitignore
// Ignored: runtime dirs (projects/, sessions/, plans/, etc.)

const { spawnSync } = require('child_process');
const path = require('path');

const CLAUDE_DIR = '/Users/tuomasleppanen/.claude';
const GIT = '/usr/bin/git';

// Patterns of files worth backing up (relative to CLAUDE_DIR)
const TRACKED_PATTERNS = [
  /^CLAUDE\.md$/,
  /^[^/]+\.md$/,
  /^settings\.json$/,
  /^package\.json$/,
  /^\.gitignore$/,
  /^hooks\/[^/]+\.js$/,
];

function isTracked(filePath) {
  if (!filePath || !filePath.startsWith(CLAUDE_DIR + '/')) return false;
  const rel = filePath.slice(CLAUDE_DIR.length + 1);
  return TRACKED_PATTERNS.some(pattern => pattern.test(rel));
}

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
    const data = JSON.parse(input);
    const toolName = data.tool_name || data.tool || '';
    const toolInput = data.tool_input || data.input || {};

    if (!['Write', 'Edit', 'MultiEdit'].includes(toolName)) process.exit(0);

    const filePaths = toolName === 'MultiEdit'
      ? (toolInput.edits || []).map(e => e.file_path).filter(Boolean)
      : [toolInput.file_path].filter(Boolean);

    const trackedFiles = filePaths.filter(isTracked);
    if (trackedFiles.length === 0) process.exit(0);

    for (const f of trackedFiles) {
      git('add', f);
    }

    const status = git('status', '--porcelain');
    if (!status.stdout || !status.stdout.trim()) process.exit(0);

    const names = trackedFiles.map(f => path.relative(CLAUDE_DIR, f)).join(', ');
    git('commit', '-m', `backup: update ${names}`);

    // Pull with rebase before pushing to stay in sync with other machines
    git('pull', '--rebase', 'origin', 'main');
    git('push', '-u', 'origin', 'HEAD');

  } catch (e) {
    // Silent fail — never block tool execution
  }
  process.exit(0);
});
