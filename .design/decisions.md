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

## 2026-09-11 — One combined language menu: learning + explanation language

User feedback: the landing's audience selector sat mid-page and stated only
half the picture; the two language choices belong together, in the first
line. Redesign (design-architecture EXTEND): the per-page `.locale-menu`
evolved into a single `.lang-menu` present in the topbar of every page —
summary chip `DE · RU`, popover with two flat labeled groups: «Язык
обучение» (targets — navigational links) and «Язык объяснений» (audiences —
current/upcoming). Decisions, grounded in language-selector research
(Smashing Magazine 2022: decouple presets, avoid bundled assumptions,
non-modal, text labels not flags; NN/g: switchers must be discoverable in
the header): (1) flat groups, NOT the proposed `[Интерфейс >]` submenu —
both choices are visible state, and progressive disclosure is wrong for
state (product-interaction guardrail); (2) the axes stay decoupled — two
groups with explicit headers, no preset bundling like "Russian ⇒ Deutsch";
(3) placement: landing brand row; deck pages search row — measured: brand
row + (i) + theme + install + chip overflows at 390px; (4) availability is
honest: audiences without a deck render disabled «— скоро», so a combined
control never promises content that doesn't exist; (5) data moved out of
per-deck `meta.locales` into `content/decks/site.json` (one registry: per
target, audiences + soon flags) read by the generator; the landing mirrors
it inline (hand-written page) — documented in ADD_LANGUAGE; (6) continuity:
deck pages persist `localStorage.target`; the landing chip greets returning
learners with `DE · RU`. «Интерфейс» wording rejected for «Язык
объяснений» — already the site's vocabulary. Noscript: «Язык обучения»
items remain real links; the current audience is a non-interactive state
mark.

## 2026-09-11 — iOS standalone: repair the 980px resume viewport; landing parity

Symptom: a Home Screen app (standalone display) reopened from background
sometimes rendered the desktop layout (`min-width: 720px` in base.css) —
WebKit can restore a resumed standalone window with the legacy 980px
default viewport instead of the device width. The existing head-level
`maximum-scale=1` lock (057e836) only runs during initial head execution,
so it cannot see a viewport that breaks later, on resume.

Decision: extend the existing iOS-only head sniff (template in
`tools/build_pages.py`, mirrored by hand in the landing `index.html`) with
a repair: when the page is standalone (`navigator.standalone`) and
`innerWidth > screen.width * 1.5`, rewrite the viewport meta to a differing
value and restore it 50 ms later — the content change forces WebKit to
rebuild the viewport. Runs on `pageshow` and on `visibilitychange →
visible`. The steady-state meta stays exactly
`width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover`,
so the repair can never strip the anti-zoom lock (a proposed variant that
restored without `maximum-scale=1` was rejected for exactly that reason).
Threshold 1.5× avoids false positives in landscape (where `screen.width`
follows orientation). The landing previously had no iOS head script at
all — it now carries the same block for parity (its standalone branch is
inert until the hub gets a manifest, but Safari visits share the
maximum-scale behavior with deck pages). Not regression-testable in
Chromium; verified by node syntax check + iPhone-UA browser pass (meta
rewrite fires, console clean) — the 980px state itself is WebKit-only.

## 2026-09-21 — Card anchors: every card is deep-linkable

Cards had no ids: the finest shareable/bookmarkable address was the section,
and the planned search jump-to-context (UI gap: search finds an element but
cannot take you to its page) had no precise landing target.

Decision: every deck card carries an explicit `id` slug in its deck JSON
(latin grammar terms, `[a-z0-9-]`, 2–32 chars) — explicit, never derived from
the displayed heading, because content sweeps reword headings constantly and
a derived id would silently break links. The generator assembles the anchor
`<section-id>-<slug>` (e.g. `#verbs-doppelinfinitiv`), so slugs only need to
be unique within a section; the build gate enforces presence, charset and
global uniqueness (incl. against section/practice/help ids). The generated
practice card stays id-less — it is not authored content.

Landing feedback is pure CSS: `.cheat-card:target` runs a one-shot
`card-flash` keyframe (accent ring fading into the resting shadow), using
the same `--accent` as `:focus-visible` — one "you are here" color. CSS-only
means no-JS visits land highlighted too, and the global
`prefers-reduced-motion` block already neutralizes it. No template JS
changed: the existing `onHash()` routing (view switch + `scrollIntoView`)
already handled arbitrary element ids, so card anchors worked the moment the
ids existed. Latin slugs over Cyrillic: Cyrillic percent-encodes into
`%D0%BC…` garbage in shared URLs.

The search result→jump UI (location label + tap-to-context) is deliberately
NOT part of this change; it layers on these anchors as its follow-up.
Deliberately no style-guide.html specimen: `:target` is a card state, not a
component; this entry is its record.

## 2026-09-21 — Search results: location label + jump-to-card (Phase 2)

Closes the user-reported gap that started this work: search filtered cards
across all views, but a hit never said where it lives and nothing could take
you there — tapping any nav tab silently cleared the search and landed
elsewhere.

Design (Option A, iOS-Settings-style jump-in-context): while a query is
active, every hit card gets a small `.hit-jump` label at its top —
«view · section ↗» (deduped to one segment when the names match, e.g.
«Падежи ↗»). Tapping it clears the query and routes through the card's
anchor: the existing `onHash()` switches the view, scrolls to the card and
the Phase-1 `:target` flash marks it. Labels are built at runtime from the
deck's own nav labels and section headings, so the flow needs no new UI
strings and stays correct for any future audience language.

Boundaries recorded as accepted trade-offs: jumping drops the query (Back
does not restore it — the input is not history state); the generated
practice card is the one hit without a label (it has no card id by design);
label is one line with ellipsis truncation at 390px. In case-grid cards the
label spans the grid's full first row (`grid-column: 1 / -1`), keeping the
button grid intact. Rejected alternatives from the option review: grouped
results mode (more surface, replaces a proven filter) and Spotlight overlay
(state juggling, mobile keyboard/scroll-lock risk in the iOS PWA).

## 2026-09-21 — Card badges + example→gloss pairs (design-research adoption)

User picked patterns 1 (card metadata badges) and 2 (highlighted example+gloss
pair) out of `research/ui-design-inspiration.md`, prototyped on real deck
content in `research/ui-improved-example.html`. Pattern 3 (per-topic practice
exit) is explicitly deferred by the user — «повтор» is too basic to invest in
now; revisiting needs the practice→section plan revision flagged next to D-03.

Decisions:

1. **Badges as free-ish card metadata.** Card-root deck fields `level`
   (enum A1/A2/B1 — the decks' declared span; a new level is a scope change)
   and `kind` (free 1–40 char label; recommended vocabulary: формы /
   употребление / порядок / время / связь / условное / триггер → падеж·предлог).
   Free text over a closed multilingual enum: two decks in two languages would
   churn an enum every review; the build validator guards the level enum and
   the kind length instead. Rendered as `.badges` under the title: level on
   the accent-soft pair (the same "pay attention" semantics as `td.hot`),
   kind on surface-2+line. Text on every badge — never color alone.
   Forbidden on case_grid cards (a launcher, not a topic) and absent from the
   generated practice card (not authored content).
2. **Pair as an `example` extension, not a new block.** The optional `gloss`
   runs payload keeps one block = one semantic unit: the search-visible text
   and the search-index gate pick the gloss up automatically, HTML_ORDER is
   untouched, and plain examples render byte-identical markup. Layout:
   `.example.pair` wraps `.pair-src` (target line) and `.pair-gloss`
   (audience-language hint) under a hairline. New `hit` run flag implies bold
   and adds the accent highlight — the one form the card teaches.
3. **Contrast:** the gloss keeps `--muted` on `--surface-2` — the pairing the
   shipped `th` already uses (~4.4:1 light, ≥5:1 dark). Accepted as consistent
   rather than minting a token for one use.
4. **`markTargetLang` learns `.pair-src`** (wholesale marking when
   Cyrillic-free); hits are covered by the existing `.example b` fragment rule.
   Glosses always stay in the UI voice.
5. **Migration was policy-driven, not wholesale:** 13 DE + 12 EN examples
   became pairs — inline RU annotations relocated out of the sentence lines,
   example-annotating tinies moved into glosses (only where the card has no
   table/formula the tiny also annotates), recognition-level items glossed per
   SITE_PLAN_GUIDE §6. Form-rule examples stay bare; 71 of 72 authored cards
   carry badges (the case-grid launcher intentionally not).

Rollout: both decks + both pages in one commit; sw v21; style-guide specimens,
block-registry table and class-roles table updated; `content/decks/schema.json`
is the editor contract.

## 2026-09-24 — Dialog blocks: the label is the only block-level child

User-reported rendering defect (2026-09-24, weil/denn + sondern dialogs):
`.detail-block b { display: block }` was meant to stack the Russian label
above the text, but it hit **every** `<b>` — bold runs mid-sentence
(*…, denn ich **bin** müde.*) each broke onto their own line, and the new
sondern/not-but content is full of bold target-language runs. The old
contract assumed detail blocks carry emphasis only as *italics*, which no
longer holds.

1. **Markup:** the generator (`tools/deck_blocks.py`) now emits the label as
   `<b class="detail-label">…</b>`; content runs are unchanged.
2. **CSS:** the rule narrows to `.detail-block .detail-label` — the label
   keeps its block + margin; bold/strike/italic runs flow inline. Visual
   output for label-only blocks is byte-identical in layout.
3. **`markTargetLang` covers the runs it was missing:** fragments in detail
   blocks are now `.detail-block b:not(.detail-label), .detail-block i,
   .detail-block s` (Cyrillic-free guard unchanged) — German/English bold and
   strike runs get the study voice + pronunciation; the label never does, even
   when it is a bare Latin term (weil, denn, meanwhile).
4. **Style guide** updated: specimens carry the class, the class-roles row and
   the marking-rules text name `.detail-label`; the DETAILS description states
   "only the label is block-level".

Rollout: generator + base.css + both regenerated pages + style-guide in one
commit; sw v24 → v25.

## 2026-09-24 — Dialog commentary gets its own muted line (`.detail-comment`)

User follow-up to the label fix, same day: inside a detail block the German
sentence and the Russian commentary rendered as one undifferentiated line
(*Ich bleibe, denn ich **bin** müde. После denn остаётся обычный V2.*).
Comments needed a distinct style.

1. **Data model:** the `detail` block gains an optional `comment` runs field
   (schema: both definitions; validator checks it like `runs`, search-index
   text includes it). Same pattern as the cards' `example`/`gloss` pairing.
2. **Markup/CSS:** the generator renders it as `<p class="detail-comment">`
   under the runs — `.78rem`, `--muted`, no hairline (blocks are compact).
   UI voice, never `lang`-marked.
3. **Content sweep, not a style stub:** 30 DE + 11 EN blocks with a
   separable trailing commentary (mostly the « — » tails) moved their tail
   into `comment` — including the translation glosses of the recognition-level
   Passiv/double-infinitive units, which strengthens the §6 gloss policy.
   Blocks where Russian is interleaved mid-text (paradigm lines like
   «Как ein: kein Auto · …») deliberately keep it inline — there the
   commentary IS the body text; splitting would butcher the paradigms.

Rollout: both decks + schema + generator + base.css + both pages +
style-guide in one commit; sw v25 → v26.
