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
| 16 | P2 | User-reported 2026-09-24 (weil/denn + sondern dialogs): `.detail-block b { display: block }` — written for the Russian label — hit **every** `<b>` in a dialog block, so bold runs mid-sentence (*…, denn ich **bin** müde.*) each broke onto their own line and the period wrapped alone. Latent since the first dialogs (they only used italics inline); became prominent once the sondern/not-but content shipped bold target-language runs. | Label is now the only block-level child: generator emits `<b class="detail-label">`, CSS narrowed to `.detail-block .detail-label`; `markTargetLang` additionally covers bold/strike runs (not the label). Details in `.design/decisions.md` 2026-09-24. |

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

---

## 2026-09-28 — Readability and navigation pass

In-app browser review of the landing at narrow-panel width and both deck
pages at narrow-panel and desktop widths found small secondary explanations
and nav labels. Search showed cards from all views while the prior view stayed
visibly selected.

- Increased supporting text sizes across cards, examples, tables, landing
  language cards and the bottom nav in the shared type scale.
- Added a visible, announced search result count and cleared the nav selection
  while cross-view results are shown; clearing search restores the prior view.
- Removed decorative grammar cues from screen-reader nav labels.

Verified in the browser: EN search shows a count and no selected nav item;
DE search filters across views, and clearing restores the selected view.
Both generated-page checks pass. The landing, DE and EN pages loaded with
the preview server stopped after their first load. A measured 390px overflow
check and a full keyboard/screen-reader pass were not run in this pass.


## 2026-10-21 — Whole-entry legends and stacked modal meanings

User screenshot showed modal terms and meanings splitting across rows, with
middle dots attached to preceding words. Resolved in the shared renderer/CSS:

- Default legends wrap complete term/meaning entries as flex items. Dots
  follow the preceding entry, with balanced spacing. Only an entry wider
  than its container wraps internally; text is not truncated.
- Explicit `layout: "list"` renders semantic UL/LI markup, one entry per
  row without dots. All four modal cards and both German modal dialogs use
  it. Skin A reuses the existing legend typography; classic also works.
- Schema, stdlib validation/rendering, all four generated pages and the living
  specimen were updated together; rationale is in `.design/decisions.md`.

Chromium/agent-browser evidence, preview server at 127.0.0.1:8931:

- 320/390/768/1280px × classic/skin A × auto/light/dark × 18 views = 432
  combinations: no page/card horizontal overflow. Whole-entry width probes
  found no entry shrunk below its preferred width when it fits the container.
- All modal lists have the expected six German or four English entries,
  semantic UL/LI/role=list, and no pseudo-element separator.
- All 165 reachable dialog keys opened/closed in both skins at 390px
  (330 checks), with populated bodies and no horizontal dialog overflow.
- Imperativ/modal searches return hits in all pairs; clearing restores the
  active view. No browser errors. Phone screenshot visually inspected for
  readable modal rows; inline particle inventory also visually inspected.
- Detailed metrics: `$BB_THREAD_STORAGE/legend-layout-browser.json`;
  screenshot: `$BB_THREAD_STORAGE/legend-modal-mobile.png`.
- Full keyboard/screen-reader, print/noscript and installed-device relaunch
  checks NOT RUN for this focused update. Semantic markup and CSS-only layout
  preserve content without requiring JavaScript; this is source evidence,
  not a claim those runtime lanes ran.


## 2026-10-21 — Russian audience row and Notebook default

The landing's Russian audience option was a span styled only while `.cur`
was present. Selecting English removed the class and its menu-row spacing.
Resolved by using the same native anchor as the other audience options; the
row retains padding and can be focused/activated with Enter in either skin.

Notebook is the static/default skin on the landing, all four generated decks
and the style guide. A saved Classic preference removes the attribute in the
head before stylesheets; missing, invalid or blocked storage keeps Notebook.
Server-rendered radio states match the default. Shared contract and theme
authoring instructions updated; cache v51.

Focused Chromium checks via agent-browser at 127.0.0.1:8931:

- 30 storage/route combinations: absent, Classic, Notebook, invalid and empty
  saved values across all six surfaces; skin attribute, radio state and
  roving tabindex agree. Blocked storage and JavaScript-disabled checks also
  retain Notebook on all six surfaces. Without JS, skin/theme controls are
  hidden on the landing and deck pages.
- 72 layout combinations: six surfaces × both skins × auto/light/dark ×
  390/1280px; no horizontal page overflow.
- Russian link spacing and Enter navigation verified in both skins. Actual
  appearance controls switch, arrow-key selection works, reload preserves
  choices, and all four decks plus the landing reload offline with v51.
- No browser errors. Light/dark phone screenshots visually checked. Evidence:
  `$BB_THREAD_STORAGE/menu-default-browser.json`,
  `$BB_THREAD_STORAGE/russian-menu-fixed-light.png` and
  `$BB_THREAD_STORAGE/russian-menu-fixed.png`.
- All four generated-page checks, shell consistency and diff whitespace pass.
  Full screen-reader, print and installed-device relaunch checks NOT RUN.
  Grammar/content review NOT RUN: no language content changed.


## 2026-10-21 — Landing localization and automatic audience selection

Scope: landing UI and v52 cache update; no deck content, generated deck HTML,
shared component styles or language scope changed.

- **PASS — 22 browser cases:** regional DE/EN/RU tags, ordered browser
  fallback, unsupported/empty preference lists, explicit-choice precedence,
  invalid stored choice, legacy EN/DE migration, ambiguous legacy RU,
  RU→DE→EN→RU switching without navigation, reload persistence, focus/current
  state, both skins with all three themes, 390×844 and 1440×1000 overflow
  checks, blocked-storage detection/switching, and automatic defaults not
  becoming saved choices. Each case checked visible cards/menu targets and
  their exact supported-pair links. German mobile/menu screenshots inspected.
- **PASS — 15 smoke cases:** all four direct deck URLs retained the URL's
  audience with English saved as the landing preference; keyboard selection,
  Escape/outside dismiss; offline landing reload, language switching,
  navigation into a deck and its offline reload; all four legacy redirects
  online and offline after the online visit. No browser errors recorded.
- **PASS — noscript:** Chromium with scripts disabled showed the Russian
  landing, both RU deck cards and native language-menu links; the English
  explanation link navigated directly to `/de/en/`. Dead theme/skin controls
  were hidden by the existing noscript rules.
- **PASS — static/runtime checks:** all four `build_pages.py --check` commands;
  landing `DECKS` matched live pairs in `site.json`; all 53 `APP_SHELL` URLs
  returned HTTP 200 locally; `git diff --check` clean.
- **NOT RUN:** Safari/real-device install/relaunch; grammar, syllabus and
  teaching-quality gates (UI copy only; no grammar changes). This record
  does not change prior content-audit verdicts.

Browser evidence: local Chromium, `http://127.0.0.1:8931/`, 2026-10-21.
Live deployment verification is performed after pushing the same commit.

## 2026-10-23 — Italian/French integration and target-language fragments

Scope: landing plus `de/ru/`, `de/en/`, `en/ru/`, `en/de/`, `it/en/`,
`fr/en/`, served beneath `/learn-language-cheat-sheet/` locally. Reviewer:
parent Codex agent, distinct from the IT/FR content authors. This records UI
and runtime observations, not linguistic acceptance. Root cache: v54.

- At 390×844 and 1280×900, all six pages loaded with no observed page
  overflow. Manifests, favicon and Apple-touch icon requests returned 200;
  both project-menu destinations rendered. All view destinations had the
  expected aria-current and visible sections. Empty search and clear restored
  the active view. All reachable dialog triggers opened a populated dialog;
  ×, Escape and backdrop dismissal passed.
- Both skins and all three theme modes were exercised on every deck;
  theme cycles and saved Notebook selection survived reload. Screenshots of
  IT/FR mobile and desktop views were visually inspected. New target marks,
  target serif text, English meaning support and fixed bottom navigation
  render within the viewport. These are Chromium checks, not iOS/Android
  standalone installation evidence.
- Landing RU/EN/DE filtering and links passed; English offers DE/IT/FR,
  Russian DE/EN, German EN. Manual English preference survived reload.
- Latin-audience legend terms received the appropriate target lang tag on
  all four Latin-audience decks. Explicit target runs in card/dialog prose
  are now supported by the shared selector; unmarked French fragments are
  a content-authoring finding tracked in CONTENT_AUDIT.
- Page error buffers were empty on all six decks. The initial offline-mode
  harness's navigator.onLine assertion was not reliable across CLI navigation;
  offline acceptance uses the subsequent origin-down test instead: after
  worker installation, stop the owned HTTP server, load the landing and all
  six deck URLs, and verify an uncached request fails. All seven cached
  navigations passed. Three cached legacy redirect stubs also resolved with
  the origin stopped; four legacy routes passed online.
- Both new pair shells include favicon and all PNG sizes, including 32px,
  in APP_SHELL. The worker installed and controlled the subpath successfully.
  Generator checks and shell consistency passed. Source text in existing
  DE/EN decks was compared unchanged after excluding seven emphasis-only
  b→i run changes; no grammatical wording was changed there.

Evidence from this session lives in parent thread storage: runtime-it-fr.json,
its final failure restricted to the superseded navigator.onLine assertion,
offline-it-fr.json (PASS), IT/FR mobile/desktop screenshots and resource
snapshots. Every named browser session was closed and the owned HTTP server
stopped in finally blocks. Resource inspection showed no remaining task
browser/server tree; unrelated services were preserved.

NOT RUN: real-device standalone installation, live deployment, a fresh
browser-language/storage-blocking matrix (unchanged detection algorithm).
Independent grammar gates are recorded only in CONTENT_AUDIT.

### Final correction-boundary runtime retest — 2026-10-23

- **PASS:** all 156 combinations of deck view × two skins × three theme
  modes at 390×844, across all six decks; no horizontal page overflow.
  Manual dark and light preferences each survived reload on every deck.
- **PASS:** all reachable dialog triggers populated their dialog. Latin
  bold target fragments in legends, card paragraphs/notices and dialog
  bodies received the correct target `lang`; English/German glosses and
  italic audience hints retained the audience language. A direct dialog
  paragraph probe also passed. No page errors or console messages observed.
- **PASS:** representative old anchors (`#preps`, `#nouns`, `#conditionals`)
  opened the owning view with matching aria-current state.
- Evidence: parent storage `final-runtime-it-fr.json` and
  `final-runtime-source-hashes.txt`; named session `it-fr-bktaq`. This
  extends the first desktop/mobile/dialog/search/landing pass above after
  the explicit language-run corrections. It is a UI retest, not grammar
  certification. The final origin-down offline result is recorded below.

- **PASS — final origin-down offline retest:** v54 installed 72 shell
  requests under `/learn-language-cheat-sheet/`. With the owned HTTP server
  stopped, the landing and all six deck URLs loaded populated pages;
  an uncached fetch failed, proving origin unavailability. All four cached
  redirects (`deutsch/`, `english/`, `de/`, `deutsch.html`) resolved to their
  expected decks. Evidence: parent storage `offline-it-fr.json`.
- Browser and HTTP-server cleanup completed in finally blocks. Before/after
  `memo inspect` records and process checks found no task browser/server
  left running; unrelated processes were preserved. Real-device installation
  and live deployment remain **NOT RUN**.

- **PASS — matching search:** English `subjunctive` and Italian `piacciono` /
  French `voudrais` found the expected cards while their owning views were
  inactive. Search cleared nav selection while active, and clearing search
  restored the previous view. Final IT/FR mobile screenshots were visually
  inspected. Evidence: `search-runtime-it-fr.json`, `it-final-mobile.png`,
  `fr-final-mobile.png`; both page hashes are recorded in that evidence.

### Final independent-review fixes — 2026-10-23

Independent review found one English `on` mistakenly marked as French, one
unmarked French lemma `trouver`, and a German comparison ending `-t` tagged
as English. Corrected those three runs without changing their text. The
last change brings the existing-deck audience-hint adaptations to eight.

**PASS:** fresh v54 cache responses for the final `fr/en/` and `en/de/`
pages matched the on-disk SHA256 values. After stopping the owned origin,
all seven landing/deck navigations and all four legacy redirects passed
again. Actual offline DOM checks confirmed English `on` remains English,
French pronoun `on` and lemma `trouver` are French, and the comparison `-t`
retains German. An uncached request failed. Evidence:
`final-offline-it-fr.json`, `resources-before-final-offline-it-fr.json`,
`resources-after-final-offline-it-fr.json` in parent storage. Cleanup passed.
The earlier full UI matrix carries forward across these three inspected
markup-only corrections; no layout, rule or interaction code changed.

Final explicit process/port check: no task-session process and no listener on
8931 remained (`final-cleanup-check.json` in parent storage).

### Independent shared integration review — 2026-10-23

French agent `thr_4bsuy4n7xv`, distinct from the parent integration author,
reviewed the registry, landing, worker, template, pair assets/manifests,
all generated menu changes and eight audience-hint adaptations. **ACCEPT**:
51 focused static checks passed; S1 (German comparison `-t`) is independently
closed after the exact b→i retest. Existing DE/EN wording/anchors were
unchanged outside the permitted menu/tagging/emphasis differences. The
reviewer inspected the parent runtime artifacts and final page hashes;
no duplicate browser/runtime execution or linguistic verdict was claimed.
Full scope, snapshots, hashes and findings:
[shared review](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/shared-integration-review/review.md).
