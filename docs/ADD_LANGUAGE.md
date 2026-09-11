# Playbook: adding a new language cheatsheet

## Responsibility

This playbook owns the repository procedure for adding a language: create its
self-contained folder, implement the accepted plan, connect shared site
surfaces, validate and ship. It does not own language scope, shared UI rules,
content-review rules or deployment policy; it links to those owners.

A deck is the pairing **(target language × audience language)**, e.g.
`de-ru` = German explained in Russian. It lives as
`content/decks/<target>-<audience>.json` and is rendered by
`tools/build_pages.py` into `<target>/<audience>/index.html` (schema:
`content/decks/schema.json`). Everything shared (tokens/contract, sw, tools,
docs) lives at the repo root.

> Both current decks are generated this way (`de/ru/`, `en/ru/`, migrated
> 2026-09-11 from hand-written `deutsch/` / `english/`, which are now redirect
> stubs kept for old URLs and installed PWAs). A new deck is authored as JSON,
> not copied from HTML.

## 0. Establish the content target

Before adapting a page, answer [the SITE_PLAN guide](SITE_PLAN_GUIDE.md) and
prepare the accepted content target. Record stable topic IDs, Russian
learner questions, required depth, view ownership, practice mapping and every
accepted exclusion or deferral with its rationale and reconsideration trigger.

Compare the proposed inventory with named syllabus and grammar references
using [content validation](CONTENT_VALIDATION.md). Sources, unresolved
questions and results go in [CONTENT_AUDIT.md](../CONTENT_AUDIT.md), not in the
plan. Do not treat the copied language page as a coverage template.

## 1. Author the deck and render it

Start from the closest existing deck as a content reference (not a coverage
template — see step 0):

```bash
cp content/decks/de-ru.json content/decks/<target>-<audience>.json
python3 tools/build_pages.py content/decks/<target>-<audience>.json
```

Then, before adapting the deck's content:

- `meta` — set `deck`, `target`, `audience`, `target_lang`, `lang` (the
  audience's ISO code — it becomes `<html lang>`), `out`, `site_path`
  (`<target>/<audience>/`), brand fields, titles and `plan_path`
  (`<target>/<audience>/SITE_PLAN.md`).
- `<target>/<audience>/SITE_PLAN.md` — the accepted target from step 0; copied
  content is not valid for the new deck. Fix its `../../` links.
- `<target>/<audience>/manifest.webmanifest` — name/short_name/description;
  `start_url`/`scope` stay `./`; icons stay `./icons/…`.
- `<target>/<audience>/icons/` — regenerate (step 2).

## 2. Generate icons

```bash
# add the needed letters to FONT in tools/make_icons.py first, then:
python3 tools/make_icons.py --mark IT --out ital
```

Each glyph is a 5×7 bitmap (rows of `X`/`.`). Letters already present:
A, D, E, N, a. The set lands in `<out>/icons/` (32/180/192/512 + maskable) —
use `<target>/<audience>` as `--out`. Edit `icons/favicon.svg` letters by hand
(SVG text — no font needed).

## 3. The shared page contract

Follow [the design system](../.design/DESIGN_SYSTEM.md). The generator
(`tools/build_pages.py`) already provides the shell; the items below are
deck-level integration checks, not a second copy of that contract:

- `meta.lang` = audience language (`<html lang>`), brand mark = target code.
  `meta.site_path` depth drives the `../../` prefix for root assets — don't
  hardcode `../` anywhere.
- Keep `TARGET_LANG` behavior (generator-managed): it sets `lang` attributes
  (screen-reader pronunciation + the serif study voice) on pure-target
  `.example`/`.answer`/`.table-scroll` containers and on bold/italic/
  Cyrillic-free slot fragments.
- Section ids stay lowercase-English slugs; **never reuse another language's
  ids unless the sections match** — anchors are per-page anyway.
- One `details` entry per chip; keys kebab-case; explanation in the audience
  language, target-language terms stay in the target language.
- Every section carries the plan's `view`; bottom-navigation destinations and
  legacy-anchor routing match the plan (a deck may keep `practice` as its own
  nav destination, like `de-ru`, or footer-only, like `en-ru`).
- Every card gets `search` with audience-language + target-language keywords.
- Register `'../../sw.js'`; manifest `./manifest.webmanifest`; og:url/og:image
  absolute: `https://andkirby.github.io/learn-language-cheat-sheet/<target>/<audience>/…`.
- Practice implements the plan's topic mapping; the generator wires `.reveal`,
  `aria-expanded` and `aria-controls`. Review all answers; learner exercises
  do not replace validation of every rule, table and example.

## 4. Wire into the site

1. Root `sw.js`: add `'./<target>/<audience>/'`, `…/index.html`,
   `…/manifest.webmanifest` and its icons to `APP_SHELL`;
   **bump `CACHE_VERSION`**.
2. `content/decks/site.json`: add the audience to the target's entry (drop
   `"soon"` when its deck ships) — the header language menu on every deck
   page regenerates from it. If your target language has grammar terminology
   that belongs in `data-search` without appearing on a card (the Russian
   equivalent is shown instead), add those terms to the target's
   `grammar_terms` — the build gate flags any search token that names
   content the card does not show; searcher-script words (Cyrillic etc.)
   and inflections are matched automatically.
3. Landing `index.html`: mirror the registry change — `DECKS`, the
   `.lang-menu` «Язык обучения»/«Язык объяснений» markup — and, for a new
   target, add a `.lang-card` (mark, name, topics, meta, `→`,
   `data-target`). A new audience for an existing target usually needs no
   new card.
4. `README.md`: add the URL row.

## 5. Verify (same gates as existing pages)

Complete [content validation](CONTENT_VALIDATION.md) and record the reviewed
revision, references and all four gate results in
[CONTENT_AUDIT.md](../CONTENT_AUDIT.md). A new language needs a full review.
Then run the separate runtime checks:

```bash
python3 -m http.server 8931
```

- Console clean at `http://127.0.0.1:8931/<target>/<audience>/`; manifest + icons resolve.
- 390px: no horizontal page overflow; tables scroll inside `.table-scroll`.
- Theme toggle cycles auto/light/dark and survives reload.
- Search filters/restores across all views; dialogs open/close (×, Escape,
  backdrop); practice reveal works.
- View switching: each nav tap shows its view (active item =
  `aria-current`); a legacy anchor like `#preps` opens the right view and
  scrolls to the section; tapping a nav item clears an active search.
- Offline reload works after first visit.

## 6. Ship

Commit (`feat: add <language> cheatsheet` / `feat: add <audience> deck`),
push to `main`; GitHub Pages deploys automatically. Verify
`https://andkirby.github.io/learn-language-cheat-sheet/<target>/<audience>/`
returns 200 (first build can lag a minute), then from the landing page with
the audience selected.

## Ownership after shipping

- A change that affects **all** languages (tokens, components, sw behavior)
  goes through `.design/decisions.md` and is applied to every page in the
  same commit.
- Accepted language-specific scope and exclusions stay in that language's
  `SITE_PLAN.md`. Open questions and review evidence stay in
  `CONTENT_AUDIT.md`.
