"""The Robot Vacuum's Best Excuse — make.fun entry program.

Writes one line, at most 140 characters, in which a robot vacuum
explains why it missed a spot, to /output/entry.txt.

The line is a fixed, hand-written entry (not generated at run time):
a deadpan first-person excuse rooted in the vacuum's own world
(cliff sensors), with the punchline at the very end.
"""

import os
import sys

ENTRY = (
    "My cliff sensors saw the edge of the rug and decided "
    "my life was worth more than your crumbs."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    # Gate mirror: UTF-8 text, 1 to 140 characters, not only whitespace.
    if not (1 <= len(ENTRY) <= 140):
        print(f"entry length {len(ENTRY)} outside 1..140", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    ENTRY.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts characters, so write exactly
    # the line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and verify: the file on disk must be byte-identical
    # to the entry, so a partial write can never pass silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != ENTRY:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
