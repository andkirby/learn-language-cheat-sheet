"""Deck JSON → the committed HTML page. Stdlib only.

render(deck, deck_path, site) assembles sections/cards/practice via the
block registry (deck_blocks), substitutes the @@TOKENS@@ of the sibling
page_template.html skeleton, and returns the page as a string. Block
markup comes from the registry; everything here is page-level assembly.
"""
import pathlib

from deck_blocks import BLOCKS, HTML_ORDER
from deck_html import esc, escq, js, runs_html


def block_html(block):
    for key in HTML_ORDER:
        if key in block:
            return BLOCKS[key].html(block)
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
            "body": "".join(BLOCKS["detail"].html({"detail": b}) for b in d["blocks"])}


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
