# Design System — Language Cheat Sheets

Shared contract for every page in the hub: the landing (`index.html`) and each
language cheatsheet (`deutsch/`, `english/`, …) — single-file pages, no build
step, no external dependencies. This contract constrains all UI changes;
each language's `SITE_PLAN.md` owns that language's scope and content.

## Product character & density

- Compact reference cards, not a textbook. First layer = trigger + rule + one
  short example; depth lives in tap-to-open bottom-sheet dialogs.
- Russian explanation first, German terminology retained.
- Content width capped at 980px; the page must never scroll horizontally.

## Tokens

CSS custom properties in each page's `:root` are the **only** source of
truth for color. Raw hex/rgba in component rules is forbidden — the one
exception is the `:root` token blocks themselves (plus black-key shadows).
Every page ships the same token set.

| Role | Light | Dark | Used for |
|---|---|---|---|
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
| `--hero-1`/`-2`, `--hero-text`, `--hero-line`, `--hero-card` | navy gradient block | slightly deeper | hero only (always dark) |
| `--grab`, `--backdrop`, `--shadow`, `--radius`, `--nav-h` | — | — | sheet handle, dialog backdrop, elevation, shape |

Rules:

- New color need → add a semantic token here first, then use it. Never reuse a
  primitive for a different meaning.
- Both themes must ship together: changing a light value requires its dark
  counterpart to stay ≥ 4.5:1 for text.
- `theme-color` meta tags must match `--bg` light/dark values.

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
  (`.cards.two` → 2 cols, `.cards.three` → 3, `.case-grid` → 4, `.rule-grid` → 4).
- Grid/flex children that contain wide content (tables) must be allowed to
  shrink: `.cards > * { min-width: 0 }` — tables scroll inside
  `.table-scroll`, never the page.
- `scroll-padding-top: 116px` keeps anchored sections clear of the sticky topbar.
- Bottom nav is fixed, 5 destinations (`#cases`, `#forms`, `#order`,
  `#clauses`, `#verbs`), respects `env(safe-area-inset-bottom)`.

## Components

| Component | Contract |
|---|---|
| `.cheat-card` | Atomic unit; content + optional `.chips`. Searchable via `data-search`. Must shrink (see layout). |
| `.tap` (chip) | Opens a `DETAILS` dialog entry or reveals an answer. Variants: `.neutral` (secondary), `.case` (44px). Visual min-height 40px + `::after` hit-area expansion to ≥46px. No other button styles. |
| `.table-scroll` + `table` | Horizontal scroll container; `td.hot` marks case-changing forms via `--on-accent-soft`. |
| `.formula` + `.slot` | Sentence-position diagram. Variants: `.verb` (ok tokens), `.end` (warn tokens), `.sub` (accent tokens). |
| `.notice` / `.warning` | Callouts. Accent = info, warn tokens = caveat. |
| `.answer` + `.reveal` | Show/hide practice answer; `aria-expanded`/`aria-controls` required; visible without JS (noscript unhides). |
| `dialog` bottom sheet | One shared `#detailDialog`; title/lead set from `DETAILS`; closes via ×, Escape, backdrop tap (`event.target === dialog`). |
| `.bottom-nav` | Active item gets `.active` **and** `aria-current="true"`; non-nav sections map via `NAV_MAP` (preps→cases, extras→forms). |
| `.jump-chip` | Anchor pills to sections; hidden while `body.searching`. |
| `.theme-btn` | 44px topbar icon button; cycles/persists the theme (see Theming). |
| `.lang-card` (landing only) | Whole-card link to a language folder: mark + name + topics + `→`; hover accent border. |

## Interaction states & feedback

- Focus: global `:focus-visible` = 3px `var(--accent)` outline, offset 2px.
  Never remove without replacement.
- Search (`body.searching`): hero and jump chips hide; cards/sections with no
  match hide; `#noResults` appears at 0 matches; clearing restores everything.
  Search must never destroy dialog or answer state.
- `prefers-reduced-motion`: smooth scroll and all transitions off.

## Accessibility baseline

- Primary controls ≥44px effective touch target (visual size may be smaller
  with hit-area padding).
- No information by color alone (`td.hot` is also bold).
- Contrast ≥ 4.5:1 for text in both themes.
- Keyboard: every control reachable and operable; dialog traps focus natively
  (`showModal`), closes with Escape.
- System font stack only; no external fonts.

## Content/copy conventions

- UI language Russian; German grammar terms stay German (Dativ, weil, V2).
- Examples ≤ 2 lines; bold marks the pattern-carrying words.

## Governance & exceptions

- Changing a token, adding a component/variant, or deviating from anything
  above requires an entry in `decisions.md` — and must be applied to **every**
  page in the same commit (shared contract).
- Content coverage/scope changes go to that language's `SITE_PLAN.md` first,
  then the page (its update protocol applies).
- New languages follow `docs/ADD_LANGUAGE.md`; they inherit this contract
  without renegotiation.
