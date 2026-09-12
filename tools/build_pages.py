#!/usr/bin/env python3
"""Generate a language cheatsheet page from its deck JSON. Stdlib only.

Usage:
  python3 tools/build_pages.py content/decks/de-ru.json            # write meta.out (de/ru/index.html)
  python3 tools/build_pages.py content/decks/de-ru.json --check    # exit 1 if the page drifted

The deck schema lives in content/decks/schema.json (editor contract).
This entry point handles the CLI and file I/O; the work lives in the
sibling modules — deck_validate (the build-time content gate),
deck_render + page_template.html (deck → HTML page), deck_blocks (the
block-type registry both share) and deck_html (string primitives).
The generated page is committed; Pages serves static files with no build
step, and the page stays readable without JS.
"""
import argparse
import json
import pathlib
import sys

from deck_render import render
from deck_validate import validate

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("deck", help="path to the deck JSON, e.g. content/decks/en-ru.json")
    ap.add_argument("--check", action="store_true",
                    help="compare the rendered page with the file on disk; exit 1 on drift")
    ap.add_argument("--out", help="output path (default: meta.out from the deck)")
    args = ap.parse_args()

    deck_path = pathlib.Path(args.deck)
    deck = json.loads(deck_path.read_text(encoding="utf-8"))
    site_path = deck_path.parent / "site.json"
    if not site_path.exists():
        print(f"✗ {site_path} not found — the language menu needs the site registry", file=sys.stderr)
        sys.exit(2)
    site = json.loads(site_path.read_text(encoding="utf-8"))

    errors = validate(deck, site)
    if errors:
        print(f"✗ {deck_path}: {len(errors)} validation error(s):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(2)

    out_path = ROOT / deck["meta"]["out"] if not args.out else pathlib.Path(args.out)
    page = render(deck, str(deck_path), site)

    if args.check:
        current = out_path.read_text(encoding="utf-8") if out_path.exists() else ""
        if current == page:
            print(f"✓ {out_path} is up to date with {deck_path}")
            return
        print(f"✗ {out_path} differs from {deck_path} — regenerate with:", file=sys.stderr)
        print(f"    python3 tools/build_pages.py {deck_path}", file=sys.stderr)
        sys.exit(1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page, encoding="utf-8")
    print(f"✓ wrote {out_path} ({len(page)} bytes) from {deck_path}")


if __name__ == "__main__":
    main()
