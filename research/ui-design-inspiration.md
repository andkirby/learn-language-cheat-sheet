# UI/UX design inspiration for learner cheatsheet pages

Date: 2026-09-21 · Method: web research (design galleries, design-system
catalogs, product reviews) · Scope: pattern-level references for our kind of
page — offline grammar cheatsheets for Russian-speaking A1–B1 learners.

Status: **research only; nothing here is adopted.** The three candidate
patterns at the end are prototyped in `ui-improved-example.html` (this
folder). Adoption would follow the normal route: base.css component +
deck-schema fields + `.design/decisions.md` entry, rolled out to every
language page in one commit (DESIGN_SYSTEM.md governance).

Constraints that filter everything below: static pages, no build step, no
external fonts/CDNs (AGENTS.md). So only *patterns* transfer, never
libraries — every proposal must be plain CSS/JS on the existing semantic
tokens.

## Bucket 1 — Cheatsheet / reference-card design (our form factor)

- **DevDocs.io** (https://devdocs.io) — the reference PWA gold standard.
  Search-first: `/` or Ctrl+K focuses search; instant results over ~100k
  entries because every item carries a short, "obvious" identifier instead
  of relying on full text; `?` help overlay; explicit offline mode; dark
  theme. Validates our search-first design and generalizes the C-11–13
  hidden-keywords lesson: search tokens are a designed surface, not an
  accident. Their offline toggle is also a model for *communicating* the
  offline capability instead of it being invisible.
- **htmlreference.io / cssreference.io** — one concept per card, every card
  carries type badges ("block", "inline", "self-closing"), cards grouped
  into collections. The badge-on-every-card pattern is the cheapest scanning
  upgrade for our category views.

## Bucket 2 — Learner-facing grammar references (our exact users)

- **British Council LearnEnglish grammar reference**
  (https://learnenglish.britishcouncil.org) — already a content reference;
  as UI: one rigid per-topic template — rule → example sentences →
  interactive practice. Template consistency is what makes it scannable.
- **Lingolia Deutsch** (https://deutsch.lingolia.com) — same recipe plus
  clean conjugation tables; every topic ends with one "check yourself"
  exercise → the per-topic practice-exit pattern.
- **Reverso Context** (https://context.reverso.net/translation) and
  **Glosbe** (https://glosbe.com) — examples in context with the L1
  translation paired line-by-line and the matched form highlighted inside
  the sentence. This is our gloss policy («deciding hints»,
  docs/SITE_PLAN_GUIDE §6) rendered as a visual pattern: aligned
  example+translation pairs with the target form visually marked.

## Bucket 3 — Language-learning app UX (mobile)

- **Duolingo design system** (design blog https://blog.duolingo.com;
  catalogued at https://adele.uxpin.com and https://styles.refero.design) —
  one saturated brand color, abstract token names, oversized confident
  display type, 10px spacing grid. Transferable: bigger heading type, one
  accent identity per language card on the landing. Streaks/XP/gamification:
  **out of scope** per accepted plans.
- **DW Nicos Weg** (https://learngerman.dw.com) — rated the best free
  structured A1→B1 German course (reviews:
  https://www.langtrak.com,
  https://languagelibrarian.com); UI built around visible level badges
  (A1/A2/B1) and a learning path. Cheap borrow: level-tag topics in deck
  data, badges in views.
- Real-screen galleries: **Mobbin** (https://mobbin.com, Duolingo/Babbel
  flows) and free alternative **Banani** (https://www.banani.co).

## Bucket 4 — Reading experience & principles

- **javascript.info** (https://javascript.info) — the best hybrid
  tutorial+reference: hierarchical TOC, stable clean anchors, light/dark
  toggle, header language switcher across 14+ translations (structural
  analog of our combined language menu), "last updated" freshness markers.
- **Laws of UX** (https://lawsofux.com) — citable principles (progressive
  disclosure, Hick's law) for future `.design/decisions.md` entries.

## Candidate patterns (prototyped in ui-improved-example.html)

1. **Card metadata badges** — level (A1/A2/B1) + type («формы» /
   «предлог → падеж») pills on every card (htmlreference, Nicos Weg).
   Needs deck-schema fields (`level`, `kind`) + validator, then a small
   base.css component.
2. **Highlighted example + gloss pair** — target form highlighted inside
   the sentence, short RU deciding-hint visually paired below
   (Reverso Context). Extends the existing `.example` component; note
   `markTargetLang` would need to learn the new container.
3. **Per-topic practice exit** — end-of-section «Повторить раздел →» chip
   (Lingolia / British Council). Needs practice items tagged per section in
   the deck schema — plan-first territory (adjacent to D-03, which is
   closed pending plan revision).

Deliberately **not** pursued: gamification (streaks/XP/mascot — excluded
by plans), external search/services (offline contract), any JS framework
(no build step).
