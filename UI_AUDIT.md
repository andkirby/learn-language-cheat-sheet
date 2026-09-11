# UI Audit — 2026-09-10

This file owns dated UI review evidence, fixed findings and unresolved UI
findings. The living shared UI contract is `.design/DESIGN_SYSTEM.md`; this
audit is not a second contract.

The initial entries came from a browser-verified Chrome audit at 390×844 and
desktop of the then-root German `index.html`. Later sections record the same-day
multi-language changes. This documentation pass did not re-run the site; run
the checks in `AGENTS.md` before treating the evidence as current.

Current unresolved findings from this audit are search-term highlighting and
a scroll affordance for `.table-scroll`. Both are accepted deferrals with no
scheduled implementation.

## Fixed

| # | Severity | Finding (evidence) | Fix |
| --- | --- | --- | --- |
| 1 | P1 | PWA assets missing — `manifest.webmanifest`, `sw.js`, `icons/icon-192.png` all HTTP 404; console: "A bad HTTP response code (404) was received when fetching the script". Android install impossible (`beforeinstallprompt` never fires), no offline cache. | Created `manifest.webmanifest`, `sw.js` (versioned app-shell cache), icons via `tools/make_icons.py`. |
| 2 | P1 | Horizontal page overflow at 390px: `document.documentElement.scrollWidth` = 610 vs viewport 390. Cause: `.cheat-card` grid items default `min-width: auto`, blown out by `table { min-width: 560px }`; `.table-scroll` never scrolled. Violated the then-current SITE_PLAN mobile requirement. | `.cards > * { min-width: 0 }`; tables now scroll inside `.table-scroll`. |
| 3 | P1 | No favicon — console 404 for `/favicon.ico`, blank tab icon. | `icons/favicon.svg` + `icon-32.png` links in `<head>`. |
| 4 | P2 | Tap chips 36px tall — below the then-current 44px touch-target baseline. | Visual 40px + `::after` hit-area expansion (≈46px effective); `.tap.case` 44px. |
| 5 | P2 | Focus indicator barely visible: `outline: 3px rgba(107,78,255,.35)`. | Solid `var(--accent)` 3px, works in both themes. |
| 6 | P2 | Active bottom-nav item exposed state only as class (no `aria-current`), screen readers unaware of position. | `aria-current="true"` maintained by the observer. |
| 7 | P2 | ~20 raw hex colors in component rules (`#3d2db5`, `#e7f6f1`, `#fff3d8`, …) — no dark theme possible, contrast untracked. | Migrated to semantic tokens with light+dark values (`.design/DESIGN_SYSTEM.md`); dark theme via `prefers-color-scheme`. |
| 8 | P3 | During search, hero and jump chips stay visible above results; chips link to sections that are filtered out. | `body.searching` hides hero + jump row. |
| 9 | P3 | Viewing `#preps` (not a nav target) kept "Формы" highlighted — misleading active state. | `NAV_MAP` covers every section; practice/install-help honestly clear the highlight. |
| 10 | P3 | WebKit `type=search` shows its own ✕ next to the custom clear button (double affordance). | Native cancel button suppressed via `::-webkit-search-cancel-button`; custom ✕ now only shows while typing. |
| 11 | P3 | Without JavaScript: practice answers permanently hidden (toggles dead), chips/install buttons do nothing silently. | `<noscript>` hides dead controls and unhides answers. |
| 12 | P3 | `backdrop-filter` unprefixed — no blur on older iOS Safari. | `-webkit-backdrop-filter` added (topbar, bottom nav). |
| 13 | P3 | No Open Graph/Twitter meta — blank messenger/Telegram previews. | og/twitter tags added; `og:image` needs an absolute URL after deploy (README). |
| 14 | P3 | No print stylesheet; `.ios-tip` dead CSS. | Print styles added; dead rule removed. |
| 15 | P3 | Install button did not react to `appinstalled` (stayed after install). | Handler hides the button. |

## Working correctly (verified, no change needed)

- Dialog: opens on chip tap, focus moves inside, closes via ×, Escape.
- Practice reveal toggles text ("Показать"/"Скрыть") and answer
  visibility.
- Search: filters `.cheat-card` by text + `data-search`, hides empty sections,
  shows "Ничего не найдено" on zero matches, and fully restores on clear.
- Sticky topbar, bottom nav links, anchor offsets at 390px and desktop.
- `prefers-reduced-motion` respected.

## Findings carried into later passes

- `lang="de"` on German example sentences (screen-reader pronunciation) —
  many small edits; batch with next content pass.
- ~~Manual light/dark toggle (currently OS-follow only).~~ — added in the
  second pass below.
- Search-term highlighting inside matched cards.
- Scroll affordance (edge fade): `.jump-row` was later removed;
  `.table-scroll` remains open.
- ~~`og:url` + absolute `og:image` — possible only after the Pages URL is
  known.~~
  — set to the final URLs in the second pass below.

---

## Second pass — 2026-09-10 (multi-language hub)

| # | Severity | Finding | Status |
| --- | --- | --- | --- |
| 16 | P2 | No manual theme control (auto only) — deferred item above. | Fixed: `.theme-btn` cycles auto/light/dark on every page, persisted in `localStorage`, metas synced. |
| 17 | P2 | Site grows to multiple languages; single flat page + single manifest doesn't scale. | Fixed: per-language folders (page+manifest+icons+plan), shared root `sw.js`, landing hub, `docs/ADD_LANGUAGE.md` playbook. |
| 18 | P3 | Live `/deutsch.html` URL would break when moving the page into `deutsch/`. | Fixed: meta-refresh + canonical redirect to `./deutsch/`. |
| 19 | P3 | English page missing entirely. | Added: full RU→EN A1–B1 cheatsheet at feature parity (tenses, articles, order/questions, modals, prepositions traps, conditionals, practice). |
| 20 | P3 | og:url/og:image were relative — previews unreliable. | Fixed: absolute URLs on all pages. |

Deferred (second pass): `lang="de"`/`lang="en"` on target-language examples
(done in pass 3 below); search-term highlighting; scroll affordances.

---

## Third pass — 2026-09-10 (lookup-deck navigation)

| # | Severity | Finding | Status |
| --- | --- | --- | --- |
| 21 | P2 | Three parallel nav mechanisms (jump chips, bottom nav + `NAV_MAP` scrollspy, search) partly duplicated each other; scrollspy highlights approximated on one long page; as an installed standalone PWA there is no address bar / Ctrl+F. | Fixed: bottom nav = true view switcher (`data-view` on sections; no scrollspy, no `NAV_MAP`); hero, jump chips, numbered headings and the install-help section removed (install help → dialog + footer anchor). Views — DE: Падежи/Формы/Порядок(+глаголы)/Придаточные/Повтор; EN: Артикли(+местоимения+слова)/Времена/Порядок/Глаголы(+условные)/Предлоги. |
| 22 | P3 | Deferred from pass 1: `lang="de"`/`lang="en"` on target-language examples (screen-reader pronunciation). | Fixed by convention: JS marks `.example b`, `.answer b`, `.detail-block i` and Cyrillic-free formula slots with the page's target language, at load and after each dialog render. |
| 23 | P2 | iOS standalone (Add to Home Screen) can relaunch with a restored zoom level > 1 and no pinch-out; reported by the user after installing. Known WebKit behavior, not page CSS (meta was already `initial-scale=1`). User-side remedy: force-quit the app, or delete + re-add the icon at 100% zoom. | Mitigated: iOS-only `maximum-scale=1` via synchronous `<head>` UA sniff on both language pages. Safari ignores the attribute (pinch-zoom stays), Android/desktop untouched, landing (not installable) unchanged. `CACHE_VERSION` → v4. |

Search is now global across views while `body.searching` is set (matching
sections from other views become visible; clearing restores the active
view). Print expands all views; noscript shows the full stacked deck.
