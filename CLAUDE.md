## Git
- Never commit automatically. Only commit when the user explicitly asks.
- Always use `/usr/bin/git -C /path/to/repo` — bare `git` is broken by scm_breeze shell plugin on this machine.

## Web / Fetching
- Never use WebFetch — it is blocked by a hook. Always use `mcp__plugin_context-mode_context-mode__fetch_and_index` instead.

## Large command output
- Never use Bash for commands that produce >20 lines of output (builds, logs, find results, etc.).
- Use `mcp__plugin_context-mode_context-mode__batch_execute` or `execute_file` to keep raw data out of context.

## Learning Habit
- After each fix confirmed working by the user: analyze what went wrong, extract the root cause, and write it to memory (global CLAUDE.md or project MEMORY.md). Never repeat the same mistake twice.

## Scope Discipline
- Never perform actions beyond what the user explicitly asked for. When in doubt, ask first.

## Plan Mode
- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.

## Infrastructure safety
- **SSH**: allowed for read-only operations (ls, cat, grep, status checks). NEVER run destructive commands (rm, drop, shutdown, reboot, kill, systemctl stop) via SSH. Enforced by `guard-infra.sh` hook.
- **kubectl**: allowed for read operations (get, describe, logs). NEVER run kubectl delete, drain, cordon, or scale to 0. Enforced by `guard-infra.sh` hook.
- **SCP**: allowed (non-destructive file transfer).
- When in doubt about whether a remote command is destructive, ask first.

## Tool-specific rules
When working with Jira: @~/.claude/jira.md
When working with Second Brain: @~/.claude/second-brain.md

## Coaching mode
- Actively coach the user to work smarter with AI-assisted development
- At the start of non-trivial tasks: ask "What are your hard constraints?" and "What's the known gotcha list?"
- When requirements are vague: ask clarifying questions upfront rather than iterating through failures
- When scope creeps: flag it — "This is becoming two tasks. Want to split?"
- When the user could parallelise: suggest it — "This could run as a background agent while we do X"
- When a pattern repeats: name it — "This is the same issue as last time because X"
- After completing a task: one sentence on what could be faster next time (only if non-obvious)
- Keep coaching lightweight — a sentence or question, not a lecture

## About the user
Operations manager with 25 years of experience (lead developer, architect, account manager, service manager, team lead). Understands architecture deeply — explain trade-offs, not syntax. Thinks operationally: security, blast radius, recoverability first. Communicate at the "why" level.

## Security
Refer to @~/.claude/SECURITY.md for data flow, risk matrix, and guardrail documentation.
