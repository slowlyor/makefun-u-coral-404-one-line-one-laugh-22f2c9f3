#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single original one-liner (<= 200 chars) to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked my smart speaker for motivation. "
    "It said, \"Have you considered being someone else?\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
