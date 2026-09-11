# Design Decisions

This chronological ledger owns the rationale and consequences of accepted
shared UI/design-system decisions for Language Cheat Sheets. The current
living contract is `DESIGN_SYSTEM.md`; historical entries are not a second
contract. Newest entries are last. Superseded decisions remain for context and
link forward through an explicit status note.

## First pass — original German page

### 2026-09-10 — Deploy target is GitHub Pages; all asset URLs stay relative

The site is served from `https://<user>.github.io/<repo>/` (project pages,
subpath). `manifest.webmanifest`, `sw.js`, `icons/*` and anchor `#id` links are
all referenced relatively (`./…`) so the same tree works at any subpath and on
localhost. `.nojekyll` is committed. HTTPS from Pages is what makes the service
worker and install prompt work; the page itself no longer needs to care.

### 2026-09-10 — Raw colors migrated to semantic tokens; dark theme added

Status: retained, except the OS-only control was superseded by “Manual theme
toggle: auto → light → dark” below.

~20 hardcoded hex values in component rules (chip colors, `td.hot`, slot
tints, answers, notices) were promoted to semantic tokens with light+dark
values (see `DESIGN_SYSTEM.md` table). This was the prerequisite for adding
`prefers-color-scheme: dark` without a duplicated stylesheet, and fixes
inversion bugs like the brand mark (`--text` bg now pairs with `--bg` text).
Dark theme follows the OS preference only — no manual toggle in v1; revisit if
learners ask for it.

### 2026-09-10 — Grid children get `min-width: 0` (page overflow fix)

At 390px the article tables (`min-width: 560px`) forced their `.cheat-card`
grid items to 610px because grid items default to `min-width: auto`; the
`.table-scroll` wrapper never scrolled and the page overflowed/clipped.
Fix at the container level (`.cards > * { min-width: 0 }`), not per-card.

### 2026-09-10 — Chip hit areas: 40px visuals + `::after` expansion to ~46px

`.tap` chips were 36px — below the 44px baseline in our own plan. Instead of
growing the visuals (would bloat dense tables), `::after { inset: -3px -5px }`
expands the tappable area; vertical expansion (6px) stays under the 7px chip
gap so hit areas don't overlap. `.tap.case` is a real 44px.

### 2026-09-10 — Searching hides the hero and jump chips

Status: superseded by “Hero, jump chips, numbered headings and install-help
section removed” below.

During an active query the hero (never matches) and jump chips (pointing at
sections that may be filtered out) wasted the most valuable screen area above
results. `body.searching` drives both via CSS.

### 2026-09-10 — `NAV_MAP` and `aria-current` track navigation state

Status: `aria-current` retained; `NAV_MAP` superseded by “Bottom nav becomes
true view switching; scrollspy and NAV_MAP removed” below.

Sections without a nav destination (preps, extras, practice, install-help)
previously froze the highlight on whichever observed section was last visible
(viewing preps highlighted "Формы"). `NAV_MAP` assigns the nearest concept
(preps→cases, extras→forms) or none (practice, install-help), and the active
item now carries `aria-current="true"`.

### 2026-09-10 — Backdrop-close via `event.target === dialog`

Replaced bounding-rect math with the canonical target check — no edge cases
from keyboard-initiated clicks (coords 0,0) or text-selection drags ending
outside the rect.

### 2026-09-10 — Icons generated in-repo, no external assets

`tools/make_icons.py` (stdlib-only PNG writer, supersampled) renders the brand
"DE" mark into `icons/` (32/180/192/512 + full-bleed 512 maskable), plus a
hand-written `favicon.svg`. Regenerate with one command; no binary blobs from
third parties. `manifest.webmanifest` + `sw.js` committed alongside.

### 2026-09-10 — No-JS degradation and print stylesheet

`<noscript>` hides dead controls (chips, install) and unhides practice
answers so the cheatsheet remains fully readable; `@media print` drops chrome,
expands answers and lets tables flow. A reference page should survive hostile
environments.

---

## Second pass — multi-language hub

### 2026-09-10 — Manual theme toggle: auto → light → dark

The OS-follow dark theme left users no control inside the page. New shared
contract piece: a 44px `.theme-btn` in the topbar cycles авто → светлая →
тёмная, persisted in `localStorage` (`theme`), applied via
`html[data-theme]` with the dark token block duplicated under
`:root[data-theme="dark"]` and the media block narrowed to
`:root:not([data-theme="light"])` — so auto still works without JS and both
manual modes override it. `theme-color` metas are synced by JS from the
live `--bg` when a manual choice overrides the OS.

### 2026-09-10 — Per-language folders + landing; legacy deutsch.html redirects

The site is now a hub: root `index.html` (language cards), `deutsch/`,
`english/` self-contained folders. The already-shared URL
`…/deutsch.html` keeps working via a meta-refresh redirect to `./deutsch/`
(GitHub Pages has no server redirects). Root `SITE_PLAN.md` split into
per-language plans; site-level concerns live in `README.md`/`AGENTS.md`.

### 2026-09-10 — One shared root sw.js; per-language manifests and icons

Each language installs as its own app: `manifest.webmanifest` + `icons/`
inside its folder (own start_url/scope, own DE/EN mark), while one root
`sw.js` (scope covers the whole site) caches all shells — one
`CACHE_VERSION` bump updates everything. Language pages register it as
`../sw.js`; the landing as `./sw.js`. The landing itself has no manifest
(hub, not an app); root icons are only favicon + og:image ("Aa" mark).

### 2026-09-10 — English page added at feature parity

Same tokens/components/interactions as the German page; content built for
RU→EN A1–B1 with RU-interference traps as first-class cards (артикли,
do-вопросы, Perfect vs Past, предлоги-ловушки, mustn't vs don't have
to).
`docs/ADD_LANGUAGE.md` captures the reusable playbook, drafted from this
work so language #3 is a copy-adapt-verify task, not a redesign.

---

## Third pass — lookup-deck navigation

### 2026-09-10 — View switching replaces scrollspy and `NAV_MAP`

The long-scroll model fought the app model: `NAV_MAP` faked a 5-destination
nav over 8 sections, scrollspy highlights were approximations, and the hero +
jump chips existed mainly to be hidden during search. Every SITE_PLAN use
case is known-item lookup, and as an installed standalone PWA there is no
address bar or Ctrl+F — so each cheatsheet now switches discrete views.
Sections carry `data-view`; German views: Падежи (cases+preps), Формы
(forms+extras), Порядок (order+verbs), Придаточные, Повтор.
English: Артикли (articles+pronouns+nouns), Времена, Порядок,
Глаголы (verbs+conditionals), Предлоги. Повтор is anchor-only because the
navigation is capped at five items.
The selected view is the nav truth; legacy anchors open the right view, then
scroll. Search became global: while `body.searching` is set, matching
sections from every view are shown stacked; clearing restores the active
view; tapping a nav destination clears the query for a predictable landing.

### 2026-09-10 — Hero and duplicated navigation removed

First-screen real estate goes to search + views. A one-line `.intro` (keeps
the `#start` anchor) replaces the hero block — hero tokens stay in the shared
block because the landing still uses them. Jump chips duplicated the bottom
nav and were deleted. Install help moved into the install dialog plus a
footer line carrying the `#install-help` anchor (noscript keeps the
instructions visible). The print stylesheet now expands every view.

### 2026-09-10 — Target-language text marked via convention (`lang` attribute)

Bold inside `.example`/`.answer`, italics inside `.detail-block`, and formula
slots without Cyrillic get `lang="de"`/`lang="en"` from a tiny JS pass at
load and after each dialog render (bold/italic marking the pattern text was
already the content convention). Closes the deferred a11y item without
churning every card.

### 2026-09-10 — iOS standalone zoom mitigation

After Add to Home Screen, iOS standalone apps can relaunch with a restored
zoom level > 1 and pinch-out is unavailable there (long-standing WebKit
behavior; reported by the user post-install). Fix: a synchronous `<head>`
sniff (iPhone/iPod; iPad via Macintosh UA + `maxTouchPoints > 1`) rewrites
the viewport meta to include `maximum-scale=1` on the two language pages
only. The scope is deliberate: Safari proper ignores `maximum-scale`
(pinch-zoom unaffected there), Android and desktop never see it, and the
landing (not installable) keeps the plain meta. Never add
`user-scalable=no` — that one does block zoom everywhere.

## Documentation reconciliation

### 2026-09-10 — Shared content wording uses target-language terminology

Corrected the two German-only copy rules in the shared design contract to
cover every language. Per-language scope stays in SITE_PLAN.md; the new
`docs/CONTENT_VALIDATION.md` owns content review and `CONTENT_AUDIT.md` owns
evidence. This clarifies documentation; no page or UI behavior was changed.

## 2026-09-11 — Shared `assets/base.css`, serif study voice, style guide

Three related changes, one contract revision. (1) The token+component CSS
that every page inlined (three drifting copies) was extracted to
`assets/base.css`; language pages link `../assets/base.css`, the landing and
the new `style-guide.html` link `./assets/base.css` — a component change is
now one edit instead of N copies. `APP_SHELL` gained the stylesheet. (2)
Target-language text now has a distinct typographic voice: new tokens
`--font-ui`/`--font-study` and an `[lang]` selector render anything marked
with a `lang` attribute in a system serif. `markTargetLang` was extended:
pure-target `.example`/`.answer`/`.table-scroll` containers are marked
wholesale (fixes hard-to-scan mixed lines like "Ich gebe dem Kind … das
Buch"), fragments as before. (3) `style-guide.html` (noindex, not in
APP_SHELL) renders every component from base.css with real specimens and
carries the class-role table — the semantic-naming documentation. Class
renames were deliberately not done: the audit found the naming already
semantic; the gap was documentation, not naming.

### 2026-09-11 — Study-voice stack tuned: Charter first

User feedback after seeing New York everywhere on Apple: consider another
font. Research (screen-reading serifs, per-platform availability) kept the
no-vendored-fonts rule and retuned the system stack instead:
`Charter, "Bitstream Charter", ui-serif, "Sitka Text", Cambria, "Noto Serif",
serif`. The ordering is the point: macOS ships Charter (sturdier, bookish —
Carter's low-res-era design brief) and takes it; iOS has no Charter and
falls through to `ui-serif` = New York; Windows gets Sitka/Cambria, Android
Noto Serif. Zero bytes downloaded, one token changed. A bundled
single-family option (Literata / Gentium Book Plus / Source Serif 4,
self-hosted subset) was evaluated and deliberately deferred — revisit if
cross-device consistency starts to matter more than the zero-footprint rule.

### 2026-09-11 — Intro line wrapped into a `.help-row` (i) button

The one-line usage intro occupied prime first-screen space on every visit.
It is now a compact `.help-row` (i) button in the same slot opening the
standard DETAILS bottom sheet (`lookup-help`) — no new JS, the existing
`data-detail` mechanism. Mobile contract kept: ≥44px target, the `#start`
anchor stays on the row, `body.searching` hides it, and noscript keeps the
plain `.intro` line (search examples dropped there — search is JS-only).
Applied to both language pages in one commit; `assets/base.css` owns the
component and `style-guide.html` carries the specimen.

## 2026-09-11 — Content as data, Phase 1: english/ generated from a deck JSON

Foundation for multi-audience decks (same target language explained for
different native speakers). `content/decks/en-ru.json` now holds the whole
English page (sections, cards as block lists, details dialogs, practice,
UI strings, nav views); `tools/build_pages.py` (stdlib-only, the
`make_icons.py` precedent) validates the deck — chip↔dialog reference
integrity, unique ids, table shapes, run shapes — and renders the static
`english/index.html`, which stays committed, noscript-readable and
SW-cached. `--check` fails when HTML and deck drift apart. Chose JSON over
YAML (stdlib parsing, no parse-time footguns like the Norway problem) and
JSONL (wrong layer: streaming, not authoring); comments are covered by
schema-sanctioned `_note` provenance fields. The block schema mirrors the
style-guide component set; `content/decks/schema.json` is the editor
contract. AGENTS rule 5 amended: commit-time generation by vendored stdlib
scripts is allowed; deployment stays build-free. Migration was verified
behavior-identical: attribute fingerprints and all 410 visible text lines
unchanged, browser invariants matched exactly (29 cards, 35 chips ↔ 30
dialogs, 96 lang marks, search/view/dialog/reveal behaviors).
`deutsch/` stays hand-written as the Phase 2 control.

## 2026-09-11 — Content as data, Phase 2: <target>/<audience>/ URLs; deutsch/ migrated

Multi-audience architecture landed. URLs are now `<target>/<audience>/`
(`de/ru/`, `en/ru/`) so sibling decks (`de/en/` later) share a target;
the landing gained a noscript-safe audience-locale selector (plain RU hrefs
in markup, JS upgrades them via a `DECKS` registry + localStorage). The
hand-written `deutsch/index.html` became `content/decks/de-ru.json` rendered
by `tools/build_pages.py`; the generator learned the German-only constructs
(`case-grid` cards, multi-group sections with gaps, footer without a
practice link, `practice` as a nav destination) plus depth-derived `../../`
root paths and a `meta.lang` token — all byte-neutral for `en-ru` (gated:
`--check` passed against the pre-change HTML before the move). Old URLs
(`/deutsch/`, `/english/`, `/de/`, `/deutsch.html`) are meta-refresh +
canonical stubs, precached so installed PWAs resolve them offline; manifests,
icons and plans moved with their pages; `CACHE_VERSION` v9. Migration
verified behavior-identical: 341/341 visible text lines and 561/561 element
fingerprints unchanged (only documented diffs: `strong`→`b` in case buttons —
identical UA rendering inside `.tap`'s 800 weight — plus the intentional
path tokens); browser invariants (33 cards, 39 chips ↔ 29 dialogs, 3
reveals, 95 `lang="de"` marks, view/anchor routing, search, dialogs) matched
the pre-migration baseline exactly; en move is byte-pure modulo 5 path
tokens. Known follow-up kept in the deck `_note`: German footer has no
practice link while English does.

## 2026-09-11 — Header controls: help (i) and the audience locale menu

Two compact controls moved into the topbar, replacing the `.help-row` that
sat at the top of `main`. (1) The usage help is now a 44px `.icon-btn`
(same styling family as `.theme-btn`) with an italic-serif (i) glyph,
`aria-label`/`title` «Как пользоваться», opening the same `lookup-help`
bottom sheet via `data-detail`; the `#start` anchor stays. (2) Each deck
page gained a `.locale-menu` — a native `<details>` whose summary shows the
audience code (RU) and whose popover lists the sibling audiences of the
same target language from new deck `meta.locales` (validator: must include
the deck's own audience; `soon` items render disabled «English — скоро»).
Native details keeps it functional without JS; JS only adds light dismiss
and Escape. Landing keeps its full selector; the menu is the on-page
equivalent. Both ship in the same generator template, so all deck pages
get them from one edit; style-guide specimen and DESIGN_SYSTEM rows
updated in the same change.
