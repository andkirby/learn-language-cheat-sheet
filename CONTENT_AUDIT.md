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

Current overall status: **NOT RUN** for both languages. Documentation
structure has been reviewed, but no page source, rendered content or external
language reference has been inspected.

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
| DE-G01 | German | Present conjugation, sein/haben and irregular stems | Required depth and placement | Open |
| DE-G02 | German | nicht versus kein and negation placement | Required depth and placement | Open |
| DE-G03 | German | Imperative | Include, defer or exclude | Open |
| DE-G04 | German | Perfekt formation/auxiliary choice and Präteritum usage | Required depth and tense boundary | Open |
| DE-G05 | German | Plural formation, comparison and adjective endings without an article | Split into reviewable decisions | Open |
| DE-G06 | German | Verb-governed cases and reflexive verbs | Required depth and placement | Open |
| EN-G01 | English | be questions/negatives and there is/are | Required depth and placement | Open |
| EN-G02 | English | Negation beyond modal prohibitions | Required depth and placement | Open |
| EN-G03 | English | Past Continuous and narrative tense contrasts | Include, defer or exclude | Open |
| EN-G04 | English | Present Perfect with duration and continuous aspect | Required tense boundary | Open |
| EN-G05 | English | Relative clauses | Include, defer or exclude | Open |
| EN-G06 | English | Imperative, basic linking words and reported speech | Split into reviewable decisions | Open |
| EN-G07 | English | Dedicated numbers/date/time reference | Include, defer or exclude; earlier information architecture implied coverage without defining it | Open |

## Findings and follow-up

| ID | Topic / evidence | Consequence | Required action | Status / retest |
| --- | --- | --- | --- | --- |
| C-01 | `AGENTS.md` verification and both plans' update protocols previously contained only runtime/design gates | Working UI could be mistaken for reviewed grammar | Add and link content gates | Documentation fixed; page review NOT RUN |
| C-02 | EN-05/06: English plan previously used signal-word selection and “время названо?” | Shortcut boundaries were not required | Require meaning/context and contrasting examples; inspect actual tense cards/dialogs against references | Plan revised 2026-09-10; page aligned 2026-09-11 (meaning-first card/dialog/practice answer, `since 2020` limit on card); independent reference retest pending |
| C-03 | Both plans: baseline without independent syllabus comparison or sourced level placement | Completeness cannot be established | Resolve DE-G01–06 and EN-G01–07 plus any gaps found by reference comparison | Open; explicit category exclusions now recorded in both plans |
| C-04 | Shared design contract specified German terminology despite serving English too | Shared content guidance was language-specific | State target-language terminology in the shared contract | Documentation fixed in both relevant bullets; no UI change |
| C-05 | Add-language playbook required three practice items without topic mapping | Exercise count could substitute for coverage evidence | Map practice to topics; review every answer; use additional audit probes where needed | Procedure fixed; practice remapped on both pages 2026-09-11 (DE-03/07/08, EN-01/04/06) — answer review pending |
| C-06 | Plan-authoring questions and scope-decision rules were spread across several files | Authors could omit exclusions or put evidence into the plan | Add one authoring owner and standardize both language plans | Documentation fixed; content baseline remains NOT RUN |
| C-07 | User-reported teaching-quality gaps (2026-09-11): DE `objects` lead named no verbs, DE `tekamolo` «База» used unglossed Temporal/Kausal/Modal/Lokal, DE `perfekt` «Важно» named no verbs; sweep added DE `wo-wohin` caveat and `passive` block without examples, EN `svo` lead typo («roles») | Learner cannot act on a rule whose terms or exceptions are not exemplified | Fix the six units; run the full unit-by-unit Teaching gate later | Six units fixed in page 2026-09-11 (author review); Teaching gate still NOT RUN — see D-01 |
| C-08 | User-reported (2026-09-11): DE possessives table shows only `mein`; the «одна модель для всех основ» design was unclear until explained in conversation | A correct-by-scope presentation reads as incomplete coverage to the learner | State the one-model rule on the card (stems named, «основа + окончание») and add a `dein` example in the dialog | Fixed in page 2026-09-11 (author review); Teaching gate still NOT RUN |
| C-09 | User-reported (2026-09-11): DE ein-words table has no reading key — why Akk. m = `meinen`, Dat. = `-em/-er/-en` was unclear | A declension table without its generating rule must be memorised cell by cell | Add the key: endings mirror the definite article (den→meinen, dem→meinem, der→meiner); only three «empty» cells (Nom. m/n, Akk. n); Akk. visible in masc. only, Dat. marks all genders | Fixed in page 2026-09-11 (`why-ein-endings` chip + dialog); Teaching gate still NOT RUN |
| C-10 | User-reported (2026-09-11): the bold/`td.hot` table convention was missed entirely by the first learner — it is documented for developers (style-guide, DESIGN_SYSTEM) but never labeled for learners | An unlabeled visual convention does not exist for the reader it is meant to serve | One consistent `.tiny` legend under every table with hot cells (3 DE, 1 EN) | Fixed in page 2026-09-11; Teaching gate still NOT RUN |

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
