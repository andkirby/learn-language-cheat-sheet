# French for English speakers: proposed content plan

Researched 2026-10-23. Pair: `fr-en`; proposed URL: `fr/en/`.
Original status: **OPEN PROPOSAL — research/planning only**. At research
completion no French page existed and no content/runtime gate had passed.
The research below preserves that proposal and its provenance. On 2026-10-23
the parent authorized its recommended scope and French authoring; accepted
scope now belongs to [fr/en/SITE_PLAN.md](../fr/en/SITE_PLAN.md). The later
authoring record below is separate from independent acceptance, which remains
pending. This file deepens the French portion of the
[common proposal](italian-french-en.md); shared files and audit remain parent-owned.

## Recommendation and boundary

Keep a mobile grammar lookup reference for English-speaking A1–B1 learners:
plain English explanations, French examples with natural English meaning
support, concise decision cards and bounded dialogs. Recommend contemporary
standard French as taught in France; label conversational/formal differences
and material regional variants. Do not equate “standard” with “only valid”.

The initial 30-unit outline hid independently reviewable requirements.
The inventory below gives them separate IDs; related requirements may share
a card/dialog only when the whole unit remains bounded. This is a selective
reference, **not a complete French course, DELF syllabus or certification**.
Do not force all content into 30 cards or equate a mapped source item with
implemented coverage. Before acceptance, test whether shared cards fit; split
an overloaded card without losing its topic IDs.

Recommend bounded productive B1 treatment of present subjunctive, pluperfect,
preceding-object agreement, double pronouns, passive and gerund. Include
present-frame reported speech; defer full past-frame backshift. Include core
relatives productively and a clearly marked recognition bridge to compound
relatives. Nominalisation is an explicit proposed deferral, not an omission.

Shared engineering, registry/landing work, icons, manifests, offline packaging,
release mechanics and existing-deck regression work stay in the
[common proposal §§5–6](italian-french-en.md#5-verified-implementation-implications)
and [ADD_LANGUAGE](../docs/ADD_LANGUAGE.md). No new generator architecture,
practice, audio or explanation locale is proposed here. ROADMAP's original
Russian-interference criterion must be adapted to English interference for
this authorized new pair; its bounded lookup principle still applies.

## Evidence and method

All links in the source register were accessed live on **2026-10-23**.
“Verified fact” below means the cited source was inspected for that point;
it does not certify unwritten deck content. Level placement comes from E1;
Tex supplies grammar evidence, not independent CEFR certification. `P` and
`Rec` are **our recommended depth**, not productive/receptive labels inferred
from the inventory's typography. Repeated entries at successive levels mean
increasing scope, not that every paradigm is an A1 requirement.

### Primary baseline

**E1:** Eaquals/CIEP/Eurocentres/ACPLS, *Inventaire linguistique des contenus
clés des niveaux du CECRL*, copyright 2015, [publisher PDF](https://www.eaquals.org/wp-content/uploads/Inventaire_ONLINE_full-1.pdf).
Inspected: introduction printed pp. 4–5; purpose/recommendations pp. 14–16;
Annex E grammar at printed p. 56 (A1), pp. 57–58 (A2), p. 59 (B1), and p. 60
(B2 comparison). PDF page numbers are respectively **58, 59–60, 61, 62**
(one-based viewer pages; printed number + 2). Annex D printed pp. 50–54
(PDF 52–56) was checked for additional candidates and distinctions.

E1 is a consensus-based planning reference and a starting point for contextual
selection. Its introduction does not prescribe a method or obligatory
curriculum. CIEP participation does not make this a mandated DELF grammar
list. The common research recorded direct FEI requests blocked by
`ERR-BOT-403`; this session used the accessible publisher-hosted PDF instead
and did not retest the FEI endpoint.

The checklist in §4 maps **all 94 grammar bullets in Annex E's A1–B1 slice**:
35 A1, 29 A2, 30 B1. Each bullet has a locator and proposed disposition;
compound bullets retain all components. That is the precise comparison
boundary: not every function, vocabulary theme, example or higher-level row
in the entire publication. Annex D supplements are called out separately.
This completes a research mapping, **not the Baseline acceptance gate**.

### Grammar reference register

All `T` references are University of Texas at Austin, *Tex's French Grammar*,
HTML lessons (no page numbers/edition displayed). Section names below locate
the inspected material. Use original explanations/examples, not Tex's cartoon
scenarios. The [index](https://www.laits.utexas.edu/tex/gr/index.html) was also
checked to expose candidates outside the initial outline.

| Ref | Exact lesson links/titles and inspected sections | Use/limit |
| --- | --- | --- |
| T1 | [Determiners: definite articles](https://www.laits.utexas.edu/tex/gr/det2.html), forms, elision, general concepts, likes/dislikes, no article; [Determiners: indefinite articles](https://www.laits.utexas.edu/tex/gr/det4.html), forms/uses, negative, plural adjective, professions; [Determiners: partitive articles](https://www.laits.utexas.edu/tex/gr/det5.html), forms/uses/negative | Article contrast and exceptions; not a claim that every English zero article maps alike |
| T2 | [Possessive determiners](https://www.laits.utexas.edu/tex/gr/det6.html), forms; [Demonstrative determiners](https://www.laits.utexas.edu/tex/gr/det7.html), forms; [Expressions of quantity](https://www.laits.utexas.edu/tex/gr/det8.html), quantity + de; [Tout](https://www.laits.utexas.edu/tex/gr/det9.html); [Indefinite determiners](https://www.laits.utexas.edu/tex/gr/det10.html) | Candidate forms and bounded function-word sets; individual future examples still need review |
| T3 | [Adjectives: formation and placement](https://www.laits.utexas.edu/tex/gr/adj2.html); [Adjectives whose meaning varies with placement](https://www.laits.utexas.edu/tex/gr/adj5.html); [Comparisons with adjectives](https://www.laits.utexas.edu/tex/gr/adj6.html); [Superlative of adjectives](https://www.laits.utexas.edu/tex/gr/adj7.html); [Bon/meilleur vs. bien/mieux](https://www.laits.utexas.edu/tex/gr/adj8.html); [Adverbs: formation and placement](https://www.laits.utexas.edu/tex/gr/adv2.html), formation/placement sections | Foundation/reference comparison; uncommon spelling exceptions require authoring-time checks |
| T4 | [Passé composé with avoir](https://www.laits.utexas.edu/tex/gr/tap2.html), uses/formation/negation; [Passé composé with être](https://www.laits.utexas.edu/tex/gr/tap3.html), formation, transitivity, agreement | Auxiliary/form evidence; motion is not a sufficient auxiliary rule |
| T5 | [Passé composé of pronominal verbs](https://www.laits.utexas.edu/tex/gr/tap4.html), formation/agreement/exceptions/negation | Reflexive direct versus indirect object, following body-part object |
| T6 | [Narration: passé composé vs. imparfait](https://www.laits.utexas.edu/tex/gr/tap8.html), foreground/background, change of state, final context caveat; [Plus-que-parfait](https://www.laits.utexas.edu/tex/gr/tap9.html), formation/uses | Past contrast and prior-past meaning; English tense names are not conversion rules |
| T7 | [Direct object pronouns](https://www.laits.utexas.edu/tex/gr/pro5.html), forms/placement/agreement; [Indirect object pronouns](https://www.laits.utexas.edu/tex/gr/pro8.html), forms/placement | Pronoun positions and preceding direct-object agreement; do not turn the simplified English “to” cue into a universal test |
| T8 | [Pronoun y](https://www.laits.utexas.edu/tex/gr/pro6.html), place/certain verbs/placement; [Pronoun en](https://www.laits.utexas.edu/tex/gr/pro7.html), uses/placement | Place, quantity and governed complements; examples concerning people need contextual checking |
| T9 | [Order of object pronouns present tense](https://www.laits.utexas.edu/tex/gr/pro9.html), overview, y/en, direct/indirect combinations, negation; affirmative-imperative table | Common two-pronoun combinations, not permission to combine every table cell |
| T10 | [Regular subjunctive](https://www.laits.utexas.edu/tex/gr/tas1.html), formation and stem changes; [Subjunctive usage: obligation](https://www.laits.utexas.edu/tex/gr/tas3a.html); [Subjunctive usage: will, emotion, desire](https://www.laits.utexas.edu/tex/gr/tas4.html), will/emotion/one subject; [Conjunctions that take the subjunctive](https://www.laits.utexas.edu/tex/gr/tas5.html), conjunction list | Common frames, infinitive alternative, indicative after affirmative espérer; not “subjunctive = uncertain/unreal” |
| T11 | [Past subjunctive](https://www.laits.utexas.edu/tex/gr/tas6.html), formation/uses; [Ways to avoid the subjunctive](https://laits.utexas.edu/tex/gr/tas8.html), infinitive alternatives | Defines the boundary being deferred; alternatives must preserve subjects and meaning |
| T12 | [Active vs. passive voice](https://www.laits.utexas.edu/tex/gr/tav1.html), formation/uses/ways to avoid passive | Focus, agreement, on/active alternatives; avoid “French never uses passive” |
| T13 | [Present participle](https://www.laits.utexas.edu/tex/gr/vpp1.html), formation, en + participle, English -ing warning | Gerund with same subject; bare participle uses are a separate expansion |
| T14 | [Relative pronouns: qui and que](https://www.laits.utexas.edu/tex/gr/pror1.html); [Relative pronouns: ce qui, ce que](https://www.laits.utexas.edu/tex/gr/pror2.html); [Relative pronouns: dont, où, etc.](https://www.laits.utexas.edu/tex/gr/pror3.html), dont/où/lequel, no-antecedent constructions | Syntactic role, not people/things; compound-preposition limit on dont |
| T15 | [Reported speech in the present](https://www.laits.utexas.edu/tex/gr/tad1.html), reporting statements/questions/orders; [Reported speech in the past](https://www.laits.utexas.edu/tex/gr/tad2.html), subordinate tense table | Present-frame scope versus backshift series; past lesson's categorical tense wording needs a second-source nuance check before teaching it |
| T16 | [Si clauses](https://www.laits.utexas.edu/tex/gr/tac3.html), present/imperfect/pluperfect sections; [Depuis, pendant, pour: 'for'](https://www.laits.utexas.edu/tex/gr/prep1.html), three-way duration contrast | Bounded conditions and time; do not teach every si + imperfect as impossible |
| T17 | [Basic negation: ne ... pas](https://www.laits.utexas.edu/tex/gr/neg2.html), simple/compound tense placement and spoken omission | Standard written form plus conversational recognition |
| T18 | [Demonstrative pronouns](https://www.laits.utexas.edu/tex/gr/pro11.html), forms/uses; [Possessive pronouns](https://www.laits.utexas.edu/tex/gr/pro12.html), forms/uses; [Indefinite pronouns](https://www.laits.utexas.edu/tex/gr/pro10.html), quelqu'un/chacun; [Prepositions with infinitives](https://www.laits.utexas.edu/tex/gr/pre4.html), à/de and other preposition groupings | Prevent silent omission of pronouns; complement selection is lexical and must be learned in frames |

Supplementary search found CCDMD, *La concordance des temps à l'indicatif :
la simultanéité*, [PDF](https://ameliofrancais.ccdmd.qc.ca/storage/amelioration-du-francais/ressources/1697833657-09Concordance_V2.pdf),
search extract p. 4. Direct fetch returned 403; **not counted as inspected
full-text evidence**. Obtain an accessible authoritative reference on retained
present/general truths if the deferred backshift series is reopened.

## Proposed learner contract and surfaces

Primary questions:

1. Which noun/article/adjective form conveys my meaning?
2. Which present, past or future construction fits this situation?
3. Which object am I replacing, and where does its pronoun go?
4. How do I ask, negate, request or express obligation?
5. Which time/place expression fits, especially English “for/since/in”?
6. How do I connect a reason, condition, contrast or relative clause?
7. When does French require a different construction from English?

Every card needs a trigger, essential pattern, meaning-supported example and
any limit without which the card would be false. Dialogs hold contrasts,
short paradigms and bounded exceptions. Examples/formulas receive English
`gloss`; dialog examples receive adjacent English `comment`. Teach opaque
forms with their lemma where useful. Explain auxiliaries by function; do not
translate their parts mechanically. Keep accents, apostrophes and elision
inside the affected grammar unit, including h-aspiré limits where needed.

Proposed views: `forms`, `verbs`, `sentences`, `connections`. In the tables,
`section/card` identifies the proposed surface; the anchor would be
`section-card`, and the `DETAILS` key is the card slug. Rows sharing that
surface are separate review obligations within one bounded card/dialog.
There are 64 proposed review-topic IDs (63 Req, one Def), currently grouped
into 62 provisional card/dialog owners. This is an explicit scope/cost estimate,
not a fixed UI quota or a delivery commitment. These are proposals, not
published/reserved anchors. Search should use visible
English intent terms plus correct French terms; test accents/elisions without
promising accent folding. No legacy French anchors exist to preserve yet.

`Req` = recommend Required; `Def` = recommend Deferred. `P` = bounded
productive use and recognition; `Rec` = recognition with meaning support,
no generation paradigm promised. Levels show recommended entry/deepening;
E1 provides the placement basis except explicitly marked supplements.

### Forms

| ID | Topic / learner question | Level; recommendation | Proposed section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-01 | Noun gender: which agreement set? | A1 P; Req | `nouns/noun-forms`: learn noun with determiner, gender ≠ sex → common cues with exceptions | E1 A1.16; Tex index nouns |
| FR-02 | Noun plural: which written ending? | A1 P; Req | `nouns/noun-forms`: default -s with visible irregular limit → common -x/-aux and invariant forms | E1 A1.17; Tex index number |
| FR-03 | Articles: a/the/zero in English — what in French? | A1 P; Req | `determiners/articles`: un/une/des vs le/la/les/l' → generic reference, likes, professions and elision limits | T1 |
| FR-04 | Partitives: an unspecified amount or a whole category? | A1 P; Req | `determiners/partitives`: du/de la/de l' contrast → negation, être/contrast exceptions; do not confuse du with every de + le | T1 |
| FR-05 | Quantities: how much/many, measures and de? | A1→B1 P; Req | `determiners/quantity`: number/measure/quantity frame → de/d', beaucoup vs beaucoup de, comparisons of amounts, numeric distance/percentage frames | T2; E1 A1.19–20 |
| FR-06 | Possessive determiner: his/her or noun agreement? | A1 P; Req | `determiners/possessives`: agree with possessed noun → son/sa ambiguity, mon amie, body-part cross-reference | T2 |
| FR-07 | Demonstrative determiner: this/that + noun? | A1 P; Req | `determiners/demonstratives`: ce/cet/cette/ces → -ci/-là, contrast with pronouns | T2 |
| FR-08 | Adjective agreement: which ending? | A1→A2 P; Req | `adjectives/adjective-forms`: gender/number model → common irregulars; no universal “add e” rule | T3 |
| FR-09 | Adjective position: before or after, with what meaning? | A1→A2 P; Req | `adjectives/adjective-position`: default plus small pre-noun set → meaning-changing contrasts; not an absolute mnemonic | T3; Tex index position lessons |
| FR-10 | Comparison: more/as/less and the most? | A2 P; Req | `adjectives/comparison`: plus/aussi/moins…que, superlative → meilleur/mieux, adjective/adverb/noun distinctions | T3 |
| FR-11 | Tout and indefinite determiners: all/every/some? | A2→B1 P; Req | `determiners/indefinites`: tout/toute/tous/toutes before nouns → small quelques/certains/chaque set; contrast standalone forms | T2; E1 Annex D printed p. 51 / PDF p. 53 supplement |
| FR-46 | Degree, amount and frequency: very/too/enough/often? | A1→B1 P; Req | `adverbs/degree-frequency`: très vs beaucoup, trop/assez → frequency positions, environ/presque/autant; finite function set | T2–T3 |
| FR-47 | Manner adverbs: how, and in which position? | B1 P; Req | `adverbs/manner`: common -ment formation with limits → irregulars, simple/compound placement; no rigid universal position | T3 |
| FR-61 | Nominalisation: which noun corresponds to a verb? | B1 Rec candidate; Def | No initial card; future `nouns/nominalisation` → original contextual noun/verb contrasts, no productive suffix algorithm | E1 B1.17; grammar accuracy review pending |
| FR-64 | Number/date/time grammar: how do I write a date or tell time? | A1 P supplement; Req | `numbers/dates-time`: cardinal/ordinal/date/time frames → premier vs other dates, grammatical number conventions; no calendar vocabulary catalogue | E1 A1 functions p. 56, not an Annex E grammar bullet |

### Verbs

| ID | Topic / learner question | Level; recommendation | Proposed section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-14 | Regular present patterns: which ending? | A1 P; Req | `present/present-patterns`: regular -er/-ir/-re models → stem/spelling changes; not all -ir verbs follow finir | E1 A1.01; Tex index verb groups |
| FR-15 | Essential irregular present: which common form? | A1 P; Req | `present/present-irregulars`: être/avoir/aller/faire entry points → bounded venir/prendre/faire-family references; modal forms owned by FR-18 | E1 A1.01; Tex index irregular verbs |
| FR-16 | Ongoing/recent action: doing or just did? | A1 P; Req | `present/present-meaning`: present covers English simple/progressive → être en train de emphasis; venir de + infinitive for recent past | E1 A1.02/.05; Tex index present/passé immédiat |
| FR-17 | Reflexives: which se form and position? | A1→A2 P; Req | `patterns/reflexives`: subject-matched pronoun → reciprocal/idiomatic limit, negation, infinitive and compound positions; link agreement | T5; Tex index pronominal verbs |
| FR-18 | Ability, wanting, duty and necessity: infinitive or clause? | A1 P; Req | `patterns/modals-obligation`: pouvoir/vouloir/devoir + infinitive and il faut → no “to” inserted; il ne faut pas = must not, not need not | E1 A1.11–12; T10–T11 |
| FR-19 | Passé composé: how do I form a completed event? | A1 limited→A2 P; Req | `past/passe-compose`: auxiliary + participle, common avoir forms → irregular participles, negation; English past/perfect context | T4 |
| FR-20 | Être auxiliary and subject agreement: which verbs? | A1 limited→A2 P; Req | `past/etre-auxiliary`: bounded verb set and agreement → transitive sortir/monter contrast, marcher/courir counterexample; reflexive caveat visible | T4–T5 |
| FR-21 | Imparfait: background, habit or ongoing state? | A2 P; Req | `past/imparfait`: formation and viewpoint → être exception, contextual duration; not simply “used to” | E1 A2.04; T6 |
| FR-22 | Past-tense choice in a story: event or background? | A2→B1 P; Req | `past/past-choice`: contextual pair → bounded states vs changes; narrative present recognition; keywords do not choose tense | T6 |
| FR-23 | Pluperfect: what had happened before another past point? | B1 P; Req | `past/pluperfect`: imperfect auxiliary + participle, prior-past context → same auxiliary/agreement rules; depuis/venait de counterexamples | T6 |
| FR-24 | Future reference: present, aller + infinitive or futur simple? | A1 near→A2 simple P; Req | `future/future-reference`: patterns and intent/context → regular/essential irregular stems, future after quand; no “near = soon” absolute | E1 A1.03/A2.02; Tex index future lessons |
| FR-25 | Present conditional: polite request, advice or imagined outcome? | A1 chunks→B1 P; Req | `mood/conditional`: polite chunks then stem + imperfect endings → wishes/advice/obligation, link si; no past-conditional system | E1 A1.14/B1.06–07; T16 |
| FR-26 | Commands: which form and where do pronouns go? | A1 limited→A2 P; Req | `mood/imperative`: tu/nous/vous and negative form → essential irregulars, -s before y/en, affirmative-pronoun exception visible | T7, T9; Tex index imperative |
| FR-27 | Present subjunctive formation: which form after a trigger? | B1 P bounded; Req | `mood/subjunctive-forms`: model endings and common forms → two-stem/irregular forms checked separately; not every verb from ils alone | T10; irregular paradigm verification remains |
| FR-28 | Subjunctive choice: obligation/emotion or asserted belief? | B1 P bounded; Req | `mood/subjunctive-choice`: il faut que/je veux que/être content que → affirmative espérer/croire indicative, same-subject infinitives, limited conjunctions; fact can take subjunctive | T10–T11 |
| FR-29 | Passive: what was done, rather than who did it? | B1 P bounded + Rec; Req | `voice/passive`: être + agreed participle → present/compound-past examples, par-agent, active/on alternatives; de-agent as recognition note | T12 |
| FR-30 | Gerund: while/by doing the same-subject action? | B1 P bounded; Req | `patterns/gerund`: en + -ant and same-subject condition → formation/three irregulars, simultaneity/manner; English -ing often needs infinitive | T13 |
| FR-62 | Participle agreement with an earlier direct object? | B1 P bounded; Req | `past/object-agreement`: avoir agrees with preceding COD, not COI → pronoun and que-relative examples; separate reflexive analysis; exceptional systems deferred | T5, T7, T14 |

### Sentences

| ID | Topic / learner question | Level; recommendation | Proposed section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-12 | Subject pronouns/on/tu/vous: who is acting? | A1→A2 P; Req | `subjects/subjects`: required subject, agreement, tu/vous → on as we/people/someone, third-singular verb; contextual referent agreement note | E1 A1.30/A2.21; Tex index subject pronouns |
| FR-13 | Stressed pronouns: me/him after a preposition or for emphasis? | A1 P; Req | `subjects/stressed`: moi/toi/lui etc. → coordination/emphasis and après préposition; don't substitute for all clitics | E1 A1.30; T8; Tex index disjunctive pronouns |
| FR-31 | Yes/no question: everyday, neutral or formal? | A1 P; inversion Rec then bounded P; Req | `questions/question-patterns`: statement-order/est-ce que → inversion and polite chunks; no English do-support | E1 A1.07; Tex index interrogatives |
| FR-32 | Who/what/which/where: what is the missing role? | A1→A2 P; Req | `questions/question-words`: qui/que, quel agreement and core adverbs → subject/object qu'est-ce qui/que; lequel recognition supplement only | E1 A1.06/.08; Tex index interrogatives |
| FR-33 | Not/never: where does negation sit? | A1 P; Req | `negation/basic-negation`: ne/n'…pas/jamais → auxiliary/infinitive positioning, short pas responses, spoken ne omission label | T17 |
| FR-34 | No longer/nothing/no one/only/neither: which negative pattern? | A2→B1 P; Req | `negation/negative-choices`: plus/rien/personne, no extra pas → ne…que restriction, aucun and ni…ni; negative subject positions | E1 A2.07/B1.05; Tex index negation lessons |
| FR-35 | Introducing/identifying/describing: c'est, il est or il y a? | A1 P; Req | `introducing/presentatives`: identity vs description vs existence → ce sont/voici/voilà, professions and adjective contrasts | E1 A1.31–32; Tex index c'est/il est |
| FR-36 | Direct object pronoun: him/her/it/them before which verb? | A2 P; Req | `objects/direct-objects`: me/te/le/la/nous/vous/les + elision → finite/auxiliary/infinitive and imperative contrast; link agreement | T7 |
| FR-37 | Indirect object pronoun: lui/leur or another frame? | A2 P; Req | `objects/indirect-objects`: à-person complements of selected verbs → téléphoner à vs écouter, penser à lui exception; no gender distinction in lui | T7–T8 |
| FR-38 | Y: there or à + thing? | A2 place→B1 complements P; Req | `objects/y`: place replacement → bounded verb-governed à complements; people/penser à distinction; no fixed English equivalent | T8 |
| FR-39 | En: some/how many or de + complement? | A2 quantity→B1 complements P; Req | `objects/en`: quantity replacement with retained number → bounded de complements, departure; not universal for every de phrase/person | T8 |
| FR-40 | Two object pronouns: which order in a statement or command? | B1 P bounded; Req | `objects/pronoun-order`: standard order with selected pairs → affirmative imperative order/hyphens/moi-toi; negative imperative reverts; no arbitrary combinations | T9 |
| FR-41 | Mine/yours: which possessive pronoun? | A2 P; Req | `replacement/possessive-pronouns`: le mien/la mienne etc. → noun agreement and determiner contrast, contractions | T18 |
| FR-42 | This one/that one: demonstrative pronoun or determiner? | A1 ça; A2→B1 P proposal; Req | `replacement/demonstrative-pronouns`: ça and celui/celle/ceux/celles → -ci/-là and de/relative completion; not bare celui for every “this” | E1 D p. 53 supplement; T18; exact entry depth to confirm |
| FR-43 | Someone/each/several: which standalone indefinite? | B1 P bounded; Req | `replacement/indefinite-pronouns`: quelqu'un/chacun, quelques-uns/certains → agreement, determiner vs pronoun; avoid open vocabulary expansion | E1 B1.22; T18 |
| FR-63 | Exclaiming: what a…/how…? | A2 P; Req | `questions/exclamations`: quel + agreed noun → que/comme patterns, complete glossed examples | E1 A2.06; Tex index quel |

### Connections

| ID | Topic / learner question | Level; recommendation | Proposed section/card: card duty → dialog duty | Evidence |
| --- | --- | --- | --- | --- |
| FR-44 | Place and contractions: at/to/in/from/by which form? | A1→B1 P; Req | `place/place-prepositions`: à/de + article, city/country/chez → dans/en/par/avec, near/above/below/ici/là; finite place frames, no universal English mapping | E1 A1.25–26/A2.18/B1.19; Tex index prepositions |
| FR-45 | Time/duration: since/for/ago/in/by/around? | A1→B1 P; Req | `time/time-expressions`: depuis/pendant/il y a/dans/en → present with continuing depuis, à/en/date-time; dès/à partir de/d'ici/vers, veille/lendemain, adverbs in context | T16; E1 A1.27–29/A2.19/B1.20 |
| FR-48 | Verb/adjective + preposition or infinitive: à, de or neither? | A2→B1 P bounded; Req | `complements/verb-prepositions`: selected frames learned with meaning → arrêter de/penser à, no-preposition verbs, content de/prêt à supplement; not a general translation algorithm | T18; E1 Annex D printed p. 51 / PDF p. 53 supplement |
| FR-49 | Relatives qui/que/où: which role links the clauses? | A2 P; Req | `relatives/core-relatives`: subject/object/place-time → no English object-relative omission; person/thing is not the qui/que test | T14 |
| FR-50 | Dont: de + complement or possession? | B1 P bounded; Req | `relatives/dont`: identify required de frame → contrast que, possession and no redundant de/possessive; complex-preposition limit visible | T14 |
| FR-51 | Compound relatives: what does preposition + lequel refer to? | B1 Rec; Req; full P Def | `relatives/compound-relatives`: glossed recognition and agreement family → small à/sur/avec examples, à/de contractions; complex production matrix deferred | T14; E1 B1.23 |
| FR-52 | Ce qui/ce que/ce dont and emphasis: what has no named antecedent? | B1 P bounded; Req | `relatives/ce-relatives`: choose by role → ce…c'est emphasis with matched examples; not every “what” = ce que | T14 |
| FR-53 | If/what if: likely condition, imagined situation or suggestion? | B1 P; Req | `conditions/si-patterns`: si + present/result and imperfect/conditional → imperative result, et si + imperfect suggestion; “no conditional after si” limited to conditional si, not reported whether | T16; E1 B1.01/.16 |
| FR-54 | Report what someone says/asks: que, si or question word? | B1 P bounded; Req | `reporting/reported-present`: present reporting frame → pronoun/reference changes, indirect order, wh/ce qui/ce que and orders with de + infinitive; backshift deferred | T15 |
| FR-55 | Contrast: but/whereas/on the contrary? | A1→B1 P; Req | `links/contrast`: mais then alors que/au contraire → clause boundaries and meaning distinction | E1 A1.33/A2.24/B1.25; Tex index conjunctions |
| FR-56 | Purpose: to do or so another person does? | A1→B1 P; Req | `links/purpose`: pour + noun/infinitive → afin de, pour que/afin que + present subjunctive; subject/meaning contrast | T10–T11; E1 A1.10/A2.25/B1.26 |
| FR-57 | Cause: because/because of/thanks to? | A2→B1 P; Req | `links/cause`: parce que vs noun phrase → car/comme/puisque/grâce à/en effet; don't misclassify c'est pourquoi as a cause introducer | E1 A2.26/B1.27; Tex index conjunctions |
| FR-58 | Result: so/therefore/that's why? | A1→B1 P; Req | `links/result`: alors/donc/c'est pour ça → c'est pourquoi/voilà pourquoi/par conséquent; distinguish cause and consequence | E1 A1.34/A2.27/B1.28; Tex index conjunctions |
| FR-59 | Connect/order/conclude: and/or/then/finally/also? | A1→B1 P; Req | `links/sequence`: et/ou and short sequence → en plus/également/aussi, encore, numbered sequence/conclusion; final position and meaning depend on frame | E1 A1.35/A2.28–29/B1.30; Tex index conjunctions |
| FR-60 | Concession: despite/although/yet? | B1 P bounded; Req | `links/concession`: malgré + noun vs bien que + subjunctive → cependant/pourtant/quand même; do not combine malgré que as default | T10; E1 B1.29 |

## Item-by-item baseline comparison

Locators `A1.01` etc. are this document's **ordinal numbering of the grammar
bullets**, restarting after each GRAMMAIRE heading. They are not IDs assigned
by Eaquals. Use them with the exact pages above; this avoids reproducing the
source checklist. The destination table supplies the learner question, depth,
card/dialog owner and recommendation for every mapped topic. Each row below
maps one original bullet, including repeats; notes identify compound items or
our bounded reduction. No row means “covered on a page”.

### A1 — printed p. 56 / PDF p. 58: 35 bullets

| Item | Proposed topic IDs | Mapping/depth note |
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

| Item | Proposed topic IDs | Mapping/depth note |
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

| Item | Proposed topic IDs | Mapping/depth note |
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
| B1.17 | FR-61 | **Def**: lexical nominalisation exceeds closed-class lookup scope; trigger below |
| B1.18 | FR-46, FR-47, FR-05 | Quantity and manner, including formation and placement |
| B1.19 | FR-44 | Expanded place/route/transport frames |
| B1.20 | FR-45 | All listed time-adverb/indicator functions, including relative-day reference |
| B1.21 | FR-40 | Selected double combinations plus imperative contrast |
| B1.22 | FR-43, FR-11, FR-38, FR-39, FR-48 | Indefinite pronouns/determiner distinction and governed y/en extensions |
| B1.23 | FR-50, FR-51 | Dont productive; compound relatives **Rec**, full production Def |
| B1.24 | FR-52 | No-antecedent relatives and emphasis |
| B1.25 | FR-55 | Clause contrast and contrary correction |
| B1.26 | FR-56, FR-28 | Purpose infinitive and subjunctive clauses |
| B1.27 | FR-57, FR-58 | Cause set retained; result expression routed by actual meaning |
| B1.28 | FR-58 | Result variants |
| B1.29 | FR-60, FR-28 | Noun, adverb and subjunctive concession patterns |
| B1.30 | FR-59 | Additive links and chronological conclusion |

Annex D supplements that the shorter E grammar list must not silently hide:
indefinite determiners → FR-11; adjective + preposition → FR-48;
demonstrative pronouns → FR-42. These are proposed additions, with entry-depth
confirmation still open. Past subjunctive reception, literary tenses and
higher-level systems have explicit boundaries below; no E1 A1–B1 grammar
bullet is left without a recommendation.

## Borderline recommendations: facts versus product choices

| Area | Verified grammar point | Proposed treatment and visible limit |
| --- | --- | --- |
| Subjunctive | T10 shows common obligation/will/emotion frames, infinitive alternatives and affirmative espérer + indicative. T11 distinguishes present/past subjunctive by event relationship. | Req FR-27/28: bounded present forms and triggers at B1; include affirmative croire/espérer contrast and real emotion about facts. Never call the mood simply unreal. Defer past subjunctive production/reception lesson and rare/literary moods; explicitly label the present-only limit. |
| Pluperfect | T6 forms it with an imperfect auxiliary and locates an event before a past reference point; English “had been … since” may instead need imperfect + depuis. | Req FR-23, productive narrative use. It is not deferred merely because the English name looks advanced. Defer its past-counterfactual application with the wider conditional system. |
| Participle agreement | T4–T5 separate ordinary être subject agreement from reflexive exceptions; T7 covers earlier direct objects. | Req FR-20/62 plus reflexive limits: include COD before avoir, que-relative, no COI agreement, se laver les mains/se parler contrasts. No “être always agrees; avoir never agrees” card. Defer infinitive-following/causative and exceptional agreement systems. |
| Double pronouns | T9 distinguishes ordinary order, auxiliary/infinitive placement and affirmative imperative. | Req FR-40: me le/le lui, quantity pair, affirmative/negative command contrasts. Label combinations as selected legal frames. Avoid a universal Cartesian pronoun grid. |
| Passive | T12 gives être + agreed participle and active/on alternatives. | Req FR-29: present and passé composé production; other already-known tense forms recognition. Mention passive focus and agent optionality; no exhaustive passive-tense paradigm. |
| Gerund | T13 uses en + participle for simultaneous/manner actions sharing a subject and warns that English -ing often maps to infinitive. | Req FR-30: productive simple gerund; present-participle formation as necessary support. Defer independent participial clauses/verbal-adjective system and perfect gerund. |
| Relatives | T14 selects qui/que by grammatical role, dont by a de complement, and lequel with prepositions; dont cannot replace a complex preposition ending in de. | Req FR-49/50/52 productively. FR-51: recognize the agreement family and common preposition forms with glosses; full productive contractions/complex-preposition matrix Def. State the boundary rather than silently deleting compound relatives from B1. |
| Reported speech | T15 present-frame lesson covers que/si/wh, ordinary indirect order and de + infinitive for orders. The past lesson introduces a separate tense-shift table. | Req FR-54 present reporting frame, with pronoun/reference changes. Full past reporting/backshift Def, consistent with E1's B2 comparison. Do not teach an absolute “always backshift” rule; retained-present/general-truth conditions need another inspected reference before expansion. |

## Proposed deferrals and exclusions

These are recommendations awaiting acceptance, not settled owner decisions.
A required card must still be accurate when advanced depth is deferred.

| ID / state | Boundary and rationale | Reconsideration trigger |
| --- | --- | --- |
| FR-61 / Def | Nominalisation as an independent topic: open lexical derivation and noun selection need more than a reliable suffix card. Existing glosses may explain individual nouns without claiming this coverage. | Repeated lookup need for noun/verb transformation, with a bounded set and an inspected word-formation reference; or owner chooses comprehensive inventory coverage |
| FR-D01 / Def | Full subjunctive tense system, broad doubt/concession inventory, past-subjunctive recognition lesson; exceeds the bounded present B1 target. Present-only examples must not imply present subjunctive covers anterior events. | Reading evidence repeatedly blocked by anterior subjunctive, or accepted B1+/B2 depth with a separate unit and review |
| FR-D02 / Def | Exceptional participle agreement: following infinitives, faire/laisser, impersonal/measure cases, exhaustive reflexive taxonomy. Core counterexamples remain Required. | Real examples cannot be explained by the bounded rules; expand with a reviewed separate unit |
| FR-D03 / Def | Productive full compound-relative matrix beyond FR-51 Rec. E1 places the family at B1; reduction is a product choice, not a B2 assertion. | Learners need to compose these clauses, or the owner selects full productive B1 coverage |
| FR-D04 / Def | Past-frame reported speech/backshift, deictic conversion series and exceptions. | Accepted B2 extension or recurring past-report lookup need, with second-source nuance check |
| FR-D05 / Def | Past conditional, past counterfactual/mixed si patterns, future perfect and past infinitive. Separate systems cannot be implied by present conditional/pluperfect cards. | Required reading/writing use or accepted expanded level; dedicated sourced units |
| FR-D06 / Def | Bare present-participial clauses, verbal adjectives, perfect gerund and causative faire as systems. | Specific learner probe justifies a bounded card and grammar reference pass |
| FR-D07 / Def | Exhaustive conjugation dictionary, exhaustive verb/adjective-preposition lists, idiomatic pronominal verbs and fine modal pragmatics. | Frequency evidence identifies a finite missing frame; accept that frame rather than a general catalogue |
| FR-X01 / Excluded | Productive passé simple/passé antérieur and literary subjunctive paradigms; outside everyday lookup target. No separate literary recognition lesson initially. | Product becomes literary-reading oriented or learner evidence warrants a distinct recognition unit |
| FR-X02 / Excluded | Open vocabulary, thematic phrasebook, culture/letter-writing course and DELF task training. E1's non-grammar domains are not promised by this deck. | Product-intent change, not a grammar-coverage probe |
| FR-X03 / Excluded | General pronunciation/audio/phonetic course. Grammatical orthography and necessary elision limits remain in scope. | Explicit audio/pronunciation product decision |
| FR-X04 / Excluded | Course sequencing, retention assessment and on-page practice redesign; lookup probes belong in review evidence. | Separate practice/product authorization under existing owners |
| FR-X05 / Excluded | Reciprocal audiences, native-speaker French master and regional-language catalogues. English is the explanation language; useful register/variant notes remain allowed. | Actual audience demand and a new accepted audience plan |

## Remaining consequential decisions

1. **Breadth versus first release.** Recommend all Req rows at the stated
   bounded depths, with shared-card fit tested before acceptance. This is
   broader than the initial 30-unit sketch. If a smaller release is chosen,
   explicitly defer the affected IDs and update all 94 mappings; do not claim
   complete productive A1–B1 coverage.
2. **Compound relatives and nominalisation.** Recommend FR-51 recognition
   only and FR-61 Deferred. Both are in the B1 comparison; acceptance must
   acknowledge the selective boundary. These are the main coverage tradeoffs.
3. **Language policy.** Confirm the France-oriented standard default, register
   labels and policy for common regional alternatives; do not spend the first
   release on an exhaustive variety catalogue.
4. **Supplement depth/card fit.** Confirm FR-42 entry level and FR-11/48/64
   supplements, then split any oversized present-irregular, time-expression,
   pronoun or connector card. Grammar references alone do not establish CEFR
   placement. Final acceptance needs the relevant source examples/level
   rationale, not just the index.

## Content review probes to run later

These are proposed probes and expected judgments, **not observed results**.
All need an independent linguistic reviewer. Extend them to every authored
rule, table cell, formula, example and gloss; sampling cannot pass a full gate.

| Topic(s) | Probe / expected judgment | Misleading shortcut caught |
| --- | --- | --- |
| FR-03/04/05 | Contrast **J'aime le café** (“I like coffee”), **Je bois du café** (“I'm drinking coffee”), **Je ne bois pas de café** (“I don't drink coffee”), **Ce n'est pas du café** (“It isn't coffee”). | Every English zero article maps to no article; all negation forces de |
| FR-06/08/09 | **Son amie est française** (“His/her friend is French”); contrast **son propre bureau** (“his/her own office”) with **un bureau propre** (“a clean office”). | Possessive follows owner's gender; adjective position is free/always after |
| FR-16/45 | **J'habite ici depuis deux ans** (“I've lived here for two years”); continuing now versus a completed **pendant** interval. | French present perfect for all English have + participle; for = one preposition |
| FR-19/20 | **Elle est sortie** (“She went out”) vs **Elle a sorti les clés** (“She took out the keys”); **Elle a marché** (“She walked”). | Motion always selects être |
| FR-21/22 | Contextual contrast between an ongoing activity interrupted by a call and the same activity completed that day; accept both tenses when viewpoint/context makes both defensible. | Keyword or English past-tense conversion chooses tense |
| FR-23 | **Quand je suis arrivé, elle était déjà partie** (“When I arrived, she had already left”); contrast ongoing past duration with depuis. | Any English had construction requires pluperfect |
| FR-17/62 | **Elles se sont lavées** (“They washed themselves”), **Elles se sont lavé les mains** (“They washed their hands”), **Elles se sont parlé** (“They spoke to each other”). | All reflexive participles agree with subject |
| FR-36/37/62 | **Les lettres, je les ai écrites** (“The letters — I wrote them”) vs **Je leur ai écrit** (“I wrote to them”); also **les lettres que j'ai écrites** (“the letters I wrote”). | Avoir never agrees; any preceding pronoun triggers agreement |
| FR-38/39 | **J'y pense** (“I'm thinking about it”) vs **Je pense à elle** (“I'm thinking about her”); **J'en ai deux** (“I have two [of them]”). | Y = all à phrases; en deletes the quantity |
| FR-40/26 | **Je le lui donne** (“I give it to him/her”), **Donne-le-moi** (“Give it to me”), **Ne me le donne pas** (“Don't give it to me”), **Je vais le lui donner** (“I'm going to give it to him/her”). | One position/order for all constructions |
| FR-27/28 | **Il faut que tu viennes** (“You need to come”), **Je suis content que tu sois ici** (“I'm glad you're here”), **J'espère qu'il viendra** (“I hope he'll come”), **Je veux partir** (“I want to leave”). | Que always takes subjunctive; subjunctive implies a non-fact; always two subjects required for any use |
| FR-29 | **La lettre a été envoyée** (“The letter was sent”) and an on/active alternative with the appropriate focus. | No agreement; direct English passive transfer is always preferred |
| FR-30 | **Elle apprend en lisant** (“She learns by reading”); reject a same-subject gerund rewrite when the two actions have different actors. | Every English -ing word is a French gerund |
| FR-49/50/51/52 | **le livre que je lis** (“the book I'm reading”), **la personne qui vient** (“the person who's coming”), **le livre dont j'ai besoin** (“the book I need”), **ce qui change** (“what is changing”); complex preposition + lequel recognition. | Qui means people/que things; omit relative; dont replaces every de sequence |
| FR-53 | **Si j'ai le temps, je viendrai** (“If I have time, I'll come”), **Si j'avais le temps, je viendrais** (“If I had time, I'd come”), **Et si on sortait ?** (“What if we went out?”); **Je me demande s'il viendra** (“I wonder whether he'll come”). | Conditional si and whether-si have identical restrictions; imperfect always means past/impossible |
| FR-54 | **Elle demande si tu viens** (“She asks whether you're coming”) and **Elle te dit de venir** (“She tells you to come”); check referents and ordinary indirect order. | Retain est-ce que/inversion; report all orders with que |
| FR-56/60 | **Je pars pour travailler** (“I'm leaving to work”) vs **Je parle lentement pour que tu comprennes** (“I speak slowly so you can understand”); noun after malgré vs clause after bien que. | One English connector always has one French syntax |

Every other Req ID must receive at least one ordinary-use probe, a limit or
counterexample, and gloss/naturalness review when authored. The above list
prioritizes high-risk contrasts; it is not full unit-review coverage.

## Sequenced implementation and verification proposal

1. Resolve the remaining decisions; have the baseline extraction/mapping and
   level/depth choices independently checked against E1. Verify the additional
   foundation lessons and irregular paradigms at section level. Keep full
   Baseline **NOT RUN** until the accepted topic inventory, exclusions and
   reviewer evidence exist.
2. On explicit implementation authorization, promote **settled scope only**
   into `fr/en/SITE_PLAN.md` before deck authoring. Put open decisions and
   later review evidence in the existing audit owner. Follow the
   [SITE_PLAN guide](../docs/SITE_PLAN_GUIDE.md); do not paste this research
   register as accepted implementation evidence.
3. Author by dependency: noun/determiner/subject foundations → present and
   sentence frames → objects and compound past → tense contrast/time →
   relatives/connectors → bounded B1 mood/voice/reporting. Test each card's
   independent meaning support and visible caveats. Keep topic IDs traceable
   even if card grouping changes.
4. Review the complete authored deck independently under
   [CONTENT_VALIDATION](../docs/CONTENT_VALIDATION.md): syllabus→plan,
   plan→actual card/dialog/table, and actual content→plan. Count all units;
   record exact revision/dirty scope, reviewer, sources, probes, observed
   judgments, findings and retest. All four content gates must pass.
5. Integrate through the [common engineering checklist](italian-french-en.md#6-delivery-sequence-and-exit-criteria).
   Include `strings.menu_issue: "Submit issue"`, required by the validator
   since `05eed47`; reuse the renderer's project/issue links in both menus,
   as recorded in the [shared integration requirements](italian-french-en.md#5-verified-implementation-implications).
   Coordinate shared files with the Italian owner; do not duplicate registry,
   landing, icon or worker edits. Keep an unready pair out of live navigation.
6. Run generator/search/shell checks and the complete
   [AGENTS runtime checklist](../AGENTS.md#verify-before-declaring-done),
   including affected existing pages, subpath assets, mobile overflow,
   themes/skins, menus, search, dialogs, anchors and offline reload. Follow
   that owner's temporary-process cleanup procedure. Release/deployment
   verification is a separate authorized step, never inferred from this plan.

## Work completed and gate status

Research performed: owner documents/common proposal read; publisher E1 live
text checked; 94 ordinal grammar items mapped; supplementary candidates and
higher-level boundaries compared; university grammar references checked,
with detailed inspection concentrated on the high-risk constructions.
No full authored French content exists within this task's scope.

| Check/gate | Status and scope |
| --- | --- |
| Baseline acceptance | **NOT RUN** — proposed mapping exists; decisions, final surfaces and independent level/depth review remain |
| Coverage | **NOT RUN** — no French deck/page reviewed |
| Accuracy | **NOT RUN** — source research and proposed probes do not review every eventual content unit |
| Teaching | **NOT RUN** — no complete card/dialog/gloss review |
| Generator/deck/search/shell validation | **NOT RUN** — research-only task; no new deck or registry |
| Browser/runtime/mobile/theme/search/dialog/asset checks | **NOT RUN** |
| Offline/installed PWA/live deployment checks | **NOT RUN** |
| Local document links | Checked by filesystem resolution, including local heading fragments |
| Whitespace | Checked for trailing whitespace, tabs and final newline |

Maintenance trigger for this proposal: revise when the owner settles scope,
new reference evidence changes a recommendation, or implementation exposes
an unworkable card boundary. Accepted scope and implementation evidence must
continue to live in their existing repository owners.


## Authoring handoff — 2026-10-23

Scope transition: the parent authorized all proposed Required rows at their
bounded depths, FR-61 Deferred, FR-51 recognition only and the remaining
recommended deferrals/exclusions. The [accepted target](../fr/en/SITE_PLAN.md)
was written **before** the [deck](../content/decks/fr-en.json) or generated
page. Historical “proposed” language above remains research provenance;
current scope is owned by the accepted target, not this research file.

Authored deliverables: accepted target; deck JSON; English pair-local
manifest; HTML produced only by the existing renderer against an in-memory
registry. No shared registry, worker, landing, icon, existing-deck, audit,
commit, push, browser or server mutation was performed by this author.

### Additional authoring sources

Accessed 2026-10-23; HTML sources have named sections rather than page numbers.
These supplement E1/T1–T18; they do not establish new CEFR allocations.

| Ref | Exact source and inspected location | Use |
| --- | --- | --- |
| A1 | OQLF, [Pluriel des noms en -ail](https://vitrinelinguistique.oqlf.gouv.qc.ca/22603/la-grammaire/le-nom/pluriel-des-noms/pluriel-en-x/pluriel-des-noms-en-8209ail), opening rule/exceptions; [Pluriel des noms en -ou](https://vitrinelinguistique.oqlf.gouv.qc.ca/22605/la-grammaire/le-nom/pluriel-des-noms/pluriel-en-x/pluriel-des-noms-en-8209ou), opening rule/exceptions; [Pluriel des noms en -al](https://vitrinelinguistique.oqlf.gouv.qc.ca/21821/la-grammaire/le-nom/pluriel-des-noms/pluriel-en-x/pluriel-des-noms-en-8209al), rule/exceptions | FR-01/02: avoid overly broad -aux/-oux rules in Tex’s overview |
| A2 | UT Austin, [Number: singular, plural](https://www.laits.utexas.edu/tex/gr/no2.html), regular/unchanged/irregular sections; [Gender: masculine, feminine](https://www.laits.utexas.edu/tex/gr/no3.html), people/animals/objects; [Irregular adjectives](https://www.laits.utexas.edu/tex/gr/adj4.html), forms | Foundation models checked with explicit exceptions; no2's generalization across -ail/-ou was not adopted |
| A3 | OQLF, [L’accord dans le groupe nominal](https://www.oqlf.gouv.qc.ca/francisation/ordres_prof/capsules-grammaticales/accord-groupe-nominal.aspx), Accords/Accords particuliers | Noun-controlled agreement and mixed-group standard |
| A4 | UT Austin, [Irregular subjunctive](https://www.laits.utexas.edu/tex/gr/tas2.html), two stems, avoir/être, faire/savoir/pouvoir; [Imparfait: formation](https://www.laits.utexas.edu/tex/gr/tap5.html), stem/endings; [Imparfait: states of being, habitual actions](https://www.laits.utexas.edu/tex/gr/tap6.html), states/habits | FR-21/27 forms, boundary against universal ils-stem rule |
| A5 | UT Austin, [Questions with subject/verb inversion](https://www.laits.utexas.edu/tex/gr/int3.html), hyphen/-t-/noun/compound/negative sections; [Interrogative pronouns](https://www.laits.utexas.edu/tex/gr/int5.html), people/things/prepositions; [Interrogative and exclamative quel](https://www.laits.utexas.edu/tex/gr/int4.html), question/exclamation uses | FR-31/32/63 |
| A6 | UT Austin, [Prepositions with places](https://www.laits.utexas.edu/tex/gr/pre3.html), geographic-location table; [Recent past](https://www.laits.utexas.edu/tex/gr/tap1.html), present/imperfect venir; [Future: usage](https://www.laits.utexas.edu/tex/gr/taf4.html), future contrast and French/English time clauses | FR-16/24/44/45 |
| A7 | UT Austin, [Infinitive constructions](https://www.laits.utexas.edu/tex/gr/vinf1.html), noun uses, after verbs/prepositions, negative infinitives; [Placement of adverbs with passé composé](https://www.laits.utexas.edu/tex/gr/adv3.html), main explanation; [Imperative mood](https://www.laits.utexas.edu/tex/gr/tai1.html), formation/irregulars/reflexives/negation/objects | FR-26/30/33/47/48, avoiding English -ing transfer |
| A8 | UT Austin, [Être](https://www.laits.utexas.edu/tex/gr/virr1.html), present paradigm; [Aller](https://www.laits.utexas.edu/tex/gr/virr4.html), present paradigm; [Modal verbs vouloir, pouvoir, devoir](https://www.laits.utexas.edu/tex/gr/vm1.html), each paradigm/use; [Conditional](https://www.laits.utexas.edu/tex/gr/tac1.html), formation/stems/uses | FR-15/18/25; distinguish English habitual would |
| A9 | Académie française, [Questions de langue](https://www.academie-francaise.fr/questions-de-langue), “Nombres (écriture, lecture, accord)”, “Septante, octante, nonante”, “À bicyclette, en voiture” | Number agreement, traditional/1990 hyphenation and regional alternatives; selected transport frames |
| A10 | OQLF, [Mise en évidence avec c’est… qui et c’est… que](https://vitrinelinguistique.oqlf.gouv.qc.ca/25318/la-syntaxe/la-mise-en-evidence/mise-en-evidence-avec-cest-qui-et-cest-que), final paragraph on other emphasis formulations; [Le pronom relatif dont](https://vitrinelinguistique.oqlf.gouv.qc.ca/22904/la-grammaire/les-pronoms/pronoms-relatifs/le-pronom-relatif-dont), redundancy and correction sections | Additional relative/emphasis boundary checks |

CCDMD *Pluriel des noms — cas particuliers* was found in search, but direct
PDF access failed at both current and old publisher URLs. It is **not** used
as full-text accuracy evidence; A1 supplies the relevant inspected authority.

### Author inspection and probes

Author inspection walked every authored card block, form-list row, example,
gloss and dialog block against its target row and relevant reference family.
It covered **62 cards / 372 card blocks / 248 form-list rows / 62 card
example–gloss pairs**, plus **63 dialogs / 347 dialog blocks / 312 translated
dialog pairs** (one dialog is English lookup help). All 63 Required IDs map
once to an actual owner; FR-01/02 share a card and FR-61 has no implementation.
This is author inspection, not the independent linguistic review required by
the repository. Naturalness, translations and card fit still need that review.

For each card, the ordinary case was its visible example with meaning support;
the counterexample/limit was checked against its visible notice and relevant
dialog contrasts. The following high-risk probes record the author’s expected
and observed artifact behavior. “Present” means the actual text was inspected;
it does not mean learner testing or model execution.

| IDs | Ordinary case and counterexample / expected judgment | Observed author check |
| --- | --- | --- |
| FR-01/02 | regular books; unchanged pays; festival/clou/détail must not follow a universal -aux/-oux rule | Models, clues and exceptions present; overbroad overview rule rejected using A1 |
| FR-03/04/05 | generic le café; amount du thé; negative de lait versus ce n’est pas du lait; specific beaucoup des invités | All frames and English meanings present; negation/quantity limits visible |
| FR-06/08/09 | son/sa follows noun; mon amie; adjective agreement and propre own/clean contrast | Forms/meanings and position limits present; gender not inferred from owner |
| FR-14/15/18 | six-person regular/common irregular paradigms; partir versus finir; negative necessity versus no necessity | Useful paradigms and counterframes present, not one-example placeholders |
| FR-16/45 | present with ongoing depuis; bounded pendant; venir de infinitive versus place | Contrasts and English meanings present; tense-conversion shortcut rejected |
| FR-19/20 | elle est sortie versus elle a sorti les clés; a marché | Auxiliary and transitivity caveats present on the first layer |
| FR-21/22/23 | background/event; bounded repeated past; prior-past versus imperfect + depuis / venait de | Contextual examples present; no keyword/English-tense conversion rule |
| FR-17/62 | lavées versus lavé les mains / se sont parlé; earlier lettres/que versus indirect leur | Core COD/COI and reflexive contrasts present; exceptional agreement boundary visible |
| FR-24/25/53 | future after quand; conditional result after si + imperfect; whether-si can have future | Paradigms and contrasting constructions present; “never future after any si” avoided |
| FR-26/40 | me le versus le lui; positive donne-le-moi versus negative ne me le donne pas; m’en | Both orders, hyphens and selected legal combinations present |
| FR-27/28 | regular/irregular/two-stem subjunctive; factual emotion; affirmative espérer indicative; same-actor bien que | Forms, mood contrast and same-subject counterexample present; present-only limit visible |
| FR-29/30 | passive agreement and on alternative; gerund shared subject versus English infinitive -ing | Productive bounded forms and limits present |
| FR-31/32/33/34/63 | inversion/ordinary question choices; subject/object what; rien/personne positions; quel agreement | Required question/negative/exclamation patterns and translations present |
| FR-35/36/37 | identity/description/existence; écouter direct versus répondre à; lui versus à elle | Contextual contrasts and pronoun-placement limits present |
| FR-38/39/41/42/43 | y place/thing versus person; en retained quantity; possessive/demonstrative/indefinite noun agreement | Forms, complements and English clues present; no fixed one-word equivalent claim |
| FR-46/47 | très versus beaucoup; long manner versus short compound-tense position; lent exception | Examples and limits present; rigid adverb-position rule avoided |
| FR-44/48 | place contractions and exceptions; selected verb/adjective partners; no-preposition modal | Finite frames and meaning clues present; English preposition matching rejected |
| FR-49/50/51/52 | qui/que role, dont simple de, complex-preposition lequel recognition, ce relatives/emphasis | Both object and subject examples present; FR-51 explicitly recognition only |
| FR-54 | present-frame que/si/wh and de + infinitive orders; remove est-ce que/inversion | Reported frames/reference changes present; past backshift not implied |
| FR-55/56/57/58/59/60 | clause/noun connectors; purpose subjunctive; c’est pourquoi as result; concessive fact | Distinct meanings, forms and glosses present; correct scope and limits retained |
| FR-64 | premier date, cardinal other dates, time/demie, multiplied cent/vingt and regional variants | Grammar frames and accepted spelling alternatives present; vocabulary catalogue excluded |

Author-pass fixes: inherited German no-results hints replaced; ordinary
no-JavaScript copy narrowed to visible cards; misleading repeated noun-family
shorthand avoided; relative-pronoun form typo corrected; the unpublished
FR-38 card slug changed from `y` to **`pronoun-y`** to meet the schema's two-
character minimum (plan updated before publication). The built-in validator
currently permits a one-character slug although the schema does not; shared
validation was not changed.

### Structural checks and remaining work

- Existing `deck_validate.validate(deck, site)` with an in-memory copy of the
  canonical registry extended only as needed for it/en and fr/en: **PASS**,
  strict Latin search hygiene, **zero French terminology exemptions**.
- Used JSON-schema shape constraints (required/unknown properties, refs,
  alternatives, types, enum, lengths/patterns and conditional requirements):
  **PASS** via a temporary stdlib checker. A separate installed JSON Schema
  engine was unavailable; no dependency was installed and formal independent
  Draft-7 engine validation is **NOT RUN**.
- 63/63 Required topic traces, 94 sequential baseline mappings, 62 plan/card/
  generated-anchor matches, every card’s visible limit, every form-list row’s
  meaning clue, every example’s English support and explicit bold markup:
  **PASS** mechanically. Each card has at most six first-layer form-list rows.
- Renderer output equality: **PASS** with the temporary registry. HTML static
  ID check: **PASS**, 100 unique IDs. Four generated inline scripts parse under
  `node --check`: **PASS**. These are static checks, not runtime evidence.
- Local document paths/fragments, JSON parsing, manifest English language and
  relative start/scope/icon paths, owned-file whitespace: **PASS**.
- Shared language tagging: reported to parent that the existing Latin selector
  misses bold target fragments in legends/ordinary paragraphs/notices. Parent
  owns the fix and all-six-page regeneration; French supplies explicit markup.
- Canonical registry build/shell checks and shared asset/offline integration:
  **NOT RUN** by this author; parent-owned. Manifest icon availability is not
  inferred from valid relative paths.
- Independent **Baseline / Coverage / Accuracy / Teaching: NOT RUN**. Full
  browser, mobile/card-fit, installed-PWA, offline and deployment gates:
  **NOT RUN**. No browser/server was started.

Ready for independent cross-review and shared integration, **not release
acceptance**. No known author-local blocker remains; shared tagging,
canonical generation/assets and independent linguistic review remain open.

Authoring snapshot for cross-review (SHA-256; later shared regeneration may
change HTML without changing authored grammar):

- `content/decks/fr-en.json`: `8afb8a6f5d5d57a5e8a7a1f069e9b14e6d033fdb8d0fc550c6cc17d4850940d9`
- `fr/en/SITE_PLAN.md`: `006abe165e8d865a88c3abf44242cb444dd9045c756a81920753f40666c7f8a9`
- `fr/en/manifest.webmanifest`: `ae526481d1a610f2cd18e967ab9fe99abc2b7108580efab9c66032383a3da5e2`

## 2026-10-23 author corrections for independent R1–R3 retest

This bounded correction follows the initial author handoff and independent
review. The earlier mechanical markup check covered main examples; it did not
establish complete markup of taught fragments in explanatory prose. This pass
marks French study subspans in rules, notices, comments and form-list meanings
while retaining English meanings. Scalar dialog titles/labels are English-only;
42 French-bearing scalar leads are preserved verbatim in rich **Core rule**
body blocks, with an English-only lead. Thirty existing form rows use the
schema's rich-run item alternative so their English meaning and French study
mentions can remain separate. No shared rendering contract was changed.

The inventory remains **62 cards, 248 form rows, 62 paired card examples and
63 dialogs**; moving those leads adds 42 prose blocks, giving **389 dialog
blocks**. The existing 312 translated dialog example/form pairs, all topic
IDs, anchors, grammar rules, examples, accepted depths and exclusions are
preserved. The command gloss in `pronoun-order` now reads “Don’t tell him/her
that. Tell him/her that.” English explanatory `émotion` is corrected to
`emotion`; this changes no mood-selection claim.

The FR-11/FR-48 Annex D supplement locators above now identify **printed p. 51 /
one-based PDF p. 53**, verified against that page of the publisher PDF retained
by the independent reviewer (accessed 2026-10-23). The accepted plan has matching
locators and its FR-51 Required-state typo is corrected; recognition depth is
unchanged.

Author checks: canonical build and `--check` PASS; existing strict validator
returns no errors; deterministic rendering matches; card anchors remain stable
and unique; 63 compiled dialog entries contain all 389 blocks. Normalized
before/after comparison preserves card/rule/example/gloss text apart from the
two English editorial corrections and English-only scalar headings. Moved
leads retain their original text in the rich body. Local document links and
fragments and owned-file whitespace pass. There are **zero dialog p/notice
blocks outside detail-blocks**, so this correction requires no shared selector
extension. No browser/server was started by this author.

Independent R1/R2/R3 retest, including **Teaching: NOT RUN** by this author;
parent owns the independent review handoff and canonical audit record. This
author check does not close the independent Teaching finding. Runtime,
accessibility execution, mobile/card-fit, install/offline and deployment gates
remain **NOT RUN by this author**; parent runtime evidence is separate. French
JSON, accepted plan and generated HTML are frozen for that retest.
