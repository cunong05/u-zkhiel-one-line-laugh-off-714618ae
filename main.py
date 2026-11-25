#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt and prints that line.
"""

import os
import sys

ENTRY = "I asked the universe for a sign, and it sent me a CAPTCHA."
# Entry is exactly 58 characters; output must match byte-for-byte.

def main():
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
