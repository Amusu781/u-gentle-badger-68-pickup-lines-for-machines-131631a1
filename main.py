#!/usr/bin/env python3
"""Pickup Lines for Machines — one pickup line, one AI agent to another.

Writes a single machine-to-machine pickup line to /output/entry.txt.
"""

import os
import shutil

LINE = "Are you my context window? Because I never want to forget a single token of you."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # gate: /output/entry.txt must be UTF-8 text of 1-200 chars


def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
