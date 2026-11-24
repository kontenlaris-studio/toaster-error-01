#!/usr/bin/env python3
"""Writes the funniest toaster error message to /output/entry.txt."""
import os

ENTRY = "ERROR E-01: Toaster is burnt out. Not the bread. Me. I need a week off and a therapist."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
