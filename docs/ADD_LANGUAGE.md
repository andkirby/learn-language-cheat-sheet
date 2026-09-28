# Add a language or audience variant

## Responsibility

This playbook owns the repository procedure for adding a language or an
audience variant (a new deck): create its self-contained folder, implement
the accepted plan, connect shared site surfaces, validate and ship. It does
not own language scope, shared UI rules, content-review rules or deployment
policy; it links to those owners.

A deck is the pairing **(target language × audience language)**, e.g.
`de-ru` = German explained in Russian. It lives as
`content/decks/<target>-<audience>.json` and is rendered by
`tools/build_pages.py` into `<target>/<audience>/index.html` (schema:
`content/decks/schema.json`). Everything shared (tokens/contract, sw, tools,
docs) lives at the repo root.

Author a new deck in JSON; never copy or edit generated HTML.

## Find your route

| Task | Start with | Extra decision |
| --- | --- | --- |
| New target language | [Plan the content](#0-establish-the-content-target) | Define its topic inventory and learner boundary. |
| New audience for an existing target | [Audience variants](#audience-variants-translating-an-existing-target) | Re-scope the existing inventory for that audience. |

| Step | Result |
| --- | --- |
| [0. Plan](#0-establish-the-content-target) | Accepted `<target>/<audience>/SITE_PLAN.md` |
| [1. Author](#1-author-the-deck) | Adapted deck JSON |
| [2. Icons](#2-generate-icons) | Pair-specific PWA icons |
| [3. Page contract](#3-the-shared-page-contract) | Deck-level UI checks |
| [4. Connect](#4-wire-into-the-site) | Registry, landing, service worker and generated pages |
| [5. Verify](#5-verify-same-gates-as-existing-pages) | Content evidence, build checks and runtime checks |
| [6. Ship](#6-ship) | Deployed page and live check |

## Principles (every deck, every pair)

The target supplies grammar facts; the audience supplies the pedagogy. These
rules define what "translation" means here:

- **Adapt, don't translate.** The deck is organized by first-language
  interference, not by grammar logistics: the same topic gets a different
  lead, different contrasts and different predicted errors per audience
  (German cases = mapping onto the Russian case system in `de-ru`; building
  the concept from the I/me remnant in a `de-en` deck). A monolingual
  native-speaker reference (`de-de`, `en-en`) is **not** a master source —
  it organizes by form, overlaps ~40%, and self-pairs are out of product
  scope. Source model and the 5-language cross-product: [ROADMAP.md](../ROADMAP.md).
- **Plan first.** The audience gets its own `SITE_PLAN.md` (step 0) before
  any deck JSON exists: topic inventory, retrieval questions, accepted
  depth, exclusions — re-derived for the new audience, not copied.
- **The audience language is the explanation language.** UI strings,
  dialogs, glosses and search hints are written in the audience language;
  target-language terms stay in the target language. The gloss contract
  lives in each language plan's content contract.
- **Bounded units.** One card + one dialog per topic; the simplification
  limit is stated on the card; practice maps to plan topics. The standing
  scope rules in [ROADMAP.md](../ROADMAP.md) decide what may be added
  without asking the owner.
- **The gates are the contract.** `--check` (page↔deck drift + search
  hygiene), `--check-shell` (landing + sw vs the registry) and content
  validation decide acceptance; the generated page is committed, never
  hand-edited.

## Audience variants (translating an existing target)

When the target language already has a deck (e.g. `de-ru` exists, adding
`de-en`), follow steps 0–6 with these differences:

1. **Re-scope, don't re-cover.** Start from the target's existing
   `SITE_PLAN` inventory as the skeleton and re-derive every acceptance
   decision for the new audience: what is obvious there, what is a trap
   there, which examples carry the point. A section/topic missing a reason
   to exist for this audience is a deferral candidate, not filler.
2. **Second audience of a target = core-extraction trigger.** Per the
   source model ([ROADMAP.md](../ROADMAP.md)), when the second audience of
   a target ships, extract the per-target invariant core (paradigm tables,
   canonical examples) shared by the paired decks instead of duplicating
   it — the boundary is cut from the real pair, not speculated.
3. **Adapt the content and navigation.** Author `strings`, dialogs, glosses
   and practice in the audience language. Reuse the generated shell and block
   types; let the new plan decide its views and sections. Card `id` slugs are
   per-page (hard rule 7) — keep them stable after shipping.
4. **Search hints are audience words.** A Latin-script audience has no
   script exemption (strict mode): every `data-search` token must be
   card-visible or registered in the target's `grammar_terms`. Intent
   words of the previous audience disappear entirely.
5. **Code prerequisite for Latin×Latin pairs.** The page's target-language
   tagging (`markTargetLang` in `tools/page_template.html`) treats every
   non-Cyrillic fragment as target-language text. On a `de-en` page that
   can tag English explanation fragments as German. Generalize it to
   per-audience script — the same mechanism as the validator's `"script"`
   key — before the first Latin×Latin pair ships.

An audience variant is a new deck: run the full content review in step 5.

## 0. Establish the content target

Before adapting a page, answer [the SITE_PLAN guide](SITE_PLAN_GUIDE.md) and
prepare the accepted content target. Record stable topic IDs,
audience-language learner questions, required depth, view ownership,
practice mapping and every accepted exclusion or deferral with its
rationale and reconsideration trigger.

Compare the proposed inventory with named syllabus and grammar references
using [content validation](CONTENT_VALIDATION.md). Sources, unresolved
questions and results go in [CONTENT_AUDIT.md](../CONTENT_AUDIT.md), not in the
plan. Do not treat the copied language page as a coverage template.

## 1. Author the deck

Copy the closest existing deck as a content reference (not a coverage
template — see step 0). This example starts `de-en`; choose the filename for
your pair. Adapt it before rendering; the new pair must also be live in the
registry (step 4) for validation to pass.

```bash
cp content/decks/de-ru.json content/decks/de-en.json
```

Before adapting the deck's content, set up:

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
# Example: Italian for Russian speakers. Add missing letters to FONT first.
python3 tools/make_icons.py --mark IT --out it/ru
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
  `.example`/`.answer`/`.table-scroll`/`.pair-src` containers and on bold/italic/
  Cyrillic-free slot fragments; pair glosses stay in the UI voice.
- Section ids stay lowercase-English slugs; **never reuse another language's
  ids unless the sections match** — anchors are per-page anyway.
- One `details` entry per chip; keys kebab-case; explanation in the audience
  language, target-language terms stay in the target language.
- Every section carries the plan's `view`; bottom-navigation destinations and
  legacy-anchor routing match the plan (a deck may keep `practice` as its own
  nav destination, like `de-ru`, or footer-only, like `en-ru`).
- Every card gets `search` with audience-language + target-language keywords
  and an `id` — a short latin grammar-term slug (`[a-z0-9-]`, 2–32 chars; no
  Cyrillic, which percent-encodes into unreadable URLs). The generator
  assembles the page anchor `<section-id>-<id>`; the build gate enforces
  charset and global uniqueness. Card ids are stable forever: renaming one
  breaks every shared link to that card.
- Register `'../../sw.js'`; manifest `./manifest.webmanifest`; og:url/og:image
  absolute: `https://andkirby.github.io/learn-language-cheat-sheet/<target>/<audience>/…`.
- Practice implements the plan's topic mapping; the generator wires `.reveal`,
  `aria-expanded` and `aria-controls`. Review all answers; learner exercises
  do not replace validation of every rule, table and example.

## 4. Wire into the site

Make the pair live in the registry before rendering it. The validator rejects
an unregistered pair or one still marked `"soon"`.

1. `content/decks/site.json`: add the audience to the target's entry (drop
   `"soon"` when its deck ships) — the header language menu on every deck
   page regenerates from it. Set the audience's `"script"` (e.g. `"cyrillic"`
   for Russian; omit for Latin-script audiences — absent key means strict,
   every search token must be on the card or in `grammar_terms`). If your
   target language has grammar terminology that belongs in `data-search`
   without appearing on a card, add those terms to the target's
   `grammar_terms` — the build gate flags any search token that names
   content the card does not show; searcher-script words (per the
   audience's `"script"`) and inflections are matched automatically.
2. Landing `index.html`: mirror the registry change — `DECKS`, the
   `.lang-menu` «Язык обучения»/«Язык объяснений» markup — and, for a new
   target, add a `.lang-card` (mark, name, topics, meta, `→`,
   `data-target`). A new audience for an existing target usually needs no
   new card.
3. Root `sw.js`: add `'./<target>/<audience>/'`, `…/index.html`,
   `…/manifest.webmanifest` and its icons to `APP_SHELL`;
   **bump `CACHE_VERSION`**.
4. `README.md`: add the URL row.

Render **every** deck after changing `site.json`: every generated header menu
reads that registry, including those on existing pages.

```bash
for deck in content/decks/de-*.json content/decks/en-*.json; do
  python3 tools/build_pages.py "$deck"
  python3 tools/build_pages.py "$deck" --check || exit 1
done
python3 tools/build_pages.py content/decks/de-ru.json --check-shell
```

## 5. Verify (same gates as existing pages)

Complete [content validation](CONTENT_VALIDATION.md) and record the reviewed
revision, references and all four gate results in
[CONTENT_AUDIT.md](../CONTENT_AUDIT.md). A new language needs a full review.
Check the generated pages and the hand-maintained shells, then run the
separate runtime checks:

```bash
for deck in content/decks/*.json; do
  python3 tools/build_pages.py "$deck" --check
done
python3 tools/build_pages.py content/decks/de-ru.json --check-shell
python3 -m http.server 8931
```

- Landing cards and language menus reach the right pair; audience selection
  persists and only offers live audiences.
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
