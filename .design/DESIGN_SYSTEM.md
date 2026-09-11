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
- `scroll-padding-top: 116px` keeps anchored sections clear of the sticky
  topbar.
- Bottom nav is fixed, 5 **view destinations**, respects
  `env(safe-area-inset-bottom)`. A tap switches the visible view (sections
  carry `data-view`); there is no scrollspy — the selected view is the nav
  truth. Each language plan owns its destinations, section membership and
  legacy anchors. A legacy anchor opens the section's view before scrolling.

## Components

| Component | Contract |
| --- | --- |
| `.cheat-card` | Atomic unit; content + optional `.chips`. Searchable via `data-search`. Must shrink (see layout). |
| `.tap` (chip) | Opens a `DETAILS` dialog entry or reveals an answer. Variants: `.neutral` (secondary), `.case` (44px). Visual min-height 40px + `::after` hit-area expansion to ≥46px. No other button styles. |
| `.table-scroll` + `table` | Horizontal scroll container; `td.hot` marks case-changing forms via `--on-accent-soft`. |
| `.formula` + `.slot` | Sentence-position diagram. Variants: `.verb` (ok tokens), `.end` (warn tokens), `.sub` (accent tokens). |
| `.notice` / `.warning` | Callouts. Accent = info, warn tokens = caveat. |
| `.answer` + `.reveal` | Show/hide practice answer; `aria-expanded`/`aria-controls` required; visible without JS (noscript unhides). |
| `dialog` bottom sheet | One shared `#detailDialog`; title/lead set from `DETAILS`; closes via ×, Escape, backdrop tap (`event.target === dialog`). |
| `.bottom-nav` | View switcher. Active item = selected view, gets `.active` **and** `aria-current="true"`; a tap clears an active search, updates the hash and scrolls to top. |
| `section[data-view]` | View membership. JS hides non-active views via the `hidden` attribute; search unhides matching sections across views; noscript and print show everything stacked. |
| `.theme-btn` | 44px topbar icon button; cycles/persists the theme (see Theming). |
| `.icon-btn` | 44px topbar icon button (shares `.theme-btn` styling); the (i) usage button opens the shared dialog via `data-detail="lookup-help"`; carries `#start`; hidden on noscript pages, which keep a plain `.intro` line. |
| `.locale-menu` | Topbar audience switcher: native `<details>` (works without JS) listing the sibling audiences of the same target from deck `meta.locales`; `.cur` = current audience, `.soon` = no deck yet; JS adds light dismiss + Escape. |
| `.lang-card` (landing only) | Whole-card link to a language folder: mark + name + topics + `→`; hover accent border. |

## Interaction states & feedback

- Focus: global `:focus-visible` = 3px `var(--accent)` outline, offset 2px.
  Never remove without replacement.
- Search (`body.searching`): the help row hides; cards/sections with no
  match hide — **across all views** (matching sections from other views
  become visible stacked); `#noResults` appears at 0 matches; clearing
  restores the active view. Search must never destroy dialog or answer state.
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
- Examples ≤ 2 lines; bold marks the pattern-carrying words.

## Governance & exceptions

- Changing a token, adding a component/variant, or deviating from anything
  above requires an entry in `decisions.md` — and must be applied to **every**
  page in the same commit (shared contract).
- Author or revise accepted content scope with `docs/SITE_PLAN_GUIDE.md` and
  update that language's `SITE_PLAN.md` before the page. Review results and
  unresolved content questions belong in `CONTENT_AUDIT.md`.
- New languages follow `docs/ADD_LANGUAGE.md`; they inherit this contract
  without renegotiation.
