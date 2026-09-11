# AGENTS.md

## Responsibility

This file is the coding-agent entrypoint. It owns repository-wide operating
rules, documentation routing, maintenance triggers and verification commands.
It does not own language content or shared UI details.

Multi-language PWA cheatsheet hub: German and English grammar for
Russian-speaking learners (A1–B1). Static site on GitHub Pages — no build
step, no external dependencies, everything works offline.

## Structure

```text
index.html          landing (language cards + audience-locale selector)
assets/base.css     shared stylesheet: tokens + components (specimens: style-guide.html)
style-guide.html    living component specimens + class roles (noindex, not cached)
content/decks/      deck data + schema.json + site.json (language registry) — the source of generated pages
de/ru/              German-for-Russians page: GENERATED from content/decks/de-ru.json
en/ru/              English-for-Russians page: GENERATED from content/decks/en-ru.json
deutsch/, english/  redirect stubs to ./de/ru/, ./en/ru/ (kept for old URLs and installs)
de/                 default stub → ./ru/
sw.js               shared service worker (root scope, all languages)
icons/              landing favicon + og image
tools/make_icons.py icon generator (stdlib only)
tools/build_pages.py deck→page generator + validator (stdlib only)
docs/               authoring, validation and add-language procedures
research/           external reference research notes (not content source)
CONTENT_AUDIT.md    content evidence, open questions and verdicts
UI_AUDIT.md         UI review evidence and open findings
DEBT.md             deferred work with owners and triggers
CHANGELOG.md        user-visible changes, newest first
```

Deck pages live at `<target>/<audience>/` (`de/ru/`, later `de/en/`…) so sibling
audiences share a target. Every page's header shows one combined language
menu («Язык обучения» + «Язык объяснений») driven by `content/decks/site.json`
on deck pages and mirrored by hand in `index.html` (DECKS + the menu markup) —
update both when adding a language or audience.

## Source-of-truth map

| Question | Read this first |
| --- | --- |
| How to add a new language | `docs/ADD_LANGUAGE.md` |
| How to author or revise a language plan | `docs/SITE_PLAN_GUIDE.md` |
| Accepted language scope, exclusions and topic inventory | `de/ru/SITE_PLAN.md` / `en/ru/SITE_PLAN.md` |
| How content is validated | `docs/CONTENT_VALIDATION.md` |
| Open content questions, review evidence and verdicts | `CONTENT_AUDIT.md` |
| External reference research (DE/EN grammar sites, tense-usage notes) | `research/` |
| Design tokens, components, a11y rules | `.design/DESIGN_SYSTEM.md` |
| Component specimens and class roles | `style-guide.html` |
| Why a UI decision was made | `.design/decisions.md` |
| UI review evidence and open/deferred findings | `UI_AUDIT.md` |
| Deployment / GitHub Pages | `README.md` |
| Deliberately deferred work | `DEBT.md` |
| What changed, newest first | `CHANGELOG.md` |

## Hard rules

1. Each language is **self-contained** in its folder; shared things live at
   the root. Don't cross-reference assets between language folders.
2. A language's `SITE_PLAN.md` contains accepted decisions only. Record
   Required, Deferred and Excluded scope explicitly; keep unresolved questions
   in `CONTENT_AUDIT.md`.
3. Update the language plan **before** its page when accepted scope, coverage,
   content depth, practice mapping or language-specific interaction changes.
4. All asset paths relative (`./…`, `../sw.js`) — the site lives at a GitHub
   Pages subpath.
5. No build tools, frameworks, fonts, or CDNs. Exception since 2026-09-11:
   **commit-time generation by vendored stdlib scripts is allowed** (the
   `make_icons.py` precedent). Deck pages (`de/ru/`, `en/ru/`) are edited via
   their deck JSON in `content/decks/` and regenerated with
   `python3 tools/build_pages.py <deck>`; the committed HTML is what deploys.
6. Colors only via semantic tokens (light **and** dark + manual-dark blocks)
   — see `.design/DESIGN_SYSTEM.md`. Theme toggle is part of the contract.
7. Keep section anchor ids stable within a language.
8. New tappable explanations go into that page's `DETAILS` object; cards stay
   concise, depth goes in dialogs.
9. After changing any page or asset: bump `CACHE_VERSION` in the root `sw.js`
   and add any new shell URLs to its `APP_SHELL`.
10. A UI change that touches the shared contract is applied to **every**
   language page in the same commit and logged in `.design/decisions.md`.

## Documentation stewardship

- Treat language plans as accepted targets, page/runtime observations as
  implementation evidence, and audit findings as open until resolved.
- Update an existing owner when an authorized change would make it false.
- Prefer one canonical owner plus links; do not copy shared contracts or
  review results into language plans.
- Create a new owner only for durable knowledge with a distinct responsibility,
  a named maintenance trigger and a link from this file.
- When an open content question is accepted, promote the decision to the
  relevant `SITE_PLAN.md` and update its audit finding without erasing history.

## Verify before declaring done

For grammar/content changes and new languages, follow
[content validation](docs/CONTENT_VALIDATION.md) and record results in
[CONTENT_AUDIT.md](CONTENT_AUDIT.md). Page quality requires its content gates
to pass; the runtime checklist below does not validate grammar. Restricted
reviews must label unperformed checks NOT RUN.

```bash
python3 -m http.server 8931   # open http://127.0.0.1:8931/
```

- Landing loads, language cards link to `./de/ru/`, `./en/ru/`; the locale
  selector persists its choice and only offers audiences that exist.
- Old URLs redirect: `/deutsch/` → `/de/ru/`, `/english/` → `/en/ru/`,
  `/de/` → `/de/ru/`, `/deutsch.html` → `/de/ru/` (online and offline).
- Generated pages match their decks: `python3 tools/build_pages.py
  content/decks/de-ru.json --check` (and `en-ru.json`) exits 0.
- No console errors on any page; manifests, icons, `sw.js` resolve.
- At ~390px: no horizontal page overflow; tables scroll inside `.table-scroll`.
- Theme toggle cycles авто → светлая → тёмная and persists across
  reload.
- Bottom nav switches views (active item carries `aria-current`); legacy
  anchors (`#preps` on DE, `#nouns`/`#conditionals` on EN) open the right
  view and scroll to the section.
- Search filters cards across all views and restores the active view on
  clear; dialogs close via ×, Escape, backdrop; practice reveal works.
- Offline reload works after first load.
- Live check after push:
  `https://andkirby.github.io/learn-language-cheat-sheet/`
  (+ `/de/ru/`, `/en/ru/`; `/deutsch/`, `/english/`, `/de/`,
  `/deutsch.html` redirect).

## Regenerating icons

```bash
python3 tools/make_icons.py                    # all sets (Aa, DE, EN)
python3 tools/make_icons.py --mark IT --out ital   # new language (see docs/)
```

Then bump `CACHE_VERSION` in `sw.js`.
