"""Shell consistency check: the site registry vs the hand-mirrored shells.

The registry (content/decks/site.json) is the source of truth for which
target×audience pairs exist. Two shells mirror it by hand and can drift
silently: the landing page (inline DECKS map + language-card links) and
sw.js (APP_SHELL precache list). check_landing and check_sw compare both
against the registry's live pairs; stdlib only.
"""
import re

_DECKS_RE = re.compile(r"const DECKS = \{([^}]*)\};")
_SHELL_RE = re.compile(r"const APP_SHELL = \[(.*?)\];", re.S)
_AUDS_RE = re.compile(r"['\"]([\w-]+)['\"]")
_SHELL_STRINGS_RE = re.compile(r"['\"]([^'\"]+)['\"]")

_SW_SUFFIXES = ("", "index.html", "manifest.webmanifest",
                "icons/favicon.svg", "icons/icon-192.png", "icons/icon-512.png")


def _live_pairs(site):
    """{target: [audience ids]} for every pair that is live (not «скоро»)."""
    pairs = {}
    for t in site.get("targets", []):
        live = [a["id"] for a in t.get("audiences", []) if not a.get("soon")]
        if live:
            pairs[t["id"]] = live
    return pairs


def check_landing(site, index_path):
    errors = []
    html = index_path.read_text(encoding="utf-8")
    m = _DECKS_RE.search(html)
    if not m:
        return ["landing: inline DECKS map not found in index.html"]
    pairs = {tid: _AUDS_RE.findall(auds)
             for tid, auds in re.findall(r"(\w+):\s*\[([^\]]*)\]", m.group(1))}
    expected = _live_pairs(site)
    if pairs != expected:
        errors.append(f"landing DECKS {pairs} != live registry pairs {expected} "
                      f"(mirror content/decks/site.json into index.html)")
    for t, auds in expected.items():
        for a in auds:
            if f'href="./{t}/{a}/"' not in html:
                errors.append(f"landing: no language-card link to ./{t}/{a}/")
    return errors


def check_sw(site, sw_path):
    errors = []
    m = _SHELL_RE.search(sw_path.read_text(encoding="utf-8"))
    if not m:
        return ["sw.js: APP_SHELL list not found"]
    shell = set(_SHELL_STRINGS_RE.findall(m.group(1)))
    for t, auds in _live_pairs(site).items():
        for a in auds:
            base = f"./{t}/{a}/"
            for suffix in _SW_SUFFIXES:
                if base + suffix not in shell:
                    errors.append(f"sw.js APP_SHELL is missing {base}{suffix}")
    return errors


def check_shell(site, root):
    """Both hand-mirrored shells vs the registry. Returns an error list."""
    errors = []
    errors += check_landing(site, root / "index.html")
    errors += check_sw(site, root / "sw.js")
    return errors
