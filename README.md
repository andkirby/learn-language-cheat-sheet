# Language Cheat Sheets — языковые шпаргалки

## Responsibility

This README is the human front door. It owns project orientation, the shortest
local run path, repository layout and deployment notes. Language scope,
shared UI contracts and audit evidence belong to the documents linked below.

Mobile-first cheatsheets of German and English grammar for Russian speakers
(A1–B1). Installable as PWAs and fully offline after first load.

Content maturity: the product scope is documented, but reference-based
baseline, page coverage, accuracy and teaching-quality reviews are currently
NOT RUN. See [the content audit](CONTENT_AUDIT.md).

Live: <https://andkirby.github.io/learn-language-cheat-sheet/>

Deck pages live at `<target>/<audience>/`; the landing locale selector picks
the audience (Русский today — the architecture is ready for more).

| URL | What |
| --- | --- |
| `/` | Landing — locale selector + language cards |
| `/de/ru/` | Немецкий: падежи, артикли, порядок слов, придаточные |
| `/en/ru/` | Английский: времена, артикли, вопросы, условные |
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
| `tools/build_pages.py` | Deck → page generator + validator (stdlib only) |
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
