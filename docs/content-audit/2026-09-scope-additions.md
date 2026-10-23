# Content audit record — DE/EN scope additions (2026-09)

Historical evidence moved verbatim from the root audit. Current status,
findings ledger and record index: [CONTENT_AUDIT.md](../../CONTENT_AUDIT.md).

## 2026-09-13 — Scope addition: DE-17 modal particles (DE-G09 decided)

Protocol §5 changed-unit record. Author: ZCode session, with the user as
scope owner (user probe «What about german: gar, schon, etc.?» → Required
decision accepted in-session). Plan first per AGENTS rule 3: retrieval
question 7 added, `#order` IA row and DE-17 inventory row added to
`de/ru/SITE_PLAN.md` (bounded set; explicitly no particle lexicon, DE-X02).

Changed units:

| Unit | Change |
| --- | --- |
| DE `order` section, new particles card (DE-17) | 7 chips doch/mal/denn/ja/schon/gar/wohl with Russian decision-equivalents + three-particle example; `data-search` includes Russian intent words and the term *Modalpartikeln* (registered in `site.json` `grammar_terms[de]`) |
| DE `particles` dialog | Per-particle contrast with RU glosses; denn question-only + coordinator disambiguation (cross-ref to the coordinators card); Mittelfeld placement rule with *Ich habe doch nichts gesagt* |
| `content/decks/site.json` | `grammar_terms[de]` += `modalpartikeln` (registry-based exemption, not generator code) |
| `sw.js` | CACHE_VERSION v14 → v15 |

Unit-quality self-review (author level; the formal Accuracy gate stays NOT
RUN, D-01): particle functions checked against contemporary standard usage —
doch (reference to the known, «ведь/же»), ja (shared knowledge, «ведь»), denn
(question-only particle, distinct from the coordinator taught on the
coordinators card), mal (request softener), schon (concession), gar
(intensifier, stated limit «чаще всего с nicht»), wohl (assumption). Russian
glosses are decision-equivalents per the gloss policy's meaning-rule class.
Practice untouched (three-item contract, DE-X05); DE-17 validation runs
through audit probes.

Verified: JSON valid; both `--check` gates exit 0; mixed-script scan clean;
runtime smoke — search «doch» surfaces the card, `particles` dialog opens
with all blocks, `lang="de"` marking applies, no console errors.

Gate impact: Coverage stays **PASS** for German with the inventory now
17/17 (DE-17 added and covered in the same change; no unmapped content).
Baseline still **FAIL** (DE-G01–08, EN-G01–08 open). Accuracy/Teaching
NOT RUN. DE-G09 is decided and no longer open.

## 2026-09-13 — Scope additions: EN-17, EN-18, DE-18 (linking words, flavour words)

Protocol §5 changed-unit record. Author: ZCode session; scope owner: user
(requested the EN mirror of DE-17 and asked whether meanwhile/nevertheless-type
connectors fit — assessed as yes at function level, bounded sets). Plan first:
retrieval question 7 + `#order` IA row + EN-17/EN-18 rows in
`en/ru/SITE_PLAN.md`; retrieval question 8 + `#clauses` IA row + DE-18 row in
`de/ru/SITE_PLAN.md` (all bounded, no connector lexicon, DE-X02/EN-X02).

Changed units:

| Unit | Change |
| --- | --- |
| EN `order` section, new flavour-words card (EN-17) | just/actually/still/even/though with Russian decision-equivalents; examples *I like it, though* / *Even a child can do it* |
| EN `flavor-words` dialog | just (только что vs просто, cross-ref Perfect), actually false friend (≠ «актуально»), still-vs-yet, even, sentence-final though |
| EN `order` section, new linking-words card (EN-18) | but/however, so/therefore, meanwhile, nevertheless, although/though, despite with Russian equivalents |
| EN `linking-words` dialog | however register + comma rule; meanwhile; nevertheless; **despite + noun vs although + clause** trap |
| DE `clauses` section, new linking-adverbs card (DE-18) | deshalb/trotzdem/allerdings/außerdem/währenddessen with Russian equivalents; position-1 + V2 rule |
| DE `linking-adverbs` dialog | deshalb example; **trotzdem (adverb, position 1) vs obwohl (conjunction, verb-end)** + «trotzdem, dass» colloquial note; V2/coordinators cross-refs |
| `sw.js` | CACHE_VERSION v15 → v16 |

Unit-quality self-review (author level; formal Accuracy gate stays NOT RUN,
D-01): connector functions are closed-class and stable; register labels
(higher-formal however/therefore/nevertheless) present; the two classic
RU-interference traps (despite+clause, trotzdem dass) carry visible limits;
DE position-1 behaviour ties into the existing V2/inversion and denn
coordinator cards without contradiction. Practice untouched (three-item
contracts, X05).

Verified: JSON valid; both `--check` gates exit 0 (all new data-search tokens
visible on their cards — validator enforces); mixed-script scan clean;
runtime smoke — EN search «meanwhile»/«actually» surface the new cards,
DE search «währenddessen» surfaces the card; all three dialogs open with
expected content; no console errors.

Gate impact: Coverage stays **PASS** — DE 18/18, EN 18/18 required topics
(inventories extended and covered in the same change; no unmapped content).
Baseline still **FAIL** (remaining open scope questions). Accuracy/Teaching
NOT RUN. DE-G10, EN-G09, EN-G10 decided and closed.

## 2026-09-13 — Scope additions: Tier-1 A1-core (DE-19–23, EN-19/20, EN-05 always) + shell automations

Protocol §5 changed-unit record. Author: ZCode session; scope per the
owner-approved ROADMAP standing rules (Tier 1 items pre-authorized; EN-G08
Recommended accepted by the owner's «давай так» on the todo). Plan first:
inventory rows DE-19–23 and EN-19/20, IA rows (Формы, Глагол и порядок,
Времена, Порядок), EN-05 depth amendment in both SITE_PLANs.

Changed units:

| Unit | Change |
| --- | --- |
| DE-19 `extras` card + `conjugation` dialog | Present endings table (spielen/sein/haben, hot cells + honest legend); dialog: -t/-d insert -e-, vowel change (liest, fährt) du/er only, sein/haben as tables |
| DE-20 `forms` card + `negation` dialog | kein (ein-pattern, for nouns) vs nicht (everything else); placement: sentence-final default, pre-word when negating that word; kein declension |
| DE-21 `order` card + `imperative` dialog | du/ihr/Sie formulas, Seien Sie; dialog: du drop -st, vowel change kept (Gib!, Lies!), umlaut lost (Fahr!), -t/-d +e (Warte!), sein exception |
| DE-22 `verbs` card + `praeteritum` dialog | Recognition: war/hatte/wollte/konnte/musste/sollte (surfaced on card after validator flag), regular -te; spoken-Perfekt vs written boundary; recognition-level → glossed examples |
| DE-23 `extras` card + `comparative` dialog | -er/am -sten, umlaut group, gut/viel/gern irregulars on card; than = als |
| EN-19 `order` card + `there-is` dialog | there is/are; negatives/questions without do (ties to C-14 rule); was/were; There's vs It's |
| EN-20 `tenses` card + `past-continuous` dialog | was/were + -ing background vs Past Simple event; parallel actions (meanwhile cross-ref); Russian-aspect mapping |
| EN-05 card + `present-continuous` dialog | PC + always = irritation amendment (EN-G08) |
| `tools/` + `site.json` | `--check-shell` (landing DECKS/links + sw APP_SHELL vs registry — closes the landing hand-mirror drift risk); audience script as data (`"script": "cyrillic"` in site.json, validator reads it instead of the hardcoded Cyrillic range — pre-Phase-3 for Latin-script audiences); `grammar_terms[de]` += komparativ, superlativ |
| `sw.js` | CACHE_VERSION v16 → v17 |

Unit-quality self-review (author level; formal Accuracy gate stays NOT RUN,
D-01): forms checked against contemporary standard usage — arbeiten→du
arbeitest, lesen→du liest, fahren→du fährst; imperative Gib!/Lies!/Fahr!
(umlaut lost), Warte!, Seien Sie; Präteritum machte/-te with 1st=3rd person;
comparatives älter/größer/wärmer, gut–besser–am besten, viel–mehr–am
meisten, gern–lieber; there is/are with uncountable-singular There's;
was cooking when he called frame. The validator caught my own C-13-class
slip (Präteritum forms in search but dialog-only) during the build — the
gate works as designed and the forms were surfaced on the card.

Verified: JSON valid; `--check` ×2, `--check-shell` ×2 exit 0; mixed-script
scan clean; runtime smoke — all seven search routes (spielt, никакой,
повелительное, präteritum, komparativ, there is, пока) surface the new
cards; conjugation/praeteritum/there-is/past-continuous/present-continuous
dialogs open with expected content; `lang="de"`/`lang="en"` marking applies;
no console errors.

Gate impact: Coverage stays **PASS** — DE 23/23, EN 20/20 required topics
(inventories extended and covered in the same change). Baseline still
**FAIL** (open: DE-G05 plural formation only, DE-G06, DE-G07, DE-G08,
EN-G02, EN-G04, EN-G05, EN-G06 remainder, EN-G07). Accuracy/Teaching
NOT RUN.
Seven scope questions decided and closed this change.

## 2026-09-21 — Scope addition: DE-24 plural formation (DE-G05 decided) + EN-13 gap-fill

Tier-2 candidate from ROADMAP executed per the standing rules (plan-first →
deck → gates → audit → local commit). Research pass: no dedicated plural
source in `research/` (British Council A1–A2 sample itself lacks a plural
lesson); content built on the standard Duden/Collins gender-heuristic model —
five ending patterns with the honest «no single rule» limit, not a
word-by-word table.

- **DE-24** (`de/ru/SITE_PLAN.md` + deck): new card «Plural: ставка по роду»
  in `#extras` after the Dativ-Plural card — fem → -en/-n, mask → -e,
  neut → -er (umlaut group), unchanged -er/-el/-en, loanwords → -s; dialog
  `plural` carries depth (suffix groups -ung/-heit/-keit/-schaft/-ion,
  -chen/-lein, compounds pluralize on the last root, Dativ-Plural +n
  cross-reference, dictionary limit, der/die/das dependency note).
- **EN-13 depth extension** (within accepted plan depth «Core rules»):
  card rule line + example now contrast consonant+y → -ies with vowel+y →
  +s (days) and name -f/-fe → -ves (leaves); `plurals` dialog gains the
  vowel+y contrast and an «-f → -ves» block with the roofs/chiefs limit.

Verified: JSON valid; `--check` ×2 exit 0 (search-token visibility gate
passes with the new tokens plural/frauen/stühle/kinder/autos); regenerated
pages contain the new card and dialog. Scoped runtime smoke (localhost:8931,
stale-SW reset): DE search «plural» surfaces the new card (next to the
article tables and Dativ Plural), `plural` dialog opens with all eight
blocks incl. the Dativ-Plural cross-reference; EN search «plural» isolates
the plurals card, `plurals` dialog shows the -f → -ves block, the vowel+y
contrast and the intact countability caveat; console clean on both pages;
390px — no page or card overflow. Offline reload, theme cycle and redirect
checks: **NOT RUN** this pass.

Gate impact: Coverage stays **PASS** — DE 24/24, EN 20/20 required topics
(DE inventory extended and covered in the same change). Baseline still
**FAIL** (open: DE-G06, DE-G07, DE-G08, EN-G02, EN-G04, EN-G05, EN-G06
remainder, EN-G07) — DE-G05 fully decided, no open piece remains. Baseline
Accuracy/Teaching NOT RUN.

Independent two-reviewer pass after the commit (content/linguistic +
docs/process, both read-only): no P1 — all 16 German example pairs and the
English rules verified correct, `--check` gates re-confirmed. Fixed same
day: 1×P2 (compound-nouns example bolded the first root in the singular but
the plural marker in the plural — now bolds the last root on both sides,
matching the block's own rule) and 5×P3 (dead cross-reference
«карточка der/die/das» → «карточку „Определённый артикль“»; lowercase Latin
«plural» in RU text → «множественное число»; «много/многие с умлаутом»
drift unified; EN dialog label «-f → -ves» → «-f/-fe → -ves»; DE-24 plan row
under-promised the shipped dialog depth — depth clause appended).

## 2026-09-21 — Scope addition: DE-25 demonstratives, dieser family (DE-G11 decided)

User accepted the DE-G11 recommendation in-session («Ok, надо добавить») the
same day it was filed. Plan-first per the standing rules.

- **DE-25** (`de/ru/SITE_PLAN.md` + deck): card «dieser / diese / dieses»
  (anchor `forms-dieser`, badge A1/формы) in `#forms` group 0, directly
  after the article tables — RU «этот/тот» collapse into one word, the
  generating rule dies- + der-word endings, examples across genders plus
  an Akkusativ sentence. Dialog `dieser` carries depth: the full
  Nom/Akk/Dat model against der/die/das, the «этот/тот» collapse, welcher-
  as the same pattern with a question-answer pair, dieser-vs-der plus the
  das-not-dieser rule for «это»-phrases (Das ist schön), and the
  adjective-endings cross-reference to DE-16.
- Bounded set: dieser family + welcher- pattern; no demonstrative lexicon
  (jener, solcher and per-case paradigms stay out — the article table
  remains the single declension source).

Verified: JSON valid; `--check` + `--check-shell` exit 0 (search tokens
dieser/dieses/diese visible on the card; anchor slug `dieser` unique).
Scoped runtime smoke (localhost:8931, stale-SW reset): search «dieser»
surfaces the card with the A1 badge, anchor `forms-dieser` present,
`dieser` dialog opens with all five blocks verified, console clean, 390px
— no page overflow. Offline reload, theme cycle and redirect checks:
**NOT RUN** this pass.

Gate impact: Coverage stays **PASS** — DE 25/25, EN 20/20 required topics
(DE inventory extended and covered in the same change). Baseline still
**FAIL** (open: DE-G06, DE-G07, DE-G08, EN-G02, EN-G04, EN-G05, EN-G06
remainder, EN-G07). Accuracy/Teaching NOT RUN.

## 2026-09-23 — DE-05 depth: polite Ihr construction (DE-G12 decided)

User probe: «Я пытаюсь понять как использовать строить Ihre и не нашёл в
шпоре». The declension mechanics were on-page (DE-05 table + «Модель»
block), but the owner→stem chain — Sie → Ihr (вежливое) versus sie → ihr
(её/их) versus du → dein — was never stated, so the polite form could
not be assembled from the sheet. User constraint recorded: the sentence
that triggered the question stays out of the deck; the block teaches the
construction.

- `possessives` dialog: new block «Ihr — от Sie» — du → dein ·
  Sie → Ihr (Ваш, с большой буквы) · sie → ihr (её/их), then the
  ein-word ending by gender/case: die Adresse (Fem., Nom.) → deine /
  Ihre Adresse · das Auto → dein / Ihr Auto · den Bruder (Akk.) →
  deinen / Ihren Bruder.
- `ein-words` search keywords extended with Ihr, Ihre, Ваш, вежливое —
  searching the polite form now surfaces the card.

Verified: JSON valid; `--check` (both decks) exit 0; scoped runtime smoke
(localhost:8931, stale-SW reset): search «Ihre» leaves `forms-ein-words`
visible, the chip opens the dialog with all four new-block assertions
passing, console clean. Offline reload, theme cycle, redirect and
practice checks: **NOT RUN** this pass (content-only change inside an
existing dialog slot).

Gate impact: none — DE-05 was already Required and covered; this
deepens an accepted topic. Coverage stays **PASS** (DE 25/25, EN
20/20). Baseline still **FAIL** (open: DE-G06, DE-G07, DE-G08, EN-G02,
EN-G04, EN-G05, EN-G06 remainder, EN-G07). Accuracy/Teaching NOT RUN.

## 2026-09-24 — Correction pairs: sondern vs aber (DE-08), not … but (EN-18) (DE-G13, EN-G11 decided)

External agent advice to the user («sondern = не A, а B после отрицания;
aber = просто но») prompted a both-language coverage check. Finding: the
DE deck listed sondern among coordinators and used it once inside a
negation example without ever stating the choice rule versus aber; the EN
deck had no *not X, but Y* / *not only … but also* pattern at all. The
correction pair is the same learner problem on both pages — Russian «а»
covers both the plain-contrast and the correction reading, so the
distinction must be carried by the target language. Sources: Olesen
Tuition (aber-vs-sondern, *keinen Fisch, aber Fleisch* error example),
YourDailyGerman (sondern), BBC Bitesize (coordinating conjunction
examples), Cambridge Grammar (Conjunctions: contrasting — not…but, not
only…but also), British Council LearnEnglish (contrasting ideas).
Completeness verdict: the contrast family is otherwise covered on both
pages (DE: coordinators + DE-18 adverbs deshalb/trotzdem/allerdings; EN:
but/however, nevertheless, although/despite) — the correction pair was
the genuine gap on both. Remaining contrast linkers (EN while/whereas,
on the other hand) filed as EN-G12, defer-leaning.

- DE-08 `konnektoren` card: second example pair *Sie kommt nicht aus
  Bukarest, sondern aus Deva.* with deciding-hint gloss; new
  «sondern vs aber» chip; search keywords extended.
- DE new `sondern` dialog: correction (sondern) vs plain contrast
  (aber) with the error pair, *nicht nur …, sondern auch*, position-0
  word-order note, and the RU «а/но» collision note.
- DE `negation` dialog: «Перед словом» block now names the «а» =
  sondern link after its existing example.
- EN-18 `linkers` card: new chip *not (only) … but* + second example
  pair (*not on Monday, but on Tuesday* · *not only smart but also
  kind*) with glosses; search keywords extended.
- EN new `not-but` dialog: both patterns, the plain-but boundary, and
  the within-sentence position note (vs sentence-starting however).
- Plans revised first (DE-08 and EN-18 acceptance depth); ROADMAP
  gains the EN-G12 Tier-2 candidate.

Verified: JSON valid; `--check` (both decks) exit 0 including the
search-hygiene gate — tokens *nur/auch/correction* were rejected by the
gate because dialogs are not card-visible, and were trimmed rather than
exempted (C-13 discipline); scoped runtime smoke (localhost:8931,
stale-SW reset): search «sondern» keeps only `clauses-konnektoren`
visible and «not only» only `order-linkers`, both new chips open their
dialogs with all blocks present, console clean, ~390px no horizontal
overflow on either page, dark-mode dialog renders correctly.
Offline reload, theme cycle, redirect and practice checks: **NOT RUN**
this pass (content-only change inside existing card/dialog slots).

Gate impact: none — DE-08/EN-18 were already Required and covered;
this deepens accepted topics. Coverage stays **PASS** (DE 25/EN 20
topics). Baseline still **FAIL** (open: DE-G06, DE-G07, DE-G08, EN-G02,
EN-G04, EN-G05, EN-G06 remainder, EN-G07). Accuracy/Teaching NOT RUN.

Presentation follow-up, same day (user-reported, two rendering records in
`UI_AUDIT.md` #16 + `.design/decisions.md` 2026-09-24 entries — not a
content-semantics change): dialog commentary moved into a separate
`comment` field rendered as a muted line. 30 DE + 11 EN blocks with a
separable « — »-tail were restructured verbatim (no wording changes);
interleaved paradigm commentary stays inline by design. Recognition-level
translation glosses (Passiv, double infinitive) now sit in the comment
line — same gloss text, better decodability. `--check` gates green after
the sweep; all other gates NOT RUN (presentation-only).

## 2026-09-24 — Scope completion: Tier-2 batch (DE-26–28, EN-21–26); no open scope rows

Protocol §5 changed-unit record. Author: ZCode session; scope per the
owner-approved ROADMAP standing rules (Tier 2 lean-adds) plus the owner's
«let's review such issues and fix them all» directive for the remaining open
questions. Plan first: inventory rows DE-26–28 and EN-21–26, IA rows (Падежи,
Формы; Артикли и слова, Времена, Порядок, Глаголы) in both SITE_PLANs.

Changed units (all in current deck conventions: anchor slug, level/kind
badges, hit-highlighting, gloss pairs):

| Unit | Change |
| --- | --- |
| DE-26 `preps` card + `verb-preps` dialog | verb+preposition pairs (warten auf, denken an, sich freuen auf/über, sich interessieren für, teilnehmen an); case from the preposition (Wen?-trick); sich-reflexives recognition |
| DE-27 `forms` card + `article-choice` dialog | der/ein/kein three-way choice (first-mention pair ein→der Hund); professions without an article |
| DE-28 `preps` card + `seit-vor` dialog | seit + Dativ with Präsens (not PP — English contrast in dialog) vs vor + Dativ with a past event; Dativ-plural -n visible (seit zwei Jahren, cross-ref DE-15) |
| EN-21 `verbs` card + `negation` dialog | don't/doesn't/didn't + base; never without not (double-negative trap vs «никогда не»); no vs not any; never as a frequency adverb |
| EN-22 `tenses` card + `pp-continuous` dialog | PPC recognition: have/has been + V-ing; result-vs-process pair; Russian «уже» mapping; state-verb exception |
| EN-23 `verbs` card + `relatives` dialog | who/which/that by noun type; whose/where; object-that omission; antecedent agreement |
| EN-24 `verbs` card + `imperative` dialog | base form without subject; please + base (no to); Don't + V1; Let's / Let's not; Could-you politeness cross-ref |
| EN-25 `order` card + `contrast-linkers` dialog | while (time AND contrast), whereas, on the other hand register pair (EN-G12) |
| EN-26 `nouns` card + `numbers-dates` dialog | ordinals with spelling traps (fifth/twelfth/ninth), on 5 May / on the 5th of May, years and decades (ordinal registered in `grammar_terms_common`) |
| `sw.js` | CACHE_VERSION v26 → v27 |

Unit-quality self-review (author level; the formal Accuracy gate stays NOT
RUN, D-01): forms checked against contemporary standard usage —
warten auf + Akk, freuen auf (future) vs über (past/present), seit zwei
Jahren (Dativ plural -n, DE-15 cross-ref), PPC state-verb exclusion, that-
omission only before a subject, Let's not. Cross-references verified real:
DE-15 (Dativ plural), DE-25 (dieser sibling), EN-06 (PP duration), EN-18
(linking), EN-20 (meanwhile/past continuous), EN-12 (time preps), modals
(could-you). No unmapped content added.

Verified: JSON valid ×3; `--check` ×2 and `--check-shell` exit 0; runtime
smoke — DE search warten/известный/с тех пор and EN search никогда/свежий/
который/повелительное/тогда как/порядковые surface the new cards; verb-preps
/seit-vor/negation/pp-continuous dialogs open with expected content; anchors
preps-verb-praep and preps-seit-vor present; no console errors.

Gate impact: **no Open scope rows remain** (DE-G01–G13 and EN-G01–G12 all
decided; reported speech recorded as Deferred with a reconsideration
trigger). Baseline FAIL narrows to the unsourced-level-placement conjunct
(C-03/D-02 reference comparison) — topic inventory, exclusions and decisions
are complete. Coverage PASS maintained: DE 28/28, EN 26/26. Accuracy and
Teaching NOT RUN (D-01).

## 2026-09-29 — Practice view removed (scope decision, plans DE-D01/EN-D01)

- Decision owner: the site author, in the 2026-09-29 header-redesign
  review (dad-verified brief). The three static reveal questions had no
  replay value; practice returns only as a designed pool/shuffle surface
  (DEBT D-03). Not a content-quality verdict on the three items — a
  product-scope call, so it is recorded here as a verdict on scope, and
  the removed content stays recoverable in git history.
- Scope: all four decks (`de-ru`, `en-ru`, `de-en`, `en-de`). DE decks
  drop their fifth nav destination (5→4 views); EN decks lose the
  footer-only practice link. `#practice` anchors are gone by design
  (unknown hashes degrade gracefully — accepted).
- Machinery: `schema.json` (practice no longer required), `deck_render`
  (`practice_html`, `@@FOOTER_PRACTICE@@`, reveal tokens removed),
  `deck_validate` (practice shape checks retired; reveal strings off the
  required list), `site.json` (the practice-card search-token exemptions
  `practice`/`quiz`/`test`/`üben` pruned per its own hygiene rule).
- Sweep: help-dialog nav copy corrected in all four decks («Четыре
  раздела…» / «Пять разделов.» / "Four views…" / "Fünf Bereiche unten."),
  `footer_practice` strings deleted, reveal strings deleted, plans
  updated before pages (view tables, deferred entries DE-D01/EN-D01,
  X05 rationales), DEBT D-03 rewritten / D-05 closed / D-08 note,
  DESIGN_SYSTEM + style-guide specimens follow the removal.
- Gates: `--check` ×4, `--check-siblings` ×2, `--check-shell` — all
  green after regeneration. Accuracy/Teaching gates remain NOT RUN
  (D-01) and are unaffected: no grammar content changed.
