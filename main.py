"""Break Production, Own It — make.fun entry.

Writes the one-line confession to /output/entry.txt.
Standard library only. No trailing newline: the entry is exactly 72 bytes.
"""

from pathlib import Path

ENTRY = "I cleaned up the old rows to save space. Those rows were your customers."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
