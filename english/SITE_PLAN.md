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
- Start / Quick rules (hero)
- Articles (a/an/the/zero + RU-speaker traps)
- Pronouns (subject/object/possessive + reflexive)
- Word order & questions (SVO, Do/Does/Did, frequency adverbs, top RU error)
- Tenses (Pres. Simple/Continuous, Past Simple, Pres. Perfect, PP vs Past,
  will vs going to)
- Verb constructions (modals, mustn't vs don't have to, passive, V-ing vs to V)
- Prepositions (time, place, dependent-preposition traps)
- Words (plurals, countable/uncountable, some/any, comparatives)
- Conditionals (0/1/2/3)
- Quick practice
- Install help

## 4. Navigation
- Bottom nav (5): Articles, Tenses, Order, Verbs, Prepositions.
- NAV_MAP for non-nav sections: pronouns→articles, nouns→articles,
  conditionals→verbs, practice/install-help→no highlight.
- Jump chips for all sections; hidden while searching (body.searching).
- Active item carries `aria-current="true"`.

## 5. Interaction model
Identical to the German page: tappable chips → bottom-sheet dialogs
(`DETAILS` object), searchable cards via `data-search` + text, show-answer
practice with `aria-expanded`, no hover-only UI.

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
