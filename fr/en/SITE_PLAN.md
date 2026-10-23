# French cheat sheet — accepted target (fr-en)

## Responsibility and verification status

This file owns the accepted English-audience French content target for
`fr/en/`, authorized on 2026-10-23 after the [research proposal](../../research/fr-en-plan.md).
It is an accepted target, **not implementation evidence or linguistic acceptance**.
Current content-review gates and findings belong in
[CONTENT_AUDIT](../../CONTENT_AUDIT.md); runtime, offline and deployment
evidence belongs in [UI_AUDIT](../../UI_AUDIT.md). Source-backed author checks
do not count as independent review.

Follow [SITE_PLAN_GUIDE](../../docs/SITE_PLAN_GUIDE.md) for revisions and
[CONTENT_VALIDATION](../../docs/CONTENT_VALIDATION.md) for evidence. Shared UI
belongs in the [design system](../../.design/DESIGN_SYSTEM.md), integration in
[ADD_LANGUAGE](../../docs/ADD_LANGUAGE.md), operations in [README](../../README.md).

## Product, learner and language policy

Mobile grammar lookup for English-speaking A1–B1 learners: retrieve a decision,
form and meaning in one to three taps. This is a selective reference, not a
course, DELF syllabus or CEFR certification. Default: contemporary standard
French as taught in France, with conversational/formal labels and material
regional caveats. English explanations use neutral international English.
French grammatical terminology stays French with an English clue.

English interference determines the contrasts: articles with generic nouns,
possessives agreeing with the possessed noun, obligatory subject pronouns,
clitics before the relevant verb, tense viewpoint rather than English tense
conversion, and complement selection rather than word-by-word prepositions.
No grammatical terminology is assumed without a short explanation.

## Scope boundary

All 63 Required topic IDs below are accepted at their stated bounded depths.
FR-01/02 share a card; FR-61 is Deferred. Compound relatives FR-51 are
recognition only; their full productive matrix is Deferred. B1 mood, voice,
agreement and reporting cannot be silently omitted to fit a card quota.

| ID / state | Boundary and rationale | Reconsideration trigger |
| --- | --- | --- |
| FR-61 / Deferred | Nominalisation as an independent topic: open lexical derivation and noun selection need more than a reliable suffix card. Existing glosses may explain individual nouns without claiming this coverage. | Repeated lookup need for noun/verb transformation, with a bounded set and an inspected word-formation reference; or owner chooses comprehensive inventory coverage |
| FR-D01 / Deferred | Full subjunctive tense system, broad doubt/concession inventory, past-subjunctive recognition lesson; exceeds the bounded present B1 target. Present-only examples must not imply present subjunctive covers anterior events. | Reading evidence repeatedly blocked by anterior subjunctive, or accepted B1+/B2 depth with a separate unit and review |
| FR-D02 / Deferred | Exceptional participle agreement: following infinitives, faire/laisser, impersonal/measure cases, exhaustive reflexive taxonomy. Core counterexamples remain Required. | Real examples cannot be explained by the bounded rules; expand with a reviewed separate unit |
| FR-D03 / Deferred | Productive full compound-relative matrix beyond FR-51 Rec. E1 places the family at B1; reduction is a product choice, not a B2 assertion. | Learners need to compose these clauses, or the owner selects full productive B1 coverage |
| FR-D04 / Deferred | Past-frame reported speech/backshift, deictic conversion series and exceptions. | Accepted B2 extension or recurring past-report lookup need, with second-source nuance check |
| FR-D05 / Deferred | Past conditional, past counterfactual/mixed si patterns, future perfect and past infinitive. Separate systems cannot be implied by present conditional/pluperfect cards. | Required reading/writing use or accepted expanded level; dedicated sourced units |
| FR-D06 / Deferred | Bare present-participial clauses, verbal adjectives, perfect gerund and causative faire as systems. | Specific learner probe justifies a bounded card and grammar reference pass |
| FR-D07 / Deferred | Exhaustive conjugation dictionary, exhaustive verb/adjective-preposition lists, idiomatic pronominal verbs and fine modal pragmatics. | Frequency evidence identifies a finite missing frame; accept that frame rather than a general catalogue |
| FR-X01 / Excluded | Productive passé simple/passé antérieur and literary subjunctive paradigms; outside everyday lookup target. No separate literary recognition lesson initially. | Product becomes literary-reading oriented or learner evidence warrants a distinct recognition unit |
| FR-X02 / Excluded | Open vocabulary, thematic phrasebook, culture/letter-writing course and DELF task training. E1's non-grammar domains are not promised by this deck. | Product-intent change, not a grammar-coverage probe |
| FR-X03 / Excluded | General pronunciation/audio/phonetic course. Grammatical orthography and necessary elision limits remain in scope. | Explicit audio/pronunciation product decision |
| FR-X04 / Excluded | Course sequencing, retention assessment and on-page practice redesign; lookup probes belong in review evidence. | Separate practice/product authorization under existing owners |
| FR-X05 / Excluded | Reciprocal audiences, native-speaker French master and regional-language catalogues. English is the explanation language; useful register/variant notes remain allowed. | Actual audience demand and a new accepted audience plan |

## Primary retrieval questions

1. Which noun/article/adjective form conveys my meaning?
2. Which present, past or future construction fits this situation?
3. Which object am I replacing, and where does its pronoun go?
4. How do I ask, negate, request or express obligation?
5. Which time/place expression fits English for/since/in?
6. How do I connect a reason, condition, contrast or relative clause?
7. When does French require a different construction from English?

## Information architecture and stable anchors

Four views: `forms` (noun/determiner/adjective/adverb/number forms), `verbs`
(present/patterns/past/future/mood/voice), `sentences` (subjects/questions/
negation/presentatives/objects/replacement) and `connections` (place/time/
complements/relatives/conditions/reporting/links). Section/card values below
produce the permanent anchor `section-card`; dialog key = card slug.
FR-01/02 share `nouns-noun-forms` and dialog `noun-forms`. Other Required rows
have separate owners. New cards/sections may split a topic only with a plan
revision; published anchors remain stable. `#start` opens lookup help.

Cards at lower entry levels may have labeled deeper examples in their dialogs;
a badge indicates entry, not a universal CEFR allocation of every detail.
Search uses card-visible English intent and French forms, under strict Latin
search hygiene. No accentless matching is promised. Shared menu/navigation,
theme/skin, search and dialog behavior stays with the shared UI owner.

## Content-unit requirements

Each card has a retrieval question, useful form/decision model, at least one
natural French example with English `gloss`, and a visible limit preventing a
false standalone rule. Dialogs add meaningful contrasts, bounded paradigms and
exceptions with adjacent English `comment`. Every taught lexical fragment gets
a contextual clue; endings alone need no translation. Auxiliaries are explained
by function. No bare sentence formula without meaning support. Explicit
bold/hit runs identify French text for this Latin-script audience; French form comparisons use existing list/legend blocks with bold runs
and English meaning clues; plain table cells cannot carry explicit language markup. Dialog rules remain English.

Present subjunctive is bounded to common forms/obligation/emotion/will and
limited conjunctions; factual emotion can take subjunctive. Pluperfect covers
prior past, not the deferred counterfactual system. Passive production uses
present/compound past; simple gerund requires shared subject. Present-frame
reporting includes statements/questions/orders, not past-frame backshift.
Core agreement includes preceding COD/que and ordinary reflexive exceptions;
exceptional infinitive-following/causative systems remain Deferred.

No on-page practice or mastery scoring. Review probes belong in the audit.

## Required-topic inventory and acceptance depth

`P` = productive bounded use plus recognition. `Rec` = recognition with gloss,
not a promise to produce every form. Acceptance requires the complete specified
card/dialog depth, not one matching example. The named comparison is Eaquals/
CIEP et al., *Inventaire linguistique des contenus clés des niveaux du CECRL*
(2015), Annex E A1–B1, with Tex's French Grammar as grammar reference. Exact
links/sections and access date are in the [research source register](../../research/fr-en-plan.md#evidence-and-method).
Reference IDs E1/T1–T18 below point there; they are not review verdicts.

Routine supplement decisions: FR-11/48 extend the A2→B1 functional inventory
using Annex D; FR-42 introduces conversational ça at A1, demonstrative
replacement forms at A2 and de/relative completion at B1. This allocation is an
accepted teaching choice within E1's progression, not a universal exam rule.
FR-64 covers A1 number/date/time grammar justified by E1's A1 communicative
functions; it does not add a calendar-vocabulary course. FR-51 remains B1 Rec,
explicitly narrower than fully productive inventory coverage.

### Forms

| ID | Topic / learner question | Level; accepted state | Section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-01 | Noun gender: which agreement set? | A1 P; Required | `nouns/noun-forms`: learn noun with determiner, gender ≠ sex → common cues with exceptions | E1 A1.16; Tex index nouns |
| FR-02 | Noun plural: which written ending? | A1 P; Required | `nouns/noun-forms`: default -s with visible irregular limit → common -x/-aux and invariant forms | E1 A1.17; Tex index number |
| FR-03 | Articles: a/the/zero in English — what in French? | A1 P; Required | `determiners/articles`: un/une/des vs le/la/les/l' → generic reference, likes, professions and elision limits | T1 |
| FR-04 | Partitives: an unspecified amount or a whole category? | A1 P; Required | `determiners/partitives`: du/de la/de l' contrast → negation, être/contrast exceptions; do not confuse du with every de + le | T1 |
| FR-05 | Quantities: how much/many, measures and de? | A1→B1 P; Required | `determiners/quantity`: number/measure/quantity frame → de/d', beaucoup vs beaucoup de, comparisons of amounts, numeric distance/percentage frames | T2; E1 A1.19–20 |
| FR-06 | Possessive determiner: his/her or noun agreement? | A1 P; Required | `determiners/possessives`: agree with possessed noun → son/sa ambiguity, mon amie, body-part cross-reference | T2 |
| FR-07 | Demonstrative determiner: this/that + noun? | A1 P; Required | `determiners/demonstratives`: ce/cet/cette/ces → -ci/-là, contrast with pronouns | T2 |
| FR-08 | Adjective agreement: which ending? | A1→A2 P; Required | `adjectives/adjective-forms`: gender/number model → common irregulars; no universal “add e” rule | T3 |
| FR-09 | Adjective position: before or after, with what meaning? | A1→A2 P; Required | `adjectives/adjective-position`: default plus small pre-noun set → meaning-changing contrasts; not an absolute mnemonic | T3; Tex index position lessons |
| FR-10 | Comparison: more/as/less and the most? | A2 P; Required | `adjectives/comparison`: plus/aussi/moins…que, superlative → meilleur/mieux, adjective/adverb/noun distinctions | T3 |
| FR-11 | Tout and indefinite determiners: all/every/some? | A2→B1 P; Required | `determiners/indefinites`: tout/toute/tous/toutes before nouns → small quelques/certains/chaque set; contrast standalone forms | T2; E1 Annex D printed p. 51 / PDF p. 53 supplement |
| FR-46 | Degree, amount and frequency: very/too/enough/often? | A1→B1 P; Required | `adverbs/degree-frequency`: très vs beaucoup, trop/assez → frequency positions, environ/presque/autant; finite function set | T2–T3 |
| FR-47 | Manner adverbs: how, and in which position? | B1 P; Required | `adverbs/manner`: common -ment formation with limits → irregulars, simple/compound placement; no rigid universal position | T3 |
| FR-64 | Number/date/time grammar: how do I write a date or tell time? | A1 P supplement; Required | `numbers/dates-time`: cardinal/ordinal/date/time frames → premier vs other dates, grammatical number conventions; no calendar vocabulary catalogue | E1 A1 functions p. 56, not an Annex E grammar bullet |

### Verbs

| ID | Topic / learner question | Level; accepted state | Section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-14 | Regular present patterns: which ending? | A1 P; Required | `present/present-patterns`: regular -er/-ir/-re models → stem/spelling changes; not all -ir verbs follow finir | E1 A1.01; Tex index verb groups |
| FR-15 | Essential irregular present: which common form? | A1 P; Required | `present/present-irregulars`: être/avoir/aller/faire entry points → bounded venir/prendre/faire-family references; modal forms owned by FR-18 | E1 A1.01; Tex index irregular verbs |
| FR-16 | Ongoing/recent action: doing or just did? | A1 P; Required | `present/present-meaning`: present covers English simple/progressive → être en train de emphasis; venir de + infinitive for recent past | E1 A1.02/.05; Tex index present/passé immédiat |
| FR-17 | Reflexives: which se form and position? | A1→A2 P; Required | `patterns/reflexives`: subject-matched pronoun → reciprocal/idiomatic limit, negation, infinitive and compound positions; link agreement | T5; Tex index pronominal verbs |
| FR-18 | Ability, wanting, duty and necessity: infinitive or clause? | A1 P; Required | `patterns/modals-obligation`: pouvoir/vouloir/devoir + infinitive and il faut → no “to” inserted; il ne faut pas = must not, not need not | E1 A1.11–12; T10–T11 |
| FR-19 | Passé composé: how do I form a completed event? | A1 limited→A2 P; Required | `past/passe-compose`: auxiliary + participle, common avoir forms → irregular participles, negation; English past/perfect context | T4 |
| FR-20 | Être auxiliary and subject agreement: which verbs? | A1 limited→A2 P; Required | `past/etre-auxiliary`: bounded verb set and agreement → transitive sortir/monter contrast, marcher/courir counterexample; reflexive caveat visible | T4–T5 |
| FR-21 | Imparfait: background, habit or ongoing state? | A2 P; Required | `past/imparfait`: formation and viewpoint → être exception, contextual duration; not simply “used to” | E1 A2.04; T6 |
| FR-22 | Past-tense choice in a story: event or background? | A2→B1 P; Required | `past/past-choice`: contextual pair → bounded states vs changes; narrative present recognition; keywords do not choose tense | T6 |
| FR-23 | Pluperfect: what had happened before another past point? | B1 P; Required | `past/pluperfect`: imperfect auxiliary + participle, prior-past context → same auxiliary/agreement rules; depuis/venait de counterexamples | T6 |
| FR-24 | Future reference: present, aller + infinitive or futur simple? | A1 near→A2 simple P; Required | `future/future-reference`: patterns and intent/context → regular/essential irregular stems, future after quand; no “near = soon” absolute | E1 A1.03/A2.02; Tex index future lessons |
| FR-25 | Present conditional: polite request, advice or imagined outcome? | A1 chunks→B1 P; Required | `mood/conditional`: polite chunks then stem + imperfect endings → wishes/advice/obligation, link si; no past-conditional system | E1 A1.14/B1.06–07; T16 |
| FR-26 | Commands: which form and where do pronouns go? | A1 limited→A2 P; Required | `mood/imperative`: tu/nous/vous and negative form → essential irregulars, -s before y/en, affirmative-pronoun exception visible | T7, T9; Tex index imperative |
| FR-27 | Present subjunctive formation: which form after a trigger? | B1 P bounded; Required | `mood/subjunctive-forms`: model endings and common forms → two-stem/irregular forms checked separately; not every verb from ils alone | T10; common irregular forms included |
| FR-28 | Subjunctive choice: obligation/emotion or asserted belief? | B1 P bounded; Required | `mood/subjunctive-choice`: il faut que/je veux que/être content que → affirmative espérer/croire indicative, same-subject infinitives, limited conjunctions; fact can take subjunctive | T10–T11 |
| FR-29 | Passive: what was done, rather than who did it? | B1 P bounded + Rec; Required | `voice/passive`: être + agreed participle → present/compound-past examples, par-agent, active/on alternatives; de-agent as recognition note | T12 |
| FR-30 | Gerund: while/by doing the same-subject action? | B1 P bounded; Required | `patterns/gerund`: en + -ant and same-subject condition → formation/three irregulars, simultaneity/manner; English -ing often needs infinitive | T13 |
| FR-62 | Participle agreement with an earlier direct object? | B1 P bounded; Required | `past/object-agreement`: avoir agrees with preceding COD, not COI → pronoun and que-relative examples; separate reflexive analysis; exceptional systems deferred | T5, T7, T14 |

### Sentences

| ID | Topic / learner question | Level; accepted state | Section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-12 | Subject pronouns/on/tu/vous: who is acting? | A1→A2 P; Required | `subjects/subjects`: required subject, agreement, tu/vous → on as we/people/someone, third-singular verb; contextual referent agreement note | E1 A1.30/A2.21; Tex index subject pronouns |
| FR-13 | Stressed pronouns: me/him after a preposition or for emphasis? | A1 P; Required | `subjects/stressed`: moi/toi/lui etc. → coordination/emphasis and après préposition; don't substitute for all clitics | E1 A1.30; T8; Tex index disjunctive pronouns |
| FR-31 | Yes/no question: everyday, neutral or formal? | A1 P; inversion Rec then bounded P; Required | `questions/question-patterns`: statement-order/est-ce que → inversion and polite chunks; no English do-support | E1 A1.07; Tex index interrogatives |
| FR-32 | Who/what/which/where: what is the missing role? | A1→A2 P; Required | `questions/question-words`: qui/que, quel agreement and core adverbs → subject/object qu'est-ce qui/que; lequel recognition supplement only | E1 A1.06/.08; Tex index interrogatives |
| FR-33 | Not/never: where does negation sit? | A1 P; Required | `negation/basic-negation`: ne/n'…pas/jamais → auxiliary/infinitive positioning, short pas responses, spoken ne omission label | T17 |
| FR-34 | No longer/nothing/no one/only/neither: which negative pattern? | A2→B1 P; Required | `negation/negative-choices`: plus/rien/personne, no extra pas → ne…que restriction, aucun and ni…ni; negative subject positions | E1 A2.07/B1.05; Tex index negation lessons |
| FR-35 | Introducing/identifying/describing: c'est, il est or il y a? | A1 P; Required | `introducing/presentatives`: identity vs description vs existence → ce sont/voici/voilà, professions and adjective contrasts | E1 A1.31–32; Tex index c'est/il est |
| FR-36 | Direct object pronoun: him/her/it/them before which verb? | A2 P; Required | `objects/direct-objects`: me/te/le/la/nous/vous/les + elision → finite/auxiliary/infinitive and imperative contrast; link agreement | T7 |
| FR-37 | Indirect object pronoun: lui/leur or another frame? | A2 P; Required | `objects/indirect-objects`: à-person complements of selected verbs → téléphoner à vs écouter, penser à lui exception; no gender distinction in lui | T7–T8 |
| FR-38 | Y: there or à + thing? | A2 place→B1 complements P; Required | `objects/pronoun-y`: place replacement → bounded verb-governed à complements; people/penser à distinction; no fixed English equivalent | T8 |
| FR-39 | En: some/how many or de + complement? | A2 quantity→B1 complements P; Required | `objects/en`: quantity replacement with retained number → bounded de complements, departure; not universal for every de phrase/person | T8 |
| FR-40 | Two object pronouns: which order in a statement or command? | B1 P bounded; Required | `objects/pronoun-order`: standard order with selected pairs → affirmative imperative order/hyphens/moi-toi; negative imperative reverts; no arbitrary combinations | T9 |
| FR-41 | Mine/yours: which possessive pronoun? | A2 P; Required | `replacement/possessive-pronouns`: le mien/la mienne etc. → noun agreement and determiner contrast, contractions | T18 |
| FR-42 | This one/that one: demonstrative pronoun or determiner? | A1 ça; A2→B1 P; Required | `replacement/demonstrative-pronouns`: ça and celui/celle/ceux/celles → -ci/-là and de/relative completion; not bare celui for every “this” | E1 D p. 53 supplement; T18; entry depths fixed below |
| FR-43 | Someone/each/several: which standalone indefinite? | B1 P bounded; Required | `replacement/indefinite-pronouns`: quelqu'un/chacun, quelques-uns/certains → agreement, determiner vs pronoun; avoid open vocabulary expansion | E1 B1.22; T18 |
| FR-63 | Exclaiming: what a…/how…? | A2 P; Required | `questions/exclamations`: quel + agreed noun → que/comme patterns, complete glossed examples | E1 A2.06; Tex index quel |

### Connections

| ID | Topic / learner question | Level; accepted state | Section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-44 | Place and contractions: at/to/in/from/by which form? | A1→B1 P; Required | `place/place-prepositions`: à/de + article, city/country/chez → dans/en/par/avec, near/above/below/ici/là; finite place frames, no universal English mapping | E1 A1.25–26/A2.18/B1.19; Tex index prepositions |
| FR-45 | Time/duration: since/for/ago/in/by/around? | A1→B1 P; Required | `time/time-expressions`: depuis/pendant/il y a/dans/en → present with continuing depuis, à/en/date-time; dès/à partir de/d'ici/vers, veille/lendemain, adverbs in context | T16; E1 A1.27–29/A2.19/B1.20 |
| FR-48 | Verb/adjective + preposition or infinitive: à, de or neither? | A2→B1 P bounded; Required | `complements/verb-prepositions`: selected frames learned with meaning → arrêter de/penser à, no-preposition verbs, content de/prêt à supplement; not a general translation algorithm | T18; E1 Annex D printed p. 51 / PDF p. 53 supplement |
| FR-49 | Relatives qui/que/où: which role links the clauses? | A2 P; Required | `relatives/core-relatives`: subject/object/place-time → no English object-relative omission; person/thing is not the qui/que test | T14 |
| FR-50 | Dont: de + complement or possession? | B1 P bounded; Required | `relatives/dont`: identify required de frame → contrast que, possession and no redundant de/possessive; complex-preposition limit visible | T14 |
| FR-51 | Compound relatives: what does preposition + lequel refer to? | B1 Rec; Required; full production Deferred | `relatives/compound-relatives`: glossed recognition and agreement family → small à/sur/avec examples, à/de contractions; complex production matrix deferred | T14; E1 B1.23 |
| FR-52 | Ce qui/ce que/ce dont and emphasis: what has no named antecedent? | B1 P bounded; Required | `relatives/ce-relatives`: choose by role → ce…c'est emphasis with matched examples; not every “what” = ce que | T14 |
| FR-53 | If/what if: likely condition, imagined situation or suggestion? | B1 P; Required | `conditions/si-patterns`: si + present/result and imperfect/conditional → imperative result, et si + imperfect suggestion; “no conditional after si” limited to conditional si, not reported whether | T16; E1 B1.01/.16 |
| FR-54 | Report what someone says/asks: que, si or question word? | B1 P bounded; Required | `reporting/reported-present`: present reporting frame → pronoun/reference changes, indirect order, wh/ce qui/ce que and orders with de + infinitive; backshift deferred | T15 |
| FR-55 | Contrast: but/whereas/on the contrary? | A1→B1 P; Required | `links/contrast`: mais then alors que/au contraire → clause boundaries and meaning distinction | E1 A1.33/A2.24/B1.25; Tex index conjunctions |
| FR-56 | Purpose: to do or so another person does? | A1→B1 P; Required | `links/purpose`: pour + noun/infinitive → afin de, pour que/afin que + present subjunctive; subject/meaning contrast | T10–T11; E1 A1.10/A2.25/B1.26 |
| FR-57 | Cause: because/because of/thanks to? | A2→B1 P; Required | `links/cause`: parce que vs noun phrase → car/comme/puisque/grâce à/en effet; don't misclassify c'est pourquoi as a cause introducer | E1 A2.26/B1.27; Tex index conjunctions |
| FR-58 | Result: so/therefore/that's why? | A1→B1 P; Required | `links/result`: alors/donc/c'est pour ça → c'est pourquoi/voilà pourquoi/par conséquent; distinguish cause and consequence | E1 A1.34/A2.27/B1.28; Tex index conjunctions |
| FR-59 | Connect/order/conclude: and/or/then/finally/also? | A1→B1 P; Required | `links/sequence`: et/ou and short sequence → en plus/également/aussi, encore, numbered sequence/conclusion; final position and meaning depend on frame | E1 A1.35/A2.28–29/B1.30; Tex index conjunctions |
| FR-60 | Concession: despite/although/yet? | B1 P bounded; Required | `links/concession`: malgré + noun vs bien que + subjunctive → cependant/pourtant/quand même; do not combine malgré que as default | T10; E1 B1.29 |


### Named-baseline mapping

The following are all **94 GRAMMAIRE bullets** in Annex E's A1–B1 slice:
35 A1, 29 A2, 30 B1. Ordinal locators restart at each level and are local trace
IDs, not publisher IDs. Printed pp. 56, 57–58, 59 correspond to one-based PDF
pp. 58, 59–60, 61 in the [publisher PDF](https://www.eaquals.org/wp-content/uploads/Inventaire_ONLINE_full-1.pdf).
This consensus reference is a planning baseline, not a mandated DELF syllabus.
Every bullet is mapped to an accepted requirement or explicit Deferred depth;
this does not establish implemented coverage or a gate PASS.

### A1 — printed p. 56 / PDF p. 58: 35 bullets

| Item | Accepted topic IDs | Mapping/depth note |
| --- | --- | --- |
| A1.01 | FR-14, FR-15 | Regular and common irregular present |
| A1.02 | FR-16 | Ongoing-action emphasis |
| A1.03 | FR-24 | Near-future entry only |
| A1.04 | FR-19, FR-20 | Avoir plus small être set, not entire compound system |
| A1.05 | FR-16 | Recent-action frame |
| A1.06 | FR-32, FR-35 | Identification questions and answers |
| A1.07 | FR-31, FR-32, FR-25 | Question patterns; polite chunk rather than full conditional at A1 |
| A1.08 | FR-32 | Full listed core question-word set |
| A1.09 | FR-33 | Basic/never patterns and short negative response |
| A1.10 | FR-56 | Purpose infinitive |
| A1.11 | FR-18 | Positive and negative necessity |
| A1.12 | FR-18 | All three modal frames |
| A1.13 | FR-26 | Limited command forms |
| A1.14 | FR-25 | Polite formulae |
| A1.15 | FR-17 | Reflexive entry |
| A1.16 | FR-01, FR-08 | Gender plus agreement link |
| A1.17 | FR-02, FR-08 | Number plus agreement link |
| A1.18 | FR-03 | Both article families |
| A1.19 | FR-05 | Numeric/measure/distance frames included |
| A1.20 | FR-04, FR-05 | Partitive meaning and measure + de both retained |
| A1.21 | FR-08, FR-09 | Agreement and placement, not either alone |
| A1.22 | FR-06, FR-07 | Possessive and demonstrative determiners separately |
| A1.23 | FR-05, FR-46 | Quantity + noun vs standalone amount; negative de link |
| A1.24 | FR-46 | Intensity distinguished from amount |
| A1.25 | FR-44 | All listed core place/relationship frames |
| A1.26 | FR-44 | Place adverbs, not just prepositions |
| A1.27 | FR-45, FR-64 | Time prepositions and time/date syntax |
| A1.28 | FR-45 | Basic time adverbs |
| A1.29 | FR-45 | Future interval, continuing duration, elapsed time |
| A1.30 | FR-12, FR-13 | Subject and stressed forms |
| A1.31 | FR-35 | Existence |
| A1.32 | FR-35 | Identification and pointing, singular/plural |
| A1.33 | FR-55 | Basic contrast |
| A1.34 | FR-58, FR-59 | Result reading of basic links versus simple addition |
| A1.35 | FR-59 | Coordination |

### A2 — printed pp. 57–58 / PDF pp. 59–60: 29 bullets

Bullets 01–10 are on printed p. 57; 11–29 on p. 58.

| Item | Accepted topic IDs | Mapping/depth note |
| --- | --- | --- |
| A2.01 | FR-14, FR-15, FR-16 | Present and ongoing-action construction |
| A2.02 | FR-24 | Near and simple future |
| A2.03 | FR-19, FR-20, FR-16 | Both compound auxiliaries plus recent past |
| A2.04 | FR-21 | Past description |
| A2.05 | FR-22 | Contextual past contrast |
| A2.06 | FR-63 | All three exclamation patterns |
| A2.07 | FR-34 | No longer/nothing/no one |
| A2.08 | FR-18 | Modal + infinitive |
| A2.09 | FR-26 | Commands beyond initial chunks |
| A2.10 | FR-25 | Polite conditional continued |
| A2.11 | FR-20, FR-17 | Être agreement with visible reflexive limit |
| A2.12 | FR-17 | Reflexive/pronominal patterns |
| A2.13 | FR-48 | Verb-governed prepositions |
| A2.14 | FR-08, FR-09 | Both adjective obligations |
| A2.15 | FR-11 | Tout family |
| A2.16 | FR-10, FR-05 | Comparison/superlative, quantities included |
| A2.17 | FR-46 | Amount and frequency retained |
| A2.18 | FR-44 | Expanded place prepositions and adverbs |
| A2.19 | FR-45 | Duration and starting-point indicators |
| A2.20 | FR-12, FR-13, FR-36, FR-37, FR-41 | Subject/stressed, both object types, possessive pronouns |
| A2.21 | FR-12 | All three on readings |
| A2.22 | FR-38, FR-39 | Place y and quantity en |
| A2.23 | FR-49 | Subject/object and place/time relatives |
| A2.24 | FR-55 | Basic contrast retained |
| A2.25 | FR-56 | Purpose + noun and infinitive |
| A2.26 | FR-57 | Clause vs noun cause |
| A2.27 | FR-58 | Consequence |
| A2.28 | FR-59, FR-55 | Addition, sequence, continuation and contrast distinguished |
| A2.29 | FR-59 | Full listed chronological/numbered sequence set |

### B1 — printed p. 59 / PDF p. 61: 30 bullets

| Item | Accepted topic IDs | Mapping/depth note |
| --- | --- | --- |
| B1.01 | FR-53 | Suggestion with imperfect, not only a two-clause conditional |
| B1.02 | FR-22 | Past contrast deepened |
| B1.03 | FR-22, FR-14 | Past narration and narrative-present recognition |
| B1.04 | FR-23 | Prior-past construction |
| B1.05 | FR-34 | Restriction/no/neither patterns |
| B1.06 | FR-25 | Productive present conditional |
| B1.07 | FR-25, FR-53 | Wish, advice, softened obligation and imaginary scenarios; bounded frames, not all modal nuances |
| B1.08 | FR-27, FR-28 | Common obligation + subjunctive, including negative necessity |
| B1.09 | FR-27, FR-28 | Present-subjunctive forms plus feeling/obligation triggers |
| B1.10 | FR-28 | Indicative/subjunctive contrast; not a “que always” rule |
| B1.11 | FR-29 | Passive with limited productive tense range |
| B1.12 | FR-30 | Gerund with subject and English -ing limit |
| B1.13 | FR-62, FR-36, FR-49 | Preceding direct pronoun and relative object both included |
| B1.14 | FR-54 | Present reporting frame; statement and yes/no question, plus bounded wh/orders |
| B1.15 | FR-48 | Selected complement frames, not an open verb dictionary |
| B1.16 | FR-53 | Real and imagined conditional patterns; past counterfactual deferred separately |
| B1.17 | FR-61 | **Deferred**: lexical nominalisation exceeds closed-class lookup scope; trigger below |
| B1.18 | FR-46, FR-47, FR-05 | Quantity and manner, including formation and placement |
| B1.19 | FR-44 | Expanded place/route/transport frames |
| B1.20 | FR-45 | All listed time-adverb/indicator functions, including relative-day reference |
| B1.21 | FR-40 | Selected double combinations plus imperative contrast |
| B1.22 | FR-43, FR-11, FR-38, FR-39, FR-48 | Indefinite pronouns/determiner distinction and governed y/en extensions |
| B1.23 | FR-50, FR-51 | Dont productive; compound relatives **Rec**, full production Deferred |
| B1.24 | FR-52 | No-antecedent relatives and emphasis |
| B1.25 | FR-55 | Clause contrast and contrary correction |
| B1.26 | FR-56, FR-28 | Purpose infinitive and subjunctive clauses |
| B1.27 | FR-57, FR-58 | Cause set retained; result expression routed by actual meaning |
| B1.28 | FR-58 | Result variants |
| B1.29 | FR-60, FR-28 | Noun, adverb and subjunctive concession patterns |
| B1.30 | FR-59 | Additive links and chronological conclusion |


## Maintenance and acceptance

Revise this plan before changing accepted coverage, depth, card ownership,
practice mapping or language-specific interaction. Preserve anchor IDs after
publication. A content change reopens changed units, connected rules/examples/
tables and both directions of coverage under CONTENT_VALIDATION. Scope changes
reopen Baseline. Add new candidate gaps to the audit before promoting decisions.

Independent review must inventory every actual content unit, compare
syllabus→plan, plan→page and page→plan, and record sources, revision, reviewer,
ordinary/counterexample probes, findings and retests in CONTENT_AUDIT.
All four content gates and separate runtime checks must pass before release
acceptance. The [common integration proposal](../../research/italian-french-en.md#6-delivery-sequence-and-exit-criteria)
coordinates shared registry/assets/worker work; this plan does not own it.
