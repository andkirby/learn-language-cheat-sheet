# English Cheat Sheet — Site Plan / SoT

> Source-of-truth plan for the **English** page (`english/index.html`).
> Mirrors `../deutsch/SITE_PLAN.md`. Update this file first, then the UI.

## 1. Product goal
Single-page, mobile-first English grammar cheatsheet for a Russian-speaking
learner (A1–B1). Installable as a PWA, works offline after first load, most
common patterns retrievable in 1–3 taps. Same design system and interaction
model as the German page — see `../.design/DESIGN_SYSTEM.md`.

## 2. Primary use cases
1. “Какое время? Смотри на сигнальное слово.” (every day / now / yesterday / just)
2. “a, an, the или ничего?”
3. “Как построить вопрос?” (Do/Does/Did)
4. “Present Perfect или Past Simple?”
5. “Какой предлог? in / on / at; depend ON, interested IN.”
6. “Какое условное? Type 0/1/2/3.”
7. “Show one short example, then a deeper explanation if I tap.”

## 3. Information architecture
The page is a lookup deck: a one-line intro, then five bottom-nav views.
Each view groups sections by the learner's retrieval question:
- Артикли и слова (`#articles`): Articles · Pronouns · Numbers & comparison
- Времена (`#tenses`): Tenses
- Порядок (`#order`): Word order & questions
- Глаголы (`#verbs`): Verb constructions · Conditionals
- Предлоги (`#preps`): Prepositions

Повтор (`#practice`) is an anchor-only view linked from the footer (bottom
nav is capped at five). Install help lives in the install dialog plus a
footer line (`#install-help`), not in its own section. There is no hero
block and no numbered headings.

## 4. Navigation
- Bottom nav = five **view destinations**: Артикли, Времена, Порядок,
  Глаголы, Предлоги. A tap switches the visible view (sections carry
  `data-view`); the active item is the selected view with
  `aria-current="true"`. No scrollspy, no `NAV_MAP`. Tapping a destination
  also clears an active search.
- Повтор (`#practice`) is an anchor-only view, linked from the footer.
- Top search is global: it filters cheat cards across **all** views at once
  while `body.searching` is set (the intro line hides). Clearing restores
  the current view.
- Anchors stay stable: `#pronouns/#nouns` resolve inside the Артикли view,
  `#conditionals` inside Глаголы, `#start` → top, `#install-help` → footer;
  the target section's view opens first, then the section scrolls into view.
- Without JavaScript all sections are stacked and visible.

## 5. Interaction model
Identical to the German page: tappable chips → bottom-sheet dialogs
(`DETAILS` object), searchable cards via `data-search` + text, show-answer
practice with `aria-expanded`, no hover-only UI. The “Установить” button
explains itself in a dialog; there is no install section. Bold text inside
`.example`/`.answer` and italics inside `.detail-block` carry the English
text; JS sets `lang="en"` on them.

## 6. Content principles
- Russian explanation first; English terminology retained.
- Every tense card: formula + signal words + one short example.
- Mark RU-interference traps explicitly (артикли, do-вопросы, предлоги).
- Depth lives in dialogs, not on cards.

## 7. Grammar coverage (current baseline)
### Articles
- a/an by first SOUND (an hour, a university); the = known/specific;
  zero = generalization, meals, languages, sports (but: play the piano).
- Institution-as-role vs building (go to school vs the school).

### Pronouns
- I–me–my–mine … they–them–their–theirs (full table).
- Reflexive -self/-selves.

### Word order
- Strict SVO; frequency adverbs before main verb, after be.
- Do/Does/Did + V1; W-questions; who-as-subject exception.

### Tenses
- Present Simple (V+s; habits/facts), Present Continuous (am/is/are+V-ing).
- Past Simple (V2; dated past), Present Perfect (have/has+V3; result/experience).
- PP vs Past Simple decision rule (“время названо?”).
- will vs going to (+ schedule Present Simple note).

### Verbs
- Modals + V1 (can/could/must/should/may/might; have to).
- mustn't vs don't have to.
- Passive be+V3 across tenses.
- V-ing vs to V verb lists (enjoy/finish/mind vs want/decide/hope).

### Prepositions
- Time in/on/at; place in/on/at.
- Dependent prepositions: depend on, interested in, listen to, afraid of,
  good at, wait for, arrive in/at.

### Nouns/adjectives
- Plural rules + man/men, child/children, foot/feet, person/people.
- Countable vs uncountable (much/many/few/little; advice, news, money).
- some/any; comparative/superlative incl. good/better/best.

### Conditionals
- 0 (always), 1 (real future; no will after if), 2 (unreal now; were),
  3 (unreal past; recognize at B1).

## 8. PWA requirements
Same model as German: `./manifest.webmanifest` (name “English Grammar
Cheatsheet”, short “EN Cheat”), icons from `../tools/make_icons.py` with mark
`EN` in `./icons/`, shared `../sw.js` registered as `../sw.js`, HTTPS via
GitHub Pages.

## 9. Accessibility / ergonomics
Inherited from the design system — see `../deutsch/SITE_PLAN.md` §9 and
`../.design/DESIGN_SYSTEM.md`.

## 10. Update protocol
Identical to `../deutsch/SITE_PLAN.md` §10 (anchors stable, DETAILS first,
bump root `CACHE_VERSION`, test 390px + desktop + offline).

## 11. Deployment
Site-level — see `../README.md`. Served at `…/learn-language-cheat-sheet/english/`.
