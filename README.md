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

| URL | What |
| --- | --- |
| `/` | Landing — language cards |
| `/deutsch/` | Немецкий: падежи, артикли, порядок слов, придаточные |
| `/english/` | Английский: времена, артикли, вопросы, условные |
| `/deutsch.html` | Legacy URL — redirects to `/deutsch/` |

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
| `index.html` | Landing page (language cards, theme toggle) |
| `deutsch/` | German cheatsheet: `index.html`, `manifest.webmanifest`, `icons/`, `SITE_PLAN.md` |
| `english/` | English cheatsheet: same self-contained model |
| `sw.js` | Shared service worker — caches every language shell; bump `CACHE_VERSION` after changes |
| `icons/` | Landing favicon + og image (generator: `tools/make_icons.py`) |
| `docs/ADD_LANGUAGE.md` | Playbook for adding the next language |
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

## Adding a language

See `docs/ADD_LANGUAGE.md` — copy a language folder, regenerate icons,
wire it into `sw.js` + landing, verify, push.

## Content quality

Use [the SITE_PLAN guide](docs/SITE_PLAN_GUIDE.md) to define accepted scope,
including durable exclusions. The [German](deutsch/SITE_PLAN.md) and
[English](english/SITE_PLAN.md) plans own those language-specific decisions.

Follow [content validation](docs/CONTENT_VALIDATION.md) for content changes.
`CONTENT_AUDIT.md` owns unresolved questions, sources and results. A plan
states the target; it is not evidence that the page meets it.
