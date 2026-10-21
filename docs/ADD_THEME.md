# Add a design skin (a theme)

## Responsibility

This playbook owns the repository procedure for adding a selectable design
skin («Оформление»), using skin A «Тетрадь» (2026-10-11, commit `43e1448`)
as the reference implementation. It does not own the skin contract —
`.design/DESIGN_SYSTEM.md` §Skins owns that; fonts are owned by
`docs/FONTS.md`; the *why* of accepted decisions lives in
`.design/decisions.md`. A skin changes look, never content or behavior:
same markup, same anchors, same dialogs, same noscript story.

## Concepts

A **skin** is one attribute plus one stylesheet:

- `data-skin="<id>"` on `<html>` (static default `a` = Notebook; JS removes
  it for a saved Classic choice before stylesheets load). Without the
  attribute, classic stays byte-identical — the scoping gate enforces it.
- `assets/skin-<id>.css`, linked after `base.css` on every page. Tokens
  first, structure second:
  - **token layer** — three blocks mirroring base.css
    (`[data-skin="<id>"]` / auto-dark / manual-dark) re-point the semantic
    tokens. This alone re-skins everything that consumes tokens — including
    the layout lab. Mode-invariant tokens (`--radius`, `--shadow`, fonts)
    live only in the light block.
  - **structural layer** — the theme's identity: what tokens can't say
    (boxes → ink rules, pills → underlined links, fills → accent text).
    This layer is per-theme by design; it is the only non-reusable part.

Skin × theme (авто/светлая/тёмная) composes from the two attributes alone:
the skin's dark blocks tie-and-trail base's dark blocks and out-specify its
own light block. See the cascade note in `skin-a.css`'s header.

## Prerequisites

- The design exists as a **token set with light + dark values** (the .pen
  mockups' `tA-*`/`tB-*` themed variables are the precedent), not just
  screens. Extract values mechanically from the design file.
- Every text-bearing token pair passes ≥ 4.5:1 on its paper in both modes
  (derived status colors — ok/warn families — are usually not in the design
  file; derive them in the theme's hue family and contrast-check them).

## Steps

| Step | Result |
| --- | --- |
| [0. Tokens](#0-tokens) | Verified light+dark token table |
| [1. Stylesheet](#1-stylesheet) | `assets/skin-<id>.css` (gates green) |
| [2. Strings + plumbing](#2-strings--plumbing) | Schema, validator, decks, switcher rows |
| [3. Mirrors](#3-mirrors) | Template, landing, style guide |
| [4. Ship](#4-ship) | sw bump, docs, regenerated pages, verification |

### 0. Tokens

List every semantic token from `DESIGN_SYSTEM.md`'s token table with the
skin's light/dark value (paper/ink/muted/line/accent + accent-soft/
on-accent/tap-line + ok/warn families + radius/shadow/grab/backdrop +
`--font-ui`/`--font-study` + the landing `--hero-*` set). Skins that need
webfonts vendor them first — `docs/FONTS.md` — and put `@font-face` at the
top of the skin stylesheet (browsers fetch declared-but-unused fonts never,
so classic pays nothing).

### 1. Stylesheet

Create `assets/skin-<id>.css` in this order: header comment (contract
pointer, cascade explanation, gate) → `@font-face` → three token blocks →
structural rules, each group under a short comment. Every rule starts with
`[data-skin="<id>"]` (no `:root` prefix — ties with base are won by load
order, everything else by specificity). Structural rules should *remove*
base chrome (backgrounds, borders, radii, shadows) and *add* the theme's
marks (ink rules, underlines, counters). Two traps from A: over-sized fixed
boxes break on real content — size to content (`min-width` + padding), not
to a mockup square; and glyphs living in line boxes need `line-height: 0`
or they paint past their box.

Gates (must be empty / zero):

```bash
grep -E '\{' assets/skin-<id>.css | grep -vE '(@font-face|@media|@keyframes|\[data-skin="<id>"])'
python3 -c "s=open('assets/skin-<id>.css').read(); print(s.count('{')-s.count('}'))"
```

### 2. Strings + plumbing

- Decks: add the option label string (`skin_a` is the precedent; a second
  skin adds `skin_b`, etc.) to all four deck JSONs + `schema.json`
  (`definitions.strings.properties`, never `required`) + the validator's
  required tuple (`tools/deck_validate.py`).
- `tools/deck_render.py` `_skin_group_html`: add the option row
  (`data-skin-mode="<id>"`). **Generalize the hardcodes** — the reference
  implementation has these hardcodes to generalize for the next skin:
  1. static HTML and server-rendered radio rows default to `a`; the early
     head script removes the attribute only for stored `classic`, while
     the bottom script accepts `classic` and otherwise defaults to `a`
     (extend both scripts to accept any known non-classic stored value),
  2. the bottom-script `order` array is `['classic', 'a']`,
  3. `applySkin`'s meta-sync branch tests `'a'`.
- Switcher mechanics (radiogroup, roving tabindex, arrows, close-on-select,
  persistence in `localStorage.skin`, noscript = Notebook) are contract —
  reuse, don't reinvent. `.design/DESIGN_SYSTEM.md` documents them.

### 3. Mirrors

Every page-level change is made in one commit on **all** surfaces:

- `tools/page_template.html` — stylesheet link after base.css, generalized
  early script; the skin JS lives in the template once.
- `index.html` — hand-mirror: link, early script, the option row in the
  «Оформление» group, its own skin-JS copy (the landing keeps its own theme
  code; adapt names, don't assume).
- `style-guide.html` — link + early script + option row + a row in the
  `#skins` specimen token table. The honest specimen is the page itself.

### 4. Ship

1. `sw.js`: `APP_SHELL` += the skin stylesheet (+ any new font files —
   licenses stay runtime-cached), then bump `CACHE_VERSION` **once, after
   all asset edits** (shell check fails on missing files; a bump while
   assets still change strands installed visitors on the old cache).
2. Docs: `DESIGN_SYSTEM.md` (skin section + components row if new classes),
   `.design/decisions.md` entry, `CHANGELOG.md`, this file's reference
   implementation pointer if useful.
3. Regenerate: `python3 tools/build_pages.py content/decks/<deck>.json` ×4,
   then `--check` ×4 + `--check-shell` — all green.
4. Verification matrix (condensed from A's):
   - fresh, unavailable or invalid storage defaults to Notebook; an explicit
     saved Classic choice remains Classic before first paint;
   - switch both directions in menu + burger; persists across reload and
     across pages; classic restored exactly (attribute gone, system fonts,
     classic tokens, metas back to defaults);
   - identity: paper/bg, `--font-ui` on body, `--font-study` on `[lang]`,
     the theme's structural marks;
   - 2×2 skin × theme via the untouched ◐ button; `theme-color` metas ==
     computed `--bg` in **all four cells** (the auto cell is the one that
     regresses — see `applySkin`'s meta note);
   - 390px: no horizontal overflow; every deck's nav tokens fit their cue
     tags (**check the deck with the most/widest nav icons** — A shipped
     with a fixed box that fit DE's `V2` and clipped `A/D`/`weil`);
   - keyboard: roving tabindex, arrows, `aria-checked`; noscript: rows
     hidden, Notebook; offline: new assets present in the fresh cache;
   - screenshots (light + dark) for human review — numeric checks pass
     cramped-but-not-clipped layouts; eyes catch them.
