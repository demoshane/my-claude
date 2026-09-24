#!/usr/bin/env python3
"""PreToolUse Bash hook: rtk rewrite + pipefail, as ONE hook.

Two hooks that both return updatedInput race, so this wraps `rtk hook claude`
and layers pipefail on its result.

Why pipefail: `cmd | tail -N` reports tail's exit code, so a failing cmd reads
as success (and `cmd | tail && echo OK` prints OK). Transcript audit 2026-09-23
found this 6x across sessions. pipefail keeps the bounded output AND the
failure.

Skipped when the pipeline closes early (`| head`, `grep -q/-m`): the upstream
command then dies of SIGPIPE (141) and pipefail would report a false failure.
"""
import json
import re
import subprocess
import sys

PIPE = re.compile(r"(?<!\|)\|(?![|&])")
EARLY_CLOSE = re.compile(r"\|\s*head\b|\bgrep\s+(-\w*[qm]|--quiet|--max-count)")


def main() -> None:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except ValueError:
        return
    original = (payload.get("tool_input") or {}).get("command")
    if not isinstance(original, str):
        return

    out = None
    try:
        res = subprocess.run(["rtk", "hook", "claude"], input=raw, capture_output=True,
                             text=True, timeout=5)
        if res.returncode == 0 and res.stdout.strip():
            out = json.loads(res.stdout)
    except (OSError, subprocess.SubprocessError, ValueError):
        out = None  # rtk unavailable: fall back to pipefail only

    hso = (out or {}).get("hookSpecificOutput") or {}
    cmd = (hso.get("updatedInput") or {}).get("command", original)

    if PIPE.search(cmd) and not EARLY_CLOSE.search(cmd) and "pipefail" not in cmd:
        cmd = "set -o pipefail; " + cmd

    if cmd == original and out is None:
        return  # nothing changed: stay silent, zero tokens

    if out is None:
        out = {"hookSpecificOutput": {"hookEventName": "PreToolUse"}}
        hso = out["hookSpecificOutput"]
    updated = dict(payload.get("tool_input") or {})
    updated.update(hso.get("updatedInput") or {})
    updated["command"] = cmd
    hso["updatedInput"] = updated
    out["hookSpecificOutput"] = hso
    print(json.dumps(out))


if __name__ == "__main__":
    main()
