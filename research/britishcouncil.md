# RESEARCH: British Council LearnEnglish — English grammar reference

English-side counterpart to [`research/hobbydeutsch.md`](hobbydeutsch.md):
reference notes on how a well-regarded, CEFR-organized English grammar
resource structures its material, gathered 2026-09-11 as input for calibrating
our `en/ru` deck (topic inventory, depth per level, lesson shape). British
Council content is authoritative and edited — unlike the hobbydeutsch series
it can be trusted for paradigms and examples, but it is still an external
source: explain/verify, don't copy wholesale (and it is © British Council).

## What this site is

[learnenglish.britishcouncil.org](https://learnenglish.britishcouncil.org)
is the British Council's free learner site. Its grammar area has four
sections:

| Section | Shape | Scope vs ours |
| --- | --- | --- |
| **A1–A2 grammar** | 18 self-contained lessons | fully in our scope |
| **B1–B2 grammar** | 36 lessons | B1 half in scope; B2 half useful for stretch topics |
| **C1 grammar** | further lessons | out of scope |
| **English grammar reference** | 7 word-class hubs (reference, not lessons) | complementary, not level-organized |

Key structural difference from the German reference: levels are **grouped in
pairs** (A1+A2, B1+B2) rather than one section per CEFR level — individual
lesson pages carry the precise level tags ("A1 Elementary, A2
Pre-intermediate").

Access note: the site sits behind Akamai, which 403s/tar-pits plain `curl`
(even with browser headers and HTTP/1.1). Content was gathered through the
session's web-reader MCP and WebFetch digests instead — see
[Re-gathering](#re-gathering).

## Lesson template (from sampled pages)

Every lesson follows the same fixed template — this is the site's core
pedagogical pattern:

1. **Title + hook**: one question ("Do you know how to use the passive…?")
   followed by ~4 sample sentences.
2. **Grammar test 1** — a multiple-choice exercise *before* any teaching
   (diagnostic; loads from an external quiz service, not visible in HTML).
3. **Grammar explanation** — short paragraphs mixing *why* (usage, focus,
   register) with *how* (formula + examples).
4. **Grammar test 2** — same format, after teaching.
5. **Level tags + star rating** (e.g. "B1/B2, 4.1 from 194 votes").
6. **Comments** — learners post practice sentences, the BC team replies;
   long-lived lessons have 20+ pages of comments.

Explanation characteristics (sampled "Present simple: 'to be'" at A1 and
"Passives" at B1/B2):

- **Tables appear even at A1**: the *be* lesson opens its explanation with
  an Affirmative / Negative / Question three-column conjugation table
  ("I am / I am not / Am I?"); the passive lesson closes with a 7-row
  tense table where each row shows one example sentence plus its
  structural pattern ("is/are + past participle").
- **Example volume is moderate**: ~25–30 examples on the A1 *be* lesson,
  ~15 on the B1 passive lesson, always translated by context (English
  monolingual — no L1 glosses).
- **Usage notes are embedded as small rules with personality**: "I amn't"
  is impossible; contractions appear in negative short answers only;
  passive = focus shift ("My bike was stolen" — focus on my bike).
- Minimal-prose, maximum-pattern style: rules are one or two sentences,
  then examples carry the rest.

## A1–A2 grammar: topic inventory (18 lessons)

Inventory is the calibration value here; one-line notes only where the
title needs it:

1. Present simple: 'to be' — incl. contractions, short answers
2. Present simple — main verb paradigms
3. Present simple: 'have got'
4. Question forms — word order, do-support
5. Using 'there is' and 'there are'
6. Nouns: countable and uncountable
7. Articles: 'a', 'an', 'the'
8. Articles: 'the' or no article — second dedicated lesson
9. Possessive 's
10. Prepositions of place: 'in', 'on', 'at'
11. Prepositions of time: 'at', 'in', 'on'
12. Adjectives and prepositions (tired *of*, interested *in*)
13. Adjectives ending in '-ed' and '-ing' (bored/boring)
14. Comparative adjectives
15. Quantifiers: 'few', 'a few', 'little', 'a bit of'
16. Past continuous and past simple — the only past-tense lesson here
17. Infinitive of purpose (I went there *to study*)
18. Verbs followed by '-ing' or infinitive (enjoy doing / want to do)

Shape: a heavy cluster of "present + noun phrase basics", articles given
**two** lessons, prepositions split by place/time, and exactly one
past-tense lesson. Notable gaps vs a typical A1–A2 syllabus: no plural
nouns lesson, no imperatives, no possessive adjectives lesson (those live
in the word-class reference instead), no future forms at all.

## B1–B2 grammar: topic inventory (36 lessons)

Grouped thematically (raw flat list would hide the shape):

- **Tense/aspect core (9)**: present perfect; present perfect simple vs
  continuous; present perfect with just/yet/still/already; past perfect;
  past habits (used to/would/past simple); different uses of 'used to';
  past ability (could/was able to); future forms (will / be going to /
  present continuous); future continuous and future perfect; plus "the
  future: degrees of certainty" and stative verbs.
- **Modality (4)**: permission and obligation; deductions about the
  present (must/might/can't be); deductions about the past (must have…);
  (past ability above overlaps).
- **Conditionals (2)**: zero/first/second; third and mixed.
- **Reported speech (3)**: statements; questions; reporting verbs.
- **Relative clauses (2)**: defining; non-defining.
- **Connectors/discourse (3)**: although/despite/in spite of; as vs like;
  intensifiers so/such.
- **Verb patterns (3)**: verbs + -ing or infinitive *with meaning change*
  (stop doing vs stop to do); verbs and prepositions; phrasal verbs.
- **Comparison (2)**: modifying comparatives (much bigger, far better);
  using 'enough'.
- **Miscellaneous (5)**: passives; question tags; reflexive pronouns;
  gradable vs non-gradable adjectives; capital letters and apostrophes;
  British vs American English.

Shape: the center of gravity is **perfect aspect, modality, conditionals,
reported speech** — exactly the B1 grammar core. Register/orthography
topics (capitals, BrE/AmE) sit alongside syntax topics, which matches how
a B1 exam treats them.

## English grammar reference (word-class hubs)

A separate, non-leveled reference organized by word class: **Pronouns,
Determiners and quantifiers, Possessives, Adjectives, Adverbials, Nouns,
Verbs** — each hub is an index of short reference pages.

The Verbs hub (enumerated, 20 sub-pages) mirrors a full pedagogical verb
grammar: verb phrases; irregular verbs; questions and negatives; short
forms; the verb 'be'; present tense; past tense; perfect aspect;
continuous aspect; modal verbs; active and passive voice; to-infinitives;
-ing forms; talking about the present/past/future; verbs in time clauses
and if-clauses; wishes and hypotheses; clause structure and verb
patterns; delexical verbs (have/take/make/give/go/do).

Value: this is the "arranged by linguistic category" mirror of the
level-arranged lessons — same grammar reachable two ways. Our deck is
level/topic-arranged like the lessons; the hub list is a useful checklist
for reference-coverage gaps (e.g. delexical verbs is a topic neither our
inventory nor the level lessons highlight).

## Reliability

- Edited, authoritative, no language errors observed in sampled pages
  (contrast the hobbydeutsch series).
- Quality signals are public: star ratings (~4.1/5), active moderated
  comments where the BC team corrects learners' sentences — useful for
  us as a source of FAQ-style confusion points per topic.
- BrE default; AmE treated as an explicit lesson topic rather than an
  afterthought.
- One structural inconsistency: lesson URL slugs are mixed legacy patterns
  (`/a1-a2/<slug>` vs `/a1-a2-grammar/<slug>`) — old links survive.

## Ideas worth considering for our en/ru content

- **Coverage cross-check against our topic inventory**: articles as *two*
  separate lessons (zero article split out) and the quantifier set
  (few/a few/little/a bit of) as its own lesson suggest finer splitting
  than a generic "articles"/"quantifiers" card; question tags, stative
  verbs, as/like and enough are B1 staples we should consciously include
  or exclude.
- **Test-before/test-after**: the diagnostic-then-teach pattern maps
  naturally onto our practice view (attempt first, reveal explanation),
  no new mechanics needed.
- **Table shapes to steal**: the Affirmative/Negative/Question
  three-column conjugation layout is compact enough for our card tables;
  the passive tense table's "example + structural pattern per row" is a
  good dialog format.
- **Micro-rules as dialog content**: "I amn't is impossible", contraction
  restrictions in short answers, "My bike was stolen = focus on the bike"
  — the kind of one-liner notes that fit our DETAILS dialogs.
- **What does not transfer**: monolingual English-only explanations (our
  audience needs Russian L1 support — the whole point of en/ru), the
  external multiple-choice test applet, and per-lesson comment threads.

## Cross-reference with the German research

| | hobbydeutsch.de (DE) | British Council (EN) |
| --- | --- | --- |
| Unit | 15 multi-topic "cheat sheet" articles | 54 single-topic lessons + word-class reference |
| Level model | one page series per level (A1–B2) | paired levels (A1-A2, B1-B2, C1) |
| Vehicle | tables inside long SEO articles | short lesson + pre/post quiz |
| Examples | EN glosses for German | monolingual English |
| Quality | degrades with level, typos in paradigms | edited, consistent |
| Funnel | links to own games/quizzes | built-in tests before/after |

Both converge on the same lesson shape we already chose: compact card +
explanation-on-demand + practice — good sign for our model.

## Re-gathering

- `curl` fails (Akamai 403, then connection tarpit even with browser UA +
  HTTP/1.1). Use the session's web-reader MCP (`webReader`) for full
  pages or WebFetch for digests; both reach the site.
- Section URLs: `/free-resources/grammar/a1-a2`, `/free-resources/grammar/b1-b2`,
  `/free-resources/grammar/c1`,
  `/free-resources/grammar/english-grammar-reference`.
- Lesson URLs: `/free-resources/grammar/a1-a2/<slug>` (e.g.
  `present-simple-be`) with some legacy slugs under `a1-a2-grammar/`
  (e.g. `articles-a-an-the`); B1-B2 same pattern (e.g. `…/b1-b2/passives`).
- Not yet enumerated (only needed if we go deeper): sub-topics of the six
  non-Verb word-class hubs, C1 lessons, individual quiz contents (they
  load from an external service and are not in the page HTML).
