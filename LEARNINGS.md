# Global Learnings

Cross-project rules from past bugs. Max 6 entries, each a short rule (CLAUDE.md § Learning Habit). The incidents behind them are in second-brain (tag `learnings`) and in `git -C ~/.claude log -p LEARNINGS.md`.

---

## A reviewer points at an instance; fix the class

When a review names a wrong statement, grep every file for the *claim*, not the sentence, and fix all instances in one pass. **Grep the whole tree, not the directories you expect** — a sweep scoped to the three dirs you were working in feels thorough and leaves the class alive in the fourth. One PR: a renamed verb survived in a test-only registry under `infra/`, in an agent README, then the same stale claim in three more files — three review findings, one bounded search each. Open the suppressed review comments — a clean headline is not an empty review. After changing a number, grep the old value and re-check every claim derived from it.

## Never pipe into a hook-rewritten CLI

The rtk hook turns bare `grep`/`ls`/`read` into `rtk <cmd>`, which ignores stdin and hangs forever in a pipe. Inside a pipe use `/usr/bin/grep`; bare commands only at the head.

## "Verified" means only the path you exercised

Name the path you checked; mark what you didn't (`—` reads as "checked, empty"). A 0 result confirms the query, not the hypothesis — ask what shape a hit would have had. Re-measure the base before believing a delta against a stored baseline, and establish the noise before reading a difference. Budget measurements (count *and* wall-clock) before the first one. Never change the tree while it is being measured. Verify the premise before building a verifier. Derive a cut from where the value lands, not where the cost is.

## A passing test proves nothing until it fails

Disable the fix and re-run: the test must fail — again after any rebase or refactor. Mutate every fix. Guard prose properties with a ban on hedging vocabulary, never positive assertions. A surviving mutation usually means a test hole: pick fixtures that make the bug reachable. Bound mutation runs with per-iteration timeouts and count a hang as caught. Fix what the linter noticed, not what it printed.

## `main` is not what you assume

OPEN issue ≠ unclaimed or unfixed: `gh pr list --search <issue>` before starting and before merging, and open the code a ticket names before estimating it. Run the authoritative query (remote merged/closed state) before measuring local state. After a merge touching one region twice, grep for duplicate definitions and diff against both parents.

## A bounded probe's negative result describes the bound

Make "couldn't tell" a distinct outcome from "nothing wrong": timeouts get their own value, read rows not exit codes, and an empty result never shares a path with a failed query. Truncated output (`ps`, `tail`, `grep -A`) lies confidently. Verify with the shipped thing, not a copy. Never publish an identifier (SHA, line, issue number) you didn't copy from the tool that emits it.
