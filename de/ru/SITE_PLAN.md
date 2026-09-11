# Deutsch Cheat Sheet — site plan

## Responsibility and status

This file owns the accepted product intent, German content target, durable
scope decisions and language-specific information architecture for
`de/ru/index.html`. Use [the authoring guide](../../docs/SITE_PLAN_GUIDE.md)
when revising it.

It does not prove that the page matches the target or that the content is
correct. Those results belong in [CONTENT_AUDIT.md](../../CONTENT_AUDIT.md).
Shared UI behavior belongs in [the design system](../../.design/DESIGN_SYSTEM.md),
and operation and deployment belong in [README.md](../../README.md).

The page lives at `<target>/<audience>/` (`de/ru/`) so sibling audiences
(`de/en/`, …) can later share the target. The former `deutsch/` URL is a
redirect stub to here, kept for installed PWAs and old links.

Status: the product and interaction target is accepted. The content baseline
is provisional until the baseline gate is reviewed against named A1–B1 and
grammar references. Page coverage, accuracy and teaching-quality gates are
currently NOT RUN.

## Product and learner

The product is a mobile-first German grammar lookup deck for Russian-speaking
A1–B1 learners. It should make common grammar decisions retrievable in one to
three taps, remain concise on the first layer, install as a PWA and work
offline after the first successful load.

It assumes no familiarity with German grammar terminology. Russian explanations
come first; useful German terms remain visible. Examples use contemporary
Standard German as used in Germany. Austrian and Swiss variants appear only
when omission would predictably mislead the intended learner, and must be
labeled.

## Scope boundary

Required grammar topics are defined once in the inventory below. No additional
topic is implied by a heading, search keyword or content found on the page.

| Decision | Excluded content | Rationale | Reconsider when |
| --- | --- | --- | --- |
| DE-X01 | Pronunciation, phonetics and listening instruction | The product is a grammar lookup deck without audio | A pronunciation or audio learning surface is accepted |
| DE-X02 | Thematic vocabulary, phrasebook material and a comprehensive dictionary or conjugator | These require different retrieval and maintenance models | The product expands beyond grammar lookup |
| DE-X03 | Exhaustive exceptions and productive B2+ grammar | Density must serve the stated A1–B1 audience | The supported level expands or a reference review shows an A1–B1 dependency |
| DE-X04 | Systematic Austrian, Swiss and dialect comparison | Standard German is the default and regional comparison would dominate the deck | Repeated learner need or correctness risk justifies a labeled exception |
| DE-X05 | Course sequencing, mastery scoring and CEFR certification | Three practice items support retrieval; they are not an assessment system | The product adopts progress or assessment semantics |

There are no accepted deferred topics. Unresolved candidate gaps are findings
in `CONTENT_AUDIT.md`, not silent exclusions or plan commitments.

## Primary retrieval questions

1. Which case applies, and what role does it express?
2. Which article, pronoun or adjective ending do I need?
3. Where does the finite verb go?
4. How does the verb bracket change with modal, separable and perfect forms?
5. What changes in subordinate clauses?
6. Which prepositions govern Akkusativ, Dativ or Genitiv?
7. Can I see one short example and open a deeper explanation when needed?

## Information architecture

The page is a lookup deck with five view destinations:

| View | Stable anchor | Required topics |
| --- | --- | --- |
| Падежи | `#cases` | DE-01, DE-02 (`#preps`) |
| Формы | `#forms` | DE-03–05, DE-15–16 (`#extras`) |
| Глагол и порядок | `#order` | DE-06–07, DE-09, DE-12–14 (`#verbs`) |
| Придаточные | `#clauses` | DE-08, DE-10–11 |
| Повтор | `#practice` | Practice contract below |

`#start`, `#preps`, `#extras`, `#verbs` and `#install-help` are stable legacy
or direct anchors. A direct anchor opens the owning view before scrolling.
Search covers all views and restores the selected view when cleared. Install
help remains a dialog plus footer line rather than a content section.

## Content and practice contract

The shared card, dialog, search, navigation and accessibility mechanics are
defined in the design system. German content adds these requirements:

- A first-layer rule gives the learner a trigger, form or position, and one
  short natural example. A dangerous simplification includes its essential
  limit on the card.
- Example glosses follow the rule type. Form and position rules (endings,
  case forms, word order) keep examples in the target language only, with
  structural annotation — bold forms, `dem Mann = Dat.` labels, minimal
  pairs; a Russian translation cannot demonstrate German morphology or
  syntax. Meaning/usage rules (Konjunktiv II use, um … zu vs damit,
  preposition choice) add a short Russian gloss carrying the deciding
  difference, not a full translation. Declension fragments stay unglossed.
  A gloss that does not add the choice criterion is removed.
- Dialogs add reasoning, contrast or exceptions without contradicting the
  card. New tappable explanations use the page's `DETAILS` object.
- German pattern text carries `lang="de"`; Russian explanations and
  translations preserve the grammatical distinction rather than forcing a
  literal translation.
- Search metadata includes likely Russian questions and German terms.
- Practice has three contextualized items mapped to DE-03, DE-07 and DE-08.
  Answers explain the choice and identify valid alternatives. Audit probes
  provide broader validation without bloating learner practice.

## Required content inventory

All rows are required in the current target. “Core” means a learner should
be able to choose or form the pattern; “recognition” means identify and
understand it. Per-topic CEFR placement and page alignment still require
evidence in the content audit.

| ID | Learner question and required content | Surface | Acceptance depth |
| --- | --- | --- | --- |
| DE-01 | Which case? Nominativ, Akkusativ, Dativ and Genitiv with their roles and questions | `#cases` | Core: rule and natural example per case; questions are clues, not the sole explanation |
| DE-02 | Which case follows a preposition? Fixed-case groups and Wechselpräpositionen | `#preps` | Core lookup plus location/direction contrast and movement caveat |
| DE-03 | Which article ending? Definite, indefinite and kein patterns | `#forms` | Complete case/gender/plural reference plus usage examples |
| DE-04 | Which personal-pronoun form? | `#forms` | Complete nominative/accusative/dative paradigm plus examples |
| DE-05 | Which possessive and ending? mein, dein, sein, ihr, unser, euer, ihr, Ihr | `#forms` | Stems and case/gender/plural pattern plus examples |
| DE-06 | Where is the finite verb in statements, yes/no questions, W-questions and inversion? | `#order` | Core position patterns and contrasting examples |
| DE-07 | How does the verb bracket work with modal, perfect and separable constructions? | `#verbs` | Formula and natural example per construction |
| DE-08 | Which conjunction changes word order? Subordinators and coordinators | `#clauses` | Verb-final rule, non-verb-final contrast and examples |
| DE-09 | Where do time, cause, manner and place phrases tend to go? | `#order` | TeKaMoLo as a default with an explicit limitation |
| DE-10 | How do relative clauses work? | `#clauses` | Rule, pronoun role and example with sufficient dialog detail |
| DE-11 | um … zu or damit? | `#clauses` | Same-subject decision and a contrasting pair |
| DE-12 | How is hypothetical meaning expressed? würde + infinitive and wäre/hätte/könnte/müsste/sollte | `#verbs` | Core high-frequency forms and examples |
| DE-13 | How is the passive formed? | `#verbs` | Core werden + Partizip II formula and example |
| DE-14 | Why can a modal perfect contain two infinitives? | `#verbs` | Recognition note with one parsed example |
| DE-15 | When does the noun change? Dativ plural, masculine/neuter Genitiv and N-declension | `#extras` | Endings, limits and examples |
| DE-16 | Which adjective ending follows der-words and ein-words? | `#extras` | Compact overview and examples; no claim of exhaustive adjective declension |

## Acceptance and maintenance

- **This page is generated**: `de/ru/index.html` is rendered from
  [`content/decks/de-ru.json`](../../content/decks/de-ru.json) by
  `python3 tools/build_pages.py content/decks/de-ru.json`. Edit the deck, not
  the HTML; regenerate and commit both. `--check` fails when they drift.
- Revise this plan before changing accepted scope, exclusions, content depth,
  practice mapping, view membership or stable anchors.
- Keep unresolved proposals in the content audit. Promote them here only after
  a Required, Deferred or Excluded decision is accepted.
- Apply [content validation](../../docs/CONTENT_VALIDATION.md) after content
  changes and record the reviewed revision, sources, findings and gate results
  in `CONTENT_AUDIT.md`.
- Follow `AGENTS.md` for shared page-change and runtime checks. A runtime pass
  does not establish content acceptance.
