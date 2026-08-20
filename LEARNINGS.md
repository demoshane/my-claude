# Global Learnings

Cross-project rules from past bugs. Strict filter: only truly universal patterns. Keep under 40 lines.

---

## A Reviewer Points At An Instance; Fix The Class

One false claim took four review rounds because each round I fixed the line pointed at and never grepped for the claim. The fifth instance was three words from the phrase I had just rewritten. When a review names a wrong statement, search every file for the *claim*, not the sentence — then fix them in one pass. Corollary: **a clean verdict is not an empty one.** Three of those five came from Copilot's *suppressed* comments while the headline read "no new comments"; always open the suppressed block. **Re-measuring a figure invalidates the sentences derived from it**, so after changing any number grep the OLD value (a targeted `sed` fixes the phrase it matched and leaves "40 of those 234" spelled differently) — and re-derive the paragraph's *claims* too, because "on no row that has EOL data" was not a number, no grep would find it, and it had silently become false.

---

## Never Pipe Into a Hook-Rewritten CLI

The rtk PreToolUse hook rewrites bare `grep`/`ls`/`read` to `rtk <cmd>`, which is a *command*, not a stdin filter: `… | grep -v X` becomes `rtk grep -v X`, reads it as "search X in `.`", and blocks forever. Three "background tasks" sat hung for 30 min each looking like progress. In a pipe always use `/usr/bin/grep`; keep the wrapper at the head of a command where the hook intends it.

---

## "Verified" Means Only The Path You Exercised

Never present a checked and an unchecked cell in the same table and call the table verified. Mark what you did not check — a `—` reads as "checked, nothing there". Same for probes: a read-only probe does not verify the write path, one model's numbers are not another's, and a non-streaming test says nothing about streaming. When reporting, name the path exercised, not the neighbourhood. And **a 0 result confirms the query, not the hypothesis** — I probed "X present but Y absent", got 0 rows, reported "not reachable", and the real cases had X absent too, so the query could not see what it was written to test. Before trusting an empty result, ask what shape it would have had to have to show up.

---

## A Passing Test Proves Nothing Until It Fails

Disable the fix and re-run: the new test MUST fail. A test written against a predicate that already matched, or an assertion that mirrors the line of code, passes forever and guards nothing. Re-run this check **after a rebase or refactor** too — restructuring silently invalidates the earlier proof. **Mutate every fix, not just the feature.** A guard over *prose* fails in three escalating ways, each fix necessary and insufficient: `"stack" in text` survived deleting what to look for in the stack (pin the pointer); an imperative survived appending "though it usually is fine" (pin the terminator); and pinning the terminator still left the NEXT sentence free — "In practice this is rarely a concern." reversed a whole passage with every positive assertion green. A splitter on `". "` alone also misses a semicolon-inverted clause. So express a no-reassurance property as a **ban on hedging vocabulary** (`usually`, `in practice`, `rarely`, `benign`), never as positive claims: more text always outflanks a positive assertion. Omit terms the correct wording uses inside negations, or the guard fights the right text. Three sessions hit this in one day.

---

## Merged Cleanly + Tests Green ≠ Merged Correctly

An auto-merge can leave two definitions of the same function; the later one silently wins and deletes the other's behaviour, with a green suite. After any merge that touched the same region twice, grep for duplicate definitions and diff the result against BOTH parents.

---

## A Bounded Probe's Negative Result Describes The Bound, Not The World

`ps` truncating a command line, `grep -A3` cutting off the fourth list entry,
`| tail -25` discarding a run's summary, a test re-implementing the logic it meant
to check, a guard rebinding a constant computed at import — five in one session,
each returning a **confident** wrong answer, each an artefact of the query's shape
rather than a fact. Two corollaries: **verify with the shipped thing, not a copy**
(extract it if it is unreachable), and when the claim is structural — "there is one
derivation, not two" — no value comparison can make it, so read the source.
