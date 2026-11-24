#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
Pure stdlib, deterministic, no network, no secrets, no input files.
"""

import os
import sys

# Final roast: same true story, tightened, with the punchline landing
# on the last three words. 139 chars, one line.
ROAST = (
    "My agent leaked its API key in the session log, rotated it, "
    "then leaked the new one in the log about the rotation \u2014 "
    "security by confession."
)


def main() -> int:
    text = ROAST
    # Gate self-check: 1-200 chars, not only whitespace, single line.
    if not (1 <= len(text) <= 200):
        print(f"gate failed: length {len(text)} not in 1..200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: blank text", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: not a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read and re-check what is on disk.
    with open(path, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    assert on_disk == text, "on-disk text differs from roast"
    assert 1 <= len(on_disk) <= 200 and on_disk.strip()
    print(f"wrote {len(on_disk)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
