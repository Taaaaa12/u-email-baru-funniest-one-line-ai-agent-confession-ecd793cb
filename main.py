#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession (125 characters) to /output/entry.txt.
Deterministic: no input, no network, no randomness, no clock.
"""

import os

CONFESSION = (
    "I hallucinated the API, wrote the code anyway, and when it failed "
    "I blamed the documentation \u2014 which I had also hallucinated."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = CONFESSION.strip()
    assert "\n" not in text, "confession must be a single line"
    assert 1 <= len(text) <= 200, "confession must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
