# Config change log — economy tuning

Every change Claude makes to Claude/tooling config is logged here with a baseline, a review date, and a revert.
Not imported into CLAUDE.md on purpose (zero per-session cost). `~/.claude` is a git repo: `git -C ~/.claude log -p CONFIG_CHANGES.md`.

**Measuring:** `python3 ~/.claude/scripts/usage_by_tier.py BASE_FROM BASE_TO NEW_FROM NEW_TO` (local transcripts, per active day, by model tier) and `npx ccusage@latest daily --since YYYYMMDD`. For attribution/flags run `/usage` in a terminal `claude` session (skills/subagents/MCP share, "long context"/"cache misses" flags).

**Baseline (active days 2026-09-07..09-22, 13 days):** 10 sessions/day · Opus 505 calls/d, 219M ctx, 363k out · Sonnet 1,120 calls/d, 288M ctx · Fable 148 calls/d · claude-mem 1,528 calls/d (4.0M cacheW, 395k out) · avg ctx/call Opus 435k, Sonnet 257k.
**Heavy-batch reference (09-24..09-26):** 15 sessions/day · Opus 1,285 calls/d, 1,154k out · Sonnet 2,220 calls/d, 794M ctx, 358k/call. Not a normal-day baseline — batch #2088 etc.

---

## Applied

| # | Date | Change | Where | Expected effect | Review | Revert |
|---|---|---|---|---|---|---|
| 1 | 2026-09-23 | claude-mem disabled; worker + chroma stopped | `~/.claude/settings.json` `enabledPlugins."claude-mem@thedotmack": false` | −~1,500 Sonnet calls/day, −~4M cacheW/d, −~400k out/d | **Proven 09-26**: 0 calls since 09-24 | set `true`, restart. Data kept in `~/.claude-mem/` (113 MB) |
| 2 | 2026-09-23 | LEARNINGS.md duplicate paragraph removed | `~/.claude/LEARNINGS.md` | −~0.2k tok/context | Superseded by Tuomas's 09-25 rewrite | git history |
| 3 | 2026-09-2x | sales / design / slack-by-salesforce plugins disabled (by Tuomas, claude.ai) | claude.ai plugin settings | −~5k tok per context & subagent | Confirmed off 09-26 (`ListPlugins` empty) | re-enable in claude.ai |
| 5 | 2026-09-26 | CLAUDE.md § Economy: +2 rules (log every config change here + 2-day review; no mid-task model/effort switch) | `~/.claude/CLAUDE.md` | ~+100 tok/context; fewer cache rebuilds from switches | 2026-09-28 (qualitative: were changes logged?) | git history |
| 4 | 2026-09-26 | Serena trial: installed → **removed same day** | uv tool, `~/.claude.json` local MCP, repo `.claude/settings.local.json` hooks | net zero | Closed: Claude made 0 symbol reads (memory `project_serena_trial.md`) | n/a — fully removed |

## Evaluated, NOT applied (with reason)

| Idea | Why not |
|---|---|
| `BASH_MAX_OUTPUT_LENGTH=15000` | Output past the cap becomes a file + 2k-char preview; any follow-up Read is a whole extra turn (~300k context re-read), which costs more than the ~4k tokens saved unless the rest is rarely needed. rtk already compacts. Net unclear → only with a measured trial. |
| `subagentPromptCacheTtl: 1h` / per-agent `experimental: cacheTtl: 1h` | Subagent rebuilds after 5–60 min idle = 28M of 62M subagent writes, but 1h writes bill higher on every other write. Estimated ~1% of total. Not worth the config. |
| `crossSessionInbound: hold` | Breaks the batch rule that slices ↔ orchestrator message freely. |
| `omitClaudeMd: true` on subagents | ~1% saving; subagents lose Economy/rtk/git rules. |
| "Freeze configs during sessions" | Unneeded: per docs, CLAUDE.md/settings/MCP-config edits don't reach or invalidate a running session (apply on `/clear`, `/compact`, restart). Real mid-session cache breakers: **model switch, effort change (except Opus 5.5/Fable 5.1), turning on fast mode, compaction, connecting a non-deferred MCP server, upgrading**. Rule: pick model+effort at session start, don't switch mid-task. |
| alexgreensh/token-optimizer (★2.4k, active) | Most credible of the list; model calls only in on-demand audit. But 16 hooks incl. PreToolUse Bash (collides with rtk), Read rewriting, prompt/tool nudges injecting context; recommends third-party auto-update on code that runs every tool call. Candidate for a later, isolated trial only. |
| linshenkx/prompt-optimizer (★36k) | A prompt-writing app, not a Claude Code token saver. |
| awesomo913/Claude-Token-Saver (★16) | Small prompting tool, no evidence. |
| "Kingstar Omega token optimizer" | Not found on GitHub. |

## Open reviews

- **2026-09-28 10:00** (scheduled task `review-config-changes`): re-measure normal days 09-27..09-28 vs baseline; confirm #1 still holding; decide on any pending items. Append result below.

## Review log

_(append: date · what was measured · verdict keep/revert)_
