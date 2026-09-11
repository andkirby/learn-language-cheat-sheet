#!/usr/bin/env python3
"""Generate a language cheatsheet page from its deck JSON. Stdlib only.

Usage:
  python3 tools/build_pages.py content/decks/de-ru.json            # write meta.out (de/ru/index.html)
  python3 tools/build_pages.py content/decks/de-ru.json --check    # exit 1 if the page drifted

The deck schema lives in content/decks/schema.json (editor contract).
This script adds the build-time gate: reference integrity, unique ids,
table shape and run shapes. The page skeleton lives in the sibling
page_template.html (loaded verbatim; render() substitutes the @@TOKENS@@).
The generated page is committed; Pages serves static files with no build
step, and the page stays readable without JS.
"""
import argparse
import html
import json
import re
import pathlib
import sys
from collections import namedtuple

ROOT = pathlib.Path(__file__).resolve().parent.parent


def esc(s):
    return html.escape(s, quote=False)


def escq(s):
    return html.escape(s, quote=True)


def js(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------- validation

def _runs_text(runs):
    return " ".join(r.get("t", "") if isinstance(r, dict) else r for r in runs)


_UMAP = str.maketrans({"ä": "a", "ö": "o", "ü": "u", "ß": "ss"})
# word chars incl. Cyrillic (для видимого текста) — letter-runs split on punctuation/slashes
_WORD_RE = re.compile(r"[a-zà-ÿ0-9а-яёіґїє]+")


def _norm(s):
    return s.lower().translate(_UMAP).replace("'", "").replace("’", "")


def _grammar_terms(site, target_id):
    """Search-index exemptions from content/decks/site.json: grammar
    terminology that may sit in data-search without being visible on the
    card. The shared list applies to every target; a target's own list
    applies only to its decks — new languages edit site.json, not this file."""
    terms = set(_norm(t) for t in site.get("grammar_terms_common", []))
    for t in site.get("targets", []):
        if t.get("id") == target_id:
            terms |= set(_norm(x) for x in t.get("grammar_terms", []))
    return terms


# ---------------------------------------------------------------- block registry
# One entry per block type: shape check, learner-visible text (feeds the
# search-index gate) and HTML rendering all live here, so adding or changing
# a block type means adding/changing one entry — not four scattered sites.

BlockDef = namedtuple("BlockDef", "check text html")


def _runs_def(key, tag, cls=None):
    """h/p/tiny/example: a plain runs payload wrapped in one element."""
    def check(block, where, chk):
        chk.check_runs(block[key], f"{where}.{key}")

    def text(block):
        return [_runs_text(block[key])]

    def html(block):
        c = f' class="{cls}"' if cls else ""
        return f"        <{tag}{c}>{runs_html(block[key])}</{tag}>\n"

    return BlockDef(check, text, html)


def _notice_check(block, where, chk):
    chk.check_runs(block["notice"], f"{where}.notice")


def _notice_text(block):
    return [_runs_text(block["notice"])]


def _notice_html(block):
    cls = "notice warning" if block.get("warning") else "notice"
    return f"        <div class=\"{cls}\">{runs_html(block['notice'])}</div>\n"


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
                           else _runs_text(item["slot"])))
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
    return [chip["label"] if isinstance(chip["label"], str) else _runs_text(chip["label"])
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


def _detail_text(block):
    d = block["detail"]
    return [d["label"], _runs_text(d["runs"])]


def _detail_html(block):
    d = block["detail"]
    return f"<div class=\"detail-block\"><b>{esc(d['label'])}</b>{runs_html(d['runs'])}</div>"


_BLOCKS = {
    "h": _runs_def("h", "h3"),
    "p": _runs_def("p", "p"),
    "tiny": _runs_def("tiny", "p", "tiny"),
    "example": _runs_def("example", "div", "example"),
    "notice": BlockDef(_notice_check, _notice_text, _notice_html),
    "formula": BlockDef(_formula_check, _formula_text, _formula_html),
    "table": BlockDef(_table_check, _table_text, _table_html),
    "chips": BlockDef(_chips_check, _chips_text, _chips_html),
    "detail": BlockDef(_detail_check, _detail_text, _detail_html),
}
BLOCK_KEYS = set(_BLOCKS)

# Traversal orders mirror the historical key checks so even pathological
# multi-key blocks behave exactly as before (visible-text assembly order,
# block_html's first-match pick).
_TEXT_ORDER = ("h", "p", "tiny", "example", "notice", "formula", "table", "chips", "detail")
_HTML_ORDER = ("h", "p", "tiny", "example", "formula", "table", "chips", "notice", "detail")


def _card_visible_text(card):
    """Everything a learner sees on the card (search never indexes dialogs)."""
    parts = []
    if card.get("case_grid"):
        for c in card["case_grid"]:
            parts.append(_runs_text(c.get("label", [])))
        return " ".join(parts).lower().replace("ё", "е")
    for block in card.get("blocks", []):
        for key in _TEXT_ORDER:
            if key in block:
                parts.extend(_BLOCKS[key].text(block))
    return " ".join(str(p) for p in parts).lower().replace("ё", "е")


def _check_runs(errors, runs, where):
    if not isinstance(runs, list):
        errors.append(f"{where}: runs must be a list")
        return
    for i, run in enumerate(runs):
        if isinstance(run, str):
            continue
        if not isinstance(run, dict):
            errors.append(f"{where}[{i}]: run must be a string or object")
            continue
        if "br" in run:
            continue
        if "t" not in run:
            errors.append(f"{where}[{i}]: run object needs 't' or 'br'")
        for flag in ("b", "i", "s"):
            if flag in run and not isinstance(run[flag], bool):
                errors.append(f"{where}[{i}]: .{flag} must be boolean")


class _Checker:
    """Deck-shape checks (blocks, cards, groups) accumulating errors in place."""

    def __init__(self, errors, details, grammar_terms):
        self.errors = errors
        self.details = details
        self.grammar_terms = grammar_terms

    def check_runs(self, runs, where):
        _check_runs(self.errors, runs, where)

    def check_blocks(self, blocks, where):
        for i, block in enumerate(blocks):
            if not isinstance(block, dict):
                self.errors.append(f"{where}[{i}]: block must be an object")
                continue
            keys = [k for k in block if k in BLOCK_KEYS]
            if len(keys) != 1:
                self.errors.append(f"{where}[{i}]: block must have exactly one of {sorted(BLOCK_KEYS)}")
                continue
            _BLOCKS[keys[0]].check(block, f"{where}[{i}]", self)

    def check_card(self, card, where):
        if not card.get("search"):
            self.errors.append(f"{where}: search keywords required")
        if bool(card.get("blocks")) == bool(card.get("case_grid")):
            self.errors.append(f"{where}: needs exactly one of blocks / case_grid")
            return
        if card.get("case_grid"):
            for j, c in enumerate(card["case_grid"]):
                if c.get("detail") not in self.details:
                    self.errors.append(f"{where}.case_grid[{j}]: unknown detail key {c.get('detail')!r}")
                self.check_runs(c.get("label", []), f"{where}.case_grid[{j}].label")
        else:
            self.check_blocks(card["blocks"], where)
        # Search-index hygiene (see the _grammar_terms note above).
        words = set(_WORD_RE.findall(_norm(_card_visible_text(card))))
        for token in str(card.get("search", "")).split():
            t = _norm(token)
            if t in self.grammar_terms or len(t) < 3:
                continue
            if re.search(r"[\u0400-\u04FF]", token):
                continue  # searcher's own script (any Cyrillic): variants expected
            ok = t in words or any(
                len(w) >= 3 and (w.startswith(t) or t.startswith(w))
                for w in words
            )
            if not ok:
                self.errors.append(f"{where}: search token {token!r} is not visible on the card "
                                   f"(surface it on the card, or add it to grammar_terms in content/decks/site.json "
                                   f"if it is grammar terminology)")

    def check_group(self, group, where):
        if not group.get("cards"):
            self.errors.append(f"{where}: needs at least one card")
        if group.get("grid") not in ("two", "three", None):
            self.errors.append(f"{where}: grid must be two/three/null")
        if group.get("gap") and not group.get("grid"):
            self.errors.append(f"{where}: gap requires a gridded group")
        for ci, card in enumerate(group.get("cards", [])):
            self.check_card(card, f"{where} card {ci}")


def _validate_meta(deck, errors):
    meta = deck.get("meta", {})
    for field in ("deck", "target", "audience", "target_lang", "lang", "out",
                  "site_base", "site_path", "brand_mark", "brand_name",
                  "brand_sub", "apple_title", "title", "description",
                  "og_title", "og_description", "plan_path"):
        if not meta.get(field):
            errors.append(f"meta.{field} is required")


def _validate_content(deck, site, errors):
    """Views, sections, cards, practice, help, details and id uniqueness."""
    meta = deck.get("meta", {})
    details = deck.get("details", {})
    chk = _Checker(errors, details, _grammar_terms(site, meta.get("target")))

    views = deck.get("views", [])
    view_ids = [v.get("id") for v in views]
    if len(views) < 3 or len(views) > 5:
        errors.append("views must have 3-5 items")
    if len(set(view_ids)) != len(view_ids):
        errors.append("view ids are not unique")

    section_ids = []
    for si, sec in enumerate(deck.get("sections", [])):
        sid = sec.get("id", f"<section {si}>")
        section_ids.append(sec.get("id"))
        if sec.get("view") not in view_ids:
            errors.append(f"section {sid!r}: view {sec.get('view')!r} is not a nav view")
        has_cards, has_groups = bool(sec.get("cards")), bool(sec.get("groups"))
        if has_cards == has_groups:
            errors.append(f"section {sid!r}: needs exactly one of cards / groups")
            continue
        if has_cards:
            if sec.get("grid") not in ("two", "three", None):
                errors.append(f"section {sid!r}: grid must be two/three/null")
            for ci, card in enumerate(sec.get("cards", [])):
                chk.check_card(card, f"section {sid!r} card {ci}")
        else:
            for gi, group in enumerate(sec["groups"]):
                chk.check_group(group, f"section {sid!r} group {gi}")

    practice = deck.get("practice", {})
    section_ids.append(practice.get("id"))
    # practice.view is its own anchor-only view (not a bottom-nav destination);
    # it only needs to be a non-empty slug.
    if not practice.get("view"):
        errors.append("practice.view required")
    if not practice.get("items"):
        errors.append("practice.items required")
    for i, item in enumerate(practice.get("items", [])):
        chk.check_runs(item.get("q", []), f"practice.items[{i}].q")
        chk.check_runs(item.get("answer", []), f"practice.items[{i}].answer")

    help_btn = deck.get("help")
    if help_btn:
        section_ids.append(help_btn.get("id"))
        if help_btn.get("detail") not in details:
            errors.append(f"help: unknown detail key {help_btn.get('detail')!r}")

    for key, entry in details.items():
        if not entry.get("title"):
            errors.append(f"details.{key}: title required")
        for bi, block in enumerate(entry.get("blocks", [])):
            chk.check_blocks([block], f"details.{key}[{bi}]")
        if not entry.get("blocks"):
            errors.append(f"details.{key}: blocks required")

    if len([i for i in section_ids if i]) != len(set(i for i in section_ids if i)):
        errors.append(f"ids are not unique across sections/practice/help: {section_ids}")


def _validate_strings(deck, errors):
    strings = deck.get("strings", {})
    # footer_practice is optional: decks whose footer has no practice link omit it.
    for s in ("search_placeholder", "search_aria", "clear_aria", "install_label",
              "close_aria", "nav_aria", "no_results", "noscript_notice",
              "reveal_show", "reveal_hide", "footer_all",
              "footer_install", "footer_plan"):
        if not strings.get(s):
            errors.append(f"strings.{s} is required")
    _check_runs(errors, strings.get("noscript_intro", []), "strings.noscript_intro")
    for s in ("install_ios", "install_generic"):
        if not strings.get(s, {}).get("title"):
            errors.append(f"strings.{s}.title is required")


def _validate_site(deck, site, errors):
    meta = deck.get("meta", {})
    # Site registry: every deck must be present in it (it drives the menu).
    for key in ("grammar_terms_common",):
        if not isinstance(site.get(key, []), list):
            errors.append(f"site.json {key} must be a list")
    target_ids = []
    for i, t in enumerate(site.get("targets", [])):
        if not t.get("id") or not t.get("label"):
            errors.append(f"site.json targets[{i}]: id and label required")
        aud_ids = [a.get("id") for a in t.get("audiences", [])]
        if not aud_ids:
            errors.append(f"site.json target {t.get('id')!r}: needs at least one audience")
        if len(set(aud_ids)) != len(aud_ids):
            errors.append(f"site.json target {t.get('id')!r}: audience ids not unique")
        for j, a in enumerate(t.get("audiences", [])):
            if not a.get("id") or not a.get("label"):
                errors.append(f"site.json targets[{i}].audiences[{j}]: id and label required")
        if not isinstance(t.get("grammar_terms", []), list):
            errors.append(f"site.json target {t.get('id')!r}: grammar_terms must be a list")
        target_ids.append(t.get("id"))
    if len(set(target_ids)) != len(target_ids):
        errors.append("site.json: target ids not unique")
    own = next((t for t in site.get("targets", []) if t.get("id") == meta.get("target")), None)
    if own is None:
        errors.append(f"site.json: deck target {meta.get('target')!r} is missing from the registry")
    elif meta.get("audience") not in [a.get("id") for a in own.get("audiences", [])]:
        errors.append(f"site.json: target {meta.get('target')!r} has no audience {meta.get('audience')!r}")
    elif not any(a.get("id") == meta.get("audience") and not a.get("soon") for a in own["audiences"]):
        errors.append(f"site.json: the deck's own audience {meta.get('audience')!r} cannot be marked soon")
    strings = deck.get("strings", {})
    for s in ("lang_menu_aria", "lang_group_target", "lang_group_audience", "lang_soon"):
        if not strings.get(s):
            errors.append(f"strings.{s} is required (header language menu)")


def validate(deck, site):
    errors = []
    _validate_meta(deck, errors)
    _validate_content(deck, site, errors)
    _validate_strings(deck, errors)
    _validate_site(deck, site, errors)
    return errors


# ---------------------------------------------------------------- rendering

def run_html(run):
    if isinstance(run, str):
        return esc(run)
    if "br" in run:
        return "<br>"
    inner = esc(run["t"])
    if run.get("s"):
        inner = f"<s>{inner}</s>"
    if run.get("i"):
        inner = f"<i>{inner}</i>"
    if run.get("b"):
        inner = f"<b>{inner}</b>"
    return inner


def runs_html(runs):
    return "".join(run_html(r) for r in runs)


def runs_or_string_html(v):
    return esc(v) if isinstance(v, str) else runs_html(v)


def block_html(block):
    for key in _HTML_ORDER:
        if key in block:
            return _BLOCKS[key].html(block)
    raise ValueError(f"unknown block: {block}")


def card_html(card, indent="      "):
    if card.get("case_grid"):
        buttons = [f'<button class="tap case" data-detail="{escq(c["detail"])}">'
                   f"{runs_html(c['label'])}</button>" for c in card["case_grid"]]
        return (f'{indent}<div class="case-grid cheat-card" data-search="{escq(card["search"])}">\n'
                + "".join(f"{indent}  {b}\n" for b in buttons)
                + f"{indent}</div>\n")
    out = [f"{indent}<article class=\"cheat-card\" data-search=\"{escq(card['search'])}\">\n"]
    for block in card["blocks"]:
        out.append(block_html(block))
    out.append(f"{indent}</article>\n")
    return "".join(out)


def group_html(group, indent="      "):
    if group.get("grid"):
        cls = f"cards {group['grid']}"
        style = ' style="margin-top:10px"' if group.get("gap") else ""
        out = f'{indent}<div class="{cls}"{style}>\n'
        for card in group["cards"]:
            out += card_html(card, indent + "  ")
        return out + f"{indent}</div>\n"
    return "".join(card_html(card, indent) for card in group["cards"])


def _section_head(sec):
    return (f"      <div class=\"section-head\"><div><h2>{esc(sec['heading'])}</h2>"
            f"<p>{esc(sec['sub'])}</p></div>"
            + (f"<span class=\"section-badge\">{esc(sec['badge'])}</span>" if sec.get("badge") else "")
            + "</div>\n")


def section_html(sec):
    head = (f"    <section id=\"{escq(sec['id'])}\" data-section data-view=\"{escq(sec['view'])}\">\n"
            + _section_head(sec))
    if sec.get("groups"):
        body = "".join(group_html(g) for g in sec["groups"])
    else:
        body = group_html({"cards": sec["cards"], "grid": sec.get("grid")})
    return head + body + "    </section>\n"


def practice_html(practice, strings):
    out = [f"    <section id=\"{escq(practice['id'])}\" data-section data-view=\"{escq(practice['view'])}\">\n",
           _section_head(practice),
           f"      <article class=\"cheat-card\" data-search=\"{escq(practice['search'])}\">\n"]
    for i, item in enumerate(practice["items"], start=1):
        out.append("        <div class=\"practice-q\">\n")
        out.append(f"          {runs_html(item['q'])}\n")
        out.append(f"          <div class=\"chips\"><button class=\"tap neutral reveal\" data-target=\"a{i}\" "
                   f"aria-expanded=\"false\" aria-controls=\"a{i}\">{esc(strings['reveal_show'])}</button></div>\n")
        out.append(f"          <div class=\"answer\" id=\"a{i}\" hidden>{runs_html(item['answer'])}</div>\n")
        out.append("        </div>\n")
    out.append("      </article>\n")
    out.append("    </section>\n")
    return "".join(out)


# The page skeleton lives in the sibling file so template edits diff as HTML.
PAGE = (pathlib.Path(__file__).resolve().parent / "page_template.html").read_text(encoding="utf-8")


def _help_button_html(help_btn):
    if not help_btn:
        return ""
    return (f"<button class=\"icon-btn\" id=\"{escq(help_btn['id'])}\" type=\"button\" "
            f"data-detail=\"{escq(help_btn['detail'])}\" aria-haspopup=\"dialog\" "
            f"aria-label=\"{escq(help_btn['label'])}\" title=\"{escq(help_btn['label'])}\">"
            f"<span class=\"ico\" aria-hidden=\"true\">{esc(help_btn['ico'])}</span></button>")


def _lang_menu_html(deck, site):
    meta, strings = deck["meta"], deck["strings"]
    targets = site["targets"]
    cur_target = next(t for t in targets if t["id"] == meta["target"])
    t_items = []
    for t in targets:
        if t["id"] == meta["target"]:
            t_items.append(f"<span class=\"cur\">{esc(t['label'])}</span>")
        else:
            # keep the reader's audience when that deck exists, else the
            # target's first non-soon audience
            real = [a["id"] for a in t["audiences"] if not a.get("soon")]
            aud = meta["audience"] if meta["audience"] in real else real[0]
            t_items.append(f"<a href=\"../../{escq(t['id'])}/{escq(aud)}/\">{esc(t['label'])}</a>")
    a_items = []
    for a in cur_target["audiences"]:
        if a["id"] == meta["audience"]:
            a_items.append(f"<span class=\"cur\">{esc(a['label'])}</span>")
        elif a.get("soon"):
            a_items.append(f"<span class=\"soon\">{esc(a['label'])} — {esc(strings['lang_soon'])}</span>")
        else:
            a_items.append(f"<a href=\"../{escq(a['id'])}/\">{esc(a['label'])}</a>")
    return (f"<details class=\"lang-menu\" id=\"langMenu\">"
            f"<summary aria-label=\"{escq(strings['lang_menu_aria'])}\">"
            f"{esc(meta['target'].upper())} · {esc(meta['audience'].upper())}</summary>"
            f"<div class=\"lang-pop\">"
            f"<div class=\"lang-group\"><div class=\"lang-group-label\">{esc(strings['lang_group_target'])}</div>{''.join(t_items)}</div>"
            f"<div class=\"lang-group\"><div class=\"lang-group-label\">{esc(strings['lang_group_audience'])}</div>{''.join(a_items)}</div>"
            f"</div></details>")


def dialog_js(d):
    return {"title": d["title"], "lead": d["lead"],
            "body": "".join(_BLOCKS["detail"].html({"detail": b}) for b in d["blocks"])}


def render(deck, deck_path, site):
    meta, strings = deck["meta"], deck["strings"]
    og_url = meta["site_base"] + meta["site_path"]
    og_image = og_url + "icons/icon-512.png"
    # Pages live at <target>/<audience>/ depth: site_path "en/ru/" → prefix "../../"
    # for site-root assets (base.css, sw.js, the landing link).
    root = "../" * meta["site_path"].count("/")

    sections_html = "".join(section_html(s) for s in deck["sections"]) + practice_html(deck["practice"], strings)

    nav_items = []
    for i, view in enumerate(deck["views"]):
        active = ' class="nav-item active" aria-current="true"' if i == 0 else ' class="nav-item"'
        nav_items.append(f"    <a{active} href=\"#{escq(view['id'])}\" data-nav=\"{escq(view['id'])}\">"
                         f"<span class=\"ico\">{esc(view['ico'])}</span><span>{esc(view['label'])}</span></a>")

    details_js = {}
    for key, entry in deck["details"].items():
        details_js[key] = {
            "title": entry["title"],
            "lead": entry["lead"],
            "body": "".join(block_html(b) for b in entry["blocks"]),
        }

    footer_practice = ""
    if strings.get("footer_practice"):
        footer_practice = (f' · <a href="#{escq(deck["practice"]["id"])}">'
                           f'{esc(strings["footer_practice"])}</a>')

    tokens = {
        "@@DECK_PATH@@": deck_path,
        "@@HTML_LANG@@": escq(meta["lang"]),
        "@@ROOT@@": root,
        "@@APPLE_TITLE@@": escq(meta["apple_title"]),
        "@@DESCRIPTION@@": escq(meta["description"]),
        "@@OG_TITLE@@": escq(meta["og_title"]),
        "@@OG_DESCRIPTION@@": escq(meta["og_description"]),
        "@@OG_URL@@": escq(og_url),
        "@@OG_IMAGE@@": escq(og_image),
        "@@TITLE@@": escq(meta["title"]),
        "@@BRAND_MARK@@": esc(meta["brand_mark"]),
        "@@BRAND_NAME@@": esc(meta["brand_name"]),
        "@@BRAND_SUB@@": esc(meta["brand_sub"]),
        "@@THEME_AUTO_LABEL@@": escq(strings["theme"]["auto"]["label"]),
        "@@THEME_AUTO_ICON@@": esc(strings["theme"]["auto"]["icon"]),
        "@@INSTALL_LABEL@@": esc(strings["install_label"]),
        "@@SEARCH_PLACEHOLDER@@": escq(strings["search_placeholder"]),
        "@@SEARCH_ARIA@@": escq(strings["search_aria"]),
        "@@CLEAR_ARIA@@": escq(strings["clear_aria"]),
        "@@NOSCRIPT_NOTICE@@": esc(strings["noscript_notice"]),
        "@@NOSCRIPT_INTRO@@": runs_html(strings["noscript_intro"]),
        "@@HELP_BUTTON@@": _help_button_html(deck.get("help")),
        "@@LANG_MENU@@": _lang_menu_html(deck, site),
        "@@NO_RESULTS@@": esc(strings["no_results"]),
        "@@SECTIONS@@": sections_html.rstrip("\n"),
        "@@FOOTER_PRACTICE@@": footer_practice,
        "@@FOOTER_ALL@@": esc(strings["footer_all"]),
        "@@FOOTER_INSTALL@@": esc(strings["footer_install"]),
        "@@FOOTER_PLAN@@": esc(strings["footer_plan"]),
        "@@PLAN_PATH@@": esc(meta["plan_path"]),
        "@@NAV_ITEMS@@": "\n".join(nav_items),
        "@@NAV_ARIA@@": escq(strings["nav_aria"]),
        "@@CLOSE_ARIA@@": escq(strings["close_aria"]),
        "@@DETAILS@@": js(details_js),
        "@@THEME_UI@@": js(strings["theme"]),
        "@@TARGET_LANG@@": escq(meta["target_lang"]),
        "@@REVEAL_SHOW@@": strings["reveal_show"],
        "@@REVEAL_HIDE@@": strings["reveal_hide"],
        "@@INSTALL@@": js({"ios": dialog_js(strings["install_ios"]),
                           "generic": dialog_js(strings["install_generic"])}),
    }
    page = PAGE
    for token, value in tokens.items():
        page = page.replace(token, value)
    return page


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
