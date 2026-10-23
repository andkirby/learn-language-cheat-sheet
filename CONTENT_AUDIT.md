# Content audit

## Responsibility and current status

This file owns content-review status, open content questions, findings and
verdicts, and it indexes the dated review records. Full evidence, reference
provenance and per-unit ledgers live in the linked records under
[docs/content-audit/](docs/content-audit/). Records are append-only; finding
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
166 dialogs after that sweep's corrections and retests, with the runtime and
browser evidence, in the
[2026-10-20 record](docs/content-audit/2026-10-meaning-support.md#gates-and-runtime-evidence).
A fresh syllabus-to-plan/frequency-list completeness audit is **NOT RUN**;
this is not overall four-gate acceptance.

Italian/French additions (2026-10-23): **Baseline, Coverage, Accuracy and
Teaching PASS for both new decks**, following independent full reviews and
complete bounded correction retests. All findings are closed at the final
source hashes in the
[2026-10-23 record](docs/content-audit/2026-10-23-it-fr-context.md#final-current-verdict-and-revision).
Existing DE/EN baseline findings above remain unchanged. Shared integration
review is accepted; runtime checks passed separately in
[UI_AUDIT](UI_AUDIT.md). [Live deployment checks passed](UI_AUDIT.md#2026-10-23--itfr-live-deployment-check)
for the released pages. Real-device standalone installation remains **NOT RUN**.

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

## Review records

Full dated records live in [docs/content-audit/](docs/content-audit/), one
bounded file per coherent group; evidence is moved there verbatim. Each
record's old anchor from this file's history is kept on its row below.
Chronological index:

| Date | Record | Scope/verdict |
| --- | --- | --- |
| 2026-09-10 | <a id="2026-09-10--initial-documentation-review"></a>[Initial documentation review](docs/content-audit/2026-09-de-en-review-sweeps.md#2026-09-10--initial-documentation-review) | DE/EN docs-only; all gates NOT RUN |
| 2026-09-11 | <a id="2026-09-11--incremental-change-page-alignment-with-accepted-plans"></a>[Incremental change: page alignment with accepted plans](docs/content-audit/2026-09-de-en-review-sweeps.md#2026-09-11--incremental-change-page-alignment-with-accepted-plans) | DE/EN; author-level |
| 2026-09-11 | <a id="2026-09-11--teaching-quality-pass-user-reported-signals"></a>[Teaching-quality pass (user-reported signals)](docs/content-audit/2026-09-de-en-review-sweeps.md#2026-09-11--teaching-quality-pass-user-reported-signals) | DE/EN; author-level |
| 2026-09-11 | <a id="2026-09-11--full-two-language-review-pass-de--en"></a>[Full two-language review pass (DE + EN)](docs/content-audit/2026-09-de-en-review-sweeps.md#2026-09-11--full-two-language-review-pass-de--en) | DE/EN; Coverage FAIL, Accuracy/Teaching NOT RUN |
| 2026-09-11 | <a id="2026-09-11--example-gloss-policy--forms-section-examples-user-approved-sweep"></a>[Example-gloss policy + forms-section examples](docs/content-audit/2026-09-de-en-review-sweeps.md#2026-09-11--example-gloss-policy--forms-section-examples-user-approved-sweep) | DE/EN; author-level |
| 2026-09-12 | <a id="2026-09-12--incremental-change-comprehension-access-glosses"></a>[Incremental change: comprehension-access glosses](docs/content-audit/2026-09-de-en-review-sweeps.md#2026-09-12--incremental-change-comprehension-access-glosses) | DE/EN; author-level |
| 2026-09-13 | <a id="2026-09-13--incremental-change-findings-sweep-closes-c-13c-20"></a>[Incremental change: findings sweep closes C-13…C-20](docs/content-audit/2026-09-de-en-review-sweeps.md#2026-09-13--incremental-change-findings-sweep-closes-c-13c-20) | DE/EN; Coverage → PASS |
| 2026-09-13 | <a id="2026-09-13--scope-addition-de-17-modal-particles-de-g09-decided"></a>[Scope addition: DE-17 modal particles (DE-G09)](docs/content-audit/2026-09-scope-additions.md#2026-09-13--scope-addition-de-17-modal-particles-de-g09-decided) | DE |
| 2026-09-13 | <a id="2026-09-13--scope-additions-en-17-en-18-de-18-linking-words-flavour-words"></a>[Scope additions: EN-17, EN-18, DE-18 (linking/flavour words)](docs/content-audit/2026-09-scope-additions.md#2026-09-13--scope-additions-en-17-en-18-de-18-linking-words-flavour-words) | DE/EN |
| 2026-09-13 | <a id="2026-09-13--scope-additions-tier-1-a1-core-de-1923-en-1920-en-05-always--shell-automations"></a>[Scope additions: Tier-1 A1-core + shell automations](docs/content-audit/2026-09-scope-additions.md#2026-09-13--scope-additions-tier-1-a1-core-de-1923-en-1920-en-05-always--shell-automations) | DE/EN |
| 2026-09-21 | <a id="2026-09-21--scope-addition-de-24-plural-formation-de-g05-decided--en-13-gap-fill"></a>[Scope addition: DE-24 plural formation + EN-13 gap-fill](docs/content-audit/2026-09-scope-additions.md#2026-09-21--scope-addition-de-24-plural-formation-de-g05-decided--en-13-gap-fill) | DE/EN |
| 2026-09-21 | <a id="2026-09-21--scope-addition-de-25-demonstratives-dieser-family-de-g11-decided"></a>[Scope addition: DE-25 demonstratives (DE-G11)](docs/content-audit/2026-09-scope-additions.md#2026-09-21--scope-addition-de-25-demonstratives-dieser-family-de-g11-decided) | DE |
| 2026-09-23 | <a id="2026-09-23--de-05-depth-polite-ihr-construction-de-g12-decided"></a>[DE-05 depth: polite Ihr construction (DE-G12)](docs/content-audit/2026-09-scope-additions.md#2026-09-23--de-05-depth-polite-ihr-construction-de-g12-decided) | DE |
| 2026-09-24 | <a id="2026-09-24--correction-pairs-sondern-vs-aber-de-08-not--but-en-18-de-g13-en-g11-decided"></a>[Correction pairs: sondern vs aber, not … but (DE-G13, EN-G11)](docs/content-audit/2026-09-scope-additions.md#2026-09-24--correction-pairs-sondern-vs-aber-de-08-not--but-en-18-de-g13-en-g11-decided) | DE/EN |
| 2026-09-24 | <a id="2026-09-24--scope-completion-tier-2-batch-de-2628-en-2126-no-open-scope-rows"></a>[Scope completion: Tier-2 batch (DE-26–28, EN-21–26)](docs/content-audit/2026-09-scope-additions.md#2026-09-24--scope-completion-tier-2-batch-de-2628-en-2126-no-open-scope-rows) | DE/EN |
| 2026-09-28 | <a id="2026-09-28--new-deck-de-en-german-explained-in-english-audience-variant"></a>[New deck: de-en (audience variant)](docs/content-audit/2026-09-28-audience-decks.md#2026-09-28--new-deck-de-en-german-explained-in-english-audience-variant) | DE→EN |
| 2026-09-28 | <a id="2026-09-28--new-deck-en-de-english-explained-in-german-audience-variant"></a>[New deck: en-de (audience variant)](docs/content-audit/2026-09-28-audience-decks.md#2026-09-28--new-deck-en-de-english-explained-in-german-audience-variant) | EN→DE |
| 2026-09-29 | <a id="2026-09-29--practice-view-removed-scope-decision-plans-de-d01en-d01"></a>[Practice view removed (scope decision)](docs/content-audit/2026-09-scope-additions.md#2026-09-29--practice-view-removed-scope-decision-plans-de-d01en-d01) | all decks; DEBT D-03 |
| 2026-10-20 | <a id="2026-10-20--meaning-support-in-all-four-language-pairs"></a>[Meaning support in all four language pairs](docs/content-audit/2026-10-meaning-support.md#2026-10-20--meaning-support-in-all-four-language-pairs) | all four; Accuracy+Teaching PASS, 164 cards/166 dialogs |
| 2026-10-21 | <a id="2026-10-21--documentation-and-release-follow-up"></a>[Documentation and release follow-up](docs/content-audit/2026-10-meaning-support.md#2026-10-21--documentation-and-release-follow-up) | all four; live checks |
| 2026-10-21 | <a id="2026-10-21--readable-term-lists-and-explicit-german-imperativ-contrast"></a>[Readable term lists and German Imperativ contrast](docs/content-audit/2026-10-meaning-support.md#2026-10-21--readable-term-lists-and-explicit-german-imperativ-contrast) | DE siblings |
| 2026-10-23 | <a id="2026-10-23--italianfrench-english-audience-implementation-and-independent-review"></a>[Italian/French implementation and independent review](docs/content-audit/2026-10-23-it-fr-context.md#2026-10-23--italianfrench-english-audience-implementation-and-independent-review) · [Italian record](docs/content-audit/2026-10-23-italian-review.md) · [French record](docs/content-audit/2026-10-23-french-review.md) | IT/FR; all four gates PASS per language |

## Next full review record

Create a new record file in `docs/content-audit/` (`<date>-<topic>.md`,
starting with the standard pointer header used by its siblings) and add a row
to the index above; preserve previous evidence in place. Include:

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
