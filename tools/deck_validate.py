"""The build-time content gate: deck + site.json validation. Stdlib only.

validate(deck, site) returns a flat error list (empty = deck is
buildable). Covers meta completeness, view/section/card shape via the
block registry (deck_blocks), dialog reference integrity, practice and
help shape, id uniqueness, UI strings, and the site.json registry —
including the search-index hygiene gate (data-search tokens must be
learner-visible or exempted as grammar terminology in site.json).
"""
import re

from deck_blocks import BLOCKS, BLOCK_KEYS, TEXT_ORDER, runs_text

_UMAP = str.maketrans({"ä": "a", "ö": "o", "ü": "u", "ß": "ss"})
# word chars incl. Cyrillic (для видимого текста) — letter-runs split on punctuation/slashes
_WORD_RE = re.compile(r"[a-zà-ÿ0-9а-яёіґїє]+")

# Audience-script exemptions, configured per audience in site.json ("script").
# A data-search token in the searcher's own script may legitimately differ
# from the card wording. Absent or unknown script = no exemption (strict),
# so Latin-script audiences get no free pass.
_SCRIPTS = {"cyrillic": re.compile(r"[\u0400-\u04FF]")}


def _audience_script(site, target_id, audience_id):
    own = next((t for t in site.get("targets", []) if t.get("id") == target_id), None)
    aud = next((a for a in (own or {}).get("audiences", [])
                if a.get("id") == audience_id), None)
    return _SCRIPTS.get((aud or {}).get("script"))


# Card anchor slugs: latin grammar terms only — Cyrillic slugs percent-encode
# into unreadable shared URLs. 2-32 chars, inner hyphens allowed.
_SLUG_RE = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?")

# Badge levels track the deck's A1–B1 span; new levels mean a scope change.
_LEVELS = ("A1", "A2", "B1")


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


def _card_visible_text(card):
    """Everything a learner sees on the card (search never indexes dialogs)."""
    parts = []
    if card.get("case_grid"):
        for c in card["case_grid"]:
            parts.append(runs_text(c.get("label", [])))
        return " ".join(parts).lower().replace("ё", "е")
    for block in card.get("blocks", []):
        for key in TEXT_ORDER:
            if key in block:
                parts.extend(BLOCKS[key].text(block))
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
        for flag in ("b", "i", "s", "hit"):
            if flag in run and not isinstance(run[flag], bool):
                errors.append(f"{where}[{i}]: .{flag} must be boolean")


class _Checker:
    """Deck-shape checks (blocks, cards, groups) accumulating errors in place."""

    def __init__(self, errors, details, grammar_terms, audience_script):
        self.errors = errors
        self.details = details
        self.grammar_terms = grammar_terms
        self.audience_script = audience_script

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
            BLOCKS[keys[0]].check(block, f"{where}[{i}]", self)

    def check_card(self, card, where):
        if not card.get("search"):
            self.errors.append(f"{where}: search keywords required")
        slug = card.get("id")
        if not slug:
            self.errors.append(f"{where}: card id is required (anchor slug; the page "
                               f"anchor is <section-id>-<card-id>)")
        elif not _SLUG_RE.fullmatch(slug):
            self.errors.append(f"{where}: card id {slug!r} must be 2-32 chars of "
                               f"[a-z0-9-] with no leading/trailing hyphen")
        # Badges (level/kind) are article-card metadata only: case-grid
        # launchers and generated cards never carry them.
        if "level" in card or "kind" in card:
            if card.get("case_grid"):
                self.errors.append(f"{where}: level/kind badges are not supported on case_grid cards")
            else:
                lvl = card.get("level")
                if lvl is not None and lvl not in _LEVELS:
                    self.errors.append(f"{where}: level {lvl!r} must be one of {sorted(_LEVELS)}")
                kind = card.get("kind")
                if kind is not None and (not isinstance(kind, str) or not 1 <= len(kind) <= 40):
                    self.errors.append(f"{where}: kind must be a 1-40 char label")
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
            if self.audience_script and self.audience_script.search(token):
                continue  # searcher's own script (configured per audience): variants expected
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
    chk = _Checker(errors, details, _grammar_terms(site, meta.get("target")),
                   _audience_script(site, meta.get("target"), meta.get("audience")))

    views = deck.get("views", [])
    view_ids = [v.get("id") for v in views]
    if len(views) < 3 or len(views) > 5:
        errors.append("views must have 3-5 items")
    if len(set(view_ids)) != len(view_ids):
        errors.append("view ids are not unique")

    section_ids = []
    card_anchors = []  # <section-id>-<card-id>; slug uniqueness is per-section
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
                if card.get("id"):
                    card_anchors.append(f"{sec['id']}-{card['id']}")
        else:
            for gi, group in enumerate(sec["groups"]):
                chk.check_group(group, f"section {sid!r} group {gi}")
                for card in group.get("cards", []):
                    if card.get("id"):
                        card_anchors.append(f"{sec['id']}-{card['id']}")

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

    all_anchor_ids = [i for i in section_ids if i] + card_anchors
    if len(all_anchor_ids) != len(set(all_anchor_ids)):
        errors.append(f"ids are not unique across sections/practice/help/cards: {all_anchor_ids}")


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
            if a.get("script") is not None and a.get("script") not in _SCRIPTS:
                errors.append(f"site.json targets[{i}].audiences[{j}]: unknown script "
                              f"{a.get('script')!r} (known: {sorted(_SCRIPTS)})")
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
