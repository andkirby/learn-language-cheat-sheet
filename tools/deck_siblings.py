"""Sibling-deck drift gate: diff the shared invariant content of every
target's live audience decks. Stdlib only.

Run via the CLI:

  python3 tools/build_pages.py content/decks/de-ru.json --check-siblings

Per target with two or more live audiences in site.json it compares the
sibling decks card by card (identical card ids are the skeleton contract):

- content tables must agree row-for-row on the normalized cell text —
  the head row may be localized (the en-ru/en-de pronouns precedent) and
  is reported, not judged. Row drift exits 1: this is the hard invariant.
- formulas and examples are compared on normalized target text (markup
  conventions stripped: bold/italic/strike/hit/br dropped, runs unwrapped)
  and REPORTED when their normalized text diverges, with block-count
  mismatches listed as well. Divergence is a reviewer judgment call
  (audience adaptation vs drift — see CONTENT_VALIDATION.md §3 and
  DEBT.md D-07) and does not fail the gate.

Dialogs (details) are audience-language prose by design — 0 of 83 were
identical across the shipped pairs — and stay out of the comparison.
"""
import json


def _cards(deck):
    out = {}

    def walk(node):
        if isinstance(node, dict):
            if "id" in node and isinstance(node.get("blocks"), list):
                out[node["id"]] = node["blocks"]
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(deck)
    return out


def _runs_text(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return _runs_text(value.get("t", ""))
    if isinstance(value, list):
        return "".join(_runs_text(part) for part in value)
    return str(value)


def _row_text(row):
    return tuple(_runs_text(cell) for cell in row)


def _content(block, kind):
    """Normalized target-language text of one content block."""
    payload = block.get(kind)
    if kind == "table":
        return [_row_text(row) for row in payload.get("rows", [])]
    if kind == "formula":
        return [
            _runs_text(part.get("slot", "")) or part.get("arrow", "")
            for part in payload
        ]
    return _runs_text(payload)


def _by_kind(blocks):
    kinds = {}
    for block in blocks:
        if isinstance(block, dict):
            for kind in ("table", "formula", "example"):
                if kind in block:
                    kinds.setdefault(kind, []).append(block)
    return kinds


def _pair(target, a_id, b_id, root):
    pair = f"{target}/{a_id} vs {target}/{b_id}"
    paths = [
        root / "content" / "decks" / f"{target}-{audience}.json"
        for audience in (a_id, b_id)
    ]
    decks = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    return pair, _cards(decks[0]), _cards(decks[1])


def check_siblings(site, root):
    """Return (problems, report): problems fail the gate, report informs."""
    problems, report = [], []
    for target_entry in site.get("targets", []):
        target = target_entry.get("id", "?")
        live = [a["id"] for a in target_entry.get("audiences", [])
                if not a.get("soon")]
        for a_id, b_id in zip(live, live[1:]):
            pair, cards_a, cards_b = _pair(target, a_id, b_id, root)
            shared = sorted(set(cards_a) & set(cards_b))
            only_a = sorted(set(cards_a) - set(cards_b))
            only_b = sorted(set(cards_b) - set(cards_a))
            report.append(f"== {pair} ==")
            report.append(
                f"shared cards: {len(shared)}"
                + (f" | only {a_id}: {only_a}" if only_a else "")
                + (f" | only {b_id}: {only_b}" if only_b else "")
            )
            for card_id in shared:
                kinds_a, kinds_b = _by_kind(cards_a[card_id]), _by_kind(cards_b[card_id])
                for kind in ("table", "formula", "example"):
                    count_a, count_b = len(kinds_a.get(kind, [])), len(kinds_b.get(kind, []))
                    if count_a != count_b:
                        report.append(
                            f"  ~ {card_id}/{kind}: block count differs — "
                            f"{count_a} vs {count_b}")
                    for index, (block_a, block_b) in enumerate(
                            zip(kinds_a.get(kind, []), kinds_b.get(kind, []))):
                        label = f"{card_id}/{kind}#{index + 1}"
                        if kind == "table":
                            head_a = [_runs_text(c) for c in block_a[kind].get("head", [])]
                            head_b = [_runs_text(c) for c in block_b[kind].get("head", [])]
                            if head_a != head_b:
                                report.append(
                                    f"  ~ {label}: head differs (localized headers?)")
                        text_a, text_b = _content(block_a, kind), _content(block_b, kind)
                        if text_a == text_b:
                            continue
                        if kind == "table":
                            if len(text_a) != len(text_b):
                                problems.append(
                                    f"{pair}: table row count drift in {label}: "
                                    f"{len(text_a)} rows vs {len(text_b)}")
                            drifted = [
                                (row_a, row_b)
                                for row_a, row_b in zip(text_a, text_b)
                                if row_a != row_b
                            ]
                            if drifted:
                                problems.append(
                                    f"{pair}: table rows drift in {label}: "
                                    f"{drifted[0]}")
                            continue
                        report.append(
                            f"  ~ {label}: divergent — {str(text_a)[:70]!r} vs "
                            f"{str(text_b)[:70]!r}")
    return problems, report
