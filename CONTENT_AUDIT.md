# Content audit

## Responsibility and current status

This file owns content-review evidence, reference provenance, open content
questions, findings and verdicts. Review records are append-only; finding
status and retest evidence may be updated without erasing their history.

It does not own accepted language scope. Promote an accepted Required,
Deferred or Excluded decision to the relevant
[German](de/ru/SITE_PLAN.md) or [English](en/ru/SITE_PLAN.md) plan. The
procedure is [content validation](docs/CONTENT_VALIDATION.md); plan authors use
[the SITE_PLAN guide](docs/SITE_PLAN_GUIDE.md).

Current overall status: Baseline and Coverage **FAIL** for both languages;
Accuracy and Teaching **NOT RUN** pending an independent reference-grounded
pass. The 2026-09-11 full reviewer pass (record below) inspected both decks,
both generated pages and all practice/search metadata. Runtime/browser gates
remain a separate AGENTS.md checklist.

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
| DE-G01 | German | Present conjugation, sein/haben and irregular stems | Required depth and placement | Open — reconfirmed 2026-09-11 @ `b75c890`: no paradigm unit on the page (conjugated forms appear only inside word-order cards) |
| DE-G02 | German | nicht versus kein and negation placement | Required depth and placement | Open — reconfirmed 2026-09-11 @ `b75c890`: kein appears only in declension tables; no negation unit |
| DE-G03 | German | Imperative | Include, defer or exclude | Open — reconfirmed 2026-09-11 @ `b75c890`: absent |
| DE-G04 | German | Perfekt formation/auxiliary choice and Präteritum usage | Required depth and tense boundary | Open — reconfirmed 2026-09-11 @ `b75c890`: Perfekt present only as the DE-07 bracket construction + auxiliary-choice dialog; Präteritum and the tense boundary absent |
| DE-G05 | German | Plural formation, comparison and adjective endings without an article | Split into reviewable decisions | Open — reconfirmed 2026-09-11 @ `b75c890`: plural formation and comparison absent; adjective endings without an article are covered in the `adjectives` dialog (that sub-decision could be closed) |
| DE-G06 | German | Verb-governed cases and reflexive verbs | Required depth and placement | Open — reconfirmed 2026-09-11 @ `b75c890`: helfen+Dativ and six geben-class verbs appear in dialogs/practice; no systematic unit; reflexives absent |
| DE-G07 | German | der vs ein vs kein choice (known/specific vs new, professions without article, kein as noun negation) | Retrieval question 2 arguably promises usage choice, not only form; needs an accepted depth and placement decision | Open (2026-09-11 page review, example-sweep session) |
| DE-G08 | German | seit vs vor («живу здесь два года» vs «переехал два года назад») | Textbook Russian-interference time-preposition trap; include/defer decision needed | Open (2026-09-11 page review, example-sweep session) |
| EN-G01 | English | be questions/negatives and there is/are | Required depth and placement | Open — reconfirmed 2026-09-11 @ `b75c890`: absent; the EN-04 "be/modal distinction" half is required *now* by the plan and filed as C-14 |
| EN-G02 | English | Negation beyond modal prohibitions | Required depth and placement | Open — reconfirmed 2026-09-11 @ `b75c890`: only scattered basics (doesn't/don't + any, never/rarely) |
| EN-G03 | English | Past Continuous and narrative tense contrasts | Include, defer or exclude | Open — reconfirmed 2026-09-11 @ `b75c890`: absent |
| EN-G04 | English | Present Perfect with duration and continuous aspect | Required tense boundary | Open — reconfirmed 2026-09-11 @ `b75c890`: since/for duration limit present on card/dialog; continuous aspect absent |
| EN-G05 | English | Relative clauses | Include, defer or exclude | Open — reconfirmed 2026-09-11 @ `b75c890`: absent |
| EN-G06 | English | Imperative, basic linking words and reported speech | Split into reviewable decisions | Open — reconfirmed 2026-09-11 @ `b75c890`: all three absent |
| EN-G07 | English | Dedicated numbers/date/time reference | Include, defer or exclude; earlier information architecture implied coverage without defining it | Open — reconfirmed 2026-09-11 @ `b75c890`: absent (time prepositions cover only in/on/at) |
| EN-G08 | English | Present Continuous with `always` for irritation/complaint ("He's always losing his keys") | Required/Deferred/Excluded decision; usage verified against `research/englishpage.md` (EnglishPage, "Repetition and Irritation with Always") | Open — filed 2026-09-11 full pass; deck's PC card covers now/period + state-verb limit only, no complaint use |

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
| C-13 | Search metadata (both pages): DE tokens `helfen`, `sehen` (objects card), `bis`, `entlang` (prep-akk), `gegenüber` (prep-dat), `dessen`, `deren` (relative — taught nowhere), `wo`, `wohin` (case grid) are not visible on their card; EN keywords all land on delivered content | A hit that never shows the promised word is a misleading hit; `dessen`/`deren` additionally index untaught content | Surface the tokens on the cards or trim the keywords; an uncommitted search-hygiene validator in the worktree mechanically flags this class (28 DE + 10 EN tokens; its exemption list still absorbs intentional routings such as `wurde`→Konjunktiv-II) | Open (filed 2026-09-11 full pass; overlaps in-progress D-04 work — an uncommitted trim of the flagged DE tokens was observed in the worktree during this pass and is not evaluated here, being outside the reviewed revision) |
| C-14 | EN-04 `#order`: do-support card + subject-who exception present; the plan's "be/modal distinction" (no do-support after be/modals) is absent from the whole deck | Plan-required acceptance depth missing; learner is given no *Is she…? / Can you…?* rule | Add the be/modal line to the questions card or `do-questions` dialog; the remainder overlaps EN-G01 | Open (filed 2026-09-11 full pass) |
| C-15 | EN-15 `#nouns`: comparative spelling limits only implicit — `big — bigger — the biggest` shows doubling by example; -y→-ier and e-drop are absent | Plan depth names "spelling limits"; *happier/nicer* are underivable from the card | State the three spelling rules compactly in the card or `comparative` dialog | Open (filed 2026-09-11 full pass) |
| C-16 | EN-13 `#nouns`: plurals unit has rules + irregulars + invariates but no countability caveat (countability itself lives one card away in EN-14) | Plan depth for EN-13 explicitly names a countability caveat | Add a one-line caveat to the plurals unit, or record a plan-depth revision | Open (filed 2026-09-11 full pass) |
| C-17 | EN-12 `#preps`: 8 listed pairs (6 chips + `arrive in/at`, `apologize for` in the dialog); only `depend on` has a sentence example | Plan depth says "all listed combinations with examples" — ambiguous between pair-listing and per-pair examples | Add a short example per pair **or** revise the plan depth (owner decision; not promoted here) | Open (filed 2026-09-11 full pass) |
| C-18 | `en-ru.json` practice `_note` topic IDs swapped: item 2 (saw/EN-06) is noted EN-04; item 3 (Does she like/EN-04) is noted EN-06 | Provenance metadata misleads future reviews; not rendered (generator ignores `_note`) | Swap the two `_note` IDs | Open (filed 2026-09-11 full pass) |
| C-19 | DE learner-visible text defects @ `b75c890`: `ihrem` dialog title «Почему “ihрем”?» mixes Cyrillic р/е/м into the German word (deck + rendered page); `why-ein-endings` dialog «Видимо меняется только Maskulin» — «Видимо» reads as "apparently", intended "visibly" | Copying the title yields wrong characters; ambiguous wording weakens the Akk.-reading rule | Fix both strings in `de-ru.json` + regenerate | Open (filed 2026-09-11 full pass) |
| C-20 | EN example/terminology nits @ `b75c890`: `the-article` dialog uses «сверхлатив» (deck elsewhere says «превосходная»); `passive-en` dialog «Кем/чем: …by the workers, if needed.» is a fragment, not an example; `modals-en` must example (*You must stop*) shows obligation only while its label also promises deduction | Inconsistent terminology; examples that don't demonstrate the stated meaning | Rewrite the three fragments in `en-ru.json` + regenerate | Open (filed 2026-09-11 full pass) |

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
