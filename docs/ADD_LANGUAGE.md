# Playbook: adding a new language cheatsheet

How to turn this repo from {Deutsch, English} into {…, Italian, Español, …}
while keeping one design system, one service worker, and a stable site.

A language page is **self-contained**: one folder with the page, its manifest,
its icons, and its plan. Everything shared (tokens/contract, sw, tools, docs)
lives at the repo root. Target effort for a new language: one working session.

## 0. Decide scope first (before any file)

Write `Sitemap thinking` into the new `SITE_PLAN.md` **before** the page:
- Primary use cases (5–7 questions a learner asks).
- Section list (~8 sections + practice + install help; see below).
- What is *hard for a Russian speaker specifically* in this language —
  those traps get first-class cards (like артикли/предлоги for English,
  падежи/рамка for German). Search the web only if you are unsure about
  frequency-of-use or a rule you can't verify.

Default section skeleton (adapt, don't force):
1. The #1 pain (cases / articles / phonology)
2. Core reference tables (pronouns/articles/…)
3. Word order & questions
4. Tense/verb system
5. Verb constructions
6. Prepositions/particles
7. Word morphology (plurals, agreement, comparison)
8. One high-value advanced topic (conditionals / subordinate clauses)
9. Practice (3 items) · 10. Install help

## 1. Create the folder (copy as starting point)

```bash
cp -r english <lang>          # or deutsch — pick the closer grammar cousin
```

Then in `<lang>/`:
- `SITE_PLAN.md` — rewrite per step 0.
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

## 3. Page contract (what must stay identical)

From `.design/DESIGN_SYSTEM.md` — all of it: token blocks (light + dark +
manual-dark), components, focus ring, 44px targets, dialog behavior,
`body.searching`, noscript/print styles, reduced-motion.
Mechanical checklist for the copy:
- `<html lang="ru">` (UI language stays Russian), brand mark = language code.
- Section ids stay lowercase-English slugs; **never reuse another language's
  ids unless the sections match** — anchors are per-page anyway.
- `DETAILS` object: one entry per chip; keys kebab-case; RU explanation +
  DE/EN/… terms kept in the target language.
- `NAV_MAP` covers every section id (map to nearest nav concept or `null`).
- Every `.cheat-card` gets `data-search` with RU + target-language keywords.
- Register `../sw.js`; manifest `./manifest.webmanifest`; og:url/og:image
  absolute: `https://andkirby.github.io/learn-language-cheat-sheet/<lang>/…`.
- Practice: 3 items with `.reveal` + `aria-expanded` + `aria-controls`.

## 4. Wire into the site

1. Root `sw.js`: add `'./<lang>/'`, `'./<lang>/index.html'`,
   `'./<lang>/manifest.webmanifest'` and its icons to `APP_SHELL`;
   **bump `CACHE_VERSION`**.
2. Landing `index.html`: add a `.lang-card` (mark, name, topics, meta, `→`)
   pointing to `./<lang>/`.
3. `README.md`: add the URL row.

## 5. Verify (same gates as existing pages)

```bash
python3 -m http.server 8931
```
- Console clean at `http://127.0.0.1:8931/<lang>/`; manifest + icons resolve.
- 390px: no horizontal page overflow; tables scroll inside `.table-scroll`.
- Theme toggle cycles auto/light/dark and survives reload.
- Search filters/restores; dialogs open/close (×, Escape, backdrop);
  practice reveal works; bottom-nav highlight matches sections.
- Offline reload works after first visit.

## 6. Ship

Commit (`feat: add <language> cheatsheet`), push to `main`; GitHub Pages
deploys automatically. Verify
`https://andkirby.github.io/learn-language-cheat-sheet/<lang>/` returns 200
(first build can lag a minute), then from the landing page.

## Governance

- A change that affects **all** languages (tokens, components, sw behavior)
  goes through `.design/decisions.md` and is applied to every page in the
  same commit.
- A change that affects **one** language stays in that language's folder +
  its `SITE_PLAN.md`.
