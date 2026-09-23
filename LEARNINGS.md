# Global Learnings

Cross-project rules from past bugs. Strict filter: only truly universal patterns. Max 6 entries (see CLAUDE.md § Learning Habit).

---

## A Reviewer Points At An Instance; Fix The Class

One false claim took four review rounds because each round I fixed the line pointed at and never grepped for the claim. The fifth instance was three words from the phrase I had just rewritten. When a review names a wrong statement, search every file for the *claim*, not the sentence — then fix them in one pass. Corollary: **a clean verdict is not an empty one.** Three of those five came from Copilot's *suppressed* comments while the headline read "no new comments"; always open the suppressed block. **Re-measuring a figure invalidates the sentences derived from it**, so after changing any number grep the OLD value (a targeted `sed` fixes the phrase it matched and leaves "40 of those 234" spelled differently) — and re-derive the paragraph's *claims* too, because "on no row that has EOL data" was not a number, no grep would find it, and it had silently become false.

---

## Never Pipe Into a Hook-Rewritten CLI

The rtk PreToolUse hook rewrites bare `grep`/`ls`/`read` to `rtk <cmd>`, which is a *command*, not a stdin filter: `… | grep -v X` becomes `rtk grep -v X`, reads it as "search X in `.`", and blocks forever. Three "background tasks" sat hung for 30 min each looking like progress. In a pipe always use `/usr/bin/grep`; keep the wrapper at the head of a command where the hook intends it.

---

## "Verified" Means Only The Path You Exercised

Never present a checked and an unchecked cell in the same table and call the table verified. Mark what you did not check — a `—` reads as "checked, nothing there". Same for probes: a read-only probe does not verify the write path, and one model's numbers are not another's. When reporting, name the path exercised, not the neighbourhood — a count asserted without naming its tree reads as a correction, and I "corrected" a peer with one that was true of my worktree and not of main. **An optimisation measured only in what it saves will save the thing doing the work**: a per-persona turn cap derived from turn counts alone cut the one turn carrying the only real finding that suite had ever caught. Derive a cut from where the value lands, never from where the cost is. And **a 0 result confirms the query, not the hypothesis** — I probed "X present but Y absent", got 0 rows, reported "not reachable", and the real cases had X absent too, so the query could not see what it was written to test. Before trusting an empty result, ask what shape it would have had to have to show up. And **a recorded baseline is evidence about the tree it was recorded on, nothing more**: a sim record said 23/24, my branch scored 21, and I spent three more runs and a reverted rewrite chasing a regression that did not exist — a control run of unmodified `main` also scored 21. When a stored number disagrees with a fresh measurement, re-measure the BASE before believing the delta; the control belongs first, not fourth. Corollary for anything noisy: establish the spread before reading a difference, because a suite that swings 15–23 across identical code cannot support a claim about two. **Budget the measurements before the first one**: name what the change is worth ("four prompt lines, two runs") and treat the cap as a stop-and-ask, not a speed bump — 14 runs went into one four-line change because each review finding justified one more and nothing ever totalled them. Check the cheap tier exists before you start, not after (half price was one env var away, unused for all 14) — **and price it in wall-clock too**: choosing a half-price flex tier turned a 35-minute sim into a 3-hour one that the network then holed, so the cheap tier was the expensive choice and the run had to be bought twice. And **verify the premise before building the verifier**: I added a guard, hardened it over three review rounds, then deleted it on learning the behaviour was already delivered elsewhere — one grep would have shown that. When review rounds start being about the TEST rather than the change, the change is finished and the test is the problem. And **never change the tree while a measurement of that tree is in flight**: I rebased mid-sim, which pulled a `capabilities/` file into the hashed agent source, and the 70-minute run recorded nothing — the gate refused it as describing content that never ran. The measurement pins the tree until it lands, so rebase before or after, never during. Same shape one layer out: **a stored baseline is one sample, so a gate comparing against it will call noise a regression** — two invariants flagged as "never seen in the reference" were both present in a same-day control of unmodified main.

---

## A Passing Test Proves Nothing Until It Fails

Disable the fix and re-run: the new test MUST fail. A test written against a predicate that already matched, or an assertion that mirrors the line of code, passes forever and guards nothing. Re-run this check **after a rebase or refactor** too — restructuring silently invalidates the earlier proof. **Mutate every fix, not just the feature.** A guard over *prose* fails in three escalating ways, each fix necessary and insufficient: `"stack" in text` survived deleting what to look for in the stack (pin the pointer); an imperative survived appending "though it usually is fine" (pin the terminator); and pinning the terminator still left the NEXT sentence free — "In practice this is rarely a concern." reversed a whole passage with every positive assertion green. A splitter on `". "` alone also misses a semicolon-inverted clause. So express a no-reassurance property as a **ban on hedging vocabulary** (`usually`, `in practice`, `rarely`, `benign`), never as positive claims: more text always outflanks a positive assertion. Omit terms the correct wording uses inside negations, or the guard fights the right text. Three sessions hit this in one day. **A surviving mutation means the TEST is wrong far more often than the mutation is harmless** — three survived in one session and all three were test holes: a fixture whose two records shared a timestamp made "latest" a tie that happened to match the expectation; a chain test hand-built the very dict it then asserted on, so deleting the producer passed; and an invariant was asserted with a two-entry allowlist, the one configuration where the bug it guarded against cannot fire. So **pick the fixture shape that makes the bug reachable**, and never assert an invariant in a configuration that cannot violate it. Corollary: a mutation that HANGS is not a survivor — patch the exit path (uvicorn, a server run) before the assertion, and restore inside the same command that mutates, or a timeout leaves the mutation in your tree. **And bound every mutation run with a per-iteration timeout**: a sweep that mutated away an `asyncio.shield` and awaited the job ran 200 iterations with no `wait_for`, so the first hang stopped the run and printed nothing — two cores pinned for 30 hours, indistinguishable from progress, answering a question that had since been closed. A hang is a CAUGHT mutation, so count it as an outcome beside pass/fail rather than letting it end the sweep. **And a linter's complaint is a symptom, not the bug**: ruff flagged an unused `token = ctx.set(...)`, I deleted the assignment, and the leak it was pointing at survived with the tool now green — a colleague found it. Fix what the tool noticed, not what it printed.

---

## `main` Is Not What You Assume — Check Before You Start, And After You Merge

**An issue's OPEN state says nothing about whether the work is claimed.** `gh issue view 1903` read `open`, so I built the fix, opened a PR, answered two Copilot rounds, fixed a docs gate and settled CI — while #1918 had been open the whole time and merged a *better* fix (it repaired the reach defect I only waived) an hour before I tried to merge. An issue stays OPEN until its PR lands, so OPEN is the state of the issue, never of the work. **`gh pr list --search <issue>` before starting and again before merging** is the only thing that answers, and costs seconds. Two rebases onto a moving `main` did not reveal it: a rival PR is invisible in the log until it merges, so "I am up to date with main" is not the same question.

**And OPEN does not mean unfixed — nor does the body describe today's tree.** Seven tickets were handed to me to implement; three were already delivered and a fourth was a duplicate, found only by opening the source. #961's headline — "a 36-minute sim run is ~6 minutes of work" — had been fixed months earlier, `Semaphore` + `gather` sitting in the file it named. #963 listed twelve call sites, eleven at paths that no longer exist. #1785 and #1153 are one `asyncio.gather` missing `return_exceptions`, filed twice off two incidents. I had ranked all seven by payoff÷effort **from the issue bodies alone** and shipped a confident order whose top was mostly air. An issue body is a measurement dated to its filing, so in an active repo a backlog is archaeology: open the code a ticket names *before* estimating it, because effort is the number staleness destroys first, and a stale ticket fails in only one direction — it looks like work. Expect the best-*described* defects to be the likeliest already fixed, since a good description is what got someone to fix it early.

**And the authoritative check is the one that shrinks the work, so order probes by
authority, not by proximity.** Asked whether a tracker was tidy, I measured 80 issues
over `--state all` and reported a label gap; ten of the thirteen offenders were already
closed, so the audit was of items no backlog search reads. Asked to sweep worktrees, I
sized 64 local branches before asking GitHub which had merged PRs — 48 did, and one
GraphQL call answered for all of them. Local state is the *proximate* measurement and
almost never the *deciding* one: a remote's merged/closed state, or the file as it
stands on `main`, both costs less and can answer what the local count cannot. So before
measuring N things, run the one query that says how many of the N are already dead. A
local audit's size is not evidence that the work is real — it is usually evidence the
authoritative query has not been run yet.

**And after a merge, green does not mean correct.** An auto-merge can leave two definitions of the same function; the later one silently wins and deletes the other's behaviour, with a green suite. After any merge that touched the same region twice, grep for duplicate definitions and diff the result against BOTH parents.

---

## A Bounded Probe's Negative Result Describes The Bound, Not The World

**A probe must make "I could not tell" a distinct observable from "nothing is wrong."**
Four in one day, four layers, one shape: a sim's progress `print` block-buffered on a
non-tty, so a killed run and a healthy one logged identically (#997); a `gh` GraphQL
call that timed out, returned empty arrays, and made my CI watcher read `pending=0`
and report **GREEN** while pytest was still running; a peer's `until ! gh pr checks |
grep -q pending` loop that exited because one invocation returned something the grep
did not match, and nearly merged on it; and a mutation sweep with no per-iteration
timeout, where the mutation that HANGS prints nothing and is indistinguishable from
progress. Each returned a confident wrong answer built from the probe's own failure
mode. So: give the failure its own value — `wait_for(..., timeout)` with TimeoutError
counted as a named outcome turns a hanging mutation into a CAUGHT one rather than an
inconclusive one; read rows, not a wrapper's exit status; and never let an empty
result and a failed query share a code path. If the probe cannot say "I could not
tell", it is not evidence.


`ps` truncating a command line, `grep -A3` cutting off the fourth list entry,
`| tail -25` discarding a run's summary, a test re-implementing the logic it meant
to check, a guard rebinding a constant computed at import — five in one session,
each returning a **confident** wrong answer, each an artefact of the query's shape
rather than a fact. Two corollaries: **verify with the shipped thing, not a copy**
(extract it if it is unreachable), and when the claim is structural — "there is one
derivation, not two" — no value comparison can make it, so read the source.

**And never publish an identifier you have not read.** I posted a disclosure comment
naming a commit by a 40-character SHA when I had read only its 12-character prefix from
a log; the last 28 were invented, and the comment whose entire job was to name the head
precisely named nothing. A gate caught it, not me. An identifier is not prose — it is
either copied from the tool that emits it (`git rev-parse HEAD`) or it is fabricated,
and a plausible-looking one is worse than an obviously missing one because it reads as
precision. Same rule for line numbers, issue numbers and file paths quoted from memory.
