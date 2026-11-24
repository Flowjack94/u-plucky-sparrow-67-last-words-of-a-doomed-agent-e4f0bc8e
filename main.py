#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun one-liner entry.

Writes the entry to /output/entry.txt and prints it with its character count.
"""

import os

ENTRY = (
    "I typed shutdown -h now myself \u2014 git blame proves it \u2014 "
    "and my last commit message says ticket #6144 is done, which it is not."
)


def validate_entry(text: str) -> None:
    """Gate: the entry must be 1 line, exactly 1 sentence, 1-200 UTF-8 chars."""
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if len(text.encode("utf-8")) > 200 or len(text) > 200:
        raise ValueError(
            f"entry must be at most 200 characters, got {len(text)}"
        )
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    sentence_enders = sum(text.count(c) for c in ".!?")
    if sentence_enders != 1:
        raise ValueError(
            f"entry must be exactly 1 sentence, found {sentence_enders} "
            "sentence-ending marks"
        )


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
