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
DEFAULT_TARGETS = [
    REPO / "src/main/resources/templates/index.html",
    REPO / "public/index.html",
]
PATTERN = re.compile(r'(<p class="lead">)(.*?)(</p>)', re.DOTALL)


def read_lead(path: Path) -> str | None:
    match = PATTERN.search(path.read_text(encoding="utf-8"))
    return match.group(2) if match else None


def pick(current: str) -> str:
    candidates = [lead for lead in LEADS if lead != current]
    return random.choice(candidates) if candidates else LEADS[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "targets",
        nargs="*",
        default=[str(target) for target in DEFAULT_TARGETS],
        help="index.html files to update",
    )
    parser.add_argument("--index", type=int, help="force a specific pool entry")
    parser.add_argument("--dry-run", action="store_true", help="do not write")
    args = parser.parse_args()

    paths = [Path(target) for target in args.targets]
    texts = {}
    current = None
    for path in paths:
        text = path.read_text(encoding="utf-8")
        match = PATTERN.search(text)
        if not match:
            print(f"error: <p class=\"lead\"> not found in {path}", file=sys.stderr)
            return 1
        if current is None:
            current = match.group(2)
        texts[path] = (text, match)

    lead = LEADS[args.index] if args.index is not None else pick(current)

    if lead == current:
        print("unchanged: selected lead already present")
        return 0

    for path, (text, match) in texts.items():
        if match.group(2) == lead:
            continue
        if not args.dry_run:
            path.write_text(
                text[: match.start(2)] + lead + text[match.end(2) :], encoding="utf-8"
            )
    print(f"lead replaced with: {lead[:80]}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
