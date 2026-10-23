# Content audit

## Responsibility and current status

This file owns content-review evidence, reference provenance, open content
questions, findings and verdicts. Review records are append-only; finding
status and retest evidence may be updated without erasing their history.

It does not own accepted language scope. Promote an accepted Required,
Deferred or Excluded decision to the relevant
[German](de/ru/SITE_PLAN.md), [English](en/ru/SITE_PLAN.md),
[Italian](it/en/SITE_PLAN.md) or [French](fr/en/SITE_PLAN.md) plan. The
procedure is [content validation](docs/CONTENT_VALIDATION.md); plan authors use
[the SITE_PLAN guide](docs/SITE_PLAN_GUIDE.md).

Existing DE/EN status: **all candidate scope gaps are decided** (DE-G01–G13,
EN-G01–G12). Baseline **FAIL** remains on unsourced level placement
(C-03/D-02). Prior topic coverage is DE 28/28 and EN 26/26 per audience;
the 2026-10-20 sweep preserved all card/dialog identities and content topics.
Independent Accuracy and Teaching **PASS** for the 164 current cards and
166 dialogs after that sweep's corrections and retests (record below).
A fresh syllabus-to-plan/frequency-list completeness audit is **NOT RUN**;
this is not overall four-gate acceptance. Runtime/browser results are
recorded separately below.

Italian/French additions (2026-10-23): **Baseline, Coverage, Accuracy and
Teaching PASS for both new decks**, following independent full reviews and
complete bounded correction retests. All findings are closed at the final
source hashes in the dated record below. Existing DE/EN baseline findings
above remain unchanged. Shared integration review is accepted; runtime checks
passed separately in [UI_AUDIT](UI_AUDIT.md). Real-device installation and live
deployment are **NOT RUN** at the review handoff.

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

## 2026-09-10 — Initial documentation review

- Reviewer: Codex (documentation author; not an independent linguistic
  reviewer).
- Base revision: `057e836280c14c00bfd67c4ce08d793961187e87`; worktree clean
  before this documentation change. The inventories and protocol are new,
  uncommitted review scaffolding, not a page-validation result.
- Inspected: all eight pre-existing repository Markdown files (`AGENTS.md`,
  `README.md`, `docs/ADD_LANGUAGE.md`, both `SITE_PLAN.md` files,
  `.design/DESIGN_SYSTEM.md`, `.design/decisions.md`, `UI_AUDIT.md`).
- Boundary: Markdown only. No page source, rendered page, external reference
  or runtime inspection. No linguistic probes executed.
- Inventory: 16 required topic groups per language; 6 German and 7 English
  open scope candidates. Groups are not counts of actual content units.
- Actual cards/dialogs/tables/examples/answers reviewed: 0; total unknown.
- Reference register: empty. Exact grammar and syllabus sources remain to
  be selected and inspected; no reference-backed level or completeness claim.

| Gate | German | English | Reason |
| --- | --- | --- | --- |
| Baseline | NOT RUN | NOT RUN | Plan-derived inventories only; sources, levels and scope decisions pending |
| Coverage | NOT RUN | NOT RUN | Actual content not inspected or mapped |
| Accuracy | NOT RUN | NOT RUN | No linguistic reference review |
| Teaching | NOT RUN | NOT RUN | No complete card/dialog/example review |

Overall: **NOT RUN — content quality is not yet certified by this protocol.**

## Open scope questions

These are unresolved proposals discovered during the Markdown review. They
are not current requirements and are not silently excluded. Resolve each
against learner needs and named references, then promote the decision to the
language plan or close it with evidence here.

| ID | Language | Candidate topic | Missing decision/evidence | Status |
| --- | --- | --- | --- | --- |
| DE-G01 | German | Present conjugation, sein/haben and irregular stems | Required depth and placement | **Decided 2026-09-13: Required** → promoted as DE-19, shipped same day (spelling-change and -t/-d limits in the `conjugation` dialog) |
| DE-G02 | German | nicht versus kein and negation placement | Required depth and placement | **Decided 2026-09-13: Required** → promoted as DE-20, shipped same day (placement rule + kein declension in the `negation` dialog) |
| DE-G03 | German | Imperative | Include, defer or exclude | **Decided 2026-09-13: Required** → promoted as DE-21, shipped same day (du/ihr/Sie + sein exception; du vowel-change and -t/-d limits in dialog) |
| DE-G04 | German | Perfekt formation/auxiliary choice and Präteritum usage | Required depth and tense boundary | **Decided 2026-09-13 (split):** Perfekt bracket + auxiliary choice shipped earlier (DE-07); Präteritum → promoted as DE-22 recognition-level, shipped same day; the tense boundary now on-page |
| DE-G05 | German | Plural formation, comparison and adjective endings without an article | Split into reviewable decisions | **Decided:** comparison → DE-23 shipped 2026-09-13; adjective endings without an article covered by the `adjectives` dialog; plural formation → **Required** 2026-09-21, promoted as DE-24 and shipped same day (gender-based five-pattern card + `plural` dialog in `#extras`, «no single rule» limit) |
| DE-G06 | German | Verb-governed cases and reflexive verbs | Required depth and placement | **Decided 2026-09-24: Required** → promoted as DE-26, shipped same day (verb+preposition pairs, case from the preposition; sich-reflexives recognition; systematic reflexive lists deferred with the deck) |
| DE-G07 | German | der vs ein vs kein choice (known/specific vs new, professions without article, kein as noun negation) | Retrieval question 2 arguably promises usage choice, not only form; needs an accepted depth and placement decision | **Decided 2026-09-24: Required** → promoted as DE-27, shipped same day (known/one-of-many/negation + professions without an article) |
| DE-G08 | German | seit vs vor («живу здесь два года» vs «переехал два года назад») | Textbook Russian-interference time-preposition trap; include/defer decision needed | **Decided 2026-09-24: Required** → promoted as DE-28, shipped same day (seit + Präsens contrast with the English PP, vor + past event) |
| DE-G09 | German | Modal particles (Modalpartikeln): doch, mal, denn, ja, schon, gar, wohl (+ eben/halt/etwa) | User probe 2026-09-13: absent from the deck (denn appears only as coordinator, schon only as adverb in the Perfekt example); Russian encodes the same nuances (же/ведь/ну/уж/разве), so the transfer gap is real at A2–B1 — but a curated high-frequency set must not drift into the excluded particle-dictionary territory (DE-X02) | **Decided 2026-09-13: Required** → promoted to the plan as DE-17 (bounded set, decision-equivalents only) and implemented the same day — see the DE-17 record below |
| DE-G10 | German | Linking adverbs: deshalb, trotzdem, allerdings, außerdem, währenddessen | User request 2026-09-13 (meanwhile/nevertheless question); closed class, function-level meanings are stable — not phrasebook territory within a bounded set (DE-X02) | **Decided 2026-09-13: Required** → promoted as DE-18, implemented same day |
| DE-G11 | German | Demonstratives: dieser/diese/dieses (RU «этот») — and the dieser-vs-der choice | User probe 2026-09-21 («dieser — этот, где можно найти это?»): absent from the deck entirely (checked deck, page, plan, ROADMAP). dieser declines exactly on the deck's own definite-article pattern (dies- + der-word endings), so the morphology is already taught — the missing pieces are the word family itself and the RU «этот/тот» mapping (dieser covers both); natural home is `#forms` next to the article tables; welcher- shares the same pattern | **Decided 2026-09-21: Required** → promoted as DE-25 and implemented same day (card in `#forms` next to the article tables + `dieser` dialog: model, «этот/тот» collapse, welcher- pattern, dieser-vs-der and das in «это»-phrases, adjective-endings cross-reference) |
| DE-G12 | German | Polite possessive: building Ihr/Ihre from Sie (RU «Ваш») | User probe 2026-09-23 («как строить Ihre — не нашёл в шпоре»): the pieces exist (DE-05 stem list names Ihr; `possessives` dialog maps meanings; ein-words table gives endings) but no text states that capital-I Ihr is the possessive of polite Sie — the owner→stem step stays implicit. User constraint: the usage sentence that triggered the question must not ship verbatim; teach the construction itself | **Decided 2026-09-23: Required** (bounded depth within DE-05, standing ADD rules) → `possessives` dialog gained the owner→stem block the same day |
| DE-G13 | German | sondern vs aber: the correction pair after negation (nicht/kein …, sondern = «не A, а B») and nicht nur …, sondern auch | User probe 2026-09-24 (external agent advice to memorize «nicht A, sondern B = не A, а B» vs «aber = но»): sondern was listed among coordinators (DE-08) and appeared once inside a negation example, but the choice rule versus aber was never stated; RU «а» covers both functions, so the confusion is real. Sources: Olesen Tuition (error example *keinen Fisch, aber Fleisch* → sondern), YourDailyGerman, BBC Bitesize | **Decided 2026-09-24: Required** (bounded depth within DE-08, standing ADD rules) → konnektoren card gained the sondern example pair + «sondern vs aber» chip, new `sondern` dialog (correction vs plain contrast, error pair, nicht nur …, sondern auch, position-0 order), `negation` dialog names the «а» = sondern link — same day |
| EN-G09 | English | Flavour words: just, actually, still, even, though | User request 2026-09-13 (EN mirror of DE-17); includes the *actually* ≠ «актуально» false friend | **Decided 2026-09-13: Required** → promoted as EN-17, implemented same day |
| EN-G10 | English | Linking connectors: but/however, so/therefore, meanwhile, nevertheless, although/despite | User request 2026-09-13 (meanwhile/nevertheless question); function-level meanings are stable, not too contextual for a lookup card | **Decided 2026-09-13: Required** → promoted as EN-18, implemented same day |
| EN-G11 | English | Correction pair after negation: not X, but Y («не X, а Y») and not only … but also («не только …, но и») | Same user probe 2026-09-24, EN mirror of DE-G13: the linkers card (EN-18) covered but/however etc. but no within-sentence correction pattern. Sources: Cambridge Grammar (Conjunctions: contrasting — not…but), British Council LearnEnglish (contrasting ideas); inversion after fronted not only is B2 → out of scope (EN-X03) | **Decided 2026-09-24: Required** (bounded depth within EN-18, standing ADD rules) → linkers card gained the chip + pattern example pair, new `not-but` dialog (both patterns, plain-but boundary, within-sentence position note) — same day |
| EN-G12 | English | Contrast linkers while/whereas and on the other hand | Completeness sweep 2026-09-24 (DE-G13/EN-G11 session): the contrast family is otherwise covered (but/however, nevertheless, although/despite); two-clause contrast (while/whereas) and the register pair on the other hand are absent | **Decided 2026-09-24: Required** → promoted as EN-25, shipped same day (while dual-use, whereas, on the other hand as a bounded card in `#order`) |
| EN-G01 | English | be questions/negatives and there is/are | Required depth and placement | **Decided + closed:** the be/modal question half shipped 2026-09-13 (C-14); there is/are + be-negatives → EN-19 shipped same day |
| EN-G02 | English | Negation beyond modal prohibitions | Required depth and placement | **Decided 2026-09-24: Required** → promoted as EN-21, shipped same day (do-support negatives, never without not — double-negative trap, no vs not any) |
| EN-G03 | English | Past Continuous and narrative tense contrasts | Include, defer or exclude | **Decided 2026-09-13: Required** → promoted as EN-20, shipped same day (background-vs-event contrast, Russian-aspect mapping in dialog) |
| EN-G04 | English | Present Perfect with duration and continuous aspect | Required tense boundary | **Decided 2026-09-24: split** — duration (since/for) shipped earlier in EN-06; continuous aspect → EN-22 PPC recognition card shipped same day (state-verb exception in dialog) |
| EN-G05 | English | Relative clauses | Include, defer or exclude | **Decided 2026-09-24: Required** → promoted as EN-23, shipped same day (who/which/that, whose/where, object-that omission, antecedent agreement) |
| EN-G06 | English | Imperative, basic linking words and reported speech | Split into reviewable decisions | **Decided 2026-09-24 (split):** linking → shipped earlier as EN-18; imperative → EN-24 shipped same day; reported speech → **Deferred** (backshift is a multi-card series with B1+ density; reconsider when the supported level expands) |
| EN-G07 | English | Dedicated numbers/date/time reference | Include, defer or exclude; earlier information architecture implied coverage without defining it | **Decided 2026-09-24: Required** → promoted as EN-26, shipped same day (ordinals with spelling traps, dates on 5 May / on the 5th of May, years and decades) |
| EN-G08 | English | Present Continuous with `always` for irritation/complaint ("He's always losing his keys") | Required/Deferred/Excluded decision; usage verified against `research/englishpage.md` (EnglishPage, "Repetition and Irritation with Always") | **Decided 2026-09-13: Required** → folded into EN-05 acceptance depth; shipped same day (card hint + dialog block) |

## Findings and follow-up

| ID | Topic / evidence | Consequence | Required action | Status / retest |
| --- | --- | --- | --- | --- |
| C-01 | `AGENTS.md` verification and both plans' update protocols previously contained only runtime/design gates | Working UI could be mistaken for reviewed grammar | Add and link content gates | Documentation fixed; page review NOT RUN |
| C-02 | EN-05/06: English plan previously used signal-word selection and “время названо?” | Shortcut boundaries were not required | Require meaning/context and contrasting examples; inspect actual tense cards/dialogs against references | Plan revised 2026-09-10; page aligned 2026-09-11 (meaning-first card/dialog/practice answer, `since 2020` limit on card); retested 2026-09-11 full pass @ `b75c890`: card + `pp-vs-past` dialog + practice answer all meaning-first with the counterexample present, aligned with the registered Cambridge section — fully independent reference retest still pending |
| C-03 | Both plans: baseline without independent syllabus comparison or sourced level placement | Completeness cannot be established | Resolve DE-G01–06 and EN-G01–07 plus any gaps found by reference comparison | Open (EN-G08 added 2026-09-11); explicit category exclusions recorded in both plans |
| C-04 | Shared design contract specified German terminology despite serving English too | Shared content guidance was language-specific | State target-language terminology in the shared contract | Documentation fixed in both relevant bullets; no UI change |
| C-05 | Add-language playbook required three practice items without topic mapping | Exercise count could substitute for coverage evidence | Map practice to topics; review every answer; use additional audit probes where needed | Procedure fixed; practice remapped on both pages 2026-09-11 (DE-03/07/08, EN-01/04/06); answers reviewed 2026-09-11 full pass @ `b75c890`: all six correct with alternatives surfaced (`einem Mann`; `play football` contrast) |
| C-06 | Plan-authoring questions and scope-decision rules were spread across several files | Authors could omit exclusions or put evidence into the plan | Add one authoring owner and standardize both language plans | Documentation fixed; content baseline remains unresolved (see C-03) |
| C-07 | User-reported teaching-quality gaps (2026-09-11): DE `objects` lead named no verbs, DE `tekamolo` «База» used unglossed Temporal/Kausal/Modal/Lokal, DE `perfekt` «Важно» named no verbs; sweep added DE `wo-wohin` caveat and `passive` block without examples, EN `svo` lead typo («roles») | Learner cannot act on a rule whose terms or exceptions are not exemplified | Fix the six units; run the full unit-by-unit Teaching gate later | Six units fixed in page 2026-09-11; retested 2026-09-11 full pass @ `b75c890`: all six fixes present in the decks; Teaching gate still NOT RUN — see D-01 |
| C-08 | User-reported (2026-09-11): DE possessives table shows only `mein`; the «одна модель для всех основ» design was unclear until explained in conversation | A correct-by-scope presentation reads as incomplete coverage to the learner | State the one-model rule on the card (stems named, «основа + окончание») and add a `dein` example in the dialog | Fixed in page 2026-09-11; retested 2026-09-11 @ `b75c890`: card note + `dein` example present in deck |
| C-09 | User-reported (2026-09-11): DE ein-words table has no reading key — why Akk. m = `meinen`, Dat. = `-em/-er/-en` was unclear | A declension table without its generating rule must be memorised cell by cell | Add the key: endings mirror the definite article (den→meinen, dem→meinem, der→meiner); only three «empty» cells (Nom. m/n, Akk. n); Akk. visible in masc. only, Dat. marks all genders | Fixed in page 2026-09-11 (`why-ein-endings` chip + dialog); retested 2026-09-11 @ `b75c890`: present in deck |
| C-10 | User-reported (2026-09-11): the bold/`td.hot` table convention was missed entirely by the first learner — it is documented for developers (style-guide, DESIGN_SYSTEM) but never labeled for learners | An unlabeled visual convention does not exist for the reader it is meant to serve | One consistent `.tiny` legend under every table with hot cells (3 DE, 1 EN) | Fixed in page 2026-09-11; retested 2026-09-11 @ `b75c890`: legends present under all 4 tables |
| C-11 | DE-03 `#forms`: definite-article unit is table + hot legend only — no chip, no example; the ein/kein unit's examples live in its dialogs | Plan depth for DE-03 requires "usage examples"; der/die/das in use appears only in *other* topics' dialogs (case dialogs, `why-ein-endings`) | Add a usage line or minimal pair to the definite-article card, or attach a dialog | Fixed 2026-09-11 (example sweep, author review): definite card gained `Ich sehe **den** Mann. / mit **dem** Mann`; ein-card gained `Ich habe **einen** Bruder und **eine** Schwester. / mit **meinem** Bruder · mit **meiner** Schwester` |
| C-12 | DE-04 `#forms`: personal-pronoun unit is table + `pronouns` triples dialog; no sentence-level example anywhere in the unit | Plan depth requires "paradigm plus examples"; form recall without usage | Add one natural usage example (e.g. *Kannst du mir helfen?*) | Fixed 2026-09-11 (example sweep, author review): card gained `Kennst du **ihn**? — Ich helfe **ihm**.`; dialog triplets gained она/они/Вы glosses and a Genitiv-absence note |
| C-13 | Search metadata (both pages): DE tokens `helfen`, `sehen` (objects card), `bis`, `entlang` (prep-akk), `gegenüber` (prep-dat), `dessen`, `deren` (relative — taught nowhere), `wo`, `wohin` (case grid) are not visible on their card; EN keywords all land on delivered content | A hit that never shows the promised word is a misleading hit; `dessen`/`deren` additionally index untaught content | Surface the tokens on the cards or trim the keywords; an uncommitted search-hygiene validator in the worktree mechanically flags this class (28 DE + 10 EN tokens; its exemption list still absorbs intentional routings such as `wurde`→Konjunktiv-II) | Fixed by follow-up commits 2026-09-11→13: the hygiene validator landed in the generator (mechanical gate on every `--check`, see D-04), invisible tokens were trimmed, and `dessen`/`deren` were surfaced by teaching genitive relatives on the relative card + dialog; both `--check` gates green @ `0b5e442` |
| C-14 | EN-04 `#order`: do-support card + subject-who exception present; the plan's "be/modal distinction" (no do-support after be/modals) is absent from the whole deck | Plan-required acceptance depth missing; learner is given no *Is she…? / Can you…?* rule | Add the be/modal line to the questions card or `do-questions` dialog; the remainder overlaps EN-G01 | Fixed 2026-09-13: card `tiny` «be и модальные обходятся без do: **Is she…? Can you…?**» + `do-questions` dialog block «be / модальные» (inversion, do only for lexical verbs); EN-04 now covered |
| C-15 | EN-15 `#nouns`: comparative spelling limits only implicit — `big — bigger — the biggest` shows doubling by example; -y→-ier and e-drop are absent | Plan depth names "spelling limits"; *happier/nicer* are underivable from the card | State the three spelling rules compactly in the card or `comparative` dialog | Fixed 2026-09-13: `comparative` dialog «Орфография» block (big → bigger, happy → happier, nice → nicer); EN-15 now covered |
| C-16 | EN-13 `#nouns`: plurals unit has rules + irregulars + invariates but no countability caveat (countability itself lives one card away in EN-14) | Plan depth for EN-13 explicitly names a countability caveat | Add a one-line caveat to the plurals unit, or record a plan-depth revision | Fixed 2026-09-13: `plurals` dialog «Только исчисляемые» caveat (water/advice/information, cross-reference to the EN-14 card); EN-13 now covered |
| C-17 | EN-12 `#preps`: 8 listed pairs (6 chips + `arrive in/at`, `apologize for` in the dialog); only `depend on` has a sentence example | Plan depth says "all listed combinations with examples" — ambiguous between pair-listing and per-pair examples | Add a short example per pair **or** revise the plan depth (owner decision; not promoted here) | Fixed 2026-09-13 via the examples route (plan unchanged, no scope decision needed): `dependent-preps` dialog «Примеры» block gives a sentence for every listed pair; EN-12 now covered |
| C-18 | `en-ru.json` practice `_note` topic IDs swapped: item 2 (saw/EN-06) is noted EN-04; item 3 (Does she like/EN-04) is noted EN-06 | Provenance metadata misleads future reviews; not rendered (generator ignores `_note`) | Swap the two `_note` IDs | Fixed 2026-09-13: notes now read EN-06 (item 2) and EN-04 (item 3) |
| C-19 | DE learner-visible text defects @ `b75c890`: `ihrem` dialog title «Почему “ihрем”?» mixes Cyrillic р/е/м into the German word (deck + rendered page); `why-ein-endings` dialog «Видимо меняется только Maskulin» — «Видимо» reads as "apparently", intended "visibly" | Copying the title yields wrong characters; ambiguous wording weakens the Akk.-reading rule | Fix both strings in `de-ru.json` + regenerate | Fixed 2026-09-13: title «Почему ihrem?», «Видимо» → «Заметно»; mixed-script scan clean on both decks and pages |
| C-20 | EN example/terminology nits @ `b75c890`: `the-article` dialog uses «сверхлатив» (deck elsewhere says «превосходная»); `passive-en` dialog «Кем/чем: …by the workers, if needed.» is a fragment, not an example; `modals-en` must example (*You must stop*) shows obligation only while its label also promises deduction | Inconsistent terminology; examples that don't demonstrate the stated meaning | Rewrite the three fragments in `en-ru.json` + regenerate | Fixed 2026-09-13: «превосходная степень»; full example «The house was built **by the workers**. — рабочими»; must block split «необходимость: You must stop. · строгий вывод: He must be tired» |
| C-21 | User-reported (2026-09-12): DE double-infinitive unit (DE-14) carries no translation in its card example or either dialog example block, while the unit is declared recognition-level («Достаточно узнавать») | The form notes («не gemusst», «haben поднимается») attach to sentences the learner cannot decode; the gloss policy's form/meaning axis missed decodability (the Passiv dialog, same class, is glossed) | Amend the gloss policy with the recognition-level class and gloss the three examples | Fixed 2026-09-12 (comprehension-access change, author review): policy amended in the guide + both plans + validation §3; card and both dialog blocks glossed |

## 2026-09-11 — Incremental change: page alignment with accepted plans

Protocol §5 changed-unit record. Reviewer: ZCode (page-change author; not an
independent linguistic reviewer — author review only, full gates remain
NOT RUN). Base: `057e836` + uncommitted documentation rework; both pages
were unmodified before this change. `CACHE_VERSION` bumped to `v5`.

References consulted (accessed 2026-09-11; author-level grounding, not the
full baseline comparison):

- Lingolia, “Konjunktiv I und II” — <https://deutsch.lingolia.com/de/grammatik/verben/konjunktiv>:
  würde + Infinitiv for most verbs; direct forms wäre/hätte/könnte/müsste/sollte;
  unreal conditions, polite requests, advice, wishes.
- Grammis (IDS Mannheim), “Ersatzinfinitiv” — <https://grammis.ids-mannheim.de/systematische-grammatik/1615>
  (+ <https://www.deutschplus.net/pages/Ersatzinfinitiv>): Perfekt with core
  modal verbs uses the infinitive instead of Partizip II; *Ich habe arbeiten
  müssen*; *…, weil ich habe arbeiten müssen*.
- Cambridge Dictionary Grammar, “Past simple or present perfect?” —
  <https://dictionary.cambridge.org/us/grammar/british-grammar/past-simple-or-present-perfect>:
  present perfect = time up to now / connection with the present; past simple
  with finished periods; present perfect with unfinished periods (*today*)
  and *for/since* duration.

Changed units (all verified: structural integrity, `node --check`, runtime
browser pass at 390px with no console errors):

| Unit | Change | Coverage after change |
| --- | --- | --- |
| DE-12 card + `konjunktiv2` dialog (`#verbs`) | Added (was required, missing) | Covered (author-reviewed) |
| DE-14 card + `double-infinitive` dialog (`#verbs`) | Added recognition note with parsed example | Covered (author-reviewed) |
| DE practice item 1 answer | Now surfaces `der → dem` (DE-03 step) and the `einem Mann` alternative | Matches DE-03/07/08 mapping |
| EN-06 card + `pp-vs-past` dialog + practice item 2 | Meaning/context first; “время названо?” demoted to a clue with the `since 2020` counterexample on the card | Covered (author-reviewed); C-02 page half done |
| EN practice items 1 and 3 | Replaced per plan mapping: `play the piano` (EN-01), `Does she like` (EN-04); the conditional item (EN-16) left the practice set — consequence of the accepted three-topic mapping, recorded here | Matches EN-01/04/06 mapping |

Verified unaffected neighbors: DE-13 Passiv card/dialog unchanged;
EN-05 cards already present markers as secondary clues; EN-09 passive dialog
lists only the four shown tense forms (no “all tenses” claim).

Gate impact: none of the four gates changes status — Baseline, Coverage,
Accuracy and Teaching remain NOT RUN pending the full independent review.
This record only establishes that the changed units match the accepted plans
and cited references at author level.

## 2026-09-11 — Teaching-quality pass (user-reported signals)

Reviewer: ZCode (page author; user acting as first learner reviewer). Trigger:
three units reported unclear by the user while reading the live German page.
Method: targeted class-sweep of every dialog lead and caveat-style block
(«Важно», «Но», «Запомни», «База») on both pages — not the unit-by-unit
Teaching gate. `CACHE_VERSION` v6.

Fixed units:

| Unit | Was | Now |
| --- | --- | --- |
| DE `objects` (DE-01 area) | «Некоторые глаголы легко дают Dativ + Akkusativ» — no verbs, no why | Lead states the two-object requirement; body lists geben, schenken, zeigen, bringen, sagen, erklären + the geben parse |
| DE `tekamolo` (DE-09) | Temporal → Kausal → Modal → Lokal, unglossed | Russian question glosses (когда?/почему?/как?/где?) + one demo sentence |
| DE `perfekt` (DE-07) | «форму которых надо просто знать» — no verbs | ist geblieben / ist passiert vs hat getanzt named |
| DE `wo-wohin` (DE-02) | Caveat reasoned but no example | im Park / in den Park contrast pair added |
| DE `passive` (DE-13) | «Не путай с Perfekt» label over a Perfekt-passive form | Relabeled «А вот Perfekt Passiv» |
| EN `svo` (EN-03) | Lead typo «roles» in Russian text | «роли» |
| DE possessives card + `possessives` dialog (DE-05; later same day, finding C-08) | One-model table design lived only in the dialog; learner read `dein` as missing | Card tiny note names the stems and the «основа + окончание» rule; dialog adds a `dein` example |
| DE ein-words card + `why-ein-endings` dialog (DE-03/05; later same day, finding C-09) | Declension table had no generating rule; endings read as arbitrary | New chip «Почему meinen?» + dialog: endings mirror the definite article; three empty cells; Akk./Dat. reading rules |
| All tables with `td.hot` (DE×3, EN×1; later same day, finding C-10) | Bold/accent convention never labeled for learners | Consistent `.tiny` legend under each table: «Жирным — формы-ловушки…» |

Verified: chip↔dialog bijection, `node --check`, curly-quote scan clean.
Gates unchanged: all four remain NOT RUN.

## 2026-09-11 — Full two-language review pass (DE + EN)

Reviewer: ZCode review session — separate from the authoring sessions but the
same tool lineage, **not** a human linguistic reviewer; per protocol §3 the
formal Accuracy and Teaching gates therefore stay NOT RUN (see D-01).

Revision: committed `b75c890`, tree clean at review start — both
`--check` gates verified exit 0 on that state. At report time the worktree
carries another session's uncommitted work (dirty paths: `de/ru/SITE_PLAN.md`,
`en/ru/SITE_PLAN.md`, `tools/build_pages.py`, `content/decks/de-ru.json`,
`content/decks/en-ru.json`, `de/ru/index.html`, `en/ru/index.html` — a
gloss-by-rule-type contract in both plans, a search-hygiene validator, and
keyword-trim fixes to the decks/pages). All findings below are measured
against committed `b75c890` content; the uncommitted changes are not
evaluated by this record.

Scope: full pass, both directions, for `content/decks/de-ru.json` →
`de/ru/index.html` and `content/decks/en-ru.json` → `en/ru/index.html`.
Runtime/browser checks: **NOT RUN** (separate gate in AGENTS.md).

References: no new external access this pass. Retests of DE-12, DE-14 and
EN-06 were measured against the excerpts already registered in the
2026-09-11 incremental record (Lingolia "Konjunktiv I und II"; Grammis
"Ersatzinfinitiv"; Cambridge "Past simple or present perfect?"). The baseline
syllabus comparison (C-03) was not performed.

Inventory and counts:

| | DE | EN |
| --- | --- | --- |
| Required topics inventoried | 16/16 | 16/16 |
| Cards | 32 (incl. case grid) | 29 |
| Tables | 3 | 1 |
| Content dialogs | 28 (+ `lookup-help`) | 29 (+ `lookup-help`) |
| Practice Q&A | 3 | 3 |
| `data-search` lists | 33 | 30 |

Inspected: both deck JSONs in full; validator/search/lang-marking code paths
in `tools/build_pages.py` (search indexes `card.textContent + data-search`
only, never dialogs — verified in the page JS; chip→DETAILS bijection
enforced by `validate()` and manually confirmed, no orphan keys; client-side
`lang` marking identical on both pages); generated pages via drift check plus
spot-checks and a mixed-script scan; both SITE_PLANs; this file; `DEBT.md`.

### Coverage (plan → page)

| Topic | Coverage | Evidence |
| --- | --- | --- |
| DE-01 | covered | `#cases` grid + dialogs `nominativ`/`akkusativ`/`dativ`/`genitiv` (role + example each) + `objects` card/dialog |
| DE-02 | covered | 4 `preps` cards + `prep-akk`/`prep-dat`/`two-way` dialogs + `wo-wohin` movement caveat (*im / in den Park*) |
| DE-03 | **partial** → covered (post-sweep retest 2026-09-11) | Both declension tables with legends; anchor examples added to both article units (C-11 fixed; author review) |
| DE-04 | **partial** → covered (post-sweep retest 2026-09-11) | Full table + usage sentence on card + glossed triples (C-12 fixed; author review) |
| DE-05 | covered | Stems + one-model rule on card (C-08 retest ✓); examples in `possessives` dialog |
| DE-06 | covered | V2 + inversion + questions cards; `v2` dialog (position ≠ word) |
| DE-07 | covered | Modal/perfekt/separable formulas with parsed examples; `perfekt` dialog names sein/haben verbs (C-07 retest ✓) |
| DE-08 | covered | weil/dass/wenn/obwohl/ob + coordinators card with verb-second contrast; `coordinators` dialog |
| DE-09 | covered | TeKaMoLo card + Russian-glossed dialog + explicit "не железный закон" limit |
| DE-10 | covered | Relative card (der/den) + `relative` dialog (gender/number vs case) |
| DE-11 | covered | um … zu / damit card + same-subject decision in `um-damit` |
| DE-12 | covered | würde + direct forms on card; `konjunktiv2` dialog (Lingolia-aligned) |
| DE-13 | covered | werden + Partizip II formula + example; `passive` dialog shows Präsens and Perfekt Passiv |
| DE-14 | covered | Recognition note + parsed *habe arbeiten müssen*; `double-infinitive` dialog (Grammis-aligned) |
| DE-15 | covered | Dativ plural with limit («если его ещё нет»), Genitiv -s/-es («часто»), N-decl + `n-decl` list |
| DE-16 | covered | Hedged compact overview + `adjectives` dialog (der-words / ein-words / no article) |
| EN-01 | covered | a/an/the card + `a-an`/`the-article`/`zero-article` dialogs + institution card + `school-exceptions` |
| EN-02 | covered | Four-column paradigm + `my-mine`/`reflexive` usage dialogs |
| EN-03 | covered | `svo` card/dialog + frequency card/dialog (before V, after be; never/rarely negative) |
| EN-04 | **partial** | Do-support + subject-who exception present; be/modal distinction absent from the deck (C-14) |
| EN-05 | covered | PS/PC cards + `present-continuous` contrast + state-verb limit |
| EN-06 | covered | Meaning-first card + `since 2020` limit + `pp-vs-past` dialog (C-02 retest ✓) |
| EN-07 | covered | will/going-to card + `future` dialog incl. scheduled present |
| EN-08 | covered | Modals card + `modals-en` (must vs have to) + `mustnt` contrast |
| EN-09 | covered | be + V3 with exactly the four shown forms; no "all tenses" claim |
| EN-10 | covered | Listed patterns + labeled stop meaning-change in `gerund-infinitive` |
| EN-11 | covered | in/on/at time + place cards/dialogs; labeled exceptions (*at night*, *at the weekend* (брит.), *in hospital* (брит.)) |
| EN-12 | **partial** | 8 listed pairs; only *depend on* has a sentence example (C-17) |
| EN-13 | **partial** | Rules + irregulars + invariates present; countability caveat absent from the unit (C-16) |
| EN-14 | covered | much/many/few/little + some/any cards/dialogs; RU-interference traps (*advice/news/money*, *some* in requests) |
| EN-15 | **partial** | Patterns + high-frequency irregulars present; spelling limits implicit only (C-15) |
| EN-16 | covered | Types 0–2 core with meaning; Type 3 framed as recognition |

Practice: DE items map to DE-03/07/08 and EN items to EN-01/06/04 (the
swapped `_note` metadata is C-18). All six answers correct; alternatives
surfaced (DE *einem Mann*; EN *play football* contrast).

### Coverage (page → plan)

Every card, dialog, table cell, practice item and search list on both pages
maps back to a topic ID: DE 32 cards + 28 dialogs + 3 practice → DE-01…16,
EN 29 cards + 29 dialogs + 3 practice → EN-01…16. No unmapped content on
either page. Search keywords that exceed their card's visible content are
filed as C-13 (search-metadata finding, not scope).

### Accuracy and teaching observations (reviewer pass, not the formal gates)

No wrong rule, form, paradigm cell or practice answer was found on either
page; simplifications carry their limits (TeKaMoLo "не закон", "часто
Genitiv" + colloquial-Dativ caveat, "универсальная форма" bounded by the
named direct forms, `since 2020` counterexample, PC state-verb list,
Type-1 "не will after if"). Counterexample probes: *Ich jogge im Park*
(motion, Dativ) present in `wo-wohin`; Present Continuous + *always*
(complaint use) absent deck-wide → filed as EN-G08. Remaining defects are
wording/metadata/search issues (C-13, C-18, C-19, C-20) and coverage gaps
(C-11, C-12, C-14–C-17). Cross-language contract: mechanics, hot-legend
convention (3 DE + 1 EN), search and lang-marking behavior identical; the
DE nav-view vs EN footer-link practice placement is encoded in both plans
and is an accepted divergence.

### Gate verdicts

| Gate | German | English | Reason |
| --- | --- | --- | --- |
| Baseline | FAIL | FAIL | DE-G01–06, EN-G01–07 (+EN-G08) undecided; level placement unsourced (C-03). Positive: inventories complete; exclusions carry rationale and reconsideration triggers |
| Coverage | FAIL | FAIL | DE-03/DE-04 partial (C-11/C-12); EN-04/12/13/15 partial (C-14–C-17). All other topics covered; no unmapped content |
| Accuracy | NOT RUN | NOT RUN | Every unit reviewed at reviewer level with no wrong content found; reference-grounded independent pass still outstanding (protocol §3, D-01) |
| Teaching | NOT RUN | NOT RUN | C-07–C-10 retests verified present and effective; unit-by-unit gate pending; new wording/teaching findings C-11, C-12, C-17, C-19, C-20 |

Overall: content **not accepted**. Next actions: resolve the filed findings
(cheapest first: C-18, C-19, C-20; then coverage C-11/C-12/C-14–C-17 and
C-13 keyword hygiene), then scope decisions on the G-findings and the
independent reference-grounded pass required by D-01/D-02. This record does
not change any SITE_PLAN.

## 2026-09-11 — Example-gloss policy + forms-section examples (user-approved sweep)

Protocol §5 changed-unit record. Reviewer: ZCode (page-change author; author
review only — gate statuses from the full pass above are unchanged except
the C-11/C-12/C-13 retests noted there). Trigger: user question about
example sentences/translations, plus the page review discussed with the
user. Base: working tree on top of `b75c890`.

Policy (both plans updated first): example glosses follow the rule type —
form/position rules keep target-language-only examples with structural
annotation; meaning/usage rules add a short Russian gloss carrying the
deciding difference; fragments stay unglossed.

Changed units:

| Unit | Change | Note |
| --- | --- | --- |
| DE forms cards ×3 (DE-03/04/05) | One bare anchor example each; honest per-table hot legends (article tables: Maskulin-Akkusativ + весь Dativ, Genitiv consciously cold as rarer at A1–B1; pronoun table: Dativ ≠ Akkusativ); Genitiv/Dativ-Plural noun-ending pointer | C-11/C-12 fixes; the previous generic legend stated a rule the marking did not follow |
| DE `pronouns` / `possessives` / `relative` dialogs | она/они/Вы triplet glosses; Genitiv-absence note; euer→eure trap block; genitive-relatives block | smaller review items |
| DE cards: `ihrem` chip relabeled «Почему mit ihrem Bruder?»; relative card genitive line; modal-verb list tiny; W-word list tiny; `möchte` added to Konjunktiv direct forms; Passiv chip relabeled «Passiv в двух временах» (dialog contrasted two passive tenses, not Passiv-vs-Perfekt) | keyword visibility + honesty fixes |
| DE examples: Perfekt/Konjunktiv-II/um…zu-vs-damit gained deciding glosses (— движение → sein; — нереальное сейчас; — субъект тот же/субъекты разные); wo/wohin example gained (Wo?)/(Wohin?) tags | gloss policy (meaning rules) |
| EN cards: pronouns table gained `I saw **him**. · This is **his** car.`; mustn't examples gained «здесь нельзя» / «не обязательно» | EN-02 usage example; gloss policy |
| DE/EN search metadata | ~22 keywords trimmed or surfaced | C-13 fix; enforced by the new build gate in `tools/build_pages.py` (exemptions live per target in `site.json` `grammar_terms` + `grammar_terms_common`; Cyrillic searcher-words exempt by Unicode range incl. Ukrainian letters; inflections matched by prefix) |

Consequences to track: searching `helfen` no longer matches the objects
card; it returns only cards visibly containing a form of it (Konjunktiv II
example, practice answer) until DE-G06 resolves. DE-G07 (der vs ein choice)
and DE-G08 (seit vs vor) filed above. C-14..C-17 from the full pass are
untouched by this sweep and remain open.

Verification: visible-text diff vs pre-change snapshots contains only the
listed edits; structural invariants unchanged (card/chip/dialog counts,
view/anchor routing, search/reveal/dialog probes — «dessen»→relative card,
«können»→modal card); lang-mark counts shift exactly as accounted (+8 bold
anchors, +3 new pure-German example containers, −3 containers that gained
Cyrillic glosses); `--check` idempotent both decks (includes the new search
gate); JS syntax clean; 390px no overflow; console clean.

## 2026-09-12 — Incremental change: comprehension-access glosses

Protocol §5 changed-unit record. Reviewer: ZCode (page-change author; author
review only — full gates remain NOT RUN). Base: `50dd17a`, worktree clean.
Trigger: user-reported comprehension failure on the live double-infinitive
dialog (C-21) — recognition-level examples carried no translation.

Change: the example-gloss policy gains a third class — recognition-level
constructions and any example the intended learner cannot be expected to
decode always carry a short gloss; there the gloss is comprehension access
to the sentence the rule is about, not the choice criterion. The principle
is recorded in [the SITE_PLAN guide](docs/SITE_PLAN_GUIDE.md) §6
(cross-language owner), instantiated in both language plans, and added as
a review check in [content validation](docs/CONTENT_VALIDATION.md) §3.
No external reference consulted: the change translates existing sentences
and adds no grammar.

| Unit | Change | Coverage after change |
| --- | --- | --- |
| DE-14 card example (`#verbs`) | `Ich habe arbeiten müssen. — Я должен был работать. Не “gemusst”.` | Covered (author-reviewed) |
| DE-14 `double-infinitive` dialog, «Форма» | `Ich habe lange arbeiten müssen. — Я долго должен был работать.` + existing Partizip-II note kept | Covered (author-reviewed) |
| DE-14 `double-infinitive` dialog, «В придаточном» | `…, weil ich lange habe arbeiten müssen. — «…что мне долго пришлось работать»` + existing word-order note kept | Covered (author-reviewed) |

EN sweep: every detail/example block in `en-ru.json` scanned
(mechanical Cyrillic-free block list + author judgment) — all
English-only blocks are A1–B1-decodable sentences or word-list fragments;
no recognition-level unit exists, no change required.

Verified: `--check` idempotent both decks (validator + search gate pass);
rendered diff confined to the unit — card example and dialog body, three
strings, nothing else (page 50854 → 50945 bytes). Gates unchanged: all
four remain NOT RUN.

## 2026-09-13 — Incremental change: findings sweep closes C-13…C-20

Protocol §5 changed-unit record. Reviewer/implementer: ZCode (same session as
the 2026-09-11 full pass; not an independent linguistic reviewer). Base:
`0b5e442` (which had already closed C-11/C-12 via the example sweep and
C-13's mechanical half via the validator), worktree clean. `CACHE_VERSION`
v13 → v14.

Changed units (all verified: both `--check` gates exit 0, mixed-script scan
clean, runtime smoke test below):

| Unit | Change | Finding |
| --- | --- | --- |
| EN-04 questions card + `do-questions` dialog (`#order`) | be/modal no-do rule: card `tiny` + dialog block «be / модальные» | C-14 |
| EN-15 `comparative` dialog (`#nouns`) | «Орфография» block: doubling, -y → -ier, e-drop | C-15 |
| EN-13 `plurals` dialog (`#nouns`) | «Только исчисляемые» caveat with cross-ref to EN-14 | C-16 |
| EN-12 `dependent-preps` dialog (`#preps`) | «Примеры» block: sentence example for every listed pair | C-17 |
| EN practice `_note` metadata | Topic-ID swap corrected (EN-06 / EN-04) | C-18 |
| DE-05 `why-ein-endings` + `ihrem` dialogs (`#forms`) | «Видимо» → «Заметно»; title «Почему “ihрем”?» → «Почему ihrem?» | C-19 |
| EN `the-article`, `passive-en`, `modals-en` dialogs | «сверхлатив» → «превосходная степень»; full by-phrase example; must obligation vs deduction split | C-20 |

Verified unaffected neighbors: DE-03/DE-04 example lines from the 2026-09-11
sweep intact; genitive-relative teaching on the DE relative unit intact
(C-13 surface half); chip↔dialog bijection re-enforced by the generator's
validator; practice items and answers untouched.

Runtime smoke test (scoped; not the full AGENTS.md checklist): served via
`http.server 8931`, service-worker cache reset, both pages reloaded — no
console errors; EN search «interested» filters to the dependent-preps card;
DE search «wem» works; `do-questions`, `comparative`, `dependent-preps`,
`plurals`, `ihrem` dialogs open with the new blocks; practice reveal works;
`lang="en"` marking present on dialog examples. Offline reload, 390px
overflow, theme cycle and redirect checks: **NOT RUN** this pass.

Gate impact: Coverage → **PASS** for both languages (16/16 required topics
covered; all content mapped back to scope in the 2026-09-11 pass, and no
unmapped content was added). Baseline remains **FAIL** (DE-G01–06, EN-G01–08
undecided). Accuracy and Teaching remain **NOT RUN** pending the independent
reference-grounded pass (D-01). EN-G08 (Present Continuous + always) still
requires an owner decision and is not promoted to the plan.

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
[the de-en plan](de/en/SITE_PLAN.md).

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
[the en-de plan](en/de/SITE_PLAN.md).

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

## 2026-10-20 — Meaning support in all four language pairs

### Authorization, scope and provenance

- The site author approved making words and examples understandable in each
  deck's explanation language. The four plans and validation policy now
  require comprehension support for form/position rules as well as usage
  rules. No vocabulary-course expansion or interaction redesign.
- Base revision: `4e40239b7e7dbbb26c21e10adda4cf1205718045`.
  Reviewed working-tree sources: `content/decks/de-ru.json`, `de-en.json`,
  `en-ru.json`, `en-de.json`; generated pages in the corresponding four
  target/audience folders. Plans, schema description, shared design contract,
  decision ledger, this audit, DEBT, changelog and service-worker version
  accompany the change. Existing untracked `.mcp.json`, `designs/` and
  `research/lovable-approach.md` were not changed.
- Author: Codex primary agent. Independent linguistic reviewer:
  `/root/linguistic_review`, a separate agent with read-only access. It
  inspected all cards, dialogs and their tables/examples, compared against
  HEAD, consulted the references below, reported defects, and retested the
  corrections. Initial FAIL findings and final PASS are both preserved here;
  automated generation/browser checks do not certify linguistic accuracy.
- Every card example now has an audience-language `gloss`. Sentence formulas
  have adjacent translations; key word lists use the existing term/meaning
  legends. Dialog examples have translations in comments or adjacent prose.
  Inflected forms are linked to their lemma where useful. Auxiliaries are
  explained by function. Duplicate lists were removed after mobile inspection.

### Content inventory and immutable source snapshots

Counts are actual data units, not topic counts. The unit-location inventory
below identifies every reviewed card and dialog by its stable key; the four
SHA-256 values pin the final authored data, including all table cells,
formulas, terms and dialog blocks. Existing source examples (159 blocks),
formulas (62 blocks), tables (10, 274 header/body cells), card anchors and
dialog keys were compared with HEAD and preserved. Meaning clues and
explanatory corrections are the changes.

| Deck | Cards | Dialogs | Translated example blocks | Dialog blocks | SHA-256 |
| --- | ---: | ---: | ---: | ---: | --- |
| de-ru | 44 | 42 | 40 | 144 | `e598bd58532199ce3770807162f61434f46afdd928d5e3632732de35a868d79b` |
| de-en | 44 | 42 | 40 | 154 | `7d2592aa9854780be59daae0cedb21bf1e9fc4a6240ab2ea89642ab5801d7564` |
| en-ru | 38 | 41 | 39 | 138 | `70684f73103b7af91da13a7dc0836d2fda099e1b86bef386c5f9ca9c1c39348d` |
| en-de | 38 | 41 | 40 | 158 | `a8d5c6981897a0933aceb449e00b33a7fd25acdb589df2ac7ba9ed3c0bc580cb` |

For each listed unit, the review probe was: can a learner decode the actual
words/formula/example in the explanation language, does its gloss preserve
the relevant meaning, and do the rule and dialog agree? Expected: contextual
meaning and valid forms without misleading one-to-one claims. Observed:
missing meanings and the findings below were corrected; all listed units
passed independent semantic/teaching review after retest. This does not
assign CEFR levels or certify a complete curriculum.

**de-ru — card anchors** (in `de/ru/index.html`; source cards under `sections`):

`cases-faelle`, `cases-wo-wohin`, `cases-objects`, `forms-artikel`, `forms-dieser`, `forms-artikelwahl`, `forms-ein-words`, `forms-negation`, `forms-pronomen`, `preps-praep-akk`, `preps-praep-dat`, `preps-wechsel`, `preps-praep-gen`, `preps-verb-praep`, `preps-seit-vor`, `order-v2`, `order-inversion`, `order-w-fragen`, `order-tekamolo`, `order-partikeln`, `order-imperativ`, `verbs-modalverben`, `verbs-perfekt`, `verbs-trennbare`, `verbs-passiv`, `verbs-konjunktiv2`, `verbs-doppelinfinitiv`, `verbs-praeteritum`, `clauses-weil`, `clauses-dass`, `clauses-wenn-als`, `clauses-obwohl`, `clauses-ob`, `clauses-konnektoren`, `clauses-um-zu-damit`, `clauses-relativsatz`, `clauses-verknuepfungen`, `extras-verb-endungen`, `extras-dativ-plural`, `extras-plural`, `extras-genitiv-s`, `extras-n-deklination`, `extras-adjektive`, `extras-komparativ`.

**de-ru — dialog locations** (`content/decks/de-ru.json`, `details.<key>`):

`lookup-help`, `linking-adverbs`, `conjugation`, `negation`, `imperative`, `praeteritum`, `comparative`, `article-choice`, `verb-preps`, `seit-vor`, `nominativ`, `akkusativ`, `dativ`, `genitiv`, `wo-wohin`, `objects`, `possessives`, `why-ein-endings`, `ihrem`, `pronouns`, `prep-akk`, `prep-dat`, `two-way`, `v2`, `tekamolo`, `particles`, `modal`, `perfekt`, `separable`, `passive`, `konjunktiv2`, `double-infinitive`, `wenn-als`, `obwohl`, `coordinators`, `sondern`, `um-damit`, `relative`, `dieser`, `plural`, `n-decl`, `adjectives`.

**de-en — card anchors** (in `de/en/index.html`; source cards under `sections`):

`cases-faelle`, `cases-wo-wohin`, `cases-objects`, `forms-artikel`, `forms-dieser`, `forms-artikelwahl`, `forms-ein-words`, `forms-negation`, `forms-pronomen`, `preps-praep-akk`, `preps-praep-dat`, `preps-wechsel`, `preps-praep-gen`, `preps-verb-praep`, `preps-seit-vor`, `order-v2`, `order-inversion`, `order-w-fragen`, `order-tekamolo`, `order-partikeln`, `order-imperativ`, `verbs-modalverben`, `verbs-perfekt`, `verbs-trennbare`, `verbs-passiv`, `verbs-konjunktiv2`, `verbs-doppelinfinitiv`, `verbs-praeteritum`, `clauses-weil`, `clauses-dass`, `clauses-wenn-als`, `clauses-obwohl`, `clauses-ob`, `clauses-konnektoren`, `clauses-um-zu-damit`, `clauses-relativsatz`, `clauses-verknuepfungen`, `extras-verb-endungen`, `extras-dativ-plural`, `extras-plural`, `extras-genitiv-s`, `extras-n-deklination`, `extras-adjektive`, `extras-komparativ`.

**de-en — dialog locations** (`content/decks/de-en.json`, `details.<key>`):

`lookup-help`, `verb-preps`, `seit-vor`, `nominativ`, `akkusativ`, `dativ`, `genitiv`, `wo-wohin`, `objects`, `prep-akk`, `prep-dat`, `two-way`, `dieser`, `article-choice`, `possessives`, `why-ein-endings`, `ihrem`, `negation`, `pronouns`, `conjugation`, `plural`, `n-decl`, `adjectives`, `comparative`, `v2`, `tekamolo`, `particles`, `imperative`, `modal`, `perfekt`, `separable`, `passive`, `konjunktiv2`, `double-infinitive`, `praeteritum`, `wenn-als`, `obwohl`, `coordinators`, `sondern`, `um-damit`, `relative`, `linking-adverbs`.

**en-ru — card anchors** (in `en/ru/index.html`; source cards under `sections`):

`articles-articles`, `articles-zero-article`, `pronouns-pronouns`, `order-svo`, `order-do-questions`, `order-frequency`, `order-mistakes`, `order-nuances`, `order-linkers`, `order-contrast-linkers`, `order-there-is`, `tenses-present-simple`, `tenses-present-continuous`, `tenses-past-simple`, `tenses-present-perfect`, `tenses-pp-vs-past`, `tenses-future`, `tenses-past-continuous`, `tenses-pp-continuous`, `verbs-modals`, `verbs-mustnt`, `verbs-passive`, `verbs-gerund-infinitive`, `verbs-relatives`, `verbs-negation`, `verbs-imperative`, `preps-time`, `preps-place`, `preps-dependent`, `nouns-plurals`, `nouns-countable`, `nouns-some-any`, `nouns-comparative`, `nouns-numbers-dates`, `conditionals-cond1`, `conditionals-cond2`, `conditionals-cond0`, `conditionals-cond3`.

**en-ru — dialog locations** (`content/decks/en-ru.json`, `details.<key>`):

`lookup-help`, `flavor-words`, `linking-words`, `not-but`, `there-is`, `past-continuous`, `negation`, `pp-continuous`, `relatives`, `imperative`, `contrast-linkers`, `numbers-dates`, `a-an`, `the-article`, `zero-article`, `school-exceptions`, `my-mine`, `reflexive`, `svo`, `do-questions`, `frequency`, `present-simple`, `present-continuous`, `past-simple`, `present-perfect`, `pp-vs-past`, `future`, `modals-en`, `mustnt`, `passive-en`, `gerund-infinitive`, `time-preps`, `place-preps`, `dependent-preps`, `plurals`, `countable`, `some-any`, `comparative`, `cond0`, `cond1`, `cond2`.

**en-de — card anchors** (in `en/de/index.html`; source cards under `sections`):

`articles-articles`, `articles-zero-article`, `pronouns-pronouns`, `order-svo`, `order-do-questions`, `order-frequency`, `order-mistakes`, `order-nuances`, `order-linkers`, `order-contrast-linkers`, `order-there-is`, `tenses-present-simple`, `tenses-present-continuous`, `tenses-past-simple`, `tenses-present-perfect`, `tenses-pp-vs-past`, `tenses-future`, `tenses-past-continuous`, `tenses-pp-continuous`, `verbs-modals`, `verbs-mustnt`, `verbs-passive`, `verbs-gerund-infinitive`, `verbs-relatives`, `verbs-negation`, `verbs-imperative`, `preps-time`, `preps-place`, `preps-dependent`, `nouns-plurals`, `nouns-countable`, `nouns-some-any`, `nouns-comparative`, `nouns-numbers-dates`, `conditionals-cond1`, `conditionals-cond2`, `conditionals-cond0`, `conditionals-cond3`.

**en-de — dialog locations** (`content/decks/en-de.json`, `details.<key>`):

`lookup-help`, `a-an`, `the-article`, `zero-article`, `school-exceptions`, `my-mine`, `reflexive`, `plurals`, `countable`, `some-any`, `comparative`, `numbers-dates`, `svo`, `do-questions`, `frequency`, `flavor-words`, `linking-words`, `not-but`, `there-is`, `present-simple`, `present-continuous`, `past-simple`, `present-perfect`, `pp-vs-past`, `future`, `past-continuous`, `pp-continuous`, `contrast-linkers`, `modals-en`, `mustnt`, `passive-en`, `gerund-infinitive`, `relatives`, `negation`, `imperative`, `cond0`, `cond1`, `cond2`, `time-preps`, `place-preps`, `dependent-preps`.

### Reference register (accessed 2026-10-20)

These are evidence for the tested grammatical distinctions, not CEFR placement.
The existing per-topic level/syllabus comparison remains outstanding.

| Ref | Exact reference / section | Use |
| --- | --- | --- |
| M-01 | [IDS grammis: Präteritum versus Präsensperfekt](https://grammis.ids-mannheim.de/kontrastive-grammatik/4180), introduction and Unterschiede im Gebrauch | Context/register limits of German past-tense contrasts |
| M-02 | [Duden: euer](https://www.duden.de/rechtschreibung/euer_Anrede_wessen), Flexion | Both eurem and euerm are valid |
| M-03 | [Duden: seit](https://www.duden.de/rechtschreibung/seit_seitdem), examples | seit can occur with Perfekt; ongoing-state Präsens is not a blanket prohibition |
| M-04 | [IDS grammis: Präpositionalobjekt](https://grammis.ids-mannheim.de/sgt/2279) | Fixed verb/preposition/case government |
| M-05 | [Cambridge English Grammar Today: Relative pronouns](https://dictionary.cambridge.org/grammar/british-grammar/relative), subject/object and omission sections | Object-relative omission in defining clauses; subject relatives retained |
| M-06 | [Cambridge: Past simple (I worked)](https://dictionary.cambridge.org/grammar/british-grammar/past-simple-i-worked), forms and questions | be has was/were and does not use did |
| M-07 | [Cambridge: Adverbs and adverb phrases](https://dictionary.cambridge.org/uk/grammar/british-grammar/adverbs-and-adverb-phrases), position | Individual adverb positions; frequency-position limits |
| M-08 | [Cambridge: Must](https://dictionary.cambridge.org/grammar/british-grammar/must), obligation and must/have to | Obligation overlap and form differences |
| M-09 | [Cambridge: Play or …?](https://dictionary.cambridge.org/us/grammar/british-grammar/play-or-), musical instruments | Usually the, not an absolute rule |
| M-10 | [Goethe-Institut: Gesund Leben](https://www.goethe.de/resources/files/pdf341/final-goethe-book-pages.pdf), 3.f Modalverben | Necessity/permission and prohibition contrast |

### Findings and retest results

All findings below were initially FAIL. All are now **RESOLVED / retest PASS**.
Card names and `details` keys below are exact locations within the named decks.

| ID | Location | Probe → expected / observed after correction |
| --- | --- | --- |
| M-F01 | All four decks, every card/example and all dialogs | Decode without an external translator → audience-language meanings supplied; structural emphasis retained; all 159 example blocks paired |
| M-F02 | de-en `perfekt`, `praeteritum` cards/dialogs | Ich habe gegessen → I ate / I have eaten by context; removed false never-present-perfect claim (M-01) |
| M-F03 | Both German `verb-praep` / `verb-preps` | warten auf + Akk. vs teilnehmen an + Dat. → case learned with the fixed pair, not auf alone (M-04) |
| M-F04 | Both German `seit-vor` | Ongoing residence vs Seit gestern habe ich nichts gegessen → Präsens tendency with a translated Perfekt counterexample (M-03) |
| M-F05 | Both German `possessives` | eurem/euerm → neither valid form marked wrong (M-02) |
| M-F06 | Both German `conjugation`, `plural` | wir sind/ihr seid vs regular endings; Kind→Kinder vs Buch→Bücher → exceptions and suffix/vowel distinctions accurate; Männer removed from -e examples |
| M-F07 | Both German `dieser`; de-en `artikelwahl`, `article-choice`, `konjunktiv2` | Distance and professions/direct forms → no false ban on expressing distance, an emphasized profession article, or würde sein/haben in every context |
| M-F08 | Both English `relatives` | The book (that) I read vs The book that helps → omission for object only, in defining clauses (M-05) |
| M-F09 | Both English `past-simple` | I was / you were; Were you tired? → be exception and no-did form explicit (M-06) |
| M-F10 | Both English `flavor-words`; en-de `frequency` | Actually… / Even a child… / …though → no single fixed-slot rule (M-07) |
| M-F11 | Both English `modals` / `modals-en` | must go vs have to go / Do you have to go? → exception visible on card; must/have-to split qualified (M-08) |
| M-F12 | en-de `past-continuous`, `a-an`, `zero-article`, `gerund-infinitive`, `comparative` | called→anrief; sound-based a/an; ordinary German article omission; wollen without zu; than vs as…as → translations and contrasts corrected (M-09 for instrument caveat) |
| M-F13 | en-ru `reflexive` | Full paradigm → yourselves included with meaning |
| M-F14 | Both targets, newly translated dialog comments | Each comment must translate its own source → shifted indices and unsupported alternatives removed; weil translated because; Reise/Geschenk translated trip/gift |
| M-F15 | All four, mobile copy | Meaning clues must not create duplicate inventories → repeated modal/preposition lists and the duplicated de-en plural paragraph removed |

### Gates and runtime evidence

| Gate | Result | Boundary |
| --- | --- | --- |
| Baseline | FAIL (unchanged); new syllabus audit NOT RUN | C-03/D-02: per-topic CEFR/level placement is not sourced by this sweep |
| Coverage | Prior topic coverage carried forward | Same topic inventory, 164 card identities, 166 dialog keys, tables/formulas/source examples preserved; no topic removed or added. Fresh syllabus→plan/frequency-list completeness audit NOT RUN |
| Accuracy | PASS | Separate reviewer walked all current cards/dialogs and retested substantive corrections; source register above |
| Teaching | PASS | Meaning support, example/gloss correspondence, card/dialog consistency and relevant caveats reviewed across all four pairs |

Runtime on Python's HTTP server at `http://127.0.0.1:8931/`:

- `python3 tools/build_pages.py content/decks/<pair>.json --check` ×4:
  PASS. `--check-shell`: PASS. `--check-siblings`: no table-row drift;
  reported formula/example differences are the pre-existing audience
  adaptations (source formulas/examples match HEAD exactly), not new drift.
- Chromium via agent-browser, 390×844: all 18 deck views across classic/skin A
  and auto/light/dark (108 view/skin/theme combinations) have no horizontal
  page/card overflow. All examples render as pairs: 40/40/39/40; bare = 0.
  All 165 reachable dialog keys opened and closed with populated bodies and
  no dialog overflow. One existing en-de `present-perfect` dialog is unlinked
  (the card links to `pp-vs-past`); its data was independently reviewed.
- Modal searches return matches in every pair; clearing search restores the
  selected view. Theme and skin persist across reload on all four pages.
  Native Escape closure was exercised on the German modal dialog; close
  buttons were exercised for every reachable dialog. Backdrop closure NOT RUN.
- Landing, all four deck routes and four legacy redirects passed online and
  offline (9 routes in each mode); all four deck routes also passed offline
  reload with translated examples intact. Cache `lang-cheat-v48`: 53 responses,
  all status 200. No browser errors recorded.
- Browser detail logs are local run artifacts:
  `$BB_THREAD_STORAGE/meaning-support-browser.json` and
  `$BB_THREAD_STORAGE/meaning-support-offline.json`.
  Landing locale persistence, desktop-width visual inspection and installed
  device/PWA relaunch NOT RUN in this batch. Live GitHub Pages check NOT RUN:
  the change has not been pushed.

D-01 remains open for the syllabus-to-plan/frequency-list pass; D-02 remains
open for sourced level placement. D-07 trigger (c) fired because this sweep
is a cross-audience content fix larger than one line: the separate,
byte-identical core-extraction refactor is pending in DEBT, not included in
this content change. No overall four-gate certification is claimed.

## 2026-10-21 — Documentation and release follow-up

- Released content revision: `4e5382159a846cf9b805c3786dec7f810eb2b7ca`.
  All four deck SHA-256 snapshots above are unchanged.
- Durable-doc pass corrected README's stale review status, added the
  meaning-support contract to both authoring playbooks, and aligned accepted
  plan wording for word order, purpose clauses, hypothetical forms and if.
- A final specimen pass removed the style guide's superseded “hints, not
  translations” instruction, added translations to its two card specimens,
  and corrected Russian-only wording in the shared contract/agent entrypoint.
  This documentation page change advances the service-worker cache to v49.
- Style-guide smoke: Chromium at 390×844, both card specimens render paired
  translations, page width equals viewport width, superseded policy absent,
  no browser errors. All four generated-page checks and shell check pass.
- GitHub Pages built `4e53821` successfully. Live HTTP checks on 2026-10-21:
  landing, all four generated pages, sw.js and all four legacy stubs returned
  200 and matched the released local files byte-for-byte. This extends the
  2026-10-20 local runtime evidence; it does not change the content-gate verdicts.

## 2026-10-21 — Readable term lists and explicit German Imperativ contrast

- Authorized scope: one-entry-per-row modal meanings; whole-entry inline
  wrapping with balanced dots; an explicit German statement/request example.
  Base: `a487f7237431c867b0f985ad370018812fc87c1b`.
- Linguistic changes are confined to `order-imperativ` and
  `details.imperative` in de-ru/de-en, with DE-21 plan depth updated first.
  The cards define the use of Imperativ and contrast **Sie warten.** with
  **Warten Sie bitte!**, carrying Russian/English translations. The dialogs
  retain du/ihr/Sie formation and explain that a declarative sentence can
  function as a firm instruction without becoming an imperative form.
- Independent reviewer `/root/linguistic_review` read both changed cards,
  their dialogs and owner rows against the named base; scoped Accuracy
  **PASS**, Teaching **PASS**, no substantive findings. All other deck wording
  was compared unchanged after excluding legend layout metadata. Carry
  forward the 2026-10-20 full linguistic review only for those unchanged units.
- References (reviewer accessed 2026-10-21):
  [IDS, Aussagemodus: Interpretation als Aufforderung](https://grammis.ids-mannheim.de/systematische-grammatik/1872)
  and [IDS, Distanzform in Aufforderungen](https://grammis.ids-mannheim.de/systematische-grammatik/389).
  Probe: ordinary statement versus formal request → expected verb-before-Sie
  for the imperative form, with no universal ban on Sie + verb; observed PASS
  in both cards and dialogs, with matching translations.
- Counts remain 164 cards and 166 dialogs. The new comparison adds one paired
  example to each German deck: 41/41/39/40 example blocks, 161 total, all
  glossed. Card anchors, dialog keys, tables and existing formula/example
  content are preserved. Modal legends use `layout: "list"` on all four
  modal cards and in both German modal dialogs; other inventories retain
  their content and default inline layout.

Final authored deck snapshots (SHA-256):

- `de-ru`: `64a8a766c1664ffb9e6a0177bd89691a83e68984fe61a79e7eb0e5f3dbccf0b9`
- `de-en`: `8bfbd6d66c53828ea2c5dcc7cb3bc2b66da1bab6dbc5de020cfcfe6f45011899`
- `en-ru`: `f42d785ad599277b4295f9a2cc151c85cf61ee88113ef51834170bb63f21eec6`
- `en-de`: `c6a98c934e29973205749a67a8023167a8effe4294542451cd7f0ddaf6147f50`

Verification: all four builds and generated-page checks PASS; shell check
PASS; sibling check has no table-row drift. Existing audience-adapted
formula/example differences remain; the new comparison is identical across
German siblings. Negative probe `legend.layout: "columns"` is rejected by
the stdlib validator; valid list markup has UL/LI semantics and role=list.
New `layout` metadata does not enter the search text.

Baseline remains FAIL for sourced level placement; fresh syllabus/frequency
coverage NOT RUN (D-01/D-02). Browser layout evidence is recorded in UI_AUDIT.
The service-worker cache is v50. Live release verification is performed
following push; no pre-push deployment claim is made here.

## 2026-10-23 — Italian/French English-audience implementation and independent review

Scope: new `it-en` and `fr-en` decks, accepted plans and generated pages;
shared registry/landing/template/assets integration is runtime evidence in
[UI_AUDIT](UI_AUDIT.md#2026-10-23--italianfrench-integration-and-target-language-fragments).
The owner authorized the recommended bounded targets after the research.
No reciprocal audience, explanation locale or practice system was added.
This is acceptance of the selected scope, not a full CEFR/exam curriculum.

Git base: `05eed47bf715288739f35ef63d8859a1f72758b0`. These additions are
uncommitted working-tree files; HEAD alone does not identify the reviewed
content. Italian author: `thr_pfrpzvtcz9`, independent reviewer:
`thr_4bsuy4n7xv`. French author: `thr_4bsuy4n7xv`, independent reviewer:
`thr_pfrpzvtcz9`. Parent `thr_bktaq44cyt` integrated shared files and
independently checked the final Italian markup-only boundary.

Owned dirty paths: `content/decks/{it-en,fr-en}.json`, `it/en/`, `fr/en/`,
the three IT/FR research files, registry/landing/worker/icon generator and
page template; all six generated pages, eight emphasis-only source
runs in `de-en`/`en-de`, shared authoring/design docs and current audits.
Pre-existing unrelated `.mcp.json`, `designs/`, `research/lovable-approach.md`
and unrelated AGENTS hunks were preserved. No commit or push was performed.

### Inspected scope and baseline

Italian: all 36 normalized CILS rows and 31 Urbino grammar rows compared
with the publisher references. All 53 Required units mapped both directions:
51 cards in 20 sections, 307 card blocks, 180 form-list rows, 51 paired
examples and 52 dialogs/201 blocks, including the two hosted recognition
units IT-51/52 and help. Eight deferrals and six exclusions are explicit.
Selective B1 extensions and productive versus recognition depth are
identified as product allocations rather than universal CEFR claims.

French: all 94 A1/A2/B1 grammar bullets (35/29/30) independently compared
with Eaquals/CIEP 2015 Annex E and inspected grammar references. All 63
Required IDs map to 62 cards in 24 sections, 372 card blocks and 248
form-list rows; FR-01/02 share an owner, FR-61 nominalisation is Deferred.
All 63 dialogs, forms, English meanings, exception prose and scope limits
were read. Original snapshot: 347 dialog blocks; correction moves target
material from scalar leads to supported rich bodies without expanding scope.
Final corrected block counts and retest boundary are recorded below.

Every owned card/dialog block and paradigm member was inspected, not only
its example probe. No practice/hidden-answer surface exists. Per-unit
coverage/probe ledgers and exact primary-reference locations/access dates
are retained below. Raw snapshots, complete run inventories and independent
reports are in the linked BB storage records; their source hashes identify
the exact reviewed material. Structural validators do not certify grammar.

### Findings and closure

| Finding | Original observed problem | Final disposition |
| --- | --- | --- |
| IT F1 | Any modified family noun was said to retain its possessive article | CLOSED: bounded diminutive/prenominal rule plus postposed-modifier variation; independently matched against Messina DICO |
| IT F2 | Taught Italian mentions remained in plain English runs | CLOSED: explicit target runs; full correction retest plus final 22-container markup-only boundary |
| IT F3 | English subject was said to control an Italian ending | CLOSED: Italian grammatical subject; related subject/piacere forms rechecked |
| FR R1 | Repeated French fragments lacked explicit target markup in rule/notice/lead prose | CLOSED: complete markup retest, including English-on regression and residual trouver lemma |
| FR R2 | Awkward English tell-command gloss | CLOSED: natural English tell-command gloss, unchanged French forms |
| FR R3 | Two Annex D page locators and Required typo | CLOSED: independently reopened printed p.51 / PDF p.53 and confirmed unchanged scope |

Historical FAIL entries in the initial ledgers below remain evidence of the
found defects; they do not override the dated correction retests. Existing
DE/EN Baseline findings C-03/D-02 are outside this new-language acceptance
and remain open; eight b→i audience-hint adaptations do not alter their grammar.

### Italian full-inspection evidence (initial snapshot; retests close findings below)

#### Per-unit coverage and ordinary/counterexample probes

These are **desk review probes**, applied to the actual authored forms and stated rules; they are not browser runs or learner-testing results. The “boundary probe” deliberately tests a shortcut/overgeneralization or the productive/recognition limit. “Matches” means the inspected rule/form/gloss supports the expected ordinary judgement and admits/blocks the boundary case appropriately. F2 markup findings cut across otherwise linguistically correct units. Each listed card’s complete block range and dialog’s complete block range were inspected, not only the probe example.

| ID | Actual card; owned dialog and inspected ranges | Ordinary probe / expected judgement | Boundary probe / expected judgement | Observed |
| --- | --- | --- | --- | --- |
| IT-01 | `#nouns-gender` C0–5; `D:gender` D0–2 | la notte is feminine; lunga agrees | la mano / il problema defeat an ending-only gender rule | matches |
| IT-02 | `#articles-definite` C0–5; `D:definite` D0–2 | lo studente; gli studenti; il bravo studente | the intervening adjective changes the next-sound choice | matches |
| IT-03 | `#articles-indefinite` C0–5; `D:indefinite` D0–2 | un amico versus un’amica | *un’amico is not the masculine learner form | matches |
| IT-04 | `#determiners-possessives` C0–5; `D:possessives` D0–3 | la sua macchina agrees with the car, not its owner | mio fratello maggiore/gemello can omit the article despite a modifier | FAIL F1; card core correct, dialog overgeneralizes |
| IT-05 | `#determiners-demonstratives` C0–5; `D:demonstratives` D0–2 | quei libri, but quelli standalone | *quei sono vecchi is not the independent pronoun pattern | matches |
| IT-06 | `#adjectives-agreement` C0–5; `D:agreement` D0–2 | le chiavi sono piccole; interessante → interessanti | rosa remains unchanged in maglie rosa | matches |
| IT-07 | `#adjectives-comparison` C0–5; `D:comparison` D0–3 | più alto di me; più facile leggere che scrivere | altissimo is very tall, not necessarily tallest | matches |
| IT-08 | `#determiners-indefinites` C0–5; `D:indefinites` D0–3 | qualche libro; ogni mese; molta acqua | molto belle uses invariant degree adverb, not molte | matches |
| IT-09 | `#present-present` C0–5; `D:present` D0–2 | parlo/parli/parla/parliamo/parlate/parlano; finisco/finiamo | not every -ire verb takes -isc; dormo/dormiamo | matches |
| IT-10 | `#basics-subjects` C0–5; `D:subjects` D0–3 | Parlo inglese omits a recoverable subject; Lei parla | pronto/pronta follows the actual addressee; Piove needs no dummy it | matches |
| IT-11 | `#patterns-reflexives` C0–5; `D:reflexives` D0–3 | mi alzo; ci siamo incontrati; Anna si è alzata | chiamarsi is not usefully glossed literally as call oneself | matches |
| IT-12 | `#patterns-modals` C0–5; `D:modals` D0–2 | devo partire; non posso venire; lo voglio vedere/voglio vederlo | English to does not insert a/di; duplicate clitic is rejected | matches |
| IT-13 | `#patterns-piacere` C0–5; `D:piacere` D0–2 | mi piacciono questi libri; mi piace leggere | English I is not the grammatical subject controlling piace/piacciono | matches |
| IT-14 | `#past-compound-past` C0–5; `D:compound-past` D0–3 | ho parlato; siamo partiti; ho visto/scritto/preso | a bounded ten-year stay can use compound past despite its length | matches |
| IT-15 | `#past-imperfect` C0–5; `D:imperfect` D0–4 | parlavo/credevo/dormivo; ero/avevo; background pioveva | imperfect is not selected simply because an action lasted a long time | matches |
| IT-16 | `#past-past-choice` C0–5; `D:past-choice` D0–4 | ho chiamato tre volte versus chiamavo ogni sera | bounded repeated/long events need not be imperfect; potevo does not assert realization | matches |
| IT-17 | `#future-future` C0–5; `D:future` D0–3 | parlerò and future endings/stems; Sarà a casa = probably | Se verrà, parleremo permits future; time distance alone is insufficient | matches |
| IT-18 | `#requests-conditional` C0–5; `D:conditional` D0–3 | vorrei; potresti; dovresti; parlerei with six endings | English habitual would is outside the claimed conditional use | matches |
| IT-19 | `#requests-imperative` C0–5; `D:imperative` D0–3 | parla/parlate; non parlare/non parlate; dammi/dimmi | non farlo and non lo fare both allowed; digli has no doubled gli | matches |
| IT-20 | `#mood-present-subjunctive` C0–5; `D:present-subjunctive` D0–6 | spero che tu stia bene; full regular and essere/avere paradigms | So che è utile uses indicative; same-subject penso di partire; informal variation labeled | matches |
| IT-21 | `#basics-questions` C0–5; `D:questions` D0–3 | Quanti libri hai? Quale/Quali; Chi viene? | no English do-support or compulsory inversion; quale has no gender change | matches |
| IT-22 | `#pronouns-direct` C0–5; `D:direct` D0–3 | Le chiavi? Le cerco; voglio vederlo; la lettera l’ho letta | aspettare has a direct object despite English wait for | matches |
| IT-23 | `#pronouns-indirect` C0–5; `D:indirect` D0–3 | telefono a Luca → gli telefono; le scrivo | le vedo is direct feminine plural, not the recipient le | matches |
| IT-24 | `#particles-ci` C0–5; `D:ci` D0–3 | Roma? Ci vado; progetto? Ci tengo; provo a farlo → ci provo | personal ci means us; parlare del problema takes ne, not ci | matches |
| IT-25 | `#particles-ne` C0–5; `D:ne` D0–3 | ne voglio due; non ne ho nessuno; ne parlo | partitive ne ho comprate due agrees; topic ne ho parlato does not; né is different | matches |
| IT-26 | `#prepositions-simple` C0–5; `D:simple-prepositions` D0–3 | vado a Roma / in Italia / da Anna; con Luca | di/a selected by governing pattern, not a fixed English translation | matches |
| IT-27 | `#time-place-time-place` C0–5; `D:time-place` D0–3 | vivo qui da due anni = still continuing; tra due giorni | ho studiato per un’ora is bounded; due ore fa means ago, not duration | matches |
| IT-28 | `#clauses-relatives` C0–5; `D:relatives` D0–3 | il libro che leggo; la persona con cui parlo | cannot omit object che or strand a preposition; il quale stays recognition only | matches |
| IT-29 | `#clauses-connectors` C0–5; `D:connectors` D0–3 | piove, quindi resto versus resto perché piove | infatti supports the previous claim rather than reversing cause/consequence | matches |
| IT-30 | `#basics-impersonal-si` C0–5; `D:impersonal-si` D0–3 | si dorme/si mangia bene; si vende una casa/si vendono case | ci si lava avoids si si; singular is not extended to passive plural | matches |
| IT-31 | `#nouns-plural` C0–5; `D:plural` D0–2 | libro/libri; casa/case; problema/problemi; notte/notti | città/film invariant, uovo/uova switches gender; -co plural is not automatic | matches |
| IT-32 | `#articles-partitive` C0–5; `D:partitive` D0–2 | del pane; degli amici; delle mele | il colore del vino is relational di+article; bare pane and quantity di are alternatives | matches |
| IT-33 | `#present-irregulars` C0–5; `D:irregulars` D0–7 | all six forms for essere/avere and eight other irregulars checked | io form does not predict all persons; sapere skill/fact versus conoscere familiarity | forms match; minor wording F3 |
| IT-34 | `#past-auxiliary` C0–5; `D:auxiliary` D0–3 | ho camminato; sono partita; ho finito/è finito | ho dovuto partire allowed; mi sono dovuta alzare versus ho dovuto alzarmi; ho voluto essere | matches |
| IT-35 | `#past-participle-agreement` C0–5; `D:participle-agreement` D0–3 | le ho trovate; gliele ho date; ne ho comprate tre | mi/ti allow variation; topic ne and indirect gli do not trigger object agreement | matches |
| IT-36 | `#requests-formal-command` C0–5; `D:formal-command` D0–3 | Mi dica! Entri! Non entri! Sia/abbia/faccia/vada | formal clitic before verb contrasts with informal Dimmi; noi invitation bounded | matches |
| IT-37 | `#aspect-progressive` C0–5; `D:progressive` D0–3 | sto leggendo; stavo cucinando; facendo/dicendo/bevendo | Lavoro ogni giorno is habitual; Mi piace leggere uses infinitive, not gerund | matches |
| IT-38 | `#aspect-about-to` C0–5; `D:about-to` D0–2 | sto per uscire versus sto uscendo | stavoper does not assert realization; next-year plan is not automatically imminent | matches |
| IT-39 | `#past-pluperfect` C0–5; `D:pluperfect` D0–2 | era già partito before arrival; eravamo partite | ieri ho letto e poi ho dormito need not introduce a pluperfect | matches |
| IT-40 | `#pronouns-combined` C0–5; `D:combined` D0–3 | gli/le → glie-; glielo/gliele; me lo/te lo; me ne | recipient gender does not select lo/la; gliel’ho data follows lettera; combinations stay together | matches |
| IT-41 | `#adverbs-mente` C0–5; `D:mente` D0–2 | lenta → lentamente; felice → felicemente; facile → facilmente | -le/-re e loss is qualified often; bene/male are not forced into -mente | matches |
| IT-42 | `#adverbs-adverb-use` C0–5; `D:adverb-use` D0–3 | ho già mangiato; non ho mai visto; vado spesso lì | Sei mai stato? means ever; bene versus buono, molte case versus molto belle | matches |
| IT-43 | `#numbers-numbers-dates` C0–5; `D:numbers-dates` D0–4 | 1–20; 30–90/100/1000; ventuno/ventotto/ventitré; first ten ordinals | ventitreesimo; uno/una before nouns; l’una singular versus le due plural; date primo | matches |
| IT-44 | `#adjectives-position` C0–5; `D:position` D0–2 | vecchio amico versus amico vecchio; film italiano | position can change meaning; relation adjectives normally remain postnominal | matches |
| IT-45 | `#basics-negation` C0–5; `D:negation` D0–3 | non lo capisco; nessuno viene/non viene nessuno | mai in a question can mean ever without non; negative concord is allowed | matches |
| IT-46 | `#basics-exclamations` C0–5; `D:exclamations` D0–2 | Che bella casa! Quanti libri! Quanta gente! | *Che un bel libro is not the taught pattern; question versus reaction needs context | matches |
| IT-47 | `#prepositions-contracted` C0–6; `D:contracted` D0–3 | all 35 di/a/da/in/su contractions checked against seven articles | con il/col and coi; per/tra/fra do not normally fuse; del has two functions | matches |
| IT-48 | `#clauses-subordinates` C0–5; `D:subordinates` D0–3 | So che Anna parte; penso di partire; prima di uscire | causal perché sono stanco contrasts with purpose perché tu capisca; future after quando allowed | matches |
| IT-49 | `#infinitives-verb-infinitive` C0–5; `D:verb-infinitive` D0–3 | voglio partire; comincio a; cerco/finisco di; imparo/continuo a | same-subject spero di arrivare versus different-subject spero che Anna arrivi | matches |
| IT-50 | `#clauses-real-conditions` C0–5; `D:real-conditions` D0–2 | se piove, resto/resterò; se pioverà, resterò; command consequence | open-condition indicative is not expanded to unreal or past-counterfactual systems | matches |
| IT-51 | `#mood-present-subjunctive`; `D:present-subjunctive` D6 | penso che sia partito; credo che abbia finito = prior completed event | recognition note does not promise full production or backshift; agreement pointer retained | matches at R depth |
| IT-52 | `#past-past-choice`; `D:past-choice` D4 | fu/disse/andò/fece linked to essere/dire/andare/fare and glossed | not exclusively literary or automatically selected by number of years ago | matches at R depth |
| IT-53 | `#adjectives-bello` C0–5; `D:bello` D0–2 | bel libro/bei libri; bello spettacolo/begli; bell’albero | libri belli/i libri sono belli; feminine plural belle does not become begli | matches |

Help `D:lookup-help` D0–D3: checked four-view routing, English meaning explanation, selective level statement, recognition boundaries, and search/dialog instructions against the actual deck. Text is consistent; runtime search/open/clear behavior remains NOT RUN.

Additional complete paradigm checks: all present forms for regular three conjugations plus -isc, essere/avere/andare/fare/venire/dare/stare/bere/dire/sapere and potere/dovere/volere; regular imperfect plus essere/avere and fac-/dic-/bev- models; full future/conditional endings and all listed irregular stems; tu/voi command forms and named Lei forms; all regular present-subjunctive person sets and essere/avere, listed singular irregulars; all 35 articulated-preposition cells; possessive/demonstrative/bello and adjective gender/number forms; all number/ordinal examples. No wrong paradigm member found.

#### Independently inspected primary references

All accessed **2026-10-23**. HTML section names locate the evidence; PDF pages are printed / one-based PDF pages. The source register is a claim source, not a substitute for these live reads. Text was inspected; no videos or web UI were operated. Failed/irrelevant search hits were not used. Northwestern’s imperative chapter appeared in search excerpts but full retrieval returned HTTP 403; it is not relied on for the verdict. Treccani’s explicit hortative-clitic paragraph supplies the verified evidence.

| Reference | Exact link and inspected location | Review use |
| --- | --- | --- |
| Università per Stranieri di Siena, *Linee guida CILS*, retrieved publisher version; no unsupported edition date asserted | [PDF](https://cils.unistrasi.it/public/articoli/12/linee_guida_cils_pdf%282%29.pdf), §2.1.1 pp.22–23, §2.1.2 p.26, §2.2 p.29; comparison §2.4 p.32, §2.5 p.36 | Baseline, R/P distinction, cumulative levels and later-placement comparison. This is general CILS, not a B1 cittadinanza promise. |
| Urbino CLA, Federica Rusciadelli, *ITALIANO B1*, 2026/Isem | [PDF](https://cla.uniurb.it/documenti/schede_corsi_cla/2026/Isem/Italiano_B1_Rusciadelli.pdf), p.1 “Descrizione del corso” / “Elementi grammaticali”; p.2 category headings | B1 supplement evidence and explicit boundaries; no claim about the unseen textbook lessons. |
| Rai Scuola, *Le parole dell’Italiano: tutto sul congiuntivo* | [Lesson](https://www.raiscuola.rai.it/italianoperstranieri/articoli/2021/06/Le-parole-dellItaliano-tutto-sul-congiuntivo-2c3e95f5-3fa7-48a6-b4dc-a6ffe1de2896.html), “Unità 10 – Livello B1”, paradigms and last register paragraphs | Independent B1 present-subjunctive evidence. Video playback NOT RUN. |
| Fabio Ruggiano, DICO / University of Messina, *“Mio fratello” o “il mio fratello”?*, 2025-09-23 | [Answer 1](https://dico.unime.it/ufaq/mio-fratello-o-il-mio-fratello/) | F1, postposed comparative modifier and article choices. |
| Fabio Rossi, DICO / University of Messina, *Articolo con nomi di parentela*, 2025-12-30 | [Archive section with full answer](https://portale2.unime.it/dico/tutte-le-domande-2/?include_tag=articolo), named question/answer paragraphs 2–5 | F1, separates obligatory article environments from optional postposed modifiers. |
| Treccani, *La grammatica italiana* (2012), *Possessivi, aggettivi e pronomi* | [Article](https://www.treccani.it/enciclopedia/aggettivi-e-pronomi-possessivi_%28La-grammatica-italiana%29/), endings, pronouns, “Usi” | Noun-controlled agreement, loro, family-noun examples; does not warrant the deck’s universal F1 inference. |
| Treccani, *La grammatica italiana* (2012), *Articoli*; *Vocabolario*, *articolo* | [Grammar](https://www.treccani.it/enciclopedia/articoli_%28La-grammatica-italiana%29/), definite/indefinite discussion; [dictionary](https://www.treccani.it/vocabolario/articolo/), sense 1 | Reference/indefiniteness/partitive distinctions. Parsed grammar tables were not available as text; next reference supplies detailed allomorph evidence. |
| Treccani, *Enciclopedia dell’Italiano* (2010), *Articolo* | [Article](https://www.treccani.it/enciclopedia/articolo_%28Enciclopedia-dell%27Italiano%29/), “Proprietà e tipi”, “Articolo determinativo”, singular/plural | Independent next-word sound and article-form corroboration. |
| Riccardo Cimaglia, *Ausiliari, verbi*, Treccani E.d.I. (2010) | [Article](https://www.treccani.it/enciclopedia/verbi-ausiliari_%28Enciclopedia-dell%27Italiano%29/), “Distribuzione nell’uso degli ausiliari propriamente detti”, especially modal/pronominal paragraphs | Movement shortcut, dual auxiliaries, accepted modal avere alternative and reflexive-clitic placement. |
| Mario Squartini, *Indicativo*, Treccani E.d.I. (2010) | [Article](https://www.treccani.it/enciclopedia/indicativo_%28Enciclopedia-dell%27Italiano%29/), “Natura e caratteristiche funzionali”, “Funzioni temporali”, “Funzioni aspettuali” | Perfective/imperfective viewpoint, counted/long repeated events, prior time and fact versus mood. |
| Mario Squartini, *Presente*, Treccani E.d.I. (2011) | [Article](https://www.treccani.it/enciclopedia/presente_%28Enciclopedia-dell%27Italiano%29/), “Nozione”, contemporaneity/progressive discussion | Simple present can express current action or plans, present + continuing duration. |
| Elisa De Roberto, *Futuro*, Treccani E.d.I. (2010) | [Article](https://www.treccani.it/enciclopedia/futuro_%28Enciclopedia-dell%27Italiano%29/), “Definizione”, morphology and modal uses | Future formation and non-distance-based meaning. |
| Treccani, *È corretto dire: “se pioverà, la manifestazione si terrà…”*, 2012-11-29 | [Answer](https://www.treccani.it/magazine/lingua_italiana/domande_e_risposte/grammatica/grammatica_353.html), opening answer | Direct corroboration that future after se is possible. The answer swaps protasis/apodosis labels in its parentheticals; the review uses only its unambiguous accepted example, not that labeling error. |
| Treccani, *La grammatica italiana* (2012), *Periodo ipotetico* | [Article](https://www.treccani.it/enciclopedia/periodo-ipotetico_%28La-grammatica-italiana%29/), reality/possibility/irreality paragraphs | Open indicative versus deferred unreal systems; imperative consequence. |
| Angela Frati, Crusca, *Glielo potremmo spiegare così!*, 2013-01-11 | [Answer](https://accademiadellacrusca.it/it/consulenza/glielo-potremmo-spiegare-cosi/757), tonic/atonic forms, fusion/elision and final female-recipient paragraphs | glie- for gli/le, joined spelling, optional gliel’ho elision, contemporary plural gli. |
| Stefano Telve, *Accordo [prontuario]*, Treccani E.d.I. (2011) | [Article](https://www.treccani.it/enciclopedia/accordo-prontuario_%28Enciclopedia-dell%27Italiano%29/), participle discussion, examples 12–14 | Object-partitive ne agreement in the ordinary quantified pattern. |
| Crusca, *Accordo del participio passato*, 2002-09-30, quoting Luca Serianni, *La Crusca per voi* 8 (1994), p.7 | [Answer](https://accademiadellacrusca.it/it/consulenza/accordo-del-participio-passato/23), numbered cases and variation paragraph | Why preceding objects/first-second-person clitics cannot be collapsed into a universal agreement rule. |
| Fabio Rossi, DICO, *Ancora sull’accordo del participio passato*, 2024-11-03 | [Answer](https://dico.unime.it/ufaq/ancora-sullaccordo-del-participio-passato/), response | Third-person direct-clitic agreement versus optional first/second-person agreement. |
| Treccani, *La grammatica italiana* (2012), *Imperativo* | [Article](https://www.treccani.it/enciclopedia/imperativo_%28La-grammatica-italiana%29/), missing persons, “Dubbi”, “Usi” | tu/voi, negative infinitive, short-command spelling and negative-clitic alternatives. |
| Treccani E.d.I. (2010), *Imperativo* | [Article](https://www.treccani.it/enciclopedia/imperativo_%28Enciclopedia-dell%27Italiano%29/), “Clitici con l’imperativo” | Explicit proclisis with hortative subjunctive; contrasts the informal attachment pattern. |
| Treccani, *La grammatica italiana* (2012), *Congiuntivo* | [Article](https://www.treccani.it/enciclopedia/congiuntivo_%28La-grammatica-italiana%29/), tense definition, subordinate/independent uses | Construction/register-dependent selection, four-tense system versus bounded accepted production. |
| Treccani, *La grammatica italiana* (2012), *Ci* / *Ne o né?* | [Ci](https://www.treccani.it/enciclopedia/ci_%28La-grammatica-italiana%29/), personal/locative/complement functions; [Ne](https://www.treccani.it/enciclopedia/ne-o-ne_%28La-grammatica-italiana%29/), pronoun/partitive versus conjunction | English-word substitution traps and explicit idiom boundary. |
| VIVIT, Crusca/MICC, *Il “si” impersonale* / *Il “si” passivante* | [Impersonal](https://viv-it.org/schede/si-impersonale), “Sintassi”; [Passive](https://www.viv-it.org/schede/si-passivante), “Sintassi” | Distinct impersonal versus passive agreement. |
| Treccani, *La grammatica italiana* (2012), *Relativi, pronomi* | [Article](https://www.treccani.it/enciclopedia/pronomi-relativi_%28La-grammatica-italiana%29/), che/cui/il quale and “Usi” | Subject/object che, prepositional cui, agreeing compound forms and place dove. |
| Eva Wiberg, *Passato remoto*, Treccani E.d.I. (2011) | [Article](https://www.treccani.it/enciclopedia/passato-remoto_%28Enciclopedia-dell%27Italiano%29/), eventive use and “Differenze regionali” | Recognition boundaries; contemporary regional/narrative use, no “only literary” claim. |

### Italian independent correction retest

#### Independent Italian review — correction verification, 2026-10-23

Reviewer: French author / independent Italian reviewer, BB thread `thr_4bsuy4n7xv`. VERIFY ONLY. No repository files edited; no browsers, servers, commits or pushes. This record supersedes the original snapshot’s FAIL verdict after inspecting the complete correction boundary. It carries forward the fully inspected, unchanged units from [the original full review](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/review.md), preserving its findings, 53-row content mapping, primary sources/access dates, counts and probes.

| Gate | Current verdict | Basis |
| --- | --- | --- |
| Baseline | **PASS** | Original complete 36-row CILS / 31-row Urbino comparison carried forward. The only plan change bounds IT-04’s modifier exception and adds the corroborating source; all 53 Required units, 8 deferrals and 6 exclusions remain. |
| Coverage | **PASS** | All 53 units remain: 51 cards plus IT-51/52 hosted recognition blocks; 52 dialogs, 201 blocks, 180 form rows. No location, depth or required content was removed. |
| Accuracy | **PASS** | All unchanged units retain the full original inspection; the complete semantic delta and related possessive/subject/piacere/agreement surfaces were rechecked. F1 is corrected and source-backed; no unresolved wrong form/rule/gloss found. |
| Teaching | **PASS** | F1 now states the boundary; all F2 listed plain-run omissions were corrected with explicit Italian markup and unchanged meanings; F3 now identifies the Italian grammatical subject. Card/dialog consistency rechecked. |
| Runtime, browser/visual/a11y execution, install/offline/live deployment | **NOT RUN** | Parent owns these. Static render/metadata checks are separate and do not claim runtime acceptance. |

Content is ready for parent integration/content acceptance at the exact snapshot below. This is an independent content verdict, not release or runtime acceptance.

#### Exact reviewed revision

Git HEAD is `05eed47bf715288739f35ef63d8859a1f72758b0`; the authored files remain dirty/untracked. [correction-revision.json](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/correction-revision.json) preserves the exact current dirty paths; [snapshot.json](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/snapshot.json) preserves the original dirty inventory. The originally reported `72919df604278dcb94af2f2657b35e64543143555b85050c423868f71e73d1fd` was confirmed and fully reviewed, then this correction snapshot was independently inspected. Frozen corrected copies are under `correction-snapshot/`.

| File | Corrected SHA256 |
| --- | --- |
| `it/en/SITE_PLAN.md` | `1c3a074bafef5ca48ff69d1a02a19a3ba5b88ca3d03ad59600585de18f43fc5f` |
| `content/decks/it-en.json` | `45053264210015f9d4264162b30864bcb1d72ed0ec098a255293850804d4afdc` |
| `it/en/index.html` | `62969501ec197f1b847b4cd394f0861109311ba9f3854f23fc08acb30d24f7e6` |
| `research/it-en-plan.md` | `eca5370d9678be49e95d5850b1616ae835dd7ceda367c0ac28e012719e947717` |

#### Inspected change boundary and carry-forward rule

Compared **every difference** between original and corrected Italian deck JSON, including markup wrappers, with rich-run normalization used only to expose semantic differences. The semantic diff has exactly five leaves: the IT-04 source note; IT-33 subject explanation; the possessives dialog’s label, Italian example and English comment. [correction-semantic-diff.json](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/correction-semantic-diff.json) records each old/new value. No unseen rewrite or unknown boundary is being carried forward.

All other deck text, paradigms, examples, glosses, inventories and scope are unchanged. The complete initial inspection therefore carries forward from the named `72919df…` snapshot under CONTENT_VALIDATION §5. The actual markup delta was also inspected independently: **46 rich-run containers gained 76 marked Italian subspans; zero previously marked positions were lost**. These resolve the 49 original plain-run findings (multiple plain runs can share a single container), and include the additional related number/relative-form mentions. [correction-markup-diff.json](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/correction-markup-diff.json) records every added marked span. No newly bold English explanatory span was found. New possessives text has its own explicit Italian markup and meaning support.

Plan diff: one IT-04 depth/boundary cell changes; accepted scope does not expand. Research diff: one G31 source-register row added, consistent with the already independently inspected DICO evidence. The generated page was regenerated from this exact corrected deck; deterministic byte equality plus static payload inspection confirms the changed content reaches the page.

Related surfaces re-read: complete IT-04 card and all four possessives blocks, IT-33 card and all eight irregular dialogs, IT-10 subject/address forms and all four subject blocks, IT-13 liked-item agreement and its three dialog blocks, adjective agreement, the six changed card glosses, and every changed dialog comment. Hosted IT-51/52 boundaries and full unit counts were rechecked unchanged.

#### Findings retest

| Finding | Ordinary/counterexample probe, expected result | Observed corrected result | Status |
| --- | --- | --- | --- |
| F1 family article | `mia sorella` omits; `le mie sorelle` / `il loro padre` retain; diminutive `la mia sorellina` and prenominal `la mia cara sorella` retain | All modeled and glossed correctly. | **CLOSED — PASS** |
| F1 modifier boundary | `mio fratello maggiore` / `mio fratello gemello` are valid without article; `il mio fratello gemello` also possible; `la mia cugina preferita` requires article in this ordinary noun phrase | New comment explicitly allows variation, gives each English meaning, and avoids the former any-modifier rule. Independently matches DICO’s named answers. | **CLOSED — PASS** |
| F2 target markup | Original listed Italian mentions must be explicit bold/hit subspans; English meanings stay readable and unchanged | All 49 reported plain-run instances resolved by the inspected 46-container/76-span delta, plus correctly marked new family examples. No lost marked content. | **CLOSED — PASS** |
| F3 subject controller | Ordinary irregular forms still agree with the Italian grammatical subject; `mi piacciono i libri` must not be controlled by English “I” | New line says Italian grammatical subject, including omitted pronouns. Related subjects/piacere rules remain correct and consistent. | **CLOSED — PASS** |

Sources for F1 retest (accessed 2026-10-23): Fabio Rossi, DICO/Università di Messina, *Articolo con nomi di parentela*, 2025-12-30, [named full-answer section](https://portale2.unime.it/dico/tutte-le-domande-2/?include_tag=articolo); Fabio Ruggiano, *“Mio fratello” o “il mio fratello”?*, 2025-09-23, [answer 1](https://dico.unime.it/ufaq/mio-fratello-o-il-mio-fratello/). The original review records all other primary corroboration, exact titles/sections/pages, ordinary/counterexample probes and full unit locations.

#### Corrected snapshot checks

- `python3 tools/build_pages.py content/decks/it-en.json --check`: **exit 0**.
- `deck_validate.validate` with current canonical registry: **zero errors**; `deck_render.render` equals generated page byte for byte.
- Static page: all 51 card anchors present, **no duplicate HTML IDs**, **52 DETAILS entries / 201 rendered blocks**.
- All **14 local document links and 5 linked heading fragments** resolve. All four corrected files have final newlines and no trailing whitespace.
- All four live file hashes still matched the frozen correction snapshot at the final check. Exact results: [correction-checks.json](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/correction-checks.json).
- Runtime gates remain **NOT RUN**. No repository changes were made by this review.

#### Shared integration recheck — 2026-10-23

After the parent’s registry/template integration message, all four Italian artifacts were hashed again. JSON, plan, research and generated HTML still exactly match this reviewed correction snapshot. Canonical validation again reports zero errors, and current shared rendering equals the generated HTML byte for byte. No new content or template-only difference exists at this recheck. Evidence: [integration-recheck.json](/Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/integration-recheck.json). The four content PASS verdicts carry forward unchanged; runtime remains NOT RUN by this reviewer.


### French full-inspection evidence (initial snapshot; retests close findings below)

#### Primary sources independently inspected

All following access dates: **2026-10-23**. UT HTML pages have no displayed edition/page numbers; their named sections are the locators. Sources establish the rules, while the examples/gloss judgments below concern the authored deck. The Eaquals reference establishes the selected baseline comparison, not an obligatory curriculum or certification.

| Ref | Exact title/link and inspected section(s) |
| --- | --- |
| E1 | Eaquals/CIEP/Eurocentres/ACPLS, *Inventaire linguistique des contenus clés des niveaux du CECRL* (2015), [publisher PDF](https://www.eaquals.org/wp-content/uploads/Inventaire_ONLINE_full-1.pdf): Annex E grammar, printed 56 (A1), 57–58 (A2), 59 (B1), 60 (B2 comparison); PDF 58–62 one-based. Annex D printed 51–52 / PDF 53–54 supplements. Full downloaded PDF retained as `eaquals-inventaire.pdf`; extracted columns checked. |
| U01 | UT Austin, Tex's French Grammar, [Number: singular, plural](https://www.laits.utexas.edu/tex/gr/no2.html): regular, unchanged endings, exceptional plurals. The deck appropriately avoids this source's overly broad -ail/-ou shortcuts. |
| U02 | [Gender: masculine, feminine](https://www.laits.utexas.edu/tex/gr/no3.html): people, animals, objects/ideas and ending tendencies. |
| U03 | [Determiners: definite articles](https://www.laits.utexas.edu/tex/gr/det2.html): forms, elision, generic reference and preference verbs. |
| U04 | [Determiners: indefinite articles](https://www.laits.utexas.edu/tex/gr/det4.html): forms, negative exceptions, plural adjective, profession. |
| U05 | [Determiners: partitive articles](https://www.laits.utexas.edu/tex/gr/det5.html): forms, uses and negative/contrast. |
| U06 | [Adjectives whose meaning varies with placement](https://www.laits.utexas.edu/tex/gr/adj5.html): placement contrasts. |
| U07 | [Adverbs: formation and placement](https://www.laits.utexas.edu/tex/gr/adv2.html): regular/exceptional formation, simple-verb and sentence placement. |
| U08 | [Passé composé with avoir](https://www.laits.utexas.edu/tex/gr/tap2.html): formation, irregular participles, negation. |
| U09 | [Passé composé with être](https://www.laits.utexas.edu/tex/gr/tap3.html): auxiliary selection, transitivity and agreement. |
| U10 | [Passé composé of pronominal verbs](https://www.laits.utexas.edu/tex/gr/tap4.html): agreement, following direct object, indirect reflexive/reciprocal. |
| U11 | [Narration: passé composé vs. imparfait](https://www.laits.utexas.edu/tex/gr/tap8.html): viewpoint, state/change and final context caveat. |
| U12 | [Plus-que-parfait](https://www.laits.utexas.edu/tex/gr/tap9.html): formation, prior past, duration/recent-past contrasts. |
| U13 | [Futur proche](https://www.laits.utexas.edu/tex/gr/taf1.html): formation/uses. |
| U14 | [Simple future: regular](https://www.laits.utexas.edu/tex/gr/taf2.html): formation/uses. |
| U15 | [Simple future: irregular](https://www.laits.utexas.edu/tex/gr/taf3.html): common stems and spelling changes. |
| U16 | [Future: usage](https://www.laits.utexas.edu/tex/gr/taf4.html): near/simple contrast, non-immediate examples, French/English conjunctions. |
| U17 | [Conditional](https://www.laits.utexas.edu/tex/gr/tac1.html): formation, irregulars, requests/advice and English habitual would contrast. |
| U18 | [Imperative mood](https://www.laits.utexas.edu/tex/gr/tai1.html): regular/irregular forms, y/en, reflexive/negative/positive pronouns. |
| U19 | [Regular subjunctive](https://www.laits.utexas.edu/tex/gr/tas1.html): endings and stem changes. The deck avoids an unlimited third-plural shortcut. |
| U20 | [Irregular subjunctive](https://www.laits.utexas.edu/tex/gr/tas2.html): two stems, être/avoir, faire/savoir/pouvoir. |
| U21 | [Subjunctive usage: obligation](https://www.laits.utexas.edu/tex/gr/tas3a.html): necessity and finite clauses. |
| U22 | [Subjunctive usage: will, emotion, desire](https://www.laits.utexas.edu/tex/gr/tas4.html): emotion, affirmative espérer and infinitive alternatives. Its broad hypothesis description is not adopted as an absolute. |
| U23 | [Conjunctions that take the subjunctive](https://www.laits.utexas.edu/tex/gr/tas5.html): purpose, concession and same-subject conjunction exception. |
| U24 | [Direct object pronouns](https://www.laits.utexas.edu/tex/gr/pro5.html): forms, placement and preceding-object agreement. |
| U25 | [Pronoun y](https://www.laits.utexas.edu/tex/gr/pro6.html): location/governed complements, people boundary and position. |
| U26 | [Pronoun en](https://www.laits.utexas.edu/tex/gr/pro7.html): quantity, retained measure, de-complements, placement. Its claim that en is never a direct object is not adopted; A02 below supplies the more precise agreement authority. |
| U27 | [Order of object pronouns present tense](https://www.laits.utexas.edu/tex/gr/pro9.html): regular order, positive commands, y/en and negation. |
| U28 | [Relative pronouns: qui and que](https://www.laits.utexas.edu/tex/gr/pror1.html): syntactic roles and agreement. |
| U29 | [Relative pronouns: ce qui, ce que](https://www.laits.utexas.edu/tex/gr/pror2.html): absent antecedent, whole idea and emphasis. |
| U30 | [Relative pronouns: dont, où, etc.](https://www.laits.utexas.edu/tex/gr/pror3.html): simple de versus compound preposition, lequel and no-antecedent relatives. |
| U31 | [Si clauses](https://www.laits.utexas.edu/tex/gr/tac3.html): present/imperfect patterns and distinction from reported questions. Its “impossible” description is appropriately softened in the deck. |
| U32 | [Reported speech in the present](https://www.laits.utexas.edu/tex/gr/tad1.html): statements, questions, orders and retained ordinary word order. |
| U33 | [Active vs. passive voice](https://www.laits.utexas.edu/tex/gr/tav1.html): formation/agreement, agent and active/on alternatives. |
| U34 | [Present participle](https://www.laits.utexas.edu/tex/gr/vpp1.html): formation, three irregulars, gerund/shared actor and English -ing warning. |
| U35 | [Depuis, pendant, pour: for](https://www.laits.utexas.edu/tex/gr/prep1.html): duration contrasts and bounded travel use. |
| U36 | [Basic negation: ne…pas](https://www.laits.utexas.edu/tex/gr/neg2.html): simple/compound placement and conversational omission. |
| U37 | [Alternate forms (1): ne…jamais, rien, personne, etc.](https://www.laits.utexas.edu/tex/gr/neg3.html): negative meanings, subject/object positions and combinations. |
| A01 | Académie française, *Questions de langue*, [Pronominaux (Verbes, accord du participe passé)](https://www.dictionnaire-academie.fr/article/QDL069), numbered cases 1–2: direct/indirect reflexive analysis and ordinary exceptions. |
| A02 | OQLF, Banque de dépannage linguistique, [Accord du participe passé avec le pronom en](https://vitrinelinguistique.oqlf.gouv.qc.ca/index.php?id=21037), invariability and agreement when another direct object precedes. |
| A03 | OQLF, [Verbe pronominal de sens réfléchi](https://vitrinelinguistique.oqlf.gouv.qc.ca/22954/la-grammaire/le-verbe/verbes-pronominaux/verbe-pronominal-de-sens-reflechi), use and agreement sections. |

Failed sources are not represented as read evidence: one guessed OQLF aggregate URL, UT misspellings `tafu1/tafu2` (correct `taf1/taf2` then read), and direct CCDMD conditional PDF fetch (403). A search extract of CCDMD supports the interrogative-si distinction, but this record relies on the inspected deck's clear frame plus U31/U32, not a claimed full CCDMD read. One PDF screenshot request timed out; a second request succeeded, and the downloaded PDF's layout-preserving text was used for the Annex D locators. No source was copied into the product by this review.

#### Ordinary and counterexample probes — observed judgments

These are independent desk-review judgments against actual authored units, not browser tests, learner outcomes or execution of a grammar engine. “Pass” means the inspected card/dialog supplies the right decision and limit. All probes were actually checked against the frozen source. Exact block ranges are in the ledger below.

| Probe | Expected decision / counterexample | Observed in authored content | Judgment |
| --- | --- | --- | --- |
| Gender/plural | Regular -s; avoid treating -e as reliably feminine or all -al/-ou as -aux/-oux | Noun dialog contrasts école/musée and festival/clou/détail with positive models | Pass |
| Article/negative | Likes use generic definite; ordinary negative quantity de, but negative être/contrast can retain article | Article and partitive cards/dialogs include both exceptions and the whole-category contrast | Pass |
| Possessive | Owner does not determine possessed noun gender; vowel next word matters | son/sa plus mon amie vs ma meilleure amie support the distinction; markup fails separately | Pass semantically; R1 |
| Position/comparison | Former versus old, own versus clean; meilleur is not adverb mieux | Adjective-position and comparison units show and gloss the contrasts | Pass |
| Manner | -ent/-ant families have exceptions; compound placement is not fixed for all adverbs | lentement and irregulars plus short/long placement limits present | Pass |
| Modal negative | Prohibition differs from no need | il ne faut pas vs ne pas avoir besoin are explicitly contrasted | Pass |
| Être auxiliary | sortir/monter transitivity can change auxiliary; courir/marcher are not être merely because of movement | Both ordinary and counterexamples appear visibly/in dialog | Pass; U09 |
| Reflexive agreement | Direct reflexive feminine agrees; following hands object and indirect reciprocal do not | All three examples analyzed correctly in reflexives/object-agreement dialogs | Pass; A01/A03 |
| Avoir agreement | Earlier direct pronoun/que can trigger; indirect lui does not; quantitative en normally unchanged | Earlier-object, relative and indirect contrasts present; en limit bounded to quantitative use | Pass; U24/A02 |
| Past viewpoint | Event/background and state/change; repeated or long action need not force imperfect | Contextual story, bounded repetition and duration counterexamples supplied; keyword rule rejected | Pass; U11 |
| Pluperfect | Prior past differs from continuing duration/had just | Imperfect auxiliary model and depuis/venait de counterexamples supplied | Pass; U12 |
| Future | aller + infinitive need not mean immediately; quand future does not follow English present mechanically | Next-year counterexample and future time-clause example included | Pass; U13–16 |
| Conditional | Polite/modal outcomes differ from habitual English would | Requests/advice/hypothesis modeled; habitual would sent to imperfect | Pass; U17 |
| Commands | Positive pronouns after verb, negatives before; tu -s before directly attached y/en | Positive/negative pair and vas-y/parles-en/donne-m'en correctly distinguish frames | Pass; U18/U27 |
| Subjunctive forms | Regular endings plus irregular/two-stem exceptions | Every displayed form checked, including être/avoir, allions/prenions/voulions and faire/pouvoir/savoir | Pass; U19/U20 |
| Subjunctive selection | Obligation/emotion may concern real facts; affirmative espérer/croire differ; same-actor infinitive not universal across conjunctions | Fact/emotion note, indicative contrast, infinitive alternatives and bien que exception supplied; anterior events explicitly outside present-only model | Pass; U21–23 |
| Passive/gerund | Present/compound passive agree with subject; shared actor required for simple gerund | Passive/on and state/action contrast; gerund two-actor counterexample, 3 irregular participles and infinitive alternative present | Pass; U33/U34 |
| Subject/on | Singular finite verb, contextual referent agreement can differ | All three on readings supplied; feminine plural example explicitly framed as known female we | Pass |
| Question/exclamation | Question role matters; formal inversion is not English do-support | Subject/object what, agreement, -t- and all three exclamation frames checked | Pass |
| Negation | Nothing/no one do not simply share compound positioning; negative subject and restrictive only differ | Compound rien/personne and subject patterns, plus ne…que and ni…ni supplied | Pass; U36/U37 |
| Clitic selection | écouter is direct; téléphoner à takes indirect; penser à person needs stressed construction in this bounded lesson | Contrasts prevent an English-to universal test | Pass |
| Y/en | Place versus person/topic; amount remains after en | Place chez-person frame, penser à lui, quantity/measure retention and de-person caveat supplied | Pass; U25/U26 |
| Double objects | Regular order differs from positive-command order; matrix is not free combination permission | Negative/positive, infinitive, compound and y/en examples checked; chosen-combinations limit visible | Pass; U27; R2 wording |
| Relative role | People can be objects and things subjects; dont replaces simple de, not à côté de | Role contrasts, COD agreement, complex-preposition counterexample and recognition label supplied | Pass; U28–30 |
| Si | Present/imperfect condition models; indirect whether can have future; imagined need not mean impossible | All three limits stated and illustrated; past counterfactual clearly deferred | Pass; U31/U32 |
| Duration | Continuing present depuis vs completed pendant vs future interval dans; pour is bounded | Main inventory and dialog retain distinctions, reference past and travel limits | Pass; U35/U12 |
| Reporting | Present reporting does not impose automatic past backshift; reported question uses ordinary order and order uses de-infinitive | Statement/yes-no/wh/order, immediate demain and pronoun reference all modeled; full past system deferred | Pass; U32 |
| Logic links | Aim differs from result; because-clause differs from because-of-noun; cause-source anomaly should not make c'est pourquoi a reason | Correct routed meanings, register clues and noun/clause/infinitive selection present | Pass |
| Concession | Despite+noun vs although+subjunctive, even for factual situations | Bounded distinction and factual/same-actor caveat present | Pass; U23 |
| Latin target fragment | Taught model in rule prose must carry explicit study markup | Possessives notice/present-model paragraph are plain English-voice strings | FAIL; R1 |

#### Complete card/dialog ledger

All listed units are covered at the accepted depth and were inspected in full for Accuracy and Teaching. R1 remains the global Teaching defect described above; this ledger does not silently mark it fixed. `C0–5` means all six card blocks; `D0–n` all dialog blocks. Each inventory row, every form within a paradigm run and each English comment/gloss was read. No table cells or answers exist to omit.

| Topic IDs | Actual stable anchor / dialog | JSON card pointer; full units inspected | Content judgment |
| --- | --- | --- | --- |
| FR-01, FR-02 | `nouns-noun-forms` / `noun-forms` | `/sections/0/cards/0`, C0–5; 4 inventory rows; D0–5 | Gender tendencies/hidden gender, default and irregular/unchanged plurals; exceptional families correctly bounded. |
| FR-03 | `determiners-articles` / `articles` | `/sections/1/cards/0`, C0–5; 3 inventory rows; D0–5 | Specific/new/generic, profession, negative être, plural adjective and h-aspiré boundaries present. R1 prose markup. |
| FR-04 | `determiners-partitives` / `partitives` | `/sections/1/cards/1`, C0–5; 4 inventory rows; D0–4 | Mass/category/serving and contraction distinguished; negative être/explicit contrast retained. |
| FR-05 | `determiners-quantity` / `quantity` | `/sections/1/cards/2`, C0–5; 5 inventory rows; D0–5 | Number versus measure/de, standalone amount, specific set, comparison, distance/discount frames all present. |
| FR-06 | `determiners-possessives` / `possessives` | `/sections/1/cards/3`, C0–5; 5 inventory rows; D0–4 | Possessed-noun agreement and owner ambiguity; immediate-vowel and reflexive body-part contrasts. R1. |
| FR-07 | `determiners-demonstratives` / `demonstratives` | `/sections/1/cards/4`, C0–5; 4 inventory rows; D0–3 | Four determiner forms, vowel/h boundary, noun suffix and replacement-pronoun contrast. |
| FR-11 | `determiners-indefinites` / `indefinites` | `/sections/1/cards/5`, C0–5; 4 inventory rows; D0–4 | Tout agreement, singular chaque and selected determiners; standalone contrast. |
| FR-08 | `adjectives-adjective-forms` / `adjective-forms` | `/sections/2/cards/0`, C0–5; 4 inventory rows; D0–4 | Regular/irregular agreement, vowel masculine alternants, plural/mixed-group caveats. |
| FR-09 | `adjectives-adjective-position` / `adjective-position` | `/sections/2/cards/1`, C0–5; 4 inventory rows; D0–3 | Default/common before-noun frames; meaning-changing ancien/propre/pauvre contrasts. |
| FR-10 | `adjectives-comparison` / `comparison` | `/sections/2/cards/2`, C0–5; 4 inventory rows; D0–4 | Adjective/adverb/noun comparisons, superlative agreement, meilleur/mieux/pire distinguished. |
| FR-46 | `adverbs-degree-frequency` / `degree-frequency` | `/sections/3/cards/0`, C0–5; 4 inventory rows; D0–5 | Degree/amount/frequency with noun/verb/adjective frames and placement; approximate/equal amounts. |
| FR-47 | `adverbs-manner` / `manner` | `/sections/3/cards/1`, C0–5; 5 inventory rows; D0–4 | -ment and -ant/-ent patterns, exceptions, short/long/compound placement bounded. |
| FR-64 | `numbers-dates-time` / `dates-time` | `/sections/4/cards/0`, C0–5; 5 inventory rows; D0–5 | Cardinal/ordinal/date/time grammar, premier, cent/vingt/mille, demie and France variants bounded. |
| FR-14 | `present-present-patterns` / `present-patterns` | `/sections/5/cards/0`, C0–5; 6 inventory rows; D0–4 | All six persons of three regular models, irregular -ir limit, spelling/stem changes. R1 model paragraph/lead. |
| FR-15 | `present-present-irregulars` / `present-irregulars` | `/sections/5/cards/1`, C0–5; 4 inventory rows; D0–4 | All displayed être/avoir/aller/faire forms, venir/prendre and lexical constructions checked. |
| FR-16 | `present-present-meaning` / `present-meaning` | `/sections/5/cards/2`, C0–5; 3 inventory rows; D0–4 | Simple/progressive/recent frames, infinitive position and relative recent past/place contrast. |
| FR-17 | `patterns-reflexives` / `reflexives` | `/sections/6/cards/0`, C0–5; 4 inventory rows; D0–5 | Full pronoun set, elision, negative/infinitive/compound positions and 3 agreement analyses. |
| FR-18 | `patterns-modals-obligation` / `modals-obligation` | `/sections/6/cards/1`, C0–5; 4 inventory rows; D0–4 | All displayed modal forms, infinitive selection, impersonal obligation, prohibition/no need and polite chunks. |
| FR-30 | `patterns-gerund` / `gerund` | `/sections/6/cards/2`, C0–5; 3 inventory rows; D0–5 | Shared actor, formation/spelling/3 irregulars, manner/simultaneity and English infinitive alternative. |
| FR-19 | `past-passe-compose` / `passe-compose` | `/sections/7/cards/0`, C0–5; 4 inventory rows; D0–4 | Regular/irregular participles, auxiliary function, negative placement and contextual English tense meaning. |
| FR-20 | `past-etre-auxiliary` / `etre-auxiliary` | `/sections/7/cards/1`, C0–5; 5 inventory rows; D0–5 | Bounded lexical set, agreement, transitive sortir/monter contrast and avoir-motion counterexamples. |
| FR-21 | `past-imparfait` / `imparfait` | `/sections/7/cards/2`, C0–5; 3 inventory rows; D0–4 | All endings, être exception, orthography and background/habit/duration viewpoint. |
| FR-22 | `past-past-choice` / `past-choice` | `/sections/7/cards/3`, C0–5; 3 inventory rows; D0–4 | Foreground/background, bounded repetition, states/changes and narrative-present recognition; no keyword shortcut. |
| FR-23 | `past-pluperfect` / `pluperfect` | `/sections/7/cards/4`, C0–5; 3 inventory rows; D0–5 | Imperfect auxiliaries/prior past, negative/object agreement; duration/recent-past counterexamples. |
| FR-62 | `past-object-agreement` / `object-agreement` | `/sections/7/cards/5`, C0–5; 4 inventory rows; D0–5 | Earlier COD/que vs indirect, reflexive direct/indirect and quantitative en; exceptional systems deferred. |
| FR-24 | `future-future-reference` / `future-reference` | `/sections/8/cards/0`, C0–5; 4 inventory rows; D0–5 | Near/simple/present choices, regular/all displayed irregular stems, future time clauses and distance caveat. |
| FR-25 | `mood-conditional` / `conditional` | `/sections/9/cards/0`, C0–5; 4 inventory rows; D0–5 | Full model, common stems, request/advice/wish/hypothesis and habitual English would caveat. |
| FR-26 | `mood-imperative` / `imperative` | `/sections/9/cards/1`, C0–5; 4 inventory rows; D0–5 | Tu/nous/vous models, irregulars, hyphens, negative order, directly attached y/en -s and m’en. |
| FR-27 | `mood-subjunctive-forms` / `subjunctive-forms` | `/sections/9/cards/2`, C0–5; 4 inventory rows; D0–5 | Regular model, full être/avoir, two-stem and irregular forms; limited shortcut. |
| FR-28 | `mood-subjunctive-choice` / `subjunctive-choice` | `/sections/9/cards/3`, C0–5; 4 inventory rows; D0–5 | Obligation/emotion/will, indicative belief/hope, facts and actor/infinitive limits; anterior boundary. |
| FR-29 | `voice-passive` / `passive` | `/sections/10/cards/0`, C0–5; 3 inventory rows; D0–5 | Present and compound-past production, future recognition, agreement/agent, on/active and state/action contrast. |
| FR-12 | `subjects-subjects` / `subjects` | `/sections/11/cards/0`, C0–5; 3 inventory rows; D0–5 | Subject forms/tu-vs-vous/on readings; finite singular and contextually female plural agreement. |
| FR-13 | `subjects-stressed` / `stressed` | `/sections/11/cards/1`, C0–5; 3 inventory rows; D0–4 | Complete forms, preposition/emphasis/coordination and complement-selected clitic contrast. |
| FR-31 | `questions-question-patterns` / `question-patterns` | `/sections/12/cards/0`, C0–5; 4 inventory rows; D0–5 | Three registers, inversion/hyphens/-t-, compound auxiliary and noun-subject reprise. |
| FR-32 | `questions-question-words` / `question-words` | `/sections/12/cards/1`, C0–5; 5 inventory rows; D0–5 | Who/what roles, quel agreement, core adverbs, preposition forms and bounded lequel recognition. |
| FR-63 | `questions-exclamations` / `exclamations` | `/sections/12/cards/2`, C0–5; 4 inventory rows; D0–3 | Quel agreement, que/comme clauses, meaning support and punctuation. |
| FR-33 | `negation-basic-negation` / `basic-negation` | `/sections/13/cards/0`, C0–5; 4 inventory rows; D0–4 | Simple/compound/infinitive positions, never and short pas, spoken omission and contradictory si. |
| FR-34 | `negation-negative-choices` / `negative-choices` | `/sections/13/cards/1`, C0–5; 4 inventory rows; D0–5 | Plus/rien/personne/aucun/ni/restrictive que; subject and compound placement contrasts. |
| FR-35 | `introducing-presentatives` / `presentatives` | `/sections/14/cards/0`, C0–5; 5 inventory rows; D0–4 | Identity/description/existence/pointing, profession and adjective contrasts; informal plural c’est labeled. |
| FR-36 | `objects-direct-objects` / `direct-objects` | `/sections/15/cards/0`, C0–5; 3 inventory rows; D0–5 | Full object forms/elision and finite/auxiliary/infinitive/imperative placement; agreement linked. |
| FR-37 | `objects-indirect-objects` / `indirect-objects` | `/sections/15/cards/1`, C0–5; 4 inventory rows; D0–4 | Selected à-person verbs versus direct/stressed constructions; meaning and position. |
| FR-38 | `objects-y` / `y` | `/sections/15/cards/2`, C0–5; 4 inventory rows; D0–4 | Place/governed thing/idea, chez-person location, penser-à-person and position boundaries. |
| FR-39 | `objects-en` / `en` | `/sections/15/cards/3`, C0–5; 4 inventory rows; D0–5 | Quantity/number/measure, topic/origin, people caveat and ordinary placement. |
| FR-40 | `objects-pronoun-order` / `pronoun-order` | `/sections/15/cards/4`, C0–5; 3 inventory rows; D0–5 | Regular/positive-command order, selected combinations, infinitive/compound/negative/y-en. R2 English wording. |
| FR-41 | `replacement-possessive-pronouns` / `possessive-pronouns` | `/sections/16/cards/0`, C0–5; 3 inventory rows; D0–4 | Gender/number paradigms, articles/contractions, accent and determiner contrast. |
| FR-42 | `replacement-demonstrative-pronouns` / `demonstrative-pronouns` | `/sections/16/cards/1`, C0–5; 3 inventory rows; D0–4 | Celui/celle families, ci/là/de/relative completion and conversational ça; depth bounded. |
| FR-43 | `replacement-indefinite-pronouns` / `indefinite-pronouns` | `/sections/16/cards/2`, C0–5; 5 inventory rows; D0–4 | Someone/something/chacun/plural forms; de-adjective and agreement; pronoun/determiner contrast. |
| FR-44 | `place-place-prepositions` / `place-prepositions` | `/sections/17/cards/0`, C0–5; 6 inventory rows; D0–7 | Core/expanded locatives, contractions/countries, chez/dans, route/transport and place adverbs. |
| FR-45 | `time-time-expressions` / `time-expressions` | `/sections/18/cards/0`, C0–5; 6 inventory rows; D0–8 | Continuing/completed/planned duration, elapsed/future interval, starts, relative days and listed adverbs. |
| FR-48 | `complements-verb-prepositions` / `verb-prepositions` | `/sections/19/cards/0`, C0–5; 4 inventory rows; D0–5 | Selected verb/adjective/infinitive frames, lexical meaning/selection and no-preposition counterexamples. |
| FR-49 | `relatives-core-relatives` / `core-relatives` | `/sections/20/cards/0`, C0–5; 4 inventory rows; D0–4 | Subject/object/place/time roles, people/things contrast, que agreement and no repetition. |
| FR-50 | `relatives-dont` / `dont` | `/sections/20/cards/1`, C0–5; 3 inventory rows; D0–4 | Simple de and possession; no duplicate de/possessive; complex-preposition limit. |
| FR-51 | `relatives-compound-relatives` / `compound-relatives` | `/sections/20/cards/2`, C0–5; 4 inventory rows; D0–4 | Recognition label, agreement family, à/de contractions, complex preposition and people qui alternative. |
| FR-52 | `relatives-ce-relatives` / `ce-relatives` | `/sections/20/cards/3`, C0–5; 4 inventory rows; D0–4 | No antecedent/whole idea, subordinate roles, de relation and emphasis. |
| FR-53 | `conditions-si-patterns` / `si-patterns` | `/sections/21/cards/0`, C0–5; 5 inventory rows; D0–5 | Real/imagined frames, command result, suggestion, whether-future and non-impossibility caveat. |
| FR-54 | `reporting-reported-present` / `reported-present` | `/sections/22/cards/0`, C0–5; 4 inventory rows; D0–5 | Statements/yes-no/wh/orders, referents, immediate demain and explicit past-system boundary. |
| FR-55 | `links-contrast` / `contrast` | `/sections/23/cards/0`, C0–5; 3 inventory rows; D0–3 | Mais/alors que/au contraire functions, clause contrast and temporal/corrective limits. |
| FR-56 | `links-purpose` / `purpose` | `/sections/23/cards/1`, C0–5; 3 inventory rows; D0–4 | Noun/infinitive/subjunctive clauses, actor clarity, formal afin de and negative aim. |
| FR-57 | `links-cause` / `cause` | `/sections/23/cards/2`, C0–5; 5 inventory rows; D0–5 | Clause/noun cause, shared/favorable/written explanation and en effet; result routed correctly. |
| FR-58 | `links-result` / `result` | `/sections/23/cards/3`, C0–5; 3 inventory rows; D0–4 | Result versus sequence/addition; conversational/formal and all listed variants. |
| FR-59 | `links-sequence` / `sequence` | `/sections/23/cards/4`, C0–5; 5 inventory rows; D0–6 | Addition/alternatives/continuation, full source chronology set, numbered and concluding functions. |
| FR-60 | `links-concession` / `concession` | `/sections/23/cards/5`, C0–5; 4 inventory rows; D0–4 | Malgré noun, bien que subjunctive, adverbial alternatives, factual and same-actor limits. |

Additional owner: `#start` → `lookup-help`, title/lead + D0–4; all help statements and inherited UI/meta strings were inspected. Their release/offline promises remain subject to runtime gates, not content-source inference.

### Italian final bounded retest — 2026-10-23

Reviewer: parent Codex thread thr_bktaq44cyt; independent of Italian content author thr_pfrpzvtcz9. Verify only. Authority: docs/CONTENT_VALIDATION.md §5, accepted it/en/SITE_PLAN.md §5, docs/ADD_LANGUAGE.md explicit Latin target-run convention.

Carry-forward baseline: full Italian review and independent correction retest by thr_4bsuy4n7xv, /Users/kirby/.bb/thread-storage/thr_4bsuy4n7xv/italian-review/review-current.md. All four gates PASS at deck 45053264210015f9d4264162b30864bcb1d72ed0ec098a255293850804d4afdc.

Final frozen deck: 82cde794ceb7989ba159fa38327808836cf2e3ef46ae800c0aa3e5d2e90786db. The complete recursive boundary is stored in /Users/kirby/.bb/thread-storage/thr_bktaq44cyt/italian-final-delta.json and reproducible with /Users/kirby/.bb/thread-storage/thr_bktaq44cyt/review-italian-final.py. Exactly 22 rich-run containers differ; every concatenated text string and every other JSON value/key/list order is unchanged. No scope, IDs, source, rule, form, example or English meaning changed. Plan content remains at the independent retest snapshot (before parent status-link maintenance).

Manually inspected every old/new container and newly marked subspan: demonstratives, indefinite determiners, bello agreement, sapere/piacere, lo/la/li/le/ne lists, negatives, ci, prepositions, allora, se, comparison, quantity adverbs, ordinal suffix/seconda, gerundio, past-tense names, sii and narrative tense name. Only taught Italian fragments gained bold markup; English explanatory text remains plain. No existing target-marked text was lost. Parent identified two remaining li tokens and -esimo during this check; author marked these three without changing text, and the final complete boundary above includes their independent retest.

| Claim | Verdict | Evidence |
| --- | --- | --- |
| No semantic/scope change since fully reviewed correction | PASS | Recursive JSON comparison; zero semantic differences, 22 markup containers |
| All additional bold spans are Italian study material, English voice preserved | PASS | Complete before/after container inspection, including slash-list li and ordinal -esimo |
| Generated representation matches final JSON | PASS | Canonical build_pages.py content/decks/it-en.json --check |
| Baseline / Coverage / Accuracy / Teaching | PASS | Named full independent review plus this complete bounded retest; no new or remaining blocking finding identified |

Runtime is separate and recorded in UI_AUDIT.md. No browser or deployment claim is made by this retest.


### French final independent correction retest — 2026-10-23

Reviewer `thr_pfrpzvtcz9`, independent of the French author and parent's two
final markup fixes: **ACCEPT — Baseline, Coverage, Accuracy, Teaching PASS**.
Full [retest record](/Users/kirby/.bb/thread-storage/thr_pfrpzvtcz9/french-retest/review.md),
report SHA256 `66618cce963177556624d9d18f4c94b394c50fbdbc3f5c5c8eecbfee74534f25`.
The complete prior review above carries forward only through this independently
reconstructed change boundary, under CONTENT_VALIDATION §5.

- 142 original blocks in 60 card owners changed; all were inspected.
- 234 original dialog blocks changed plus 42 inserted Core rule blocks.
  All 380 blocks in 61 affected dialogs were read, including unchanged
  connected examples, meanings, limits and counterexamples. The unchanged
  adjective-position dialog and help retain their complete prior inspection.
- All 42 former scalar leads survive verbatim in rich bodies, matched to
  their card duplicates. All 30 converted inventory rows retain term,
  separator and complete meaning. French forms/examples and main glosses
  are unchanged after unwrapping runs.
- All 37 non-markup containers were reviewed: 14 English titles, 21 labels,
  natural tell gloss and emotion spelling. No French rule was expanded,
  removed or changed. All 94 baseline rows and 63 Required mappings retain
  their state, depth and owner. Final count: 63 dialogs / 389 blocks,
  including 312 existing example/comment pairs; 248 inventory rows remain.
- Retest RT1 found the English preposition on bolded in the subjects notice;
  parent restored that single English span to plain text. RT2 found the
  residual French lemma trouver in the direct-object agreement comment;
  parent marked only that lemma, retaining English find and punctuation.
  Reviewer independently reconstructed both complete JSON deltas, confirmed
  concatenated text equality and no other changes. Both are CLOSED/PASS.
  No additional English homograph mistag was found in the complete boundary.
- R2 and R3 independently closed: French pronoun order unchanged with the
  natural English gloss; both exact Annex D locators were checked in the
  retained publisher PDF and Required typo corrected without scope change.
- Strict validation returned no errors; exact renderer parity, all 62 card
  anchors and 100 globally unique IDs passed. The reviewer did not execute
  browsers/offline/deployment; parent evidence is separate.

Author change-log records were supplementary: 14 of 433 after entries were
partial fragments, so they were not used to prove full preservation. The
independent complete JSON comparison establishes the boundary instead.

### Final current verdict and revision

| Gate | Italian | French |
| --- | --- | --- |
| Baseline | PASS | PASS |
| Coverage | PASS | PASS |
| Accuracy | PASS | PASS |
| Teaching | PASS | PASS |

No open new-language scope/content blocker remains. Existing DE/EN findings
are unaffected. This accepts the bounded plans; it does not certify all
A1–B1 grammar or learner outcomes.

| Final artifact | SHA256 |
| --- | --- |
| `content/decks/it-en.json` | `82cde794ceb7989ba159fa38327808836cf2e3ef46ae800c0aa3e5d2e90786db` |
| `it/en/SITE_PLAN.md` | `87019300d29a75b3ed92a32b9a43e818498b57cf99986cb54b2fa97137df723d` |
| `it/en/index.html` | `6a09ec249a7efdcca1ced4e934ea381d8ea44488b1e692cec4167c6127268885` |
| `content/decks/fr-en.json` | `545c2b7f6f9807180a8ddbd340d3643afe502e0e46cf2cff90781fd34fecfec2` |
| `fr/en/SITE_PLAN.md` | `3d0eb58cd3c3fac8b08046ffd0c8df84fec605794c7c42bfd6c8be3eda343a2c` |
| `fr/en/index.html` | `1a5adde4ba03a6036af1cf63cbe1eb9a4b77ce2c825b48274d277d27474f6d63` |

The reviewed Italian plan was `1c3a074bafef5ca48ff69d1a02a19a3ba5b88ca3d03ad59600585de18f43fc5f`;
French was `a6e3a7281022b2d577c57bd0fa068343d322e8d40c1a6fdd5f53f5d6509c1277`.
Parent subsequently replaced only their stale NOT RUN/pending introduction
with links to these canonical audits. Byte comparison confirms each accepted
target body from Product onward is unchanged. Those status-only edits do not
alter the inspected scope, mappings, rules or source locators.

Final shared review: ACCEPT, 51 static checks, S1 German comparison -t CLOSED;
see [UI_AUDIT](UI_AUDIT.md). Canonical page/shell checks, existing sibling table
invariants, browser/search/theme/dialog checks and origin-down offline checks
passed separately. Final cached FR/EN and EN/DE HTML hashes match the generated
files; all six decks, landing and four legacy redirects work with origin down.
All temporary task resources were closed; unrelated work was preserved.
Real-device standalone installation and deployed-site verification: NOT RUN.
No staging, commit or push was performed during the review.

## Next full review record

Append a dated record; preserve previous evidence. Include:

- Reviewer distinct from author, reviewed revision, dirty paths, languages,
  references with exact locations and dates, and baseline decisions.
- Per-topic coverage and content-unit evidence using the record fields below.
  Create one record per actual unit and cite exact locations rather than
  asserting that a whole section is correct.
- Totals: inventoried, reviewed, covered/partial/missing/unverified/excluded;
  gate verdicts and all outstanding findings with actions and retest results.

Per-unit record:

- Topic ID and unit ID
- Actual location: card, `DETAILS` key, table cell or practice answer
- Coverage state
- Reference and exact section
- Probe, expected result and observed result
- Linguistic verdict or finding ID
