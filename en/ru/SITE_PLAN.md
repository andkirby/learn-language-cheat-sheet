# English Cheat Sheet — site plan

## Responsibility and status

This file owns the accepted product intent, English content target, durable
scope decisions and language-specific information architecture for
`en/ru/index.html`. Use [the authoring guide](../../docs/SITE_PLAN_GUIDE.md)
when revising it.

It does not prove that the page matches the target or that the content is
correct. Those results belong in [CONTENT_AUDIT.md](../../CONTENT_AUDIT.md).
Shared UI behavior belongs in [the design system](../../.design/DESIGN_SYSTEM.md),
and operation and deployment belong in [README.md](../../README.md).

The page lives at `<target>/<audience>/` (`en/ru/`) so sibling audiences
(`en/de/`, …) can later share the target. The former `english/` URL is a
redirect stub to here, kept for installed PWAs and old links.

Status: the product and interaction target is accepted. The content baseline
is provisional until the baseline gate is reviewed against named A1–B1 and
grammar references. Page coverage, accuracy and teaching-quality gates are
currently NOT RUN.

## Product and learner

The product is a mobile-first English grammar lookup deck for Russian-speaking
A1–B1 learners. It should make common grammar decisions retrievable in one to
three taps, remain concise on the first layer, install as a PWA and work
offline after the first successful load.

It assumes no familiarity with English grammar terminology. Russian
explanations come first; useful English terms remain visible. Examples use
neutral contemporary international English. A British/American difference is
labeled only when it changes the taught choice or prevents a likely error.

## Scope boundary

Required grammar topics are defined once in the inventory below. No additional
topic is implied by a heading, search keyword or content found on the page.

| Decision | Excluded content | Rationale | Reconsider when |
| --- | --- | --- | --- |
| EN-X01 | Pronunciation, phonetics and listening instruction | The product is a grammar lookup deck without audio | A pronunciation or audio learning surface is accepted |
| EN-X02 | Thematic vocabulary, phrasebook material and a comprehensive dictionary | These require different retrieval and maintenance models | The product expands beyond grammar lookup |
| EN-X03 | Exhaustive British, American and regional comparison | Neutral international examples are sufficient for the target | A variety difference changes a taught decision or repeated learner need emerges |
| EN-X04 | Exhaustive exceptions and productive B2+ grammar | Density must serve the stated A1–B1 audience | The supported level expands or a reference review shows an A1–B1 dependency |
| EN-X05 | Course sequencing, mastery scoring and CEFR certification | Three practice items support retrieval; they are not an assessment system | The product adopts progress or assessment semantics |

There are no accepted deferred topics. Unresolved candidate gaps are findings
in `CONTENT_AUDIT.md`, not silent exclusions or plan commitments.

## Primary retrieval questions

1. Which tense fits the intended meaning and context?
2. Do I need a, an, the or no article?
3. How do I build a statement, negative or question?
4. Should I use Present Perfect or Past Simple?
5. Which time, place or dependent preposition applies?
6. Which conditional pattern expresses this meaning?
7. Can I see one short example and open a deeper explanation when needed?

Signal words support a tense decision; they never replace meaning and context.

## Information architecture

The page is a lookup deck with five bottom-navigation destinations and one
footer-linked practice view:

| View | Stable anchor | Required topics |
| --- | --- | --- |
| Артикли и слова | `#articles` | EN-01–02, EN-13–15 (`#pronouns`, `#nouns`) |
| Времена | `#tenses` | EN-05–07 |
| Порядок | `#order` | EN-03–04 |
| Глаголы | `#verbs` | EN-08–10, EN-16 (`#conditionals`) |
| Предлоги | `#preps` | EN-11–12 |
| Повтор | `#practice` | Practice contract below; footer link only |

`#start`, `#pronouns`, `#nouns`, `#conditionals` and `#install-help` are
stable legacy or direct anchors. A direct anchor opens the owning view before
scrolling. Search covers all views and restores the selected view when
cleared. Install help remains a dialog plus footer line rather than a content
section.

## Content and practice contract

The shared card, dialog, search, navigation and accessibility mechanics are
defined in the design system. English content adds these requirements:

- A first-layer rule gives the learner a meaning/use trigger, form or position,
  and one short natural example. Signal words are secondary clues.
- Example glosses follow the rule type. Form and position rules (paradigms,
  word order, V-ing/to V patterns) keep examples in the target language only,
  with structural annotation — bold forms, minimal pairs; a Russian
  translation cannot demonstrate English morphology or syntax. Meaning/usage
  rules (article choice, tense choice, mustn't vs don't have to) add a short
  Russian gloss carrying the deciding difference, not a full translation.
  Word fragments stay unglossed. A gloss that does not add the choice
  criterion is removed.
- A dangerous simplification includes its essential limit on the card. In
  particular, Present Perfect versus Past Simple must use meaning and discourse
  context; “is a time mentioned?” is not a sufficient decision rule.
- Dialogs add reasoning, contrast or exceptions without contradicting the
  card. New tappable explanations use the page's `DETAILS` object.
- English pattern text carries `lang="en"`; Russian explanations and
  translations preserve the relevant distinction rather than forcing a
  literal translation.
- Search metadata includes likely Russian questions and English terms.
- Practice has three contextualized items mapped to EN-01, EN-04 and EN-06.
  Answers explain the choice and identify valid alternatives. Audit probes
  provide broader validation without bloating learner practice.

## Required content inventory

All rows are required in the current target. “Core” means a learner should
be able to choose or form the pattern; “recognition” means identify and
understand it. Per-topic CEFR placement and page alignment still require
evidence in the content audit.

| ID | Learner question and required content | Surface | Acceptance depth |
| --- | --- | --- | --- |
| EN-01 | a/an, the or zero article? Sound, reference, generalization and institution use | `#articles` | Core rules, contrasting examples and essential limits |
| EN-02 | Which pronoun? Subject, object, dependent/independent possessive and reflexive forms | `#pronouns` | Complete listed paradigm plus usage examples |
| EN-03 | How are statements ordered, including frequency adverbs? | `#order` | Core SVO default, be placement and limitations with examples |
| EN-04 | How are questions formed? Do/Does/Did, W-questions and subject who | `#order` | Core formulas, be/modal distinction and subject-question exception |
| EN-05 | Present Simple or Present Continuous? | `#tenses` | Meaning/use, affirmative form and contrasting examples; signal-word limits |
| EN-06 | Past Simple or Present Perfect? | `#tenses` | Meaning/use, form and contextual contrast; reject the single-keyword shortcut |
| EN-07 | will, going to or scheduled present? | `#tenses` | Usage contrast, forms and examples |
| EN-08 | How are modals and have to used? | `#verbs` | Forms, high-frequency meanings and mustn't versus don't have to |
| EN-09 | How is the passive formed? | `#verbs` | be + V3 pattern in the explicitly shown tenses with examples; no “all tenses” claim without coverage |
| EN-10 | Which verbs take V-ing or to + verb? | `#verbs` | Listed high-frequency patterns and examples; meaning-changing cases labeled if included |
| EN-11 | Which preposition expresses time or place? | `#preps` | in/on/at contrasts with examples and essential exceptions |
| EN-12 | Which dependent preposition follows a word? | `#preps` | All listed combinations with examples; no claim of an exhaustive lexicon |
| EN-13 | How are regular and high-frequency irregular plurals formed? | `#nouns` | Core rules, listed irregulars and countability caveat |
| EN-14 | Is a noun countable, and which quantity word applies? | `#nouns` | much/many/few/little and some/any with Russian-interference traps |
| EN-15 | How are comparative and superlative forms built? | `#nouns` | Core patterns, spelling limits and high-frequency irregulars |
| EN-16 | Which conditional expresses a fact, real future, unreal present or unreal past? | `#conditionals` | Types 0–2 core; Type 3 recognition; meaning and form for every shown type |

## Acceptance and maintenance

- **This page is generated**: `en/ru/index.html` is rendered from
  [`content/decks/en-ru.json`](../../content/decks/en-ru.json) by
  `python3 tools/build_pages.py content/decks/en-ru.json`. Edit the deck, not
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
