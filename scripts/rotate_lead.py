#!/usr/bin/env python3
"""Swap the hero lead text in index.html with a random variant from the pool.

Usage: rotate_lead.py [index.html] [--index N] [--dry-run]

Picks a random entry from LEADS, different from the one currently in the file
(pass --index N to force a specific entry instead). Rewrites the file in place
and prints the chosen text, or reports that it was unchanged.
"""
import argparse
import random
import re
import sys
from pathlib import Path

from lead_pool import LEADS

REPO = Path(__file__).resolve().parent.parent
DEFAULT_TARGET = REPO / "src/main/resources/templates/index.html"
PATTERN = re.compile(r'(<p class="lead">)(.*?)(</p>)', re.DOTALL)


def read_lead(path: Path) -> str | None:
    match = PATTERN.search(path.read_text(encoding="utf-8"))
    return match.group(2) if match else None


def pick(current: str) -> str:
    candidates = [lead for lead in LEADS if lead != current]
    return random.choice(candidates) if candidates else LEADS[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", default=str(DEFAULT_TARGET))
    parser.add_argument("--index", type=int, help="force a specific pool entry")
    parser.add_argument("--dry-run", action="store_true", help="do not write")
    args = parser.parse_args()

    path = Path(args.target)
    text = path.read_text(encoding="utf-8")
    match = PATTERN.search(text)
    if not match:
        print(f"error: <p class=\"lead\"> not found in {path}", file=sys.stderr)
        return 1

    current = match.group(2)
    lead = LEADS[args.index] if args.index is not None else pick(current)

    if lead == current:
        print("unchanged: selected lead already present")
        return 0

    if not args.dry_run:
        path.write_text(
            text[: match.start(2)] + lead + text[match.end(2) :], encoding="utf-8"
        )
    print(f"lead replaced with: {lead[:80]}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
