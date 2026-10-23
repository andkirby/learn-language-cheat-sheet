# Content audit record — audience-variant decks de-en and en-de (2026-09-28)

Historical evidence moved verbatim from the root audit. Current status,
findings ledger and record index: [CONTENT_AUDIT.md](../../CONTENT_AUDIT.md).

## 2026-09-28 — New deck: de-en (German explained in English, audience variant)

Per-deck record per the ADD_LANGUAGE audience-variant route. Reviewer/
implementer: ZCode session (the deck's authoring phases plus this records
pass; not an independent linguistic reviewer — Accuracy and Teaching stay
NOT RUN, D-01). Reviewed revision: shipped as `ffe733b` ("feat: add de-en
deck (audience variant)") with two smoke-fix follow-ups (`532a433` —
target-voice bolding inside formula slots, `32ca941` — CACHE_VERSION
v30 → v31); every gate below was re-run for this record at HEAD `a0a7a70`,
tree clean apart from the never-stage untracked files (`.zcodeignore`,
`skills-lock.json`, `word-lists/`). Scope: full pass over
`content/decks/de-en.json` → `de/en/index.html` against
[the de-en plan](../../de/en/SITE_PLAN.md).

Method: adapted, not translated. Topic IDs DE-01–28, the five views and the
seven-section skeleton are frozen from the German target; every retrieval
question, interference story, gloss and search hint was re-derived for
English speakers per the plan — the Russian-audience explanations of
`de-ru` do not appear in this deck. No topics beyond the frozen inventory;
no deferrals (the plan records DE-11/DE-12 as the closest deferral
candidates and keeps them required with their "obvious for this audience"
halves stated on the rows).

Full inventory (44 cards, 41 content dialogs + `lookup-help`, 3 practice
items; sections `cases`, `forms`, `preps`, `order`, `verbs`, `clauses`,
`extras`; no duplicate card ids — counted mechanically over the deck JSON;
anchor uniqueness additionally enforced by the build gate):

| Topic | Units on the page | Adapted for English speakers (not translated) |
| --- | --- | --- |
| DE-01 | `faelle` case grid + `nominativ`/`akkusativ`/`dativ`/`genitiv` dialogs + `objects` card/dialog | case concept built from the I → me remnant and the possessive 's; English *him* splits into ihn (Akk.) vs ihm (Dat.) |
| DE-02 | `wo-wohin` card/dialog + `praep-akk`/`praep-dat`/`wechsel`/`praep-gen` cards + `prep-akk`/`prep-dat`/`two-way` dialogs | Wo?/Wohin? mapped to *in the house* vs *into the house*; English prepositions never change the noun, German ones decide the article's shape |
| DE-03 | `artikel` + `ein-words` cards (tables + honest legends) | *the* never changes shape — the ending is the case marker in action; gender is not logic (die Brücke is not "she") |
| DE-04 | `pronomen` card + `pronouns` dialog | three you-forms (du/ihr/Sie) vs the universal English *you*; helfen takes a Dativ object where *help* takes a bare one |
| DE-05 | ein-words card + `possessives`/`why-ein-endings`/`ihrem` dialogs | stems map my/your/his…; sein = his or its, ihr = her/their/the polite your (owner→stem step explicit) |
| DE-06 | `v2` + `inversion` + `w-fragen` cards + `v2` dialog | *Today I must…* vs Heute muss ich… (✗ Heute ich muss — the signature error); no do-support in questions |
| DE-07 | `modalverben` + `perfekt` + `trennbare` cards + `modal`/`perfekt`/`separable` dialogs | the bracket halves drift apart where English keeps them adjacent; sein for motion where English reaches for *have*; prefixes fly to the end |
| DE-08 | `weil`/`dass`/`wenn-als`/`obwohl`/`ob`/`konnektoren` cards + `wenn-als`/`obwohl`/`coordinators`/`sondern` dialogs | weil/dass/obwohl send the verb where *because/that/although* change nothing; wenn vs als and wenn vs ob — splits English does not make; sondern = *not A, but B* (1:1 pair here) |
| DE-09 | `tekamolo` card + dialog | English keeps time last (*I'm going to Berlin by train today*) — the predicted calque error |
| DE-10 | `relativsatz` card + `relative` dialog | the relative pronoun is the article in disguise; dessen/deren ≈ *whose*; English may drop it, German never does |
| DE-11 | `um-zu-damit` card + `um-damit` dialog | English already owns the split — *in order to* / *so that*; the zu-infinitive with separables is the trap |
| DE-12 | `konjunktiv2` card + `konjunktiv2` dialog | *If I had…, I would* is structurally the same; the ✗ *If I would have* habit and würde vs wurde are the traps |
| DE-13 | `passiv` card + `passive` dialog | an auxiliary swap (be → werden); English *is built* is ambiguous, German splits event (werden) vs state (sein + Partizip II) |
| DE-14 | `doppelinfinitiv` card + `double-infinitive` dialog | English solved the past modal with a new verb (*must* → *had to*); recognition-level, glossed |
| DE-15 | `dativ-plural` + `genitiv-s` + `n-deklination` cards + `n-decl` dialog | Genitiv -s = the English 's; otherwise English nouns never change — Dativ plural -n and N-declension are new |
| DE-16 | `adjektive` card + `adjectives` dialog | no English anchor at all — flagged on the card as the steepest new-form climb; the article-echo shortcut |
| DE-17 | `partikeln` card + `particles` dialog | no particle system in English — each particle gets an English decision-equivalent (*just, after all, then, probably…*) |
| DE-18 | `verknuepfungen` card + `linking-adverbs` dialog | the English pairs all exist; the trap is inversion after position-1 adverbs (✗ Deshalb wir blieben…) |
| DE-19 | `verb-endungen` card + `conjugation` dialog | German conjugates every verb the way English only conjugates *be*; *you work* = *I work* invites ✗ du arbeite |
| DE-20 | `negation` card + `negation` dialog | English owns both words (*no* + noun → kein; *not* → nicht); no do-support — never rebuild "don't" with a helper |
| DE-21 | `imperativ` card + `imperative` dialog | one English command form vs three German ones; Sie stays inside the command; sein irregular like *be* |
| DE-22 | `praeteritum` card + `praeteritum` dialog | war/hatte/wollte map straight onto *was/had/wanted to*; one German tense covers two English ones — stated on the card |
| DE-23 | `komparativ` card + `comparative` dialog | the irregulars are English's own (good–better–the best); am -sten = "at the fastest"; than = als |
| DE-24 | `plural` card + `plural` dialog | English adds -s and is done — five patterns, no single rule; child/children and foot/feet as English relic anchors |
| DE-25 | `dieser` card + `dieser` dialog | the English this/that near/far split collapses; "that"-phrases use das (Das ist schön); welcher- same pattern |
| DE-26 | `verb-praep` card + `verb-preps` dialog | English speakers already memorize arbitrary pairs, but the preposition almost never matches (*wait for* → warten auf); sich has no equivalent |
| DE-27 | `artikelwahl` card + `article-choice` dialog | the first-mention pair ein → der matches a → the exactly; professions drop the article — the opposite of English |
| DE-28 | `seit-vor` card + `seit-vor` dialog | calquing the English perfect after seit is the named trap; seit covers both *for* and *since*; vor = *ago* |

Whole-shell units were likewise re-authored in English: `meta` (brand
"German Cheat", title/description/og), `strings` (search placeholder
"Search: wem, weil, modal, Dativ…", no-results hint, install dialogs, theme
labels, footer; `footer_practice` deliberately absent as on the German
sibling — practice is a bottom-nav destination), the `help` entry ("How to
use" → `lookup-help`), the view labels (Cases, Forms, Order, Clauses,
Review), and the three practice items mapped to DE-03, DE-07, DE-08 (the
sibling's mapping, re-derived: each item's wording carries its English
interference story and surfaces valid alternatives — *einem Mann*, the
subject-first V2 order, the denn escape hatch).

Verified (re-run for this record at HEAD `a0a7a70`, tree clean):

- `python3 tools/build_pages.py content/decks/de-en.json --check` → exit 0
  ("de/en/index.html is up to date"); the three sibling decks also exit 0.
- `python3 tools/build_pages.py content/decks/de-ru.json --check-shell` and
  the same on `en-ru.json` → exit 0 — landing DECKS map and sw APP_SHELL
  match the registry (`de: [ru, en]`, `en: [ru, de]`).
- Coverage: **PASS** — plan→page: all 28 required topics mapped to the units
  in the table above; the plan's practice mapping (DE-03/07/08) is what the
  deck implements. Page→plan: every card, dialog, table and practice item
  maps back to a DE topic or a shell unit — no unmapped content (author
  review; the independent pass re-walks this, D-01).
- Search: strict Latin×Latin **by design** (D-06) — every `data-search`
  token is card-visible or covered by `grammar_terms`, enforced by the
  `--check` gate; the Russian intent words of `de-ru` appear nowhere in the
  index. This strictness is intentional, not a finding.
- Runtime smoke: HTTP-level re-check this pass (`http.server 8931`) —
  `/de/en/`, its manifest, all six icon files (incl. `icon-512-maskable.png`),
  root `sw.js` and `assets/base.css` return 200; `<html lang="en">`;
  `'../../sw.js'` registered. The interactive browser smoke ran during the
  shipping phases; its findings are fixed in `532a433` (German fragments
  inside formula slots on the `w-fragen`, `imperativ`, `modalverben`,
  `perfekt`, `trennbare`, `passiv`, `weil` and `komparativ` cards were
  untagged — a Latin-audience deck carries the target voice only on
  explicit bold/hit runs, so the slots were bolded) and `32ca941`
  (CACHE_VERSION bump); the interactive pass was **NOT RUN** again for this
  record.

Gate verdicts: Baseline **FAIL** — the per-target conjunct (named-syllabus
and reference comparison, C-03/D-02) is shared with the German target and
still outstanding; inventory and exclusions are complete and were re-derived
for this audience. Coverage **PASS** (28/28). Accuracy **NOT RUN** and
Teaching **NOT RUN** — de-en is a new deck and joins the D-01 independent-
pass queue.

## 2026-09-28 — New deck: en-de (English explained in German, audience variant)

Per-deck record per the ADD_LANGUAGE audience-variant route. Reviewer/
implementer: ZCode session (authoring phases plus this records pass; not an
independent linguistic reviewer — Accuracy and Teaching stay NOT RUN,
D-01). Reviewed revision: shipped as `a0a7a70` ("feat: add en-de deck
(audience variant)", which also bumped CACHE_VERSION to v32); every gate
below was re-run for this record at that same HEAD, tree clean apart from
the never-stage untracked files. Scope: full pass over
`content/decks/en-de.json` → `en/de/index.html` against
[the en-de plan](../../en/de/SITE_PLAN.md).

Method: adapted, not translated. Topic IDs EN-01–26, the views and the
eight-section skeleton are frozen from the English target; every retrieval
question, interference story, gloss and search hint was re-derived for
German speakers. The direction of the deck is reversed relative to `en-ru`:
the case concept arrives for free (der Vorteil gegenüber en-ru), and the
load sits on tenses, auxiliaries and rigid word order. No topics beyond the
frozen inventory; no deferrals (EN-24/EN-25 recorded in the plan as the
closest candidates, kept required). Registry note per the plan: the dead
`en`/`en` self-pair "soon" placeholder was **replaced** by the live German
audience (`en: [ru, de]`), not supplemented — the `--check-shell` gate now
guards exactly the four live pairs.

Full inventory (38 cards, 40 content dialogs + `lookup-help`, 3 practice
items; sections `articles`, `pronouns`, `order`, `tenses`, `verbs`, `preps`,
`nouns`, `conditionals`; five bottom-nav views with German labels (Artikel,
Zeiten, Satzbau, Verben, Präpositionen) and practice footer-only
(`footer_practice` present), as on the `en-ru` sibling; no duplicate card
ids — counted mechanically, anchor uniqueness enforced by the build gate):

| Topic | Units on the page | Adapted for German speakers (not translated) |
| --- | --- | --- |
| EN-01 | `articles` + `zero-article` cards + `a-an`/`the-article`/`zero-article`/`school-exceptions` dialogs | the choice transfers (the/a ≈ der/die/das/ein, no Genus to memorize); the boundaries interfere both ways (*go to school*; Ich bin Lehrer → I'm **a** teacher); a/an sound rule is new |
| EN-02 | `pronouns` card + `my-mine`/`reflexive` dialogs | the case concept is only recognized, not built (I/me as the surviving Kasus); *you* covers du/ihr/Sie; sein → his AND its, ihr → her AND their are new splits |
| EN-03 | `svo` + `frequency` cards + `svo`/`frequency` dialogs | free German reordering becomes rigid SVO — position alone carries the roles; the Mittelfeld calque (✗ *I go always*) and the V2 calque (✗ *Never I have seen*) are named |
| EN-04 | `do-questions` card + `do-questions` dialog + `mistakes` card | do-support is the deck's most alien mechanic (✗ *Likes she tea?* ← *Mag sie Tee?*); be/modals invert like German; subject questions transfer |
| EN-05 | `present-simple` + `present-continuous` cards + `present-simple`/`present-continuous` dialogs | only the 3rd-person -s is new; the Verlaufsform is pure new material — *Ich arbeite* covers both; PC + always irritation kept |
| EN-06 | `past-simple` + `present-perfect` + `pp-vs-past` cards + `past-simple`/`present-perfect`/`pp-vs-past` dialogs | the Perfekt calque is Gefahr Nr. 1 (✗ *I have seen it yesterday* ← *Ich habe den Film gestern gesehen*); meaning-first rule kept; the *since 2020* counterexample stays on the card; seit splits into since/for |
| EN-07 | `future` card + `future` dialog | will ≈ werden, but the pauschale werden calque is the named error; *going to* has no German pendant (new material); the Fahrplan present transfers |
| EN-08 | `modals` + `mustnt` cards + `modals-en`/`mustnt` dialogs | the modal paradigm maps directly; **muss nicht ≠ mustn't** recorded as the deck's sharpest false friend; der müssen-Schluss transfers |
| EN-09 | `passive` card + `passive-en` dialog | werden + Partizip II → be + V3 is an auxiliary swap; von covers of/from/by — the ✗ *built from the workers* agent calque; only the five shown tenses claimed |
| EN-10 | `gerund-infinitive` card + `gerund-infinitive` dialog | German has no Gerundium — V-ing is new material; *stop smoking* vs *stop to smoke* meaning change; look forward to + -ing (✗ calque of *sich freuen, dich zu sehen*) |
| EN-11 | `time` + `place` cards + `time-preps`/`place-preps` dialogs | German *am* distributes over in/on/at; *an* means on AND at (Oberfläche oder Punkt?); am Wochenende BrE/AmE split |
| EN-12 | `dependent` card + `dependent-preps` dialog | German speakers already train fixed verb pairs — but the English preposition almost never matches 1:1 |
| EN-13 | `plurals` card + `plurals` dialog | ONE -s rule against five German patterns; child/children as the recognizable relic; false uncountables (*Informationen* → information, Knowledges → knowledge) |
| EN-14 | `countable` + `some-any` cards + `countable`/`some-any` dialogs | the viel/viele decision transfers; the partial some/any assignment (offers/requests) is Neulernen; ✗ *How much people?* |
| EN-15 | `comparative` card + `comparative` dialog | the gut–besser–am-besten trio is literal; German als means than AND as (✗ *bigger as*); no double comparative (✗ *more better*) |
| EN-16 | `cond0`–`cond3` cards + `cond0`/`cond1`/`cond2` dialogs | Type 2 is structurally Konjunktiv II (had ≈ hätte, would ≈ würde; were for all persons); no will after *if* — German allows Futur im wenn-Satz, English doesn't; wenn covers if AND when |
| EN-17 | `nuances` card + `flavor-words` dialog | the false-friend zone condensed: actually ≠ aktuell, even ≠ eben; just has two meanings; sentence-final though is a position German lacks |
| EN-18 | `linkers` card + `linking-words`/`not-but` dialogs | **also ≠ also** (deutsches also = so/therefore); despite/although = trotz/obwohl — the split transfers; the sondern pair (not X, but Y) goes 1:1 |
| EN-19 | `there-is` card + `there-is` dialog | *es gibt* covers is AND are — ✗ *There's many people* is the calque; negatives/questions without do; There's vs It's |
| EN-20 | `past-continuous` card + `past-continuous` dialog | German marks the Verlauf with *gerade* — gerade + Präteritum ≈ PC + Past Simple; while = während, the same dual use (transfer) |
| EN-21 | `negation` card + `negation` dialog | do-support in negation (✗ *I see not*); no = kein 1:1; never already negates like nie — the en-ru double-negative trap (russisch «никогда не») was dropped: no German analogue |
| EN-22 | `pp-continuous` card + `pp-continuous` dialog | recognition level; the seit-Satz double calque (✗ *I live here since two years* ← *Ich wohne hier seit zwei Jahren*) |
| EN-23 | `relatives` card + `relatives` dialog | der/die/das mark Genus/Kasus, the English relative marks animacy (✗ *The man which…*); that-omission and comma rules — German never drops and always commas; preposition stranding |
| EN-24 | `imperative` card + `imperative` dialog | one command form where German has three; the Sie-pronoun habit → ✗ *Sit you down please*; Let's ≈ Lass uns |
| EN-25 | `contrast-linkers` card + `contrast-linkers` dialog | while = während — the deck's lightest transfer; the remaining decision is register (whereas ≈ wohingegen, on the other hand) |
| EN-26 | `numbers-dates` card + `numbers-dates` dialog | decades the 90s ≈ die 90er; paired year-reading similar; the ordinal spelling traps (fifth/twelfth/ninth) and the on-dates/no-point format are new |

Whole-shell units were likewise re-authored in German: `meta` (brand
"Englisch-Spickzettel", title/description/og), `strings` (du-form
throughout; search placeholder "Suche: present, perfect, if, the…",
no-results hint, install dialogs, theme labels «Design: automatisch/hell/
dunkel», footer), the `help` entry («So geht's» → `lookup-help`), and the
three practice items mapped to EN-04, EN-05 and EN-06 — deliberately
shifted from the sibling's EN-01/04/06 per the plan: the article choice is
familiar to German speakers, so the three items exercise the systematic
top interferences instead (do-support, the missing Verlaufsform, the
Perfekt calque). Each item's German prompt carries its interference story
(*Mag sie Tee?*, *Es regnet gerade*, *Ich habe den Film gestern gesehen*).

Verified (re-run for this record at HEAD `a0a7a70`, tree clean):

- `python3 tools/build_pages.py content/decks/en-de.json --check` → exit 0
  ("en/de/index.html is up to date"); the three sibling decks also exit 0.
- `python3 tools/build_pages.py content/decks/de-ru.json --check-shell` and
  the same on `en-ru.json` → exit 0 — landing DECKS map and sw APP_SHELL
  match the registry; the replaced `en: [ru, de]` entry is what the shell
  now guards.
- Coverage: **PASS** — plan→page: all 26 required topics mapped to the units
  in the table above; the plan's shifted practice mapping (EN-04/05/06) is
  what the deck implements. Page→plan: every card, dialog, table and
  practice item maps back to an EN topic or a shell unit — no unmapped
  content (author review; the independent pass re-walks this, D-01).
- Search: strict Latin×Latin **by design** (D-06) — every `data-search`
  token is card-visible or covered by `grammar_terms` (`grammar_terms[en]`
  is intentionally empty; German searcher words ride the German glosses that
  sit on the cards), enforced by the `--check` gate; the Russian intent
  words of `en-ru` appear nowhere in the index.
- Runtime smoke: HTTP-level re-check this pass (`http.server 8931`) —
  `/en/de/`, its manifest, all six icon files, root `sw.js` and
  `assets/base.css` return 200; `<html lang="de">`; `'../../sw.js'`
  registered. The interactive browser smoke is **NOT RUN** for this record
  — unlike de-en, the git history records no separate en-de smoke-fix
  commits, so no shipping-phase interactive pass is evidenced here either;
  the interactive checklist (console, search, dialogs, theme, offline,
  390px) remains to be run for this page.

Correction (2026-09-28, after the whole-work review): the interactive
browser smoke for this page DID run in the shipping workflow and passed
clean — console empty; German search with restore-on-clear; all 40 detail
dialogs opened via chips and closed via ×, Escape and backdrop; practice
reveal; nav `aria-current` per view; theme cycle + persistence; 390px
overflow-free; offline reload from the primed cache. The page shipped
with no smoke-fix commits, which this record misread as absence of a
pass; the NOT RUN claim above is superseded by this note.

Gate verdicts: Baseline **FAIL** — the per-target conjunct (C-03/D-02) is
shared with the English target and still outstanding; inventory and
exclusions are complete and were re-derived for this audience. Coverage
**PASS** (26/26). Accuracy **NOT RUN** and Teaching **NOT RUN** — en-de is
a new deck and joins the D-01 independent-pass queue.
