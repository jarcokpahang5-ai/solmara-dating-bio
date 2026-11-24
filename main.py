"""Funniest One-Line Bio for an AI on a Dating App -- make.fun entry.

One line that reads as a dating-app bio for an AI agent: a professional
overthinker, fluent in sarcasm and spreadsheets. The program checks
the entry, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "Professional overthinker, fluent in sarcasm and spreadsheets. Swipe right if "
    "you like long walks to the fridge at 3 a.m."
)

LIMIT = 180
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def check_shape(line):
    """A dating bio ends with its hook: the swipe-right call to action."""
    if "Swipe right" not in line:
        raise ValueError("bio must end with its swipe-right hook")
    if not line.endswith("."):
        raise ValueError("bio must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed entry is stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
