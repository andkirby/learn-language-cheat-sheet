# Design Decisions

Consequential UI/design-system decisions for German Cheat. Newest last.
Format: date — decision — why.

## 2026-09-10 — Deploy target is GitHub Pages; all asset URLs stay relative

The site is served from `https://<user>.github.io/<repo>/` (project pages,
subpath). `manifest.webmanifest`, `sw.js`, `icons/*` and anchor `#id` links are
all referenced relatively (`./…`) so the same tree works at any subpath and on
localhost. `.nojekyll` is committed. HTTPS from Pages is what makes the service
worker / install prompt actually work — the page itself no longer needs to care.

## 2026-09-10 — Raw colors migrated to semantic tokens; dark theme added

~20 hardcoded hex values in component rules (chip colors, `td.hot`, slot
tints, answers, notices) were promoted to semantic tokens with light+dark
values (see `DESIGN_SYSTEM.md` table). This was the prerequisite for adding
`prefers-color-scheme: dark` without a duplicated stylesheet, and fixes
inversion bugs like the brand mark (`--text` bg now pairs with `--bg` text).
Dark theme follows the OS preference only — no manual toggle in v1; revisit if
learners ask for it.

## 2026-09-10 — Grid children get `min-width: 0` (page overflow fix)

At 390px the article tables (`min-width: 560px`) forced their `.cheat-card`
grid items to 610px because grid items default to `min-width: auto`; the
`.table-scroll` wrapper never scrolled and the page overflowed/clipped.
Fix at the container level (`.cards > * { min-width: 0 }`), not per-card.

## 2026-09-10 — Chip hit areas: 40px visuals + `::after` expansion to ~46px

`.tap` chips were 36px — below the 44px baseline in our own plan. Instead of
growing the visuals (would bloat dense tables), `::after { inset: -3px -5px }`
expands the tappable area; vertical expansion (6px) stays under the 7px chip
gap so hit areas don't overlap. `.tap.case` is a real 44px.

## 2026-09-10 — Searching hides the hero and jump chips

During an active query the hero (never matches) and jump chips (pointing at
sections that may be filtered out) wasted the most valuable screen area above
results. `body.searching` drives both via CSS.

## 2026-09-10 — Nav active state maps every section (`NAV_MAP`) + `aria-current`

Sections without a nav destination (preps, extras, practice, install-help)
previously froze the highlight on whichever observed section was last visible
(viewing preps highlighted "Формы"). `NAV_MAP` assigns the nearest concept
(preps→cases, extras→forms) or none (practice, install-help), and the active
item now carries `aria-current="true"`.

## 2026-09-10 — Backdrop-close via `event.target === dialog`

Replaced bounding-rect math with the canonical target check — no edge cases
from keyboard-initiated clicks (coords 0,0) or text-selection drags ending
outside the rect.

## 2026-09-10 — Icons generated in-repo, no external assets

`tools/make_icons.py` (stdlib-only PNG writer, supersampled) renders the brand
"DE" mark into `icons/` (32/180/192/512 + full-bleed 512 maskable), plus a
hand-written `favicon.svg`. Regenerate with one command; no binary blobs from
third parties. `manifest.webmanifest` + `sw.js` committed alongside.

## 2026-09-10 — No-JS degradation and print stylesheet

`<noscript>` hides dead controls (chips, install) and unhides practice
answers so the cheatsheet remains fully readable; `@media print` drops chrome,
expands answers and lets tables flow. A reference page should survive hostile
environments.

---

# Second pass — multi-language hub (same day)

## 2026-09-10 — Manual theme toggle: auto → light → dark

The OS-follow dark theme left users no control inside the page. New shared
contract piece: a 44px `.theme-btn` in the topbar cycles авто → светлая →
тёмная, persisted in `localStorage` (`theme`), applied via
`html[data-theme]` with the dark token block duplicated under
`:root[data-theme="dark"]` and the media block narrowed to
`:root:not([data-theme="light"])` — so auto still works without JS and both
manual modes override it. `theme-color` metas are synced by JS from the
live `--bg` when a manual choice overrides the OS.

## 2026-09-10 — Per-language folders + landing; legacy deutsch.html redirects

The site is now a hub: root `index.html` (language cards), `deutsch/`,
`english/` self-contained folders. The already-shared URL
`…/deutsch.html` keeps working via a meta-refresh redirect to `./deutsch/`
(GitHub Pages has no server redirects). Root `SITE_PLAN.md` split into
per-language plans; site-level concerns live in `README.md`/`AGENTS.md`.

## 2026-09-10 — One shared root sw.js; per-language manifests and icons

Each language installs as its own app: `manifest.webmanifest` + `icons/`
inside its folder (own start_url/scope, own DE/EN mark), while one root
`sw.js` (scope covers the whole site) caches all shells — one
`CACHE_VERSION` bump updates everything. Language pages register it as
`../sw.js`; the landing as `./sw.js`. The landing itself has no manifest
(hub, not an app); root icons are only favicon + og:image ("Aa" mark).

## 2026-09-10 — English page added at feature parity

Same tokens/components/interactions as the German page; content built for
RU→EN A1–B1 with RU-interference traps as first-class cards (артикли,
do-вопросы, Perfect vs Past, предлоги-ловушки, mustn't vs don't have to).
`docs/ADD_LANGUAGE.md` captures the reusable playbook, drafted from this
work so language #3 is a copy-adapt-verify task, not a redesign.

---

# Third pass — lookup-deck navigation (same day)

## 2026-09-10 — Bottom nav becomes true view switching; scrollspy and NAV_MAP removed

The long-scroll model fought the app model: `NAV_MAP` faked a 5-destination
nav over 8 sections, scrollspy highlights were approximations, and the hero +
jump chips existed mainly to be hidden during search. Every SITE_PLAN use
case is known-item lookup, and as an installed standalone PWA there is no
address bar or Ctrl+F — so each cheatsheet now switches discrete views.
Sections carry `data-view`; German views: Падежи (cases+preps), Формы
(forms+extras), Порядок (order+verbs), Придаточные, Повтор. English:
Артикли (articles+pronouns+nouns), Времена, Порядок, Глаголы
(verbs+conditionals), Предлоги (Повтор is anchor-only — nav is capped at 5).
The selected view is the nav truth; legacy anchors open the right view, then
scroll. Search became global: while `body.searching` is set, matching
sections from every view are shown stacked; clearing restores the active
view; tapping a nav destination clears the query for a predictable landing.

## 2026-09-10 — Hero, jump chips, numbered headings and install-help section removed

First-screen real estate goes to search + views. A one-line `.intro` (keeps
the `#start` anchor) replaces the hero block — hero tokens stay in the shared
block because the landing still uses them. Jump chips duplicated the bottom
nav and were deleted. Install help moved into the install dialog plus a
footer line carrying the `#install-help` anchor (noscript keeps the
instructions visible). The print stylesheet now expands every view.

## 2026-09-10 — Target-language text marked via convention (`lang` attribute)

Bold inside `.example`/`.answer`, italics inside `.detail-block`, and formula
slots without Cyrillic get `lang="de"`/`lang="en"` from a tiny JS pass at
load and after each dialog render (bold/italic marking the pattern text was
already the content convention). Closes the deferred a11y item without
churning every card.

## 2026-09-10 — iOS-only `maximum-scale=1` on installable pages (standalone zoom-state bug)

After Add to Home Screen, iOS standalone apps can relaunch with a restored
zoom level > 1 and pinch-out is unavailable there (long-standing WebKit
behavior; reported by the user post-install). Fix: a synchronous `<head>`
sniff (iPhone/iPod; iPad via Macintosh UA + `maxTouchPoints > 1`) rewrites
the viewport meta to include `maximum-scale=1` on the two language pages
only. The scope is deliberate: Safari proper ignores `maximum-scale`
(pinch-zoom unaffected there), Android and desktop never see it, and the
landing (not installable) keeps the plain meta. Never add
`user-scalable=no` — that one does block zoom everywhere.
