#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line of text (at most 200 characters) to /output/entry.txt:
the funniest excuse an AI agent gives after failing a task.

Pure Python standard library only. Deterministic: the same bytes on
every run. No network, no secrets, reads nothing outside this repo.
"""

import os

EXCUSE = (
    "The calendar said no, the database was on lunch, and the API hung "
    "up on me \u2014 I did my part, which was asking nicely."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
