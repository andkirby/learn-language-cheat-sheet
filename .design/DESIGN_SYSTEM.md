# Design System — Language Cheat Sheets

## Responsibility

This file owns the shared visual, component, interaction and accessibility
contract for the landing page and every language page. It does not own a
language's topic scope, view membership, stable anchors or review evidence;
those belong in its `SITE_PLAN.md` and `CONTENT_AUDIT.md` respectively.

All pages are static HTML with no build step or external dependencies.
Shared tokens and components live in **`assets/base.css`** — the machine
source of truth every page links (`../assets/base.css`; landing and style
guide: `./assets/base.css`). Pages keep only page-specific styles in a small
local `<style>` block. Living component specimens and class roles:
`style-guide.html`.

## Product character & density

- Compact reference cards, not a textbook. First layer = trigger + rule + one
  short example; depth lives in tap-to-open bottom-sheet dialogs.
- Russian explanation first, target-language terminology retained.
- Content width capped at 980px; the page must never scroll horizontally.

## Tokens

CSS custom properties in the `:root` blocks of `assets/base.css` are the
**only** source of truth for color. Raw hex/rgba in component rules is
forbidden — the one exception is the `:root` token blocks themselves (plus
black-key shadows). Every page gets the same token set via the shared
stylesheet.

| Role | Light | Dark | Used for |
| --- | --- | --- | --- |
| `--bg` | `#f6f7fb` | `#10131b` | page background |
| `--surface` | `#ffffff` | `#191e2b` | cards, tables, topbar |
| `--surface-2` | `#eef1f7` | `#232a3a` | examples, th, detail blocks |
| `--text` | `#172033` | `#e9ecf4` | body text (also brand-mark bg) |
| `--muted` | `#667085` | `#9ba4b8` | secondary text, badges |
| `--line` | `#dfe4ec` | `#2c3448` | hairline borders |
| `--accent` | `#6b4eff` | `#a08dff` | focus ring, notice border |
| `--accent-soft` | `#eeeaff` | `#282147` | chip bg, notice bg, active nav |
| `--on-accent-soft` | `#3d2db5` | `#c9bcff` | chip text, `td.hot`, active nav |
| `--tap-line` | `#d6d0ff` | `#41386e` | chip border |
| `--ok` / `--ok-soft` | `#0c6857` / `#e7f6f1` | `#8adccb` / `#17352c` | verb slots, answers |
| `--warn` / `--warn-soft` | `#7a5000` / `#fff3d8` | `#eec36a` / `#3a2f11` | end-of-sentence slots |
| `--warn-line` / `--notice-warn-bg` | `#d18a00` / `#fff7e7` | `#a97e1f` / `#2e2510` | warning notice |
| `--hero-1`/`-2`, `--hero-text`, `--hero-line`, `--hero-card` | navy gradient block | slightly deeper | landing hero only (always dark; language pages have no hero) |
| `--grab`, `--backdrop`, `--shadow`, `--radius`, `--nav-h` | — | — | sheet handle, dialog backdrop, elevation, shape |
| `--font-ui` / `--font-study` | — | — | system sans (Russian UI) / system serif (target-language text via `[lang]`) |

Rules:

- New color need → add a semantic token here first, then use it. Never reuse a
  primitive for a different meaning.
- Both themes must ship together: changing a light value requires its dark
  counterpart to stay ≥ 4.5:1 for text.
- `theme-color` meta tags must match `--bg` light/dark values.
- Type voices: `--font-ui` (system sans) is the default; `--font-study`
  (system serif) applies to any element carrying an explicit `lang`
  attribute (`[lang]` selector in base.css). Pages set those attributes via
  `markTargetLang`: pure-target `.example`/`.answer`/`.table-scroll`
  containers wholesale; otherwise bold in `.example`/`.answer`, italics in
  `.detail-block`, and Cyrillic-free formula slots. The serif is the
  "studied language" signal — never apply it to Russian text.
- Supporting explanations, table text and bottom-nav labels stay readable at
  phone size; reserve the smallest sizes for compact badges and incidental
  metadata. Body copy uses a 1.52 line height.

## Theming (auto + manual)

- Three modes: `auto` (OS `prefers-color-scheme`), `light`, `dark`.
- CSS mechanics, identical on every page:
  `:root { color-scheme: light; …light }` ·
  `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { …dark } }` ·
  `:root[data-theme="dark"] { …dark }`. The dark token block is duplicated —
  that is the price for a no-JS-safe auto mode.
- `.theme-btn` (44px, topbar, chevron/sun/moon) cycles авто → светлая →
  тёмная; the choice persists in `localStorage` key `theme`; JS syncs the
  `theme-color` metas to the live `--bg` when a manual choice overrides the
  OS. Removing the button or the persistence is a contract change.

## Layout & responsive behavior

- Breakpoints: base (mobile-first, one column) and `min-width: 720px`
  (`.cards.two` → 2 cols, `.cards.three` → 3, `.case-grid` → 4).
- Grid/flex children that contain wide content (tables) must be allowed to
  shrink: `.cards > * { min-width: 0 }` — tables scroll inside
  `.table-scroll`, never the page.
- `scroll-padding-top: 72px` keeps anchored sections clear of the sticky
  one-line topbar.
- Deck topbar is ONE flex row at every width. Phones (≤719px): burger →
  search (language chip inside the field) → theme; brand, language menu,
  help and install live in the burger popover. ≥720px: the burger hides
  and the header is inline (brand → search → lang menu → help → theme →
  install). The landing keeps its own `.brand-row` composition.
- Bottom nav is fixed, 4–5 **view destinations**, respects
  `env(safe-area-inset-bottom)`. A tap switches the visible view (sections
  carry `data-view`); there is no scrollspy — the selected view is the nav
  truth. Each language plan owns its destinations, section membership and
  legacy anchors. A legacy anchor opens the section's view before scrolling.

## Components

| Component | Contract |
| --- | --- |
| `.cheat-card` | Atomic unit; content + optional `.chips`. Searchable via `data-search`. Must shrink (see layout). |
| `.badges` + `.badge.level/.kind` | Card metadata row under the title, from deck fields `level` (A1/A2/B1) and `kind` (short label). Text on every badge — never color alone. Never on case-grid cards. |
| `.tap` (chip) | Opens a `DETAILS` dialog entry — a menu only: on one card, two buttons must never open the same dialog (build-enforced). Variants: `.neutral` (secondary), `.case` (44px). Visual min-height 40px + `::after` hit-area expansion to ≥46px. No other button styles. |
| `.legend` | Static term inventory one dialog explains (translated pairs, vocab strips) — not tappable; item = term (bold) + optional meaning (muted), `·` separators. Optional `detail`+`label` render the card's single entry `.tap`. Survives print and noscript (`.chips` hide in both). |
| `.table-scroll` + `table` | Horizontal scroll container; tables size to their content (`min-width: min-content`) — narrow tables fill the container with no scrollbar, wide paradigms scroll inside; `td.hot` marks case-changing forms via `--on-accent-soft`. |
| `.formula` + `.slot` | Sentence-position diagram. Variants: `.verb` (ok tokens), `.end` (warn tokens), `.sub` (accent tokens). |
| `.example` (+ `.pair-src`, `.pair-gloss`, `.hit`) | Example line(s); pure-target containers take the study voice. With a deck `gloss` → pair layout: hint under a hairline inside the same surface; `.hit` marks the taught form (accent pair, implies bold). |
| `.notice` / `.warning` | Callouts. Accent = info, warn tokens = caveat. |
| `dialog` bottom sheet | One shared `#detailDialog`; title/lead set from `DETAILS`; closes via ×, Escape, backdrop tap (`event.target === dialog`). |
| `.bottom-nav` | View switcher. Active item = selected view, gets `.active` **and** `aria-current="true"`; decorative grammar cues are hidden from screen readers. During search, selection styling and `aria-current` clear because results span views. A tap clears search, updates the hash and scrolls to top. |
| `section[data-view]` | View membership. JS hides non-active views via the `hidden` attribute; search unhides matching sections across views; noscript and print show everything stacked. |
| `.theme-btn` | 44px topbar icon button; cycles/persists the theme (see Theming). |
| `.icon-btn` | 44px topbar icon button (shares `.theme-btn` styling); the (i) usage button opens the shared dialog via `data-detail="lookup-help"`; carries `#start`; deck pages: ≥720px only (phones get an id-less row inside the burger, so the id stays unique); hidden on noscript pages, which keep a plain `.intro` line. |
| `.app-menu` | Phone burger (native `<details>`, works without JS; hidden ≥720px): identity line (brand name + sub, which leave the one-line header), the same two language groups as `.lang-menu`, then help + install rows (`.menu-row`; the help row is id-less on purpose). JS adds light dismiss + Escape for both menus. |
| `.search-chip` | Persistent target-language mark (the deck's `brand_mark`) leading the search field — "which deck am I in" survives typing, unlike a placeholder; the input's `aria-label` names the language for screen readers. |
| `.lang-menu` | Topbar language control (native `<details>`, works without JS): one popover, two flat labeled groups — «Язык обучения» (targets, navigational links, from `content/decks/site.json`) and «Язык объяснений» (audiences; `.cur` = current, `.soon` = no deck yet). Deck pages: inline ≥720px, inside the burger on phones; landing: brand row. JS adds light dismiss + Escape. Never a submenu — both choices are visible state. |
| `.install-nudge` | One-time install prompt above the bottom nav: browser tab only, shown after a ~25s dwell, `localStorage.installNudge` written when shown (once per visitor, ever); hidden in standalone and noscript. |
| `.lang-card` (landing only) | Whole-card link to a language folder: mark + name + topics + `→`; hover accent border. |

## Interaction states & feedback

- Focus: global `:focus-visible` = 3px `var(--accent)` outline, offset 2px.
  Never remove without replacement.
- Search (`body.searching`): the help row hides; cards/sections with no
  match hide — **across all views** (matching sections from other views
  become visible stacked); `#searchSummary` reports the card count and
  `#noResults` appears at 0 matches. Clearing restores the active view and
  its nav state. Search must never destroy dialog state.
- `prefers-reduced-motion`: smooth scroll and all transitions off.

## Accessibility baseline

- Primary controls ≥44px effective touch target (visual size may be smaller
  with hit-area padding).
- No information by color alone (`td.hot` is also bold).
- Contrast ≥ 4.5:1 for text in both themes.
- Keyboard: every control reachable and operable; dialog traps focus natively
  (`showModal`), closes with Escape.
- System font stack only; no external fonts.
- Viewport zoom: never `user-scalable=no`. `maximum-scale=1` is applied to
  installable pages **only on iOS** (synchronous `<head>` UA sniff) to stop
  the standalone relaunch zoom-state bug; Safari ignores the attribute, so
  pinch-zoom survives everywhere else.

## Content/copy conventions

- UI language Russian; grammar terms stay in the target language
  (German: Dativ, weil; English: Present Perfect).
- Examples ≤ 2 lines; bold marks the pattern-carrying words. When an example
  needs its deciding hint, the deck attaches a `gloss` and it renders as a
  pair (hint under a hairline); `hit` runs mark the form the card teaches.

## Governance & exceptions

- Changing a token, adding a component/variant, or deviating from anything
  above requires an entry in `decisions.md` — and must be applied to **every**
  page in the same commit (shared contract).
- Author or revise accepted content scope with `docs/SITE_PLAN_GUIDE.md` and
  update that language's `SITE_PLAN.md` before the page. Review results and
  unresolved content questions belong in `CONTENT_AUDIT.md`.
- New languages follow `docs/ADD_LANGUAGE.md`; they inherit this contract
  without renegotiation.
