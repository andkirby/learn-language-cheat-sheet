"""The deck block registry — the single source of block-type knowledge.

Each BlockDef entry owns three concerns for one block type (h, p, tiny,
example, notice, formula, table, chips, detail):
  check — shape validation (called with the deck validator's checker)
  text  — the learner-visible words (feeds the search-index gate)
  html  — the card markup
Adding or changing a block type means adding or changing one entry here,
not scattered edits. Validation (deck_validate) and rendering
(deck_render) both dispatch through this registry.
"""
from collections import namedtuple

from deck_html import esc, escq, runs_html, runs_or_string_html

BlockDef = namedtuple("BlockDef", "check text html")


def runs_text(runs):
    return " ".join(r.get("t", "") if isinstance(r, dict) else r for r in runs)


def _runs_def(key, tag, cls=None):
    """h/p/tiny/example: a plain runs payload wrapped in one element."""
    def check(block, where, chk):
        chk.check_runs(block[key], f"{where}.{key}")

    def text(block):
        return [runs_text(block[key])]

    def html(block):
        c = f' class="{cls}"' if cls else ""
        return f"        <{tag}{c}>{runs_html(block[key])}</{tag}>\n"

    return BlockDef(check, text, html)


def _notice_check(block, where, chk):
    chk.check_runs(block["notice"], f"{where}.notice")


def _notice_text(block):
    return [runs_text(block["notice"])]


def _notice_html(block):
    cls = "notice warning" if block.get("warning") else "notice"
    return f"        <div class=\"{cls}\">{runs_html(block['notice'])}</div>\n"


def _example_check(block, where, chk):
    chk.check_runs(block["example"], f"{where}.example")
    if "gloss" in block:
        chk.check_runs(block["gloss"], f"{where}.gloss")


def _example_text(block):
    parts = [runs_text(block["example"])]
    if "gloss" in block:
        parts.append(runs_text(block["gloss"]))
    return parts


def _example_html(block):
    if "gloss" not in block:
        return f"        <div class=\"example\">{runs_html(block['example'])}</div>\n"
    return ("        <div class=\"example pair\">\n"
            f"          <div class=\"pair-src\">{runs_html(block['example'])}</div>\n"
            f"          <div class=\"pair-gloss\">{runs_html(block['gloss'])}</div>\n"
            "        </div>\n")


def _formula_check(block, where, chk):
    items = block["formula"]
    if not isinstance(items, list) or not items:
        chk.errors.append(f"{where}.formula must be a non-empty list")
        return
    for j, item in enumerate(items):
        if "arrow" in item:
            continue
        if "slot" not in item:
            chk.errors.append(f"{where}.formula[{j}]: needs 'slot' or 'arrow'")
        elif isinstance(item["slot"], list):
            chk.check_runs(item["slot"], f"{where}.formula[{j}].slot")


def _formula_text(block):
    parts = []
    for item in block["formula"]:
        parts.append(item["arrow"] if "arrow" in item
                     else (item["slot"] if isinstance(item["slot"], str)
                           else runs_text(item["slot"])))
    return parts


def _formula_html(block):
    parts = []
    for item in block["formula"]:
        if "arrow" in item:
            parts.append(f"<span class=\"arrow\">{esc(item['arrow'])}</span>")
        else:
            role = item.get("role")
            cls = f"slot {role}" if role else "slot"
            parts.append(f"<span class=\"{cls}\">{runs_or_string_html(item['slot'])}</span>")
    return "        <div class=\"formula\">" + "".join(parts) + "</div>\n"


def _table_check(block, where, chk):
    tab = block["table"]
    head = tab.get("head", [])
    for ri, row in enumerate(tab.get("rows", [])):
        if len(row) != len(head):
            chk.errors.append(f"{where}.table row {ri} has {len(row)} cells, head has {len(head)}")
        for cell in row:
            if isinstance(cell, dict) and "hot" not in cell:
                chk.errors.append(f"{where}.table row {ri}: cell object must be {{hot: ...}}")


def _table_text(block):
    tab = block["table"]
    parts = list(tab.get("head", []))
    for row in tab.get("rows", []):
        for cell in row:
            parts.append(cell["hot"] if isinstance(cell, dict) else cell)
    return parts


def _table_html(block):
    tab = block["table"]
    head = "".join(f"<th>{esc(h)}</th>" for h in tab["head"])
    rows = []
    for row in tab["rows"]:
        cells = []
        for cell in row:
            if isinstance(cell, dict):
                cells.append(f"<td class=\"hot\">{esc(cell['hot'])}</td>")
            else:
                cells.append(f"<td>{esc(cell)}</td>")
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return ("        <div class=\"table-scroll\">\n"
            "          <table>\n"
            f"            <thead><tr>{head}</tr></thead>\n"
            "            <tbody>\n"
            + "".join(f"              {r}\n" for r in rows) +
            "            </tbody>\n"
            "          </table>\n"
            "        </div>\n")


def _chips_check(block, where, chk):
    for chip in block["chips"]:
        if "detail" not in chip or "label" not in chip:
            chk.errors.append(f"{where}.chips item needs label + detail")
            continue
        if chip["detail"] not in chk.details:
            chk.errors.append(f"{where}.chips: unknown detail key {chip['detail']!r}")


def _chips_text(block):
    return [chip["label"] if isinstance(chip["label"], str) else runs_text(chip["label"])
            for chip in block["chips"]]


def _chips_html(block):
    buttons = []
    for chip in block["chips"]:
        cls = "tap neutral" if chip.get("neutral") else "tap"
        buttons.append(f"<button class=\"{cls}\" data-detail=\"{escq(chip['detail'])}\">"
                       f"{runs_or_string_html(chip['label'])}</button>")
    return '        <div class="chips">' + "".join(buttons) + "</div>\n"


def _detail_check(block, where, chk):
    chk.check_runs(block["detail"].get("runs", []), f"{where}.detail.runs")
    chk.check_runs(block["detail"].get("comment", []), f"{where}.detail.comment")


def _detail_text(block):
    d = block["detail"]
    text = [d["label"], runs_text(d["runs"])]
    if "comment" in d:
        text.append(runs_text(d["comment"]))
    return text


def _detail_html(block):
    d = block["detail"]
    html = f"<div class=\"detail-block\"><b class=\"detail-label\">{esc(d['label'])}</b>{runs_html(d['runs'])}"
    if "comment" in d:
        html += f"<p class=\"detail-comment\">{runs_html(d['comment'])}</p>"
    return html + "</div>"


BLOCKS = {
    "h": _runs_def("h", "h3"),
    "p": _runs_def("p", "p"),
    "tiny": _runs_def("tiny", "p", "tiny"),
    "example": BlockDef(_example_check, _example_text, _example_html),
    "notice": BlockDef(_notice_check, _notice_text, _notice_html),
    "formula": BlockDef(_formula_check, _formula_text, _formula_html),
    "table": BlockDef(_table_check, _table_text, _table_html),
    "chips": BlockDef(_chips_check, _chips_text, _chips_html),
    "detail": BlockDef(_detail_check, _detail_text, _detail_html),
}
BLOCK_KEYS = set(BLOCKS)

# Traversal orders mirror the historical key checks so even pathological
# multi-key blocks behave exactly as before (visible-text assembly order,
# block_html's first-match pick).
TEXT_ORDER = ("h", "p", "tiny", "example", "notice", "formula", "table", "chips", "detail")
HTML_ORDER = ("h", "p", "tiny", "example", "formula", "table", "chips", "notice", "detail")
