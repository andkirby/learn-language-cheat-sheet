# RESEARCH: hobbydeutsch.de grammar cheat-sheet series

Reference notes on the external cheat-sheet article series at
[hobbydeutsch.de](https://hobbydeutsch.de/), gathered 2026-09-11 as input for
our own German content work (topic inventory, depth calibration, table shapes).
This is **explanatory research, not source material**: the site is a
secondary, non-authoritative source with recurring language errors — do not
copy content from it without independent verification.

- Scope: all 15 "grammar cheat sheet" articles (A1 ×2, A2 ×4, B1 ×4, B2 ×5).
- Method: the site is a client-side SPA; article bodies live in per-page JS
  chunks. Pages were recovered from the router bundle and lazy chunks and
  reduced to outlines (headings + tables + lists). See
  [Re-gathering](#re-gathering) for the recipe.

## Series overview

| Page (slug under `/articles/`) | Level | Author | Core topics |
| --- | --- | --- | --- |
| `grammar-cheat-sheet-a1-part-1` | A1 | Damiya | pronouns (personal/reflexive/interrogative), gender articles, numbers, days, months |
| `grammar-cheat-sheet-a1-part-2` | A1 | Damiya | present-tense conjugation, modal verbs, simple sentences & questions, nicht/kein, possessives, prepositions (acc/dat/two-way), adjective endings |
| `German-Grammar-A2-Cheat-Sheet` | A2 | Gemma C | vocabulary & phrase upgrading, article/case tables, strong vs weak adjective endings, exam prep |
| `German-Grammar-A2-Cheat-Sheet-Part-2` | A2 | Gemma C | separable/inseparable verbs, modal verbs, reflexive verbs, two-way prepositions |
| `German-Grammar-A2-Cheat-Sheet-Part-3` | A2 | Gemma C | subordinate clauses, past tenses (Präteritum/Perfekt/Plusquamperfekt), comparatives, possessive pronouns, coordinating conjunctions, negation, indirect questions |
| `German-Grammar-A2-Cheat-Sheet-Part-4` | A2 | Gemma C | relative clauses, time expressions (am/im/um/seit/vor/nach), quantity words (viel/viele), imperatives |
| `German-Grammar-B1-Cheat-Sheet-Part-1` | B1 | Gemma C | Konjunktiv I & II, passive voice, indirect speech, Future I/II, genitive case, prepositions by case |
| `German-Grammar-B1-Cheat-Sheet-Part-2` | B1 | Gemma C | dependent clauses, relative clauses with prepositions, subordinate word order, zu/um…zu infinitives, modal verbs in the subjunctive, reflexives in complex sentences |
| `German-Grammar-B1-Cheat-Sheet-Part-3` | B1 | Gemma C | lassen (passive/causative), comparative adjective endings, clock time (halb/viertel), phrasal verbs & idioms, participles as adjectives, nominalization |
| `German-Grammar-B1-Cheat-Sheet-Part-4` | B1 | Gemma C | advanced negation (nie/niemand/nirgendwo), participle clauses, purpose clauses, verbs with fixed prepositions |
| `German-Grammar-B2-Cheat-Sheet-Part-1` | B2 | Gemma C | complex sentence structures, causal/conditional/concessive clauses, extended subordinating conjunctions, indirect questions, reported speech, advanced passive |
| `German-Grammar-B2-Cheat-Sheet-Part-2` | B2 | Gemma C | participle constructions, nominalization, advanced phrasal verbs & idioms, word order, double negatives, relative clauses with prepositional phrases |
| `German-Grammar-B2-Cheat-Sheet-Part-3` | B2 | Gemma C | reflexive verbs with prepositions, advanced Konjunktiv II, infinitives without zu, causative constructions, connectives, modal particles |
| `German-Grammar-B2-Cheat-Sheet-Part-4` | B2 | Gemma C | nuanced time expressions, temporal clauses, dialects, technical German, rhetorical devices, culture & idioms, du/Sie/ihr |
| `German-Grammar-B2-Cheat-Sheet-Part-5` | B2 | Gemma C | purpose/reason clauses (um…zu/damit/double infinitives), comparatives in complex sentences, conditionals & wishes, genitive in formal writing |

Discovery note: only the first 8 pages are in the site's `sitemap.xml`; the
B1 parts 3–4 and all five B2 parts exist only in the client-side router.
B2 content drifts from pure grammar into culture/dialect/rhetoric territory.

## Shared template and pedagogy

Every page follows the same article template, which explains what a "cheat
sheet" means on this site — it is an SEO long-read with tables, not a
compact reference card:

1. Hero image (canva.com stock), title, "Table of content" anchor box.
2. Level introduction (what the CEFR level means, word-count targets:
   ~1300 words for A2, ~2400 for B1), a "why use a cheat sheet" pitch.
3. Grammar body: `h2` topics → `h3` subtopics, with **tables as the main
   vehicle**; short paragraphs of rule prose between them.
4. Frequent inline links to the site's own interactive exercises, quizzes
   and games ("complete the grammar exercise here") — the articles exist
   substantially to funnel readers into those tools.
5. Closing encouragement, author byline (Damiya for A1, Gemma C for A2–B2).

Other cross-cutting traits:

- **Explanations are in English**, with German always glossed in English.
  A2 part 1 and later pages carry a "Please login to read full article"
  gate line, but the full content is present in the page bundle regardless.
- Tables come in a few recurring shapes (see per-page notes): paradigm
  tables (pronoun × case), EN↔DE example-pair tables, preposition tables
  with example sentences, and vocab-upgrade tables (basic word → richer
  alternatives).
- Quality declines with level: A1/A2 tables are mostly sound, while B1/B2
  prose contains noticeable typos and at least one malformed paradigm (see
  [Reliability](#reliability)).

## Per-page summaries

### A1 Part 1 — `grammar-cheat-sheet-a1-part-1`

The URL the research started from. Structure: CEFR/A1 intro, "why use a
cheat sheet" bullets, then seven lookup tables, then study tips.

- Personal pronouns: ich/du/er… across nominative, accusative, dative with
  English glosses — the standard 9-row paradigm. Solid.
- Reflexive pronouns: nominative vs accusative vs dative (mich/mir,
  dich/dir, sich…). Redundant with the first table but framed for
  reflexive use.
- Interrogative pronouns: only wer/wen/wem/wessen by case — 4 rows.
- Gender articles: der/die/das + ein/eine and "no plural indefinite" —
  a 4-row orientation table, not a declension.
- **Numbers block (the "number examples" on this page)**: a two-column-pair
  table covering 0–13, teens, 20/21/22, 50, 100, 200, 1000 — each numeral
  with its German word plus an *approximate English phonetic spelling*
  ("eins (ayns)", "zwölf (tsverlf)"). Nutshell: survival-numeral lookup for
  English speakers, chosen to demonstrate the einundzwanzig building
  pattern rather than to list 0–100. Value: shows the level expectation
  (numerals to ~1000 at A1) and the interesting choice of teaching
  pronunciation inline; for our Russian-speaking audience the phonetics
  column is irrelevant and the pattern demo is the reusable idea.
- Days of the week and months: full 7/12-row EN↔DE tables, again with
  English phonetics, Samstag/Sonnabend doublet included. Value: pure rote
  lookup; tells us this site treats calendar vocab as part of "grammar" at
  A1.
- Closing section is generic study advice (flashcards, consistency).

### A1 Part 2 — `grammar-cheat-sheet-a1-part-2`

The first real grammar-mechanics page; almost entirely tables.

- Conjugation: full paradigm for regular *lernen* and irregular *sein*,
  then a 6-modal × 6-person matrix (kann/muss/darf/soll/will/möchte).
- Simple sentences and questions: small EN↔DE example-pair tables (5 pairs
  each, e.g. "Do you speak German? — Sprichst du Deutsch?"). Nutshell:
  pattern illustrations, not exercise sets. Value: demonstrates word order
  by example only — no rule statement; a card+dialog split (rule in dialog,
  2–3 pairs on card) would carry the same content better.
- Negation: nicht vs kein, each with 5 EN↔DE pairs; the distinction is
  shown purely by examples (verbs/adjectives vs nouns).
- Possessives: *mein* declension only (nom/acc/dat × gender/plural) — a
  deliberate single-model slice of the possessive paradigm.
- Prepositions: accusative (durch/für/gegen/ohne/um) and dative (aus/bei/
  mit/nach/seit/von/zu) lists each with one example sentence per
  preposition; then two-way prepositions as an accusative-example vs
  dative-example paired table (an/auf/hinter/in/neben/über/unter/vor/
  zwischen), which quietly teaches the movement-vs-location rule by
  parallel examples.
- Adjective endings: the weak (definite-article) declension shown through
  one worked phrase (*der gute Mann*) across 4 cases × 4 gender columns,
  with English translations. Value: the "one example word inflected
  through the whole table" pattern is the most reusable idea here.

### A2 Part 1 — `German-Grammar-A2-Cheat-Sheet`

Least table-dense page; half vocabulary coaching, half adjective endings.

- Vocabulary upgrading: two 2-column tables replacing *groß/klein* with
  riesig/gigantisch/massiv/winzig/zierlich and *gut/schlecht* with emotion
  adjectives (glücklich/wütend/verwirrt/aufgeregt/traurig/überrascht).
  Nutshell: "stop using baby words" starter sets. Value: a nice framing
  (word-choice progression by level) that could map to our depth ladder.
- Phrase upgrading: meal verbs (frühstücken, Abendessen kochen), polite
  request formulas, and discourse connectors (auf der anderen Seite, im
  Vergleich…) as short bulleted EN↔DE lists — again pattern demos.
- Grammar core: gender & case explanation, then the full definite- and
  indefinite-article declension tables, followed by **strong vs weak
  adjective endings** as two separate 4×4 suffix tables, with the
  memorable rule of thumb "strong endings ≈ definite article; weak endings
  are only -e/-en". This strong/weak framing is the page's main value.
- Ends with A2 exam structure and preparation tips (listen, read, write).

### A2 Part 2 — `German-Grammar-A2-Cheat-Sheet-Part-2`

- Separable/inseparable verbs: bulleted prefix inventories (separable
  ab-/an-/auf-/aus-/ein-/heim-/her-/heraus-/herein-/herauf-; inseparable
  be-/ent-/emp-/er-/ge-/hinter-/miss-/ver-/zer-), the meaning-change
  effect (rufen → anrufen), and the syntax rule (separable prefix goes to
  sentence end; inseparable never splits), each with one worked example.
- Modal verbs: one-line meaning per modal (können/müssen/dürfen/sollen/
  wollen/mögen) plus sentence-position rules (finite verb second; modal to
  end in subordinate clauses) with a two-level example.
- Reflexive verbs: pronoun list (mich/dich/sich/uns…), three usage rules,
  and wash-dress examples. Contains an error ("Wir interessieren mich").
- Two-way prepositions: the 10-preposition list with English spatial
  glosses (including the useful "an = on a vertical surface, auf = on a
  horizontal surface" nuance) and the explicit accusative=movement /
  dative=location rule with the *Buch auf den/dem Tisch* minimal pair.

### A2 Part 3 — `German-Grammar-A2-Cheat-Sheet-Part-3`

- Subordinate clauses: conjunction inventory (wenn/weil/dass/obwohl/
  während/seitdem) + verb-to-the-end rule + the fronted-clause
  "verb, verb" pattern; examples with English glosses.
- Past tenses: three sub-sections — Präteritum (regular endings pattern,
  note that it is "mainly used in writing", mixed verbs mention), Perfekt
  (haben/sein + ge- participle; sein for movement/condition), and
  Plusquamperfekt (hatte/waren + participle, shown as a full conjugation
  table with *gelernt*). Value: standard three-past-tense slice; the
  "writing vs speech" register note is a good dialog-worthy nuance.
- Comparatives/superlatives: -er / (e)st(en) + am formula, *als* for
  "than", irregulars (gut/viel/gern), and the note that German has no
  "more/most" periphrasis.
- Possessive pronouns: stem table (mein-/dein-/sein-/ihr-… with the
  ihr=her=their and capital-Ihr=formal collisions called out) plus a
  clever suffix-only declension table (just r/e/s/n/m… per case×gender,
  with the "add -e before the letter" rule) — a compact alternative to a
  full 9×4 paradigm. Contains typos ("am moisten").
- Coordinating conjunctions: the ABER-DENN-ODER-SONDERN-UND zero-word-order
  set with an example; negation recap (nicht vs kein + placement rules:
  before adjectives/prepositions, after time adverbs); indirect questions
  (question word or *ob* as subordinator, verb final).

### A2 Part 4 — `German-Grammar-A2-Cheat-Sheet-Part-4`

- Relative clauses: der/die/das pronouns (welcher-variant for repetition
  avoidance), verb-final + comma punctuation, pronoun-adjacent placement;
  one two-sentence→one-sentence merge example.
- Time expressions: five mini-groups (am + days/parts of day, im +
  months/seasons, um + clock times, seit + durations, vor/nach + past/
  subsequent events), each as example phrase lists; in der Nacht exception;
  TeKaMoLo-ish placement note (time before place). Nutshell: preposition-
  selection drill sets rather than a paradigm. Value: the grouping itself
  is the teachable structure.
- Quantity: wenig/weniger/viel/mehr/genug/alle + a dedicated viel vs viele
  explanation (adverb+uncountable vs adjective+countable-plural) with four
  minimal-pair examples — one of the better explanations in the series.
- Imperatives: four forms (du/ihr/Sie/wir), pronoun-dropping rules,
  politeness note (bitte softening; "sounds rude but isn't").

### B1 Part 1 — `German-Grammar-B1-Cheat-Sheet-Part-1`

B1 opens with the classic intermediate jump: subjunctive, passive,
reported speech, future, genitive.

- Konjunktiv II: imperfect→subjunctive table for the six modals + haben +
  sein (hatte→hätte, war→**would-be "Ware" — source error**), plus the
  würde + infinitive escape hatch with the würde-conjugation table and an
  hypothetical example.
- Konjunktiv I: full present-stem paradigm for haben/gehen/sein (sei,
  seist, seien…), framed as journalist/formal reported speech.
- Passive voice: werden vs sein selection rule by tense (sein + worden in
  Perfekt), modal passives (muss gekauft werden), all shown by
  translating the same English sentence pairs.
- Indirect speech: direct vs indirect example pair, reporting-verb list
  (sagt/meint/behauptet/erklärt/erzählt/fragt/berichtet), pronoun +
  tense-shift conversion recipe.
- Future tenses: werden conjugation table, Future I (intent/assumption)
  and Future II (future-perfect, assumption about the past) with examples.
- Genitive: definite/indefinite article table (with keiner for plural),
  possessive pronoun table, des Kindes/Kindes noun-ending explanation,
  and the "names take -s without apostrophe" rule (Pauls Haus).
- Prepositions by case: three tables (accusative bis/gegen/entlang/durch/
  für/ohne/um; dative aus/bei/mit/nach/gegenüber/seit/zu; genitive
  außerhalb/innerhalb/anstatt/trotz/während/wegen) each with English
  glosses and examples, plus zu+zum contraction and the note that some
  genitive prepositions are shifting to dative in speech.

### B1 Part 2 — `German-Grammar-B1-Cheat-Sheet-Part-2`

- Dependent clauses: weil/da (with the fronted-da variant), wenn +
  Konjunktiv past, sodass/so…dasn result clauses — example-pair driven.
- Relative clauses with prepositions: preposition before pronoun
  (*Die Frau, mit der ich gesprochen habe…*), dative agreement.
- Word order in subordinate clauses: conjunction-first and clause-first
  (verb,verb) patterns.
- Infinitive clauses: zu-clauses and um…zu purpose clauses with examples;
  notes on which subject configurations allow them.
- Modal verbs in the subjunctive: the full 6-modal × 6-person
  könnte/müsste/dürfte/sollte/wollte/möchte matrix — the page's one
  hard paradigm.
- Reflexives in complex sentences: accusative vs dative reflexive pronoun
  table (mich/mir, dich/dir…) and meaning-changing pairs
  (sich verstehen ≠ verstehen, sich versprechen ≠ versprechen).

### B1 Part 3 — `German-Grammar-B1-Cheat-Sheet-Part-3`

- lassen: conjugation table (ließ/gelassen) + three uses (es lässt sich
  explain-construction, causative "have something done", past causative).
- Comparative/superlative adjective endings: recap of -er/-sten + am, the
  monosyllabic-umlaut rule (groß→größer), irregulars (gut/viel/gern).
- Advanced clock time: viertel vor/nach, the "halb = half TO the next
  hour" trap (halb sieben = 6:30), minutes vor/nach, von…bis ranges.
  Value: the clearest single treatment of the halb trap; good candidate
  for an explanation dialog in our UI.
- Phrasal verbs: separable-verb framing as "German phrasal verbs"
  (aufstehen, aufhören mit, anfangen mit, auskommen mit) with split
  sentence examples; plus three literal-translation idioms
  (Ich glaub mein Schwein pfeift, Das ist mir Wurst, Das ist nicht mein
  Bier). Nutshell: culture-flavored garnish. Value low for grammar
  reference, some for a fun-facts dialog.
- Participles as adjectives: present participle + -d (entspannendes Bad,
  lächelnde Frau), past participle as adjective (gebrauchtes Auto).
- Nominalization: -ung/-heit/-nis/-schaft suffixes (Backung, Schönheit)
  and the verb→noun register upgrade (Brot backen → das Backen eines
  Brotes). The Backung/Backheit examples are dubious German.

### B1 Part 4 — `German-Grammar-B1-Cheat-Sheet-Part-4`

Shortest page.

- Advanced negation: nie/niemand/nirgendwo added to kein/nicht, one
  example each.
- Participle clauses: past and present participle as reduced subordinate
  clauses (Das Buch gelesen, ging er ins Bett; Kochend hört er Musik),
  register note (literary).
- Clauses of purpose: um…zu vs damit (same-subject constraint) and zum +
  nominalized verb (zum Laufen).
- **Verbs with fixed prepositions**: the page's core is a 12-item list
  (antworten auf +Akk, aufhören mit +Dat, bitten um, danken für, denken
  an, entschuldigen für, glauben an, helfen bei/mit, sprechen mit, warten
  auf, sich engagieren für, träumen von). Nutshell: a memorization
  checklist with case labels rather than examples. Value: confirms that
  verbs-with-prepositions is a B1 staple and that case labeling belongs
  on the card; this is exactly the block type our deck's
  verbs-mit-prepositions cards already cover more thoroughly.

### B2 Part 1 — `German-Grammar-B2-Cheat-Sheet-Part-1`

- Advanced sentence structures: multi-level clause nesting (obwohl-
  fronted example; a nested relative-in-relative example that itself
  contains an error — the verb *liest* is missing).
- Complex subordinate clauses by function: causal (weil), conditional
  (wenn × real / unreal-present / unreal-past — a clean three-row
  progression), concessive (obwohl).
- Extended subordinating conjunctions: a 13-item list (weil, als, damit,
  wenn, um…zu, dass, sodass, seit/seitdem, während, bis, obwohl, sobald,
  solange) with the fronting word-order consequence spelled out.
- Indirect questions: direct→indirect transformations (Wo ist die Küche?
  → Ich frage mich, wo die Küche ist), politeness register motivation.
- Reported speech: Konjunktiv I (sei) with the uncertainty rationale.
- Advanced passive: modal + double infinitive (muss gemäht werden),
  future passive, colloquial second-werden drop.

### B2 Part 2 — `German-Grammar-B2-Cheat-Sheet-Part-2`

- Participle constructions: extendable participial attributes
  (*Die am Laptop arbeitende Frau*) — the genuinely B2 move — and
  ge-/t vs ge-/en participle formation recap.
- Nominalization: suffix recap (-schaft/-ung/-heit/-nis/-keit), das
  Laufen/das Glück/die Arbeit examples, register note (academic,
  journalistic); the promised "compound nominalization" example is
  missing from the page.
- Advanced phrasal verbs + idioms: anfangen mit/aufhören mit/umschalten
  auf; idioms Ich verstehe nur Bahnhof, Eine Extrawurst verlangen, Um den
  heißen Brei herumreden.
- Extended word order: auxiliaries and modals creating two-verb brackets,
  question structure (Haben Sie schon gegessen?), subordinate brackets.
- Double negatives: nicht nichts = affirmative; kein/nicht selection
  framed (roughly) via object presence; examples Du liest das Buch nicht
  vs Ich lese keine Bücher.
- Relative clauses with prepositional phrases: recap + relative pronoun
  declension table including genitive dessen/deren and dative denen.

### B2 Part 3 — `German-Grammar-B2-Cheat-Sheet-Part-3`

- Reflexive verbs with prepositions: a case-labeled list (sich freuen auf
  +Akk, sich konzentrieren auf +Akk, sich freuen über +Akk, …) with
  example sentences and the pronoun-after-verb placement rules.
- Advanced Konjunktiv II: politeness softening (Ich will → Ich hätte
  gerne), past vs non-past, doubt expressions (Ich bezweifle, dass…).
- Infinitive clauses without zu: modal-verb and perception/verbs like
  lernen brackets; the explanation here is muddled (examples partially
  contradict the prose).
- Causative constructions: three lassen forms (Ich lasse Henry gießen /
  Ich lasse gießen / Ich lasse mein Auto reparieren) with a transitivity
  note.
- Complex connectives: dass/opinion frames (Es scheint mir, dass),
  discourse adverbs (plötzlich, immerhin, eben).
- **Modal particles**: ja, doch, schon, eigentlich each explained with a
  mini-example (Doch, ich verstehe!; Eigentlich müsste mein Handy
  funktionieren). Nutshell: first real treatment of Modalpartikeln in the
  series, kept to four particles. Value: topic itself is the takeaway —
  a known hard-for-learners area our plans currently exclude; the
  four-particle slice is a reasonable "minimal viable" scope if ever
  revisited.

### B2 Part 4 — `German-Grammar-B2-Cheat-Sheet-Part-4`

The most off-grammar page; quality noticeably lower.

- Nuanced time expressions: gestern/bald/gleich/jetzt/später/ab und zu
  with example snippets; temporal conjunctions (bevor/seit/während/bis/
  solange/nachdem/sobald).
- Regional variants: Hochdeutsch/Plattdeutsch/Bayerisch/Schwäbisch/
  Mitteldeutsch with a greeting sample each and an unverifiable "54
  dialects" claim.
- Scientific/technical German: separable vs inseparable compound verbs in
  technical registers (ankommen, aufschreiben vs er-/ent-/be-/ge-/ver-).
- Rhetorical devices: alliteration (Milch macht müde Männer munter),
  antithesis, hyperbole, onomatopoeia, personification, comparison,
  rhetorical question — a stylistics taster, not grammar.
- Cultural references: food, festivals, costumes + four idioms (Es ist
  alles in Butter, Den Nagel auf den Kopf treffen, Weggehen wie warme
  Semmeln, Schwein haben).
- Formal vs informal: du/ihr/Sie rules, "default to Sie" advice, Berlin
  du-norm caveat — this last example contains a typo ("bitter" for
  "bitte"). Stray editorial-review fragments are visible in the page
  markup at the end.

### B2 Part 5 — `German-Grammar-B2-Cheat-Sheet-Part-5`

Final page; wraps up with syntax-level topics.

- Purpose/reason clauses, advanced: um…zu same-subject constraint vs
  damit, double-infinitive constructions with modals (muss … gegangen
  sein), zum + nominalized verb.
- Comparative/superlative in complex sentences: so…wie (even) vs als
  (uneven), predicate am größsten vs attributive declension
  (der größere Hund), with a working table of positive/comparative/
  superlative forms.
- Hypotheticals and conditionals: the full wenn matrix (real present,
  unreal present Konjunktiv II, unreal past, wishes with doch nur) —
  cleanest section of the page.
- Genitive in formal writing: meines weißen Hundes double declension,
  name + -s vs von-periphrase alternation (Vaters Haus = das Haus meines
  Vaters). The page ends with leftover proofreader comment fragments
  ("spelling error", "größere"…) — clear sign the article was published
  without cleaning up review markup.

## Reliability

Treat as a secondary source. Errors observed while summarizing (not an
exhaustive proofread):

- B1 p1 Konjunktiv II table: sein → "Ware" (should be wäre); example
  sentence starts "If ich viel Geld hätte".
- A2 p2: "Wir interessieren mich für Bücher" (uns); separable prefix list
  contains "herheraus-" (merged her-/heraus-).
- A2 p3: "am moisten" (meisten), "Einach" (einfach), "spatter" (später),
  "ist dieser Bleistift meiner?" (Ist).
- B1 p2: "He könnte…" (Er), "Er interessiet sich" (interessiert),
  "im hauz" (Haus).
- B2 p1: nested relative example omits the verb (*die das Buch … ist
  meine Mutter*); "Perfekt"/"perkekt"/"Past perfekt" spellings vary
  across pages.
- B2 p4: "Letze nacht", "bitter?" (bitte), lowercase nouns in tables
  (am morgen, im sommer style), dubious "54 dialects" statistic.
- B2 p5: umlauts missing in one table (großere, großste), leftover
  editor-comment fragments published in the page.
- Inconsistent table formatting (header rows not matching column counts)
  in B1 p1's genitive table.

Implication: fine for **topic-inventory and depth calibration**, and for
stealing *structural* ideas (table shapes, rule framings); not fine for
copying paradigms or example sentences without checking.

## Ideas worth considering for our DE content

- Level allocation is conventional (A1 = pronouns/articles/numbers/
  present tense; A2 = past tenses, prepositions, comparatives; B1 =
  Konjunktiv, passive, reported speech, genitive; B2 = particles,
  nominalization, participle attributes) and broadly matches our A1–B1
  scope — useful as a coverage cross-check against our topic inventory.
- Reusable presentation patterns: one worked word inflected through a full
  paradigm (*der gute Mann*); accusative/dative parallel-example columns
  for two-way prepositions; strong ≈ definite article / weak = -e/-en
  rule of thumb; suffix-only declension tables; "stop using baby words"
  vocabulary-upgrade tables; register notes ("Präteritum is mainly
  written") as dialog content.
- The halb-vor/nach clock explanation (A2 p3/B1 p3) and the viel/viele
  minimal pairs (A2 p4) are good models for explanation dialogs.
- What does not transfer: English-audience phonetic columns, SEO filler
  sections (level intros, "why cheat sheets", exam tips), and the
  long-article format itself — our card + DETAILS dialog + practice model
  exists precisely to avoid it.

## Re-gathering

The site is a Vite SPA. To re-collect content after they republish:

1. Article URLs: `https://hobbydeutsch.de/sitemap.xml` (partial — new
   pages may be missing), plus the full route table in the SPA bundle:
   fetch any page, take `assets/index-*.js`, and grep
   `ARTICLES_.*CHEATSHEET:"[^"]*"` for slugs and
   `import\("\./[^"]+"\)` near `Ph(` lazy wrappers for chunk files.
2. Download `https://hobbydeutsch.de/assets/<chunk>.js` per page; article
   JSX (headings/tables/lists as `children:"…"` strings) is inline there.
3. Walk the JSX strings in order to rebuild the outline; nested
   `children` values may be strings, arrays, or nested element calls, and
   strings are single- or double-quoted — a naive regex will silently
   drop tables. (A one-off extractor was written for this pass; it lives
   outside the repo on purpose — no build tooling per hard rule 5.)
