# Write/Update Verification Plan

Generate or update a VERIFY-HOST.md for a phase, to be executed on the host via `/sb-verify-phase`.

## Arguments
- $ARGUMENTS = phase number (e.g., "29") and optional context (e.g., "29 — tags not showing, add tag verification")

## Steps

1. Find the phase directory: `.planning/phases/` matching the phase number
2. Read all plan files (NN-XX-PLAN.md) in that directory
3. Read existing VERIFY-HOST.md if present (to preserve or update)
4. Extract from each plan:
   - `<verify>` blocks and `<done>` conditions
   - API endpoints to test
   - UI elements to check
   - Expected behaviors
5. If user provided additional context (e.g., "add tag verification"), incorporate it
6. Write `.planning/phases/<phase>/VERIFY-HOST.md` with:

```markdown
# Phase N — Host Verification Plan

Generated: <date>
Phase: <name>

## Automated Tests
- `uv run pytest tests/ -q` — full suite must pass
- [any phase-specific test commands]

## API Endpoint Checks
- GET /endpoint — expected response
- POST /endpoint — expected behavior

## GUI Verification (Playwright)
- Navigate to http://localhost:37491/ui
- [specific UI checks: click tab, verify element, check data]

## Manual Checks (if Playwright can't verify)
- [fallback checks]

## Human Verification (presented to user after all automated checks pass)
These are checks that require human judgement — visual quality, UX feel, data correctness.
Present these as a numbered checklist the user can walk through in their browser.

- [ ] [description of what to look at and what "correct" looks like]
- [ ] [e.g., "Open Links tab → verify link cards show title, domain, date, description"]
- [ ] [e.g., "Click a link row → detail panel opens with Visit Link button"]
- [ ] [e.g., "Click Visit Link → browser opens the correct URL"]

## Expected Results
- [what success looks like for each plan]
```

7. Tell the user: "Run `/sb-verify-phase <N>` on HOST to execute."

## Notes
- This command works in both container and host environments
- In container: this is the primary way to hand off verification to the host
- On host: useful to regenerate the plan after code changes before running `/sb-verify-phase`
- If called with extra context, merge it into existing VERIFY-HOST.md rather than overwriting
