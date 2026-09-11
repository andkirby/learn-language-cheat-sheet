# Playbook: adding a new language cheatsheet

## Responsibility

This playbook owns the repository procedure for adding a language: create its
self-contained folder, implement the accepted plan, connect shared site
surfaces, validate and ship. It does not own language scope, shared UI rules,
content-review rules or deployment policy; it links to those owners.

A language page is **self-contained**: one folder with the page, its manifest,
its icons, and its plan. Everything shared (tokens/contract, sw, tools, docs)
lives at the repo root.

## 0. Establish the content target

Before adapting a page, answer [the SITE_PLAN guide](SITE_PLAN_GUIDE.md) and
prepare the accepted content target. Record stable topic IDs, Russian
learner questions, required depth, view ownership, practice mapping and every
accepted exclusion or deferral with its rationale and reconsideration trigger.

Compare the proposed inventory with named syllabus and grammar references
using [content validation](CONTENT_VALIDATION.md). Sources, unresolved
questions and results go in [CONTENT_AUDIT.md](../CONTENT_AUDIT.md), not in the
plan. Do not treat the copied language page as a coverage template.

## 1. Create the folder (copy as starting point)

```bash
cp -r english <lang>          # or deutsch — pick the closer grammar cousin
```

Then in `<lang>/`, before adapting `index.html`:

- `SITE_PLAN.md` — replace it with the accepted target from step 0; copied
  content is not valid for the new language.
- `index.html` — replace content per the contract below.
- `manifest.webmanifest` — name/short_name/description; `start_url`/`scope`
  stay `./`; icons stay `./icons/…`.
- `icons/` — regenerate (step 2); favicon.svg letters.

## 2. Generate icons

```bash
# add the needed letters to FONT in tools/make_icons.py first, then:
python3 tools/make_icons.py --mark IT --out ital
```

Each glyph is a 5×7 bitmap (rows of `X`/`.`). Letters already present:
A, D, E, N, a. The set lands in `<out>/icons/` (32/180/192/512 + maskable).
Edit `<lang>/icons/favicon.svg` letters by hand (SVG text — no font needed).

## 3. Implement the shared page contract

Follow [the design system](../.design/DESIGN_SYSTEM.md). The items below are
integration checks, not a second copy of that contract:

- `<html lang="ru">` (UI language stays Russian), brand mark = language code.
- Link `../assets/base.css` — never copy component styles into the page.
  Page-specific styles (if truly needed) go in a small local `<style>` block.
- Set `TARGET_LANG` and keep `markTargetLang` intact: it sets `lang`
  attributes (screen-reader pronunciation + the serif study voice) on
  pure-target `.example`/`.answer`/`.table-scroll` containers and on bold /
  italic / Cyrillic-free slot fragments.
- Section ids stay lowercase-English slugs; **never reuse another language's
  ids unless the sections match** — anchors are per-page anyway.
- `DETAILS` object: one entry per chip; keys kebab-case; RU explanation +
  DE/EN/… terms kept in the target language.
- Every section carries the plan's `data-view="<view-id>"`; bottom-navigation
  destinations and legacy-anchor routing match the plan.
- Every `.cheat-card` gets `data-search` with RU + target-language keywords.
- Register `../sw.js`; manifest `./manifest.webmanifest`; og:url/og:image
  absolute: `https://andkirby.github.io/learn-language-cheat-sheet/<lang>/…`.
- Practice implements the plan's topic mapping with `.reveal`,
  `aria-expanded` and `aria-controls`. Review all answers; learner exercises
  do not replace validation of every rule, table and example.

## 4. Wire into the site

1. Root `sw.js`: add `'./<lang>/'`, `'./<lang>/index.html'`,
   `'./<lang>/manifest.webmanifest'` and its icons to `APP_SHELL`;
   **bump `CACHE_VERSION`**.
2. Landing `index.html`: add a `.lang-card` (mark, name, topics, meta, `→`)
   pointing to `./<lang>/`.
3. `README.md`: add the URL row.

## 5. Verify (same gates as existing pages)

Complete [content validation](CONTENT_VALIDATION.md) and record the reviewed
revision, references and all four gate results in
[CONTENT_AUDIT.md](../CONTENT_AUDIT.md). A new language needs a full review.
Then run the separate runtime checks:

```bash
python3 -m http.server 8931
```

- Console clean at `http://127.0.0.1:8931/<lang>/`; manifest + icons resolve.
- 390px: no horizontal page overflow; tables scroll inside `.table-scroll`.
- Theme toggle cycles auto/light/dark and survives reload.
- Search filters/restores across all views; dialogs open/close (×, Escape,
  backdrop); practice reveal works.
- View switching: each nav tap shows its view (active item =
  `aria-current`); a legacy anchor like `#preps` opens the right view and
  scrolls to the section; tapping a nav item clears an active search.
- Offline reload works after first visit.

## 6. Ship

Commit (`feat: add <language> cheatsheet`), push to `main`; GitHub Pages
deploys automatically. Verify
`https://andkirby.github.io/learn-language-cheat-sheet/<lang>/` returns 200
(first build can lag a minute), then from the landing page.

## Ownership after shipping

- A change that affects **all** languages (tokens, components, sw behavior)
  goes through `.design/decisions.md` and is applied to every page in the
  same commit.
- Accepted language-specific scope and exclusions stay in that language's
  `SITE_PLAN.md`. Open questions and review evidence stay in
  `CONTENT_AUDIT.md`.
