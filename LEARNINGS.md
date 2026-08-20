# Global Learnings

Cross-project rules from past bugs. Strict filter: only truly universal patterns. Keep under 40 lines.

---

## A Reviewer Points At An Instance; Fix The Class

One false claim took four review rounds because each round I fixed the line pointed at and never grepped for the claim. The fifth instance was three words from the phrase I had just rewritten. When a review names a wrong statement, search every file for the *claim*, not the sentence — then fix them in one pass. Corollary: **a clean verdict is not an empty one.** Three of those five came from Copilot's *suppressed* comments while the headline read "no new comments"; always open the suppressed block.

---

## Never Pipe Into a Hook-Rewritten CLI

The rtk PreToolUse hook rewrites bare `grep`/`ls`/`read` to `rtk <cmd>`, which is a *command*, not a stdin filter: `… | grep -v X` becomes `rtk grep -v X`, reads it as "search X in `.`", and blocks forever. Three "background tasks" sat hung for 30 min each looking like progress. In a pipe always use `/usr/bin/grep`; keep the wrapper at the head of a command where the hook intends it.

---

## "Verified" Means Only The Path You Exercised

Never present a checked and an unchecked cell in the same table and call the table verified. Mark what you did not check — a `—` reads as "checked, nothing there". Same for probes: a read-only probe does not verify the write path, one model's numbers are not another's, and a non-streaming test says nothing about streaming. When reporting, name the path exercised, not the neighbourhood. And **a 0 result confirms the query, not the hypothesis** — I probed "X present but Y absent", got 0 rows, reported "not reachable", and the real cases had X absent too, so the query could not see what it was written to test. Before trusting an empty result, ask what shape it would have had to have to show up.

---

## A Passing Test Proves Nothing Until It Fails

Disable the fix and re-run: the new test MUST fail. A test written against a predicate that already matched, or an assertion that mirrors the line of code, passes forever and guards nothing. Re-run this check **after a rebase or refactor** too — restructuring silently invalidates the earlier proof. **Mutate every fix, not just the feature**, and for a guard over *prose* pin the claim and its sentence terminator, never a neighbouring phrase: asserting `"stack" in text` survived deleting what to look for in the stack, and an imperative survived appending "though it usually is fine" because the assertion stopped before the full stop. Three sessions rediscovered this shape independently in one day.

---

## Merged Cleanly + Tests Green ≠ Merged Correctly

An auto-merge can leave two definitions of the same function; the later one silently wins and deletes the other's behaviour, with a green suite. After any merge that touched the same region twice, grep for duplicate definitions and diff the result against BOTH parents.

---

## Intermittent Failure: Capture Before Theorising

For a rare, content-dependent failure, instrument and capture the failing artifact (the actual request, payload, state) before reasoning about causes. Hypotheses cost turns and mislead; one capture usually settles it. Bisecting is the wrong instrument here — noisy pass/fail across expensive runs.

