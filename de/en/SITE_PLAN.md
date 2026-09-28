# German Cheat Sheet — site plan (de-en)

## Responsibility and status

This file owns the accepted product intent, German content target, durable
scope decisions and language-specific information architecture for
`de/en/index.html` — German explained in English. It is the audience-variant
plan re-derived from the German canonical plan
([de/ru/SITE_PLAN.md](../ru/SITE_PLAN.md)); topic IDs DE-01–28, the five views
and the section skeleton are frozen from there, while every retrieval
question, interference story and acceptance decision below is re-derived for
English speakers. Use [the authoring guide](../../docs/SITE_PLAN_GUIDE.md)
when revising it.

It does not prove that the page matches the target or that the content is
correct. Those results belong in [CONTENT_AUDIT.md](../../CONTENT_AUDIT.md).
Shared UI behavior belongs in [the design system](../../.design/DESIGN_SYSTEM.md),
and operation and deployment belong in [README.md](../../README.md).

The page lives at `<target>/<audience>/` (`de/en/`) beside its Russian-audience
sibling (`de/ru/`), sharing the German target inventory. Section anchors and
card `id` slugs reuse the sibling's skeleton so cross-audience references stay
legible; once shipped they are stable forever (hard rule 7).

Status: this plan is the accepted content target for the `de-en` audience.
The deck JSON, page and icons shipped 2026-09-28 (commit ffe733b); the
interactive runtime smoke ran clean. Coverage is PASS (28/28 required rows;
see CONTENT_AUDIT.md §5). Accuracy and Teaching are NOT RUN per D-01 — a
whole-work linguistic review found no errors but is not the reference-cited
gate. The per-target baseline conjunct
(named-syllabus and reference comparison, C-03/D-02) is shared with `de/ru/`;
per ROADMAP Tier 3 it is done once per target and inherited by its audiences,
while the interference traps are re-derived per audience — that re-derivation
is what this plan carries.

## Product and learner

The product is a mobile-first German grammar lookup deck for English-speaking
A1–B1 learners. It should make common grammar decisions retrievable in one to
three taps, remain concise on the first layer, install as a PWA and work
offline after the first successful load.

The interface language is English: UI strings, dialogs, practice and search
hints are written in English; German terms stay German. The deck addresses the
learner directly as "you" (plain instructional register, contractions
welcome). German examples keep their natural du-register — du/Sie is taught
content (DE-04, DE-21), not the deck's voice.

It assumes no familiarity with German grammar terminology, and it cannot
assume case terminology at all: English marks case only in the pronoun pair
(I → me) and in the possessive 's, so that remnant is where the case concept
is built (DE-01). German terms (Akkusativ, Wechselpräpositionen, TeKaMoLo)
stay visible; where an English name helps, it is introduced with the English
remnant it matches (dative = the "to him" role). Examples use contemporary
Standard German as used in Germany. Austrian and Swiss variants appear only
when omission would predictably mislead the intended learner, and must be
labeled. Explanations use neutral international English; a British/American
difference is labeled only when it changes the taught choice or prevents a
likely error.

## Scope boundary

Required grammar topics are defined once in the inventory below. No additional
topic is implied by a heading, search keyword or content found on the page.
The five exclusions are the German target's durable product boundaries,
re-checked for this audience — the re-derivation changed none of them.

| Decision | Excluded content | Rationale | Reconsider when |
| --- | --- | --- | --- |
| DE-X01 | Pronunciation, phonetics and listening instruction | The product is a grammar lookup deck without audio | A pronunciation or audio learning surface is accepted |
| DE-X02 | Thematic vocabulary, phrasebook material and a comprehensive dictionary or conjugator | These require different retrieval and maintenance models | The product expands beyond grammar lookup |
| DE-X03 | Exhaustive exceptions and productive B2+ grammar | Density must serve the stated A1–B1 audience | The supported level expands or a reference review shows an A1–B1 dependency |
| DE-X04 | Systematic Austrian, Swiss and dialect comparison | Standard German is the default and regional comparison would dominate the deck | Repeated learner need or correctness risk justifies a labeled exception |
| DE-X05 | Course sequencing, mastery scoring and CEFR certification | Three practice items support retrieval; they are not an assessment system | The product adopts progress or assessment semantics |

There are no accepted deferred topics: every DE-01–28 topic re-derived with a
live English-interference story. The topics that came closest to deferral are
DE-11 and DE-12, because English already owns their decision structure
(*in order to / so that*; *If I had …, I would*) — they stay required because
the German forms and the deciding contrasts still have to be taught; their
rows say what is obvious instead. Unresolved candidate gaps for this audience
are findings in `CONTENT_AUDIT.md`, not silent exclusions or plan commitments.

## Primary retrieval questions

The first two questions exist because German marks on the article what English
marks on pronouns (I → me) or word position.

1. Which case is this noun — and which shape does the article take?
2. Which article, pronoun or adjective ending do I need?
3. Where does the finite verb go? (German keeps the *verb* in slot 2 even when
   English keeps the subject in front.)
4. How does the verb bracket change with modal, perfect and separable forms?
5. What changes in subordinate clauses? (The verb goes to the end — because,
   that and although change nothing in English.)
6. Which prepositions govern Akkusativ, Dativ or Genitiv?
7. Which particle carries the tone — doch, mal, denn, ja, schon, gar, wohl?
   (English carries these nuances with intonation and small adverbs.)
8. Which linking adverb connects the clauses — deshalb, trotzdem, allerdings,
   außerdem, währenddessen?
9. Can I see one short example and open a deeper explanation when needed?

## Information architecture

The page is a lookup deck with five view destinations, the German sibling's
skeleton with English view labels (short nav forms: Cases, Forms, Order,
Clauses, Review). Practice stays a bottom-navigation destination, as on
`de/ru/`.

| View | Stable anchor | Required topics |
| --- | --- | --- |
| Cases | `#cases` | DE-01, DE-02, DE-26, DE-28 (`#preps`) |
| Forms | `#forms` | DE-03–05, DE-20, DE-25, DE-27; DE-15–16, DE-19, DE-23–24 (`#extras`) |
| Verbs & word order | `#order` | DE-06–07, DE-09, DE-12–14, DE-21, DE-22 (`#verbs`), DE-17 |
| Subordinate clauses | `#clauses` | DE-08, DE-10–11, DE-18 |
| Review | `#practice` | Practice contract below |

The section skeleton is the sibling's seven sections (`cases`, `forms`,
`preps`, `order`, `verbs`, `clauses`, `extras`). `#start`, `#preps`, `#extras`,
`#verbs` and `#install-help` are stable direct anchors (the page is new —
nothing here is a legacy link, but the anchors keep the sibling's names). A
direct anchor opens the owning view before scrolling. Search covers all views
and restores the selected view when cleared. Install help remains a dialog
plus footer line rather than a content section.

## Content and practice contract

The shared card, dialog, search, navigation and accessibility mechanics are
defined in the design system. German-for-English-speakers content adds these
requirements:

- A first-layer rule gives the learner a trigger, form or position, and one
  short natural example. A dangerous simplification includes its essential
  limit on the card.
- Example glosses follow the rule type, with English glosses. Form and
  position rules (endings, case shapes, word order, conjugation, plural)
  keep examples in the target language only, with structural annotation —
  bold German fragments, der → den minimal pairs, `dem Mann = Dat.` labels;
  an English translation cannot demonstrate German morphology. Meaning/usage
  rules (seit vs vor, um … zu vs damit, nicht vs kein, der/ein/kein choice,
  particle tone) add a short English gloss carrying the deciding difference,
  not a full translation. Recognition-level constructions (double infinitive,
  Präteritum as a recognition topic, Perfekt Passiv) are a third class: the
  learner is not expected to decode the example, so it always carries a short
  English gloss — comprehension access to the sentence the rule is about, not
  the choice criterion. Declension fragments stay unglossed. A gloss that
  does not add the choice criterion is removed.
- German pattern text stays German; English explanations, italic hints and
  glosses stay in the English voice. This is a Latin-script audience, so the
  generator's target-voice tagging applies only to explicit bold/hit runs —
  every German fragment that needs the study voice is bold.
- Dialogs add reasoning, contrast or exceptions without contradicting the
  card. New tappable explanations use the page's `DETAILS` object (keys
  kebab-case; explanation in English, German terms in German). Dialog names
  reuse the sibling's keys where the same dialog exists.
- Search metadata mixes English intent words with German target terms; the
  Russian intent words of `de-ru` disappear entirely — they are the previous
  audience's words and would be dead tokens here. This is a Latin-script
  audience: strict search — every `data-search` token must be card-visible or
  registered in `site.json` (`grammar_terms[de]` for German terms,
  `grammar_terms_common` for English terms); the build gate enforces this on
  every `--check`.
- Practice has three contextualized items mapped to DE-03, DE-07 and DE-08 —
  the sibling's mapping, re-derived and kept: together the three items
  exercise the highest-risk decisions for English speakers (case shape after
  the verb — der → dem; the fronted adverb with V2 and the verb bracket;
  verb-final after weil). Each item's wording carries its English
  interference story (helfen takes a Dativ object where English *help* takes
  a bare object). Answers explain the choice and identify valid alternatives.
  Audit probes provide broader validation without bloating learner practice.

## Required content inventory

All rows are required in the current target. "Core" means a learner should be
able to choose or form the pattern; "recognition" means identify and
understand it. Each row names what transfers from English, what breaks, and
which example carries the point. Per-topic CEFR placement and page alignment
still require evidence in the content audit.

| ID | Learner question and required content | Surface | Acceptance depth |
| --- | --- | --- | --- |
| DE-01 | Which case? Nominativ, Akkusativ, Dativ and Genitiv with their roles and questions, built from the English pronoun remnant (I → me) and possessive 's | `#cases` | Core: rule and natural example per case; role questions stay German (Wer? Wen? Wem? Wessen?). Obvious: the roles themselves — subject, direct object, receiver, possessor all exist in English. Traps: English shows the role by position (I see the man), German writes it on the article (der → den), so *Den Hund sieht der Mann* keeps its meaning only through the articles; English *me/him* covers both direct and receiver roles, German splits ihn (Akk.) vs ihm (Dat.); Genitiv = the 's remnant (des Mannes ≈ the man's). |
| DE-02 | Which case follows a preposition? Fixed-case groups and Wechselpräpositionen | `#preps` | Core lookup plus location/direction contrast and movement caveat. Obvious: prepositions with arbitrary government — English trains this (depend on, wait for). Traps: English prepositions never change the noun; German ones decide the article's shape. The Wo?/Wohin? split exists in English as in/into (*in the house* / *walk into the house*) — in German it is in + Dativ vs in + Akkusativ; choosing the case by feel instead of by the preposition. |
| DE-03 | Which article ending? Definite, indefinite and kein patterns | `#forms` | Complete case/gender/plural reference plus usage examples. Obvious: the choice word transfers 1:1 (the = der/die/das, a = ein, no = kein). Traps: English *the* never changes shape; German's does — the ending is the case marker in action; grammatical gender is arbitrary for English speakers (die Brücke is not "she"), so nouns are learned with their article; kein = English *no* before a noun (*no money* → kein Geld). |
| DE-04 | Which personal-pronoun form? | `#forms` | Complete nominative/accusative/dative paradigm plus examples. Obvious: the case concept itself — English I/he/they → me/him/them is the one surviving English declension. Traps: English *me/him* serves both object and receiver, German splits ihn (Akk.) vs ihm (Dat.), often *to/for him*; du/ihr/Sie vs the universal English *you* — polite Sie (capital, written like "they") has no English counterpart. Example carries the point: Kennst du ihn? — Ich helfe ihm. |
| DE-05 | Which possessive and ending? mein, dein, sein, ihr, unser, euer, Ihr | `#forms` | Stems and case/gender/plural pattern plus examples. Obvious: my/your/his/her/our/their map stem-for-stem. Traps: English possessives never inflect — German mein takes ein-word endings (meinen Vater); sein = his or its; ihr = her, their AND the polite your (capital Ihr, built from Sie — the owner→stem step stated explicitly); euer → eure. |
| DE-06 | Where is the finite verb in statements, yes/no questions, W-questions and inversion? | `#order` | Core position patterns and contrasting examples. Obvious: plain statements read like English (Ich gehe heute…). Traps: English keeps the subject before the verb under all circumstances; German keeps the verb in slot 2 — Heute muss ich arbeiten where English says *Today I must…* (✗ Heute ich muss… is the signature error); yes/no questions are verb-first and there is no do-support (Sprichst du Deutsch? — no helper verb exists); W-questions behave like English (question word + verb). |
| DE-07 | How does the verb bracket work with modal, perfect and separable constructions? | `#verbs` | Formula and natural example per construction. Obvious: modal + infinitive (I must go ≈ ich muss … gehen) and Perfekt with haben is built like *I have eaten*. Traps: the two halves drift apart — finite verb second, infinitive/participle last, where English keeps them adjacent; sein + participle for motion/change (ist gegangen) where English uses *have* throughout; separable prefixes fly to the end (Ich stehe um 7 auf) — English phrasal particles mostly stay next to the verb; spoken Perfekt translates the English simple past (see DE-22). |
| DE-08 | Which conjunction changes word order? Subordinators and coordinators | `#clauses` | Verb-final rule, non-verb-final contrast and examples; after negation the correction pair takes *sondern* (*not A, but B*), plain contrast takes *aber*, *nicht nur …, sondern auch* in the coordinators dialog. Obvious: coordinators (und, aber, denn, oder, sondern) behave exactly like English and/but/for/or. Trap: because/that/although change nothing in English — weil/dass/obwohl send the verb to the end (✗ weil ich muss arbeiten is the signature error). The two splits English does not make: *if* is conditional wenn but embedded yes/no question ob (Ich weiß nicht, ob er kommt ≈ *I don't know if/whether he's coming*); *when* is wenn for the repeated or future case but als for the one-time past (Wenn ich Zeit habe, komme ich ≈ *when(ever) I have time* vs Als ich ein Kind war ≈ *when I was a child*). sondern is the *but* of corrections; English *not A, but B* maps 1:1 after nicht/kein, so the choice rule is a direct pair here (a lighter lift than for the Russian audience, kept for the same form reason). |
| DE-09 | Where do time, cause, manner and place phrases tend to go? | `#order` | TeKaMoLo as a default with an explicit limitation. Direct collision with English: English keeps time last and, with motion verbs, place before manner (*I'm going to Berlin by train today* — place, manner, time); German leads with time and ends with place (Ich fahre heute mit dem Zug nach Berlin) — ✗ Ich fahre nach Berlin heute is the predicted error. Dialog glosses show the reordered English. |
| DE-10 | How do relative clauses work? | `#clauses` | Rule, pronoun role and example with sufficient dialog detail. Obvious: whose is the surviving English genitive relative — dessen/deren ≈ whose. Traps: the German relative pronoun is the definite article in disguise — it copies the antecedent's gender and takes the case its own clause gives it (Der Mann, der hier arbeitet / …, den ich kenne); English may drop the object relative (*the man I know*), German never does; the clause is subordinate, so its verb goes last. |
| DE-11 | um … zu or damit? | `#clauses` | Same-subject decision and a contrasting pair. Obvious for this audience: English makes the same split — um … zu ≈ *in order to* (same subject: Ich lerne Deutsch, um in Berlin zu arbeiten ≈ *I'm learning German in order to work in Berlin*), damit ≈ *so that* (different subjects: …, damit du alles verstehst ≈ *so that you understand everything*). Trap: the zu-infinitive itself — separable verbs rejoin around zu (aufzustehen). |
| DE-12 | How is hypothetical meaning expressed? würde + infinitive and wäre/hätte/könnte/müsste/sollte | `#verbs` | Core high-frequency forms and examples. Obvious: English unreal conditionals already use past + would — *If I had time, I would travel* is structurally Wenn ich Zeit hätte, würde ich reisen; Könnten Sie mir helfen? ≈ *Could you help me?* Traps: würde with sein/haben — the English ✗ *If I would have* habit maps here; use the direct forms (hätte, wäre); würde vs wurde spelling. |
| DE-13 | How is the passive formed? | `#verbs` | Core werden + Partizip II formula and example. Obvious: be + participle → werden + Partizip II is an auxiliary swap (Das Haus wird gebaut ≈ *The house is being built*). Traps: English *is built* is ambiguous between event and state — German splits werden (event) vs sein + Partizip II (state); the agent is von + Dativ (*by*); Perfekt Passiv (ist gebaut worden) is recognition-level and glossed. |
| DE-14 | Why can a modal perfect contain two infinitives? | `#verbs` | Recognition note with one parsed example. English story: English solved the past modal with a different verb (*must* → *had to*); German keeps the modal and swaps its participle for an infinitive — Ich habe arbeiten müssen, not gemusst. The learner is not expected to decode it, so the example carries an English gloss (*I had to work*). |
| DE-15 | When does the noun change? Dativ plural, masculine/neuter Genitiv and N-declension | `#extras` | Endings, limits and examples. Obvious: Genitiv -s/-es is the English 's (des Vaters ≈ *father's*). Traps: otherwise English nouns never change — German also marks Dativ plural on the noun (mit den Kindern, -n when not already there) and N-declension weak nouns take -n/-en almost everywhere (den Studenten). Form rule — fragments stay unglossed. |
| DE-16 | Which adjective ending follows der-words and ein-words? | `#extras` | Compact overview and examples; no claim of exhaustive adjective declension. English story: English adjectives never inflect (*a good man*, *with the good man*) — this topic has no English anchor at all, the steepest new-form climb in the deck. The shortcut is the deck's own: the article already shows gender and case, so after der-words the adjective mostly echoes -e/-en. |
| DE-17 | Which particle carries the tone? doch, mal, denn, ja, schon, gar, wohl | `#order` | High-frequency set with English decision-equivalents and placement after the verb; bounded set — no particle lexicon (DE-X02). English story: there is no particle system — the tone rides on intonation and small adverbs, so each particle gets an English decision-equivalent: mal ≈ *just* (Komm mal her ≈ *come here a sec*), ja ≈ *after all / you know*, denn ≈ *then/so* in questions, doch ≈ *actually / on the contrary*, schon ≈ *I suppose*, gar ≈ *at all* (with nicht), wohl ≈ *probably*; placement after the verb stays the teachable form rule. |
| DE-18 | Which linking adverb connects the clauses? deshalb, trotzdem, allerdings, außerdem, währenddessen | `#clauses` | Position 1 + verb-second rule, English equivalents (so/therefore, nevertheless/even so, though/however, besides, meanwhile), trotzdem-vs-obwohl boundary; bounded set (DE-X02). Obvious: the English pairs all exist. Trap: a position-1 adverb forces inversion — Deshalb blieben wir zu Hause where English keeps subject–verb order after *Therefore* (✗ Deshalb wir blieben…); trotzdem (adverb, position 1) vs obwohl (conjunction, verb-final) is the same distinction English makes between *nevertheless* and *although*. |
| DE-19 | Which verb ending? Present of regular verbs, sein and haben | `#extras` | Full ich/du/er/wir/ihr/sie pattern + sein/haben; -t/-d insert -e- and vowel change in dialog. Obvious: German conjugates every verb the way English only conjugates *be* (am/are/is) — the table is new, the idea of an irregular *be* is not. Trap: English changes the verb once (she works); German marks ich/du/er differently (-e, -st, -t), and the plain English *you work* — identical to *I work* — invites ✗ du arbeite (the ich-form ending) where German needs du arbeitest; the flagged cells are du liest (vowel change) and du arbeitest (-e- insert). |
| DE-20 | nicht or kein? | `#forms` | kein for nouns (ein-pattern), nicht for everything else; placement before what is negated — rest-group first (heute nicht ins Kino), sentence-final only when nothing follows. Obvious: English owns both words — *no* + noun (*I have no money* → kein Geld) and *not* (everything else → nicht). Trap: German negates the verb directly, without do-support — Ich schlafe nicht = *I don't sleep*; the English *don't* must not be rebuilt with a helper verb; nicht placement follows the negated part, not the English after-the-auxiliary spot. |
| DE-21 | How do I command or request? | `#order` | du/ihr/Sie forms; sein exception; du vowel change and -t/-d +e in dialog. Obvious: the base-form command (Komm! ≈ *Come!*). Traps: English has one command form for everyone; German has three — Komm!, Geht!, Kommen Sie! (Sie inside the command has no English shape); Seien Sie ruhig ≈ *Be quiet* (sein irregular just like *be*); du-form details (Lies!, Fahr! without umlaut, Warte!) have no English parallels — pure form learning. |
| DE-22 | Präteritum — what is it and when? | `#verbs` | Recognition: war/hatte/modals + regular -te; spoken-Perfekt vs written boundary; recognition-level → glossed examples. Obvious: war/hatte/wollte map straight onto *was/had/wanted to* — the most English-friendly tense set in the deck. Traps: the register boundary runs against English habit — speech prefers Perfekt for regular verbs (Ich habe gearbeitet = *I worked*), so ich arbeitete sounds bookish; and Perfekt does NOT translate *I have eaten* — Ich habe gegessen is the spoken *I ate*. The one-German-tense/two-English-tenses mapping is stated on the card. |
| DE-23 | Comparative and superlative? | `#extras` | -er / am -sten, umlaut group, gut/viel/gern irregulars; than = als. Obvious: the irregulars are the same ones English owns — gut–besser–am besten = *good–better–the best*, viel–mehr–am meisten = *much–more–the most*; schneller = *faster*. Traps: am + superlative (am schnellsten, literally *at the fastest*) where English uses *the*; than = als (später als du), wie only for *as … as*; the umlaut group (älter, größer) has no living English pattern — *feet/geese* are the fossil. |
| DE-24 | How is the plural formed? Five ending patterns, guessed by gender | `#extras` | Feminin → -en/-n, Maskulin → -e, Neutrum → -er (umlaut group), unchanged -er/-el/-en, loanwords → -s; "no single rule" limit; Dativ-Plural cross-reference; suffix groups (-ung/-heit/-keit…), -chen/-lein and compounds in the `plural` dialog. English story: English adds -s and is done — five patterns with no single rule is the shock. Honest anchors from English's own relics: child/children and foot/feet are the same vowel-change idea as Kind/Kinder; sheep ≈ unchanged Lehrer; loanword -s (Autos) behaves like English. |
| DE-25 | this/that — which demonstrative? dieser/diese/dieses | `#forms` | dieser copies the definite-article pattern (dies- + der-word endings); the English this/that near/far split collapses — dieser covers both, and "that"-phrases use das (Das ist schön ≈ *That's nice*); welcher- same pattern as a question-answer pair (Welcher Bus? — Dieser Bus ≈ *Which bus? — This bus.*); dieser-vs-der and adjective-endings cross-references in the `dieser` dialog. |
| DE-26 | Which preposition follows the verb? | `#preps` | High-frequency verb+preposition pairs; case comes from the preposition (Wen/Wem question trick); sich-reflexives at recognition level. Obvious: English speakers already memorize arbitrary pairs (*depend on*, *wait for*, *listen to*). Trap: the preposition almost never matches — warten auf (*wait for*), denken an (*think about*), teilnehmen an (*take part in*), sich freuen auf (*look forward to*); the case rides on the German preposition (auf → Akkusativ: Ich warte auf den Bus); sich has no English equivalent (*I look forward* — no reflexive). |
| DE-27 | der, ein or kein? | `#forms` | Three-way choice: known / one of many / negation; professions WITHOUT the article — unlike English (Ich bin Lehrer = *I'm a teacher*; ✗ ein Lehrer is the predictable error). Obvious: the choice logic is English — first mention *a dog*, then *the dog*; negation *no* (kein). The first-mention pair ein → der matches English a → the exactly; the profession rule inverts the English habit and is stated on the card with its error pair. |
| DE-28 | seit or vor? | `#preps` | seit + Dativ = duration until now — with Präsens, where English uses the Present Perfect (Ich wohne seit zwei Jahren hier = *I have lived here for two years*); vor + Dativ = a point in the past (*ago*: vor zwei Jahren = *two years ago*). Traps: calquing the English perfect into Perfekt after seit; seit covers both English *for* and *since* (duration vs point — seit zwei Jahren / seit 2020); the Dativ plural -n is visible (seit zwei Jahren, DE-15 cross-reference). |

## Acceptance and maintenance

- **This page is generated**: `de/en/index.html` will be rendered from
  [`content/decks/de-en.json`](../../content/decks/de-en.json) — authored
  against this plan in the next phase, following the sibling deck's
  conventions as they stand that day — by
  `python3 tools/build_pages.py content/decks/de-en.json`. Edit the deck, not
  the HTML; regenerate and commit both. `--check` fails when they drift.
- Revise this plan before changing accepted scope, exclusions, content depth,
  practice mapping, view membership or stable anchors.
- Keep unresolved proposals in the content audit. Promote them here only after
  a Required, Deferred or Excluded decision is accepted.
- Apply [content validation](../../docs/CONTENT_VALIDATION.md) after content
  changes and record the reviewed revision, sources, findings and gate results
  in `CONTENT_AUDIT.md`. The `de-en` deck is a new deck: it runs the full
  content review, not a carry-over from `de-ru`.
- Follow `AGENTS.md` for shared page-change and runtime checks. A runtime pass
  does not establish content acceptance.
