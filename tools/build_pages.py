#!/usr/bin/env python3
"""Generate a language cheatsheet page from its deck JSON. Stdlib only.

Usage:
  python3 tools/build_pages.py content/decks/de-ru.json            # write meta.out (de/ru/index.html)
  python3 tools/build_pages.py content/decks/de-ru.json --check    # exit 1 if the page drifted

The deck schema lives in content/decks/schema.json (editor contract).
This script adds the build-time gate: reference integrity, unique ids,
table shape and run shapes. The generated page is committed; Pages serves
static files with no build step, and the page stays readable without JS.
"""
import argparse
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

BLOCK_KEYS = {"h", "p", "tiny", "example", "formula", "table", "chips", "notice", "detail"}


def esc(s):
    return html.escape(s, quote=False)


def escq(s):
    return html.escape(s, quote=True)


def js(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------- validation

def validate(deck, site):
    errors = []
    meta = deck.get("meta", {})
    for field in ("deck", "target", "audience", "target_lang", "lang", "out",
                  "site_base", "site_path", "brand_mark", "brand_name",
                  "brand_sub", "apple_title", "title", "description",
                  "og_title", "og_description", "plan_path"):
        if not meta.get(field):
            errors.append(f"meta.{field} is required")

    views = deck.get("views", [])
    view_ids = [v.get("id") for v in views]
    if len(views) < 3 or len(views) > 5:
        errors.append("views must have 3-5 items")
    if len(set(view_ids)) != len(view_ids):
        errors.append("view ids are not unique")

    details = deck.get("details", {})
    strings = deck.get("strings", {})

    def check_runs(runs, where):
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

    def check_blocks(blocks, where):
        for i, block in enumerate(blocks):
            if not isinstance(block, dict):
                errors.append(f"{where}[{i}]: block must be an object")
                continue
            keys = [k for k in block if k in BLOCK_KEYS]
            if len(keys) != 1:
                errors.append(f"{where}[{i}]: block must have exactly one of {sorted(BLOCK_KEYS)}")
                continue
            key = keys[0]
            if key in ("h", "p", "tiny", "example", "notice"):
                check_runs(block[key], f"{where}[{i}].{key}")
            elif key == "formula":
                items = block[key]
                if not isinstance(items, list) or not items:
                    errors.append(f"{where}[{i}].formula must be a non-empty list")
                    continue
                for j, item in enumerate(items):
                    if "arrow" in item:
                        continue
                    if "slot" not in item:
                        errors.append(f"{where}[{i}].formula[{j}]: needs 'slot' or 'arrow'")
                    elif isinstance(item["slot"], list):
                        check_runs(item["slot"], f"{where}[{i}].formula[{j}].slot")
            elif key == "table":
                tab = block[key]
                head = tab.get("head", [])
                for ri, row in enumerate(tab.get("rows", [])):
                    if len(row) != len(head):
                        errors.append(f"{where}[{i}].table row {ri} has {len(row)} cells, head has {len(head)}")
                    for cell in row:
                        if isinstance(cell, dict) and "hot" not in cell:
                            errors.append(f"{where}[{i}].table row {ri}: cell object must be {{hot: ...}}")
            elif key == "chips":
                for chip in block[key]:
                    if "detail" not in chip or "label" not in chip:
                        errors.append(f"{where}[{i}].chips item needs label + detail")
                        continue
                    if chip["detail"] not in details:
                        errors.append(f"{where}[{i}].chips: unknown detail key {chip['detail']!r}")
            elif key == "detail":
                d = block[key]
                check_runs(d.get("runs", []), f"{where}[{i}].detail.runs")

    def check_card(card, where):
        if not card.get("search"):
            errors.append(f"{where}: search keywords required")
        if bool(card.get("blocks")) == bool(card.get("case_grid")):
            errors.append(f"{where}: needs exactly one of blocks / case_grid")
            return
        if card.get("case_grid"):
            for j, c in enumerate(card["case_grid"]):
                if c.get("detail") not in details:
                    errors.append(f"{where}.case_grid[{j}]: unknown detail key {c.get('detail')!r}")
                check_runs(c.get("label", []), f"{where}.case_grid[{j}].label")
        else:
            check_blocks(card["blocks"], where)

    def check_group(group, where):
        if not group.get("cards"):
            errors.append(f"{where}: needs at least one card")
        if group.get("grid") not in ("two", "three", None):
            errors.append(f"{where}: grid must be two/three/null")
        if group.get("gap") and not group.get("grid"):
            errors.append(f"{where}: gap requires a gridded group")
        for ci, card in enumerate(group.get("cards", [])):
            check_card(card, f"{where} card {ci}")

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
                check_card(card, f"section {sid!r} card {ci}")
        else:
            for gi, group in enumerate(sec["groups"]):
                check_group(group, f"section {sid!r} group {gi}")

    practice = deck.get("practice", {})
    section_ids.append(practice.get("id"))
    # practice.view is its own anchor-only view (not a bottom-nav destination);
    # it only needs to be a non-empty slug.
    if not practice.get("view"):
        errors.append("practice.view required")
    if not practice.get("items"):
        errors.append("practice.items required")
    for i, item in enumerate(practice.get("items", [])):
        check_runs(item.get("q", []), f"practice.items[{i}].q")
        check_runs(item.get("answer", []), f"practice.items[{i}].answer")

    help_btn = deck.get("help")
    if help_btn:
        section_ids.append(help_btn.get("id"))
        if help_btn.get("detail") not in details:
            errors.append(f"help: unknown detail key {help_btn.get('detail')!r}")

    for key, entry in details.items():
        if not entry.get("title"):
            errors.append(f"details.{key}: title required")
        for bi, block in enumerate(entry.get("blocks", [])):
            check_blocks([block], f"details.{key}[{bi}]")
        if not entry.get("blocks"):
            errors.append(f"details.{key}: blocks required")

    if len([i for i in section_ids if i]) != len(set(i for i in section_ids if i)):
        errors.append(f"ids are not unique across sections/practice/help: {section_ids}")

    # footer_practice is optional: decks whose footer has no practice link omit it.
    for s in ("search_placeholder", "search_aria", "clear_aria", "install_label",
              "close_aria", "nav_aria", "no_results", "noscript_notice",
              "reveal_show", "reveal_hide", "footer_all",
              "footer_install", "footer_plan"):
        if not strings.get(s):
            errors.append(f"strings.{s} is required")
    for s in ("noscript_intro",):
        check_runs(strings.get(s, []), f"strings.{s}")
    for s in ("install_ios", "install_generic"):
        if not strings.get(s, {}).get("title"):
            errors.append(f"strings.{s}.title is required")

    # Site registry: every deck must be present in it (it drives the menu).
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
    for s in ("lang_menu_aria", "lang_group_target", "lang_group_audience", "lang_soon"):
        if not strings.get(s):
            errors.append(f"strings.{s} is required (header language menu)")

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
    if "h" in block:
        return f"        <h3>{runs_html(block['h'])}</h3>\n"
    if "p" in block:
        return f"        <p>{runs_html(block['p'])}</p>\n"
    if "tiny" in block:
        return f"        <p class=\"tiny\">{runs_html(block['tiny'])}</p>\n"
    if "example" in block:
        return f"        <div class=\"example\">{runs_html(block['example'])}</div>\n"
    if "formula" in block:
        parts = []
        for item in block["formula"]:
            if "arrow" in item:
                parts.append(f"<span class=\"arrow\">{esc(item['arrow'])}</span>")
            else:
                role = item.get("role")
                cls = f"slot {role}" if role else "slot"
                parts.append(f"<span class=\"{cls}\">{runs_or_string_html(item['slot'])}</span>")
        return "        <div class=\"formula\">" + "".join(parts) + "</div>\n"
    if "table" in block:
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
    if "chips" in block:
        buttons = []
        for chip in block["chips"]:
            cls = "tap neutral" if chip.get("neutral") else "tap"
            buttons.append(f"<button class=\"{cls}\" data-detail=\"{escq(chip['detail'])}\">"
                           f"{runs_or_string_html(chip['label'])}</button>")
        return '        <div class="chips">' + "".join(buttons) + "</div>\n"
    if "notice" in block:
        cls = "notice warning" if block.get("warning") else "notice"
        return f"        <div class=\"{cls}\">{runs_html(block['notice'])}</div>\n"
    if "detail" in block:
        d = block["detail"]
        return f"<div class=\"detail-block\"><b>{esc(d['label'])}</b>{runs_html(d['runs'])}</div>"
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


def section_html(sec):
    head = (f"    <section id=\"{escq(sec['id'])}\" data-section data-view=\"{escq(sec['view'])}\">\n"
            f"      <div class=\"section-head\"><div><h2>{esc(sec['heading'])}</h2>"
            f"<p>{esc(sec['sub'])}</p></div>"
            + (f"<span class=\"section-badge\">{esc(sec['badge'])}</span>" if sec.get("badge") else "")
            + "</div>\n")
    if sec.get("groups"):
        body = "".join(group_html(g) for g in sec["groups"])
    elif sec.get("grid"):
        body = group_html({"cards": sec["cards"], "grid": sec["grid"]})
    else:
        body = group_html({"cards": sec["cards"], "grid": None})
    return head + body + "    </section>\n"


def practice_html(practice, strings):
    out = [f"    <section id=\"{escq(practice['id'])}\" data-section data-view=\"{escq(practice['view'])}\">\n"]
    head = (f"      <div class=\"section-head\"><div><h2>{esc(practice['heading'])}</h2>"
            f"<p>{esc(practice['sub'])}</p></div>"
            + (f"<span class=\"section-badge\">{esc(practice['badge'])}</span>" if practice.get("badge") else "")
            + "</div>\n")
    out.append(head)
    out.append(f"      <article class=\"cheat-card\" data-search=\"{escq(practice['search'])}\">\n")
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


PAGE = """<!doctype html>
<html lang="@@HTML_LANG@@">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <!-- iOS standalone (Add to Home Screen) restores a stale zoom level on
       relaunch and pinch-out is unavailable there; lock the scale on iOS only.
       Safari itself ignores maximum-scale (pinch-zoom stays), Android and
       desktop keep pinch-zoom entirely. -->
  <script>
    if (/iphone|ipod/i.test(navigator.userAgent) || (/macintosh/i.test(navigator.userAgent) && navigator.maxTouchPoints > 1)) {
      document.querySelector('meta[name="viewport"]').setAttribute('content', 'width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover');
    }
  </script>
  <meta name="theme-color" content="#f6f7fb" media="(prefers-color-scheme: light)" />
  <meta name="theme-color" content="#10131b" media="(prefers-color-scheme: dark)" />
  <meta name="color-scheme" content="light dark" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="default" />
  <meta name="apple-mobile-web-app-title" content="@@APPLE_TITLE@@" />
  <meta name="description" content="@@DESCRIPTION@@" />
  <link rel="manifest" href="./manifest.webmanifest" />
  <link rel="icon" href="./icons/favicon.svg" type="image/svg+xml" />
  <link rel="icon" href="./icons/icon-32.png" sizes="32x32" type="image/png" />
  <link rel="apple-touch-icon" href="./icons/icon-180.png" />
  <meta property="og:title" content="@@OG_TITLE@@" />
  <meta property="og:description" content="@@OG_DESCRIPTION@@" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="@@OG_URL@@" />
  <meta property="og:image" content="@@OG_IMAGE@@" />
  <meta name="twitter:card" content="summary" />
  <title>@@TITLE@@</title>
  <link rel="stylesheet" href="@@ROOT@@assets/base.css" />
  <!-- Generated from @@DECK_PATH@@ by tools/build_pages.py — do not edit by hand;
       regenerate with: python3 tools/build_pages.py @@DECK_PATH@@ -->
</head>
<body>
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand-row">
        <div class="brand">
          <div class="brand-mark" aria-hidden="true">@@BRAND_MARK@@</div>
          <div>@@BRAND_NAME@@<small>@@BRAND_SUB@@</small></div>
        </div>
        @@HELP_BUTTON@@<button class="theme-btn" id="themeBtn" type="button" aria-label="@@THEME_AUTO_LABEL@@">@@THEME_AUTO_ICON@@</button>
        <button class="install-btn" id="installBtn" type="button">@@INSTALL_LABEL@@</button>
      </div>
      <div class="search-row">
        <div class="search-wrap">
          <span class="search-icon" aria-hidden="true">⌕</span>
          <input id="search" class="search" type="search" autocomplete="off" enterkeyhint="search" placeholder="@@SEARCH_PLACEHOLDER@@" aria-label="@@SEARCH_ARIA@@" />
          <button id="clearSearch" class="clear-search" type="button" aria-label="@@CLEAR_ARIA@@" hidden>×</button>
        </div>
        @@LANG_MENU@@
      </div>
    </div>
  </header>

  <noscript>
    <style>
      .tap, .install-btn, .clear-search, .theme-btn, .icon-btn { display: none !important; }
      .answer[hidden] { display: block; }
    </style>
    <div class="notice" style="margin:12px 16px 0">@@NOSCRIPT_NOTICE@@</div>
    <p class="intro" style="margin:10px 16px 0">@@NOSCRIPT_INTRO@@</p>
  </noscript>

  <main>
    <div id="noResults" class="no-results">@@NO_RESULTS@@</div>

@@SECTIONS@@
    <div class="footer">@@BRAND_NAME@@ · <a href="@@ROOT@@">@@FOOTER_ALL@@</a>@@FOOTER_PRACTICE@@ · <span id="install-help">@@FOOTER_INSTALL@@</span> · @@FOOTER_PLAN@@ <code>@@PLAN_PATH@@</code></div>
  </main>

  <nav class="bottom-nav" aria-label="@@NAV_ARIA@@">
@@NAV_ITEMS@@
  </nav>

  <dialog id="detailDialog" aria-labelledby="detailTitle">
    <div class="sheet">
      <div class="grab" aria-hidden="true"></div>
      <div class="sheet-head">
        <div><h2 id="detailTitle"></h2><p class="lead" id="detailLead"></p></div>
        <button class="close-sheet" id="closeDialog" aria-label="@@CLOSE_ARIA@@" type="button">×</button>
      </div>
      <div id="detailBody"></div>
    </div>
  </dialog>

  <script>
    const DETAILS = @@DETAILS@@;

    // Theme: auto (OS) / light / dark — persisted per visitor.
    const THEME_KEY = 'theme';
    const THEME_UI = @@THEME_UI@@;
    const themeBtn = document.getElementById('themeBtn');
    const themeMetas = [...document.querySelectorAll('meta[name="theme-color"]')];
    const themeMetaDefaults = themeMetas.map(m => m.content);
    function applyTheme(mode) {
      if (mode === 'auto') document.documentElement.removeAttribute('data-theme');
      else document.documentElement.setAttribute('data-theme', mode);
      themeBtn.textContent = THEME_UI[mode].icon;
      themeBtn.setAttribute('aria-label', THEME_UI[mode].label);
      themeBtn.title = THEME_UI[mode].label;
      themeMetas.forEach((m, i) => {
        m.content = mode === 'auto' ? themeMetaDefaults[i] : getComputedStyle(document.body).backgroundColor;
      });
    }
    let themeMode = 'auto';
    try { themeMode = localStorage.getItem(THEME_KEY) || 'auto'; } catch (e) {}
    applyTheme(themeMode);
    themeBtn.addEventListener('click', () => {
      themeMode = themeMode === 'auto' ? 'light' : themeMode === 'light' ? 'dark' : 'auto';
      try { localStorage.setItem(THEME_KEY, themeMode); } catch (e) {}
      applyTheme(themeMode);
    });

    const dialog = document.getElementById('detailDialog');
    const detailTitle = document.getElementById('detailTitle');
    const detailLead = document.getElementById('detailLead');
    const detailBody = document.getElementById('detailBody');

    // Target-language text gets lang="@@TARGET_LANG@@" (screen-reader pronunciation + the
    // serif study voice from base.css). Whole containers that carry only
    // target-language text (examples, answers, declension tables) are marked directly;
    // otherwise the fragments are: bold in .example/.answer, italics in
    // .detail-block, formula slots without Cyrillic.
    const TARGET_LANG = '@@TARGET_LANG@@';
    function markTargetLang(root) {
      root.querySelectorAll('.example, .answer, .table-scroll').forEach(el => {
        if (!/[а-яё]/i.test(el.textContent)) el.lang = TARGET_LANG;
      });
      root.querySelectorAll('.example b, .answer b, .detail-block i, .formula .slot').forEach(el => {
        if (!/[а-яё]/i.test(el.textContent)) el.lang = TARGET_LANG;
      });
    }
    markTargetLang(document);

    document.addEventListener('click', (event) => {
      const trigger = event.target.closest('[data-detail]');
      if (trigger) {
        const item = DETAILS[trigger.dataset.detail];
        if (item) {
          detailTitle.textContent = item.title;
          detailLead.textContent = item.lead || '';
          detailBody.innerHTML = item.body || '';
          markTargetLang(detailBody);
          dialog.showModal();
        }
      }
      const reveal = event.target.closest('.reveal');
      if (reveal) {
        const answer = document.getElementById(reveal.dataset.target);
        if (answer) {
          answer.hidden = !answer.hidden;
          reveal.textContent = answer.hidden ? '@@REVEAL_SHOW@@' : '@@REVEAL_HIDE@@';
          reveal.setAttribute('aria-expanded', String(!answer.hidden));
        }
      }
    });

    document.getElementById('closeDialog').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', (event) => {
      if (event.target === dialog) dialog.close();
    });

    // Language menu: light-dismiss (native <details> has none) + Escape.
    const langMenu = document.getElementById('langMenu');
    if (langMenu) {
      document.addEventListener('click', (event) => {
        if (langMenu.open && !langMenu.contains(event.target)) langMenu.open = false;
      });
      document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && langMenu.open) langMenu.open = false;
      });
    }
    // Remember what is being studied so the landing can greet the learner.
    try { localStorage.setItem('target', TARGET_LANG); } catch (e) {}

    const search = document.getElementById('search');
    const clearSearch = document.getElementById('clearSearch');
    const cards = [...document.querySelectorAll('.cheat-card')];
    const sections = [...document.querySelectorAll('section[data-section]')];
    const noResults = document.getElementById('noResults');

    function applySearch() {
      const q = search.value.trim().toLowerCase();
      document.body.classList.toggle('searching', !!q);
      clearSearch.hidden = !q;
      let shown = 0;
      cards.forEach(card => {
        const hay = `${card.textContent} ${card.dataset.search || ''}`.toLowerCase();
        const match = !q || hay.includes(q);
        card.style.display = match ? '' : 'none';
        if (match) shown++;
      });
      sections.forEach(section => {
        if (!q) { section.style.display = ''; return; }
        section.hidden = false; // search spans every view
        const visible = [...section.querySelectorAll('.cheat-card')].some(c => c.style.display !== 'none');
        section.style.display = visible ? '' : 'none';
      });
      if (!q) setView(currentView); // re-apply the active view
      noResults.style.display = q && shown === 0 ? 'block' : 'none';
    }
    search.addEventListener('input', applySearch);
    clearSearch.addEventListener('click', () => { search.value = ''; applySearch(); search.focus(); });

    // Views: the bottom nav switches discrete views; the selection is the truth
    // (no scrollspy). Sections carry data-view; legacy anchors open the right
    // view first, then scroll to the section.
    const navItems = [...document.querySelectorAll('.nav-item')];
    const viewSections = [...document.querySelectorAll('section[data-view]')];
    let currentView = navItems[0].dataset.nav;
    function setView(viewId) {
      currentView = viewId;
      viewSections.forEach(s => {
        s.hidden = s.dataset.view !== viewId;
        s.style.display = '';
      });
      navItems.forEach(item => {
        const on = item.dataset.nav === viewId;
        item.classList.toggle('active', on);
        if (on) item.setAttribute('aria-current', 'true');
        else item.removeAttribute('aria-current');
      });
    }
    navItems.forEach(item => item.addEventListener('click', (event) => {
      event.preventDefault();
      const viewId = item.dataset.nav;
      if (search.value) { search.value = ''; applySearch(); } // predictable destination
      if (location.hash !== '#' + viewId) history.pushState(null, '', '#' + viewId);
      setView(viewId);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }));
    function onHash() {
      const id = location.hash.slice(1);
      const target = id ? document.getElementById(id) : null;
      const hostSection = target && target.closest('section[data-view]');
      const viewId = hostSection ? hostSection.dataset.view
        : (navItems.some(n => n.dataset.nav === id) ? id : null);
      if (!viewId) return; // unknown hash: keep the current view
      setView(viewId);
      if (target && hostSection && target !== hostSection) target.scrollIntoView();
    }
    window.addEventListener('hashchange', onHash);
    if (location.hash) onHash(); else setView(currentView);

    let deferredPrompt = null;
    const installBtn = document.getElementById('installBtn');
    const isIOS = /iphone|ipad|ipod/i.test(navigator.userAgent);
    const isStandalone = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone;
    if (isIOS && !isStandalone) installBtn.hidden = false;
    else installBtn.hidden = true;

    window.addEventListener('beforeinstallprompt', (event) => {
      event.preventDefault();
      deferredPrompt = event;
      installBtn.hidden = false;
    });

    window.addEventListener('appinstalled', () => {
      deferredPrompt = null;
      installBtn.hidden = true;
    });

    const INSTALL = @@INSTALL@@;
    installBtn.addEventListener('click', async () => {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        await deferredPrompt.userChoice;
        deferredPrompt = null;
        installBtn.hidden = true;
      } else if (isIOS) {
        detailTitle.textContent = INSTALL.ios.title;
        detailLead.textContent = INSTALL.ios.lead;
        detailBody.innerHTML = INSTALL.ios.body;
        dialog.showModal();
      } else {
        detailTitle.textContent = INSTALL.generic.title;
        detailLead.textContent = INSTALL.generic.lead;
        detailBody.innerHTML = INSTALL.generic.body;
        dialog.showModal();
      }
    });

    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => navigator.serviceWorker.register('@@ROOT@@sw.js').catch(() => {}));
    }
  </script>
</body>
</html>
"""


def render(deck, deck_path, site):
    meta, strings = deck["meta"], deck["strings"]
    og_url = meta["site_base"] + meta["site_path"]
    og_image = og_url + "icons/icon-512.png"
    # Pages live at <target>/<audience>/ depth: site_path "en/ru/" → prefix "../../"
    # for site-root assets (base.css, sw.js, the landing link).
    root = "../" * meta["site_path"].count("/")

    help_btn = deck.get("help")
    help_html = ""
    if help_btn:
        help_html = (f"<button class=\"icon-btn\" id=\"{escq(help_btn['id'])}\" type=\"button\" "
                     f"data-detail=\"{escq(help_btn['detail'])}\" aria-haspopup=\"dialog\" "
                     f"aria-label=\"{escq(help_btn['label'])}\" title=\"{escq(help_btn['label'])}\">"
                     f"<span class=\"ico\" aria-hidden=\"true\">{esc(help_btn['ico'])}</span></button>")

    def lang_menu_html(deck, site):
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

    def dialog_js(d):
        return {"title": d["title"], "lead": d["lead"],
                "body": "".join(f"<div class=\"detail-block\"><b>{esc(b['label'])}</b>{runs_html(b['runs'])}</div>"
                                for b in d["blocks"])}

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
        "@@HELP_BUTTON@@": help_html,
        "@@LANG_MENU@@": lang_menu_html(deck, site),
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
