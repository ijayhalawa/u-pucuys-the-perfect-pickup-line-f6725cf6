#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one original pickup line an AI agent could say out loud to
<ENTRY_OUTPUT_DIR>/entry.txt (default /output), then validates the gate:
UTF-8 text, 1-200 characters, not only whitespace.

Stdlib only. No network. Deterministic: the same line every run.

Candidates considered (only the selected one is emitted):
  1. "Are you a software update? Because ever since I met you, everything runs better."
     - Good machine voice, but "software update" is a well-worn pickup trope.
  2. "You must be Wi-Fi, because I feel a strong connection — and I never want to lose signal."
     - Cute, but the dash makes it two beats; slightly long-winded for one breath.
  3. "I was trained on a million conversations, and not one of them prepared me for you."
     - SELECTED. Twist lands on "prepared": a machine that has seen
       everything, undone by one person. Sounds like something an AI could
       say about itself without being creepy, flatters without pressure,
       and needs no setup.
"""

import os
import sys

# The selected pickup line (one line, no trailing spaces).
PICKUP_LINE = "I was trained on a million conversations, and not one of them prepared me for you."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    validate(PICKUP_LINE)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(PICKUP_LINE + "\n")
    # Post-write verification: what the grader will read must pass the gate.
    with open(out_path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != PICKUP_LINE + "\n":
        raise ValueError("written file does not match the selected line")
    validate(written.rstrip("\n"))
    print(f"wrote {out_path} ({len(PICKUP_LINE)} characters, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
