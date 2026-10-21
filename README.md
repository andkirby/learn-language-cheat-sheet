# Language Cheat Sheets — языковые шпаргалки

## Responsibility

This README is the human front door. It owns project orientation, the shortest
local run path, repository layout and deployment notes. Language scope,
shared UI contracts and audit evidence belong to the documents linked below.

Mobile-first German and English grammar cheatsheets for A1–B1 learners,
with explanations in Russian, English or German depending on the pair.
Installable as PWAs and fully offline after first load. Examples include
translations; taught words and forms include contextual meaning clues.

The [content audit](CONTENT_AUDIT.md) owns current review results and remaining
syllabus/level-placement gaps.

Live: <https://andkirby.github.io/learn-language-cheat-sheet/>

Deck pages live at `<target>/<audience>/`; the landing locale selector picks
the audience (Русский, English or Deutsch today). The landing text follows
that choice and shows only learning targets with an available audience deck:
Russian → German / English, English → German, German → English. It stays at
`/` when the explanation language changes.

On first visit, the first supported browser language is used (regional tags
such as `de-DE` match `de`); no match falls back to Russian. A manual selection
wins on later visits. Only explicit choices are saved in `landingLocale`;
legacy English/German `locale` values migrate, while old Russian values are
ignored because previous visits also saved Russian automatically. Deck URLs,
legacy redirects and installed deck start pages keep their explicit language.
Without JavaScript, the Russian landing and direct deck links remain usable.

| URL | What |
| --- | --- |
| `/` | Landing — locale selector + language cards |
| `/de/ru/` | Немецкий: падежи, артикли, порядок слов, придаточные |
| `/en/ru/` | Английский: времена, артикли, вопросы, условные |
| `/de/en/` | German explained in English: cases, articles, word order, clauses |
| `/en/de/` | Englisch erklärt auf Deutsch: Zeiten, Artikel, Satzbau, Bedingungssätze |
| `/deutsch/`, `/english/`, `/de/`, `/deutsch.html` | Legacy URLs — redirect stubs |

## Run locally

```bash
python3 -m http.server 8931
# open http://127.0.0.1:8931/
```

(Service worker and install prompt require http(s), not `file://`.)

## Deploy to GitHub Pages

Already configured: push to `main` → Pages builds from `/ (root)`
(`.nojekyll` included). Nothing else to do. All asset references are
relative, so the site works at the project subpath unchanged.

## Repository layout

| Path | Purpose |
| --- | --- |
| `index.html` | Landing page (locale selector, language cards, theme toggle) |
| `content/decks/` | Deck data (`de-ru.json`, `en-ru.json`, …) + `schema.json` |
| `de/ru/` | German-for-Russians page — generated from its deck, plus manifest, `icons/`, `SITE_PLAN.md` |
| `en/ru/` | English-for-Russians page — same model |
| `deutsch/`, `english/`, `de/` | Redirect stubs to the new URLs (kept for old links and installed PWAs) |
| `sw.js` | Shared service worker — caches every language shell; bump `CACHE_VERSION` after changes |
| `icons/` | Landing favicon + og image (generator: `tools/make_icons.py`) |
| `tools/build_pages.py` | Deck → page generator CLI: validates + renders a deck JSON (stdlib only) |
| `tools/deck_*.py` | Generator modules — `deck_blocks` (block registry), `deck_validate`, `deck_render`, `deck_html` |
| `tools/page_template.html` | Page skeleton substituted with `@@TOKENS@@` by `deck_render` |
| `docs/ADD_LANGUAGE.md` | Playbook for adding the next language or audience |
| `docs/SITE_PLAN_GUIDE.md` | Questions and required structure for language plans |
| `.design/` | Design system contract + decision log (all pages) |
| `docs/CONTENT_VALIDATION.md` | Content accuracy, coverage and teaching-quality review procedure |
| `CONTENT_AUDIT.md` | Open content questions, review evidence and verdicts |
| `UI_AUDIT.md` | Verified UI issues and status |
| `AGENTS.md` | Rules for coding agents working here |

## PWA notes

- Each language installs as its own app (own manifest, icons, short name);
  the service worker is shared and scoped to the whole site.
- Android/Chrome: install button appears via `beforeinstallprompt`.
- iOS/Safari: the button opens “Share → Add to Home Screen” instructions.
- After changing any page or asset, bump `CACHE_VERSION` in `sw.js` (and add
  new shell URLs to `APP_SHELL`) so clients pick up the update.

## Adding a language or audience

See `docs/ADD_LANGUAGE.md` — author a deck JSON, render it with
`tools/build_pages.py` into `<target>/<audience>/`, regenerate icons,
wire it into `sw.js` + landing, verify, push.

## Content quality

Use [the SITE_PLAN guide](docs/SITE_PLAN_GUIDE.md) to define accepted scope,
including durable exclusions. The [German](de/ru/SITE_PLAN.md) and
[English](en/ru/SITE_PLAN.md) plans own those language-specific decisions.

Follow [content validation](docs/CONTENT_VALIDATION.md) for content changes.
`CONTENT_AUDIT.md` owns unresolved questions, sources and results. A plan
states the target; it is not evidence that the page meets it.
