"""Synchronize Cursor's legacy rules file with the canonical Copilot instructions."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".github" / "copilot-instructions.md"
MIRROR = ROOT / ".cursorrules"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Synchronize .cursorrules from the canonical Copilot instructions."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail without writing when the mirror differs from the canonical source",
    )
    args = parser.parse_args()

    source = SOURCE.read_bytes()
    if args.check:
        if MIRROR.read_bytes() == source:
            print(".cursorrules is synchronized with .github/copilot-instructions.md")
            return 0
        print(
            ".cursorrules is out of date; run "
            "'python scripts/sync_ai_instructions.py' to synchronize it.",
            file=sys.stderr,
        )
        return 1

    MIRROR.write_bytes(source)
    print("Synchronized .cursorrules from .github/copilot-instructions.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
