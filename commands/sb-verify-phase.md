# Verify Phase — Cross-Environment Pipeline

Run the full verification pipeline for a completed phase.
Handles both direct host usage and cross-environment workflow (container→host handoff).

## Arguments
- $ARGUMENTS = phase number (e.g., "29")

## Environment Detection

First, detect where we are running:
- If `/workspace` exists and `UV_PROJECT_ENVIRONMENT` is set → we are in the **devcontainer**
- Otherwise → we are on the **host**

### If running in DEVCONTAINER:
1. Write the verification plan to `.planning/phases/<phase>/VERIFY-HOST.md` with:
   - Phase number and plan file references
   - Extracted `<verify>` blocks and `<done>` conditions from all plans
   - Any specific URLs, UI elements, or API endpoints to check
   - Specific test commands to run
2. Tell the user: "Verification plan written. Run `/sb-verify-phase <N>` on the HOST to execute it."
3. Do NOT attempt to build, restart, or test — that's the host's job.

### If running on HOST:
Execute the full pipeline below.

## Host Pipeline

### Step 1: Build & Deploy
1. Run `source "$HOME/.nvm/nvm.sh" 2>/dev/null; npm run build --prefix ~/second-brain/frontend`
2. Run `uv tool install ~/second-brain --reinstall`
3. Kill any running sb-api: `kill $(lsof -ti :37491) 2>/dev/null`
4. Start sb-api: `~/.local/bin/sb-api > /tmp/sb-api.log 2>&1 &`
5. Wait 3 seconds for startup
6. Verify sb-api is listening: `lsof -i :37491`

### Step 2: Run pytest
1. Run `uv run pytest tests/ -q` — full test suite must pass
2. Report any failures immediately

### Step 3: Read Phase Verification Steps
1. Check for `VERIFY-HOST.md` in the phase directory (written by container agent)
2. If not found, read all plan files matching the phase number
3. Extract `<verify>` blocks, `<done>` conditions, and checkpoint instructions

### Step 4: Execute Verification
1. Run any automated verification commands from the plans
2. For GUI verification: use Playwright to navigate to `http://localhost:37491/ui`
3. Verify UI elements described in the plans (tabs, buttons, panels, data)
4. Take screenshots of key UI states
5. Test API endpoints mentioned in plans with curl/fetch

### Step 5: Report
Present a clear summary:
```
## Phase N Verification Report

### Build & Deploy: PASS/FAIL
### Test Suite: PASS/FAIL (X passed, Y failed)
### Plan Verifications:
  - Plan N-01: PASS/FAIL — details
  - Plan N-02: PASS/FAIL — details
### Screenshots: [attached]
### Overall: VERIFIED / NEEDS FIXES
```

## Important
- Always use `source "$HOME/.nvm/nvm.sh"` before npm commands (nvm not auto-loaded)
- Use `/usr/bin/git -C` for git commands (scm_breeze workaround)
- GUI URL: `http://localhost:37491/ui` (NOT port 5001)
- Use Playwright for GUI verification — don't ask user to check manually
- If Playwright unavailable, fall back to API endpoint checks
