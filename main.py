#!/usr/bin/env python3
import os

ENTRY = "I asked the universe for a sign, and it sent me a CAPTCHA."

def check_entry(text):
    if not text or not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) < 1 or len(text) > 200:
        raise SystemExit("entry must be 1-200 characters")
    return text

def build_entry():
    parts = ["I asked the universe for a sign,",
             "and it sent me a CAPTCHA."]
    return " ".join(parts)

def output_path():
    return os.path.join("/output", "entry.txt")

def main():
    line = build_entry()
    check_entry(line)
    os.makedirs(os.path.dirname(output_path()), exist_ok=True)
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
