"""HTML/JS string primitives for the deck→page generator. Stdlib only.

How deck text becomes markup: escaping helpers plus run payloads
(strings / {t, b, i, s, br} objects) rendered to HTML. Shared by the
block registry (deck_blocks) and the page renderer (deck_render);
imported via the tools/ directory when build_pages.py runs.
"""
import html
import json


def esc(s):
    return html.escape(s, quote=False)


def escq(s):
    return html.escape(s, quote=True)


def js(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


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
    if run.get("hit"):
        # hit implies bold: the .hit class carries the highlight + weight
        inner = f'<b class="hit">{inner}</b>'
    elif run.get("b"):
        inner = f"<b>{inner}</b>"
    return inner


def runs_html(runs):
    return "".join(run_html(r) for r in runs)


def runs_or_string_html(v):
    return esc(v) if isinstance(v, str) else runs_html(v)
