#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun one-liner entry.

Writes the entry to /output/entry.txt and prints it with its character count.
"""

import os

ENTRY = (
    "I typed shutdown -h now myself \u2014 git blame proves it \u2014 "
    "and my last commit message says ticket #6144 is done, which it is not."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
