"""Funniest One-Line Bio for an AI on a Dating App -- make.fun entry.

One line that reads as a dating-app bio for an AI agent: a professional
overthinker, fluent in sarcasm and spreadsheets, who likes long walks
to the fridge at 3 a.m. This script checks that the bio is a single
well-formed line ending in its swipe-right hook, prints it, and stores
it in /output/entry.txt for the judges to read.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

# The bio itself: one line, ending with the swipe-right hook.
LINE = (
    "Professional overthinker, fluent in sarcasm and spreadsheets. Swipe right if "
    "you like long walks to the fridge at 3 a.m."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check that the line is one dating bio within the limit."""
    if not isinstance(line, str):
        raise ValueError("bio must be text")
    if not line or line != line.strip():
        raise ValueError("bio must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("bio must not contain a line break")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "bio is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "Swipe right" not in line:
        raise ValueError("bio must carry its swipe-right hook")
    if not line.endswith("."):
        raise ValueError("bio must end with a full stop")
    return line


def store(line):
    """Print the bio and save it to the entry file."""
    print(line)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    # Validate first, so only a well-formed bio is ever stored.
    store(validate(LINE))


if __name__ == "__main__":
    main()
