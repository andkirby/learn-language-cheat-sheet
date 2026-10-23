# Italian and French for English speakers: research and delivery proposal

Researched: 2026-10-23. Repository baseline: `6d48526`.

Status: **research and proposed plan**, not accepted language scope or an
implementation record. Requested first pairs: `it-en` and `fr-en`.
No decks, registry entries or live pages were added by this research.

## 1. Existing process: documents, not a repo-local skill

No repo-local `SKILL.md` or skill directory was found. A new skill is not
needed to deliver these pairs: the repository already owns the procedure.

| Owner | Use for this work |
| --- | --- |
| [ADD_LANGUAGE](../docs/ADD_LANGUAGE.md) | New-target route, deck authoring, assets, integration and release |
| [SITE_PLAN_GUIDE](../docs/SITE_PLAN_GUIDE.md) | Audience, boundaries, retrieval questions, topic IDs and syllabus mapping |
| [CONTENT_VALIDATION](../docs/CONTENT_VALIDATION.md) | Four content gates and independent linguistic review |
| [ROADMAP](../ROADMAP.md) | Lookup-product boundary and multi-audience source policy |
| [CONTENT_AUDIT](../CONTENT_AUDIT.md) | Open scope questions and later review evidence |
| [Design system](../.design/DESIGN_SYSTEM.md) | Existing shared UI contract |

`de/en/SITE_PLAN.md` and `content/decks/de-en.json` are useful English UI
and authoring examples. German topic coverage is not an Italian/French syllabus.

## 2. Recommendation

Keep the existing mobile grammar-reference product: English explanations,
target-language examples with English meaning support, offline use, concise
cards and deeper dialogs. Research scope and levels before writing either deck.

Proposed defaults: contemporary standard Italian; contemporary standard French
as commonly taught in France, with relevant register/variety labels. Use plain
English explanations. Teach the contrasts an English speaker needs to make.
These are recommendations to settle in the two language plans.

Add only `it/en/` and `fr/en/`. Italian and French do not become explanation
locales in this phase. No reciprocal pairs, audio, course sequence or practice
redesign are needed. Reuse the current generator and components; no invariant
core extraction is justified by these two first-audience decks.

## 3. Source register and research method

All sources below were accessed on 2026-10-23. Use sources to verify facts and
coverage; write original explanations, examples and glosses.

| Ref | Primary source and inspected location | Role and limitation |
| --- | --- | --- |
| I1 | Università per Stranieri di Siena, [Linee guida CILS](https://cils.unistrasi.it/1/6/12/Le_Linee_Guida_CILS.htm), [linked PDF](https://cils.unistrasi.it/public/articoli/12/linee_guida_cils_pdf%282%29.pdf), printed/PDF pp. 22, 26, 29; comparison with B2 p. 32 | Italian baseline; distinguish receptive from productive expectations at A1/A2. It is an exam syllabus, not our product scope. |
| I2 | Università di Urbino, [Italiano B1, Federica Rusciadelli](https://cla.uniurb.it/documenti/schede_corsi_cla/2026/Isem/Italiano_B1_Rusciadelli.pdf), p. 1, “Elementi grammaticali” | Second syllabus for borderline items; includes future, progressive, pluperfect, pronoun combinations and subjunctive work. A course specification, not a universal CEFR allocation. |
| I3 | Treccani, *La grammatica italiana* (2012), [Articoli](https://www.treccani.it/enciclopedia/articoli_%28La-grammatica-italiana%29/), definite/indefinite sections | Grammar accuracy reference sampled for article choice and agreement; no independent CEFR placement. |
| I4 | Mario Squartini, Treccani, *Enciclopedia dell’Italiano* (2010), [Indicativo](https://www.treccani.it/enciclopedia/indicativo_%28Enciclopedia-dell%27Italiano%29/), “Funzioni aspettuali” | Past-tense contrast; useful check against misleading English tense equivalences. |
| I5 | Treccani, *La grammatica italiana* (2012), [Congiuntivo](https://www.treccani.it/enciclopedia/congiuntivo_%28La-grammatica-italiana%29/), subordinate uses; Rai Scuola, [Tutto sul congiuntivo](https://www.raiscuola.rai.it/italianoperstranieri/articoli/2021/06/Le-parole-dellItaliano-tutto-sul-congiuntivo-2c3e95f5-3fa7-48a6-b4dc-a6ffe1de2896.html), “Unità 10 – Livello B1” | Grammar reference plus independent teaching-level evidence for a bounded introduction. |
| F1 | Eaquals/CIEP, [Inventaire linguistique des contenus clés des niveaux du CECRL](https://www.eaquals.org/wp-content/uploads/Inventaire_ONLINE_full-1.pdf), ©2015; introduction pp. 4–5, Annex E pp. 56–59 (one-based PDF pp. 58–61) | French coverage/level baseline. Publisher-hosted PDF was accessible; direct FEI document requests returned ERR-BOT-403. This is guidance, not a mandated DELF grammar checklist. |
| F2 | University of Texas at Austin, [Tex’s French Grammar index](https://laits.utexas.edu/tex/gr/index.html) and [overview](https://laits.utexas.edu/tex/gr/overview.html) | English-explained grammar reference; index checked for coverage, not a full linguistic review. Broader than our intended scope. |
| F3 | UT Austin, [Narration: passé composé vs. imparfait](https://www.laits.utexas.edu/tex/gr/tap8.html), tense contrast and context caveat | Sampled teaching/accuracy reference for a high-risk contrast. |
| F4 | UT Austin, [Direct object pronouns](https://www.laits.utexas.edu/tex/gr/pro5.html), placement; [Basic negation](https://www.laits.utexas.edu/tex/gr/neg2.html), negation and register | Sampled English-audience explanation references; further topic-specific reference checks remain necessary. |
| C1 | Council of Europe, [Reference Level Descriptions](https://www.coe.int/en/web/common-european-framework-reference-languages/reference-level-descriptions) | Explains language-specific descriptions and the status of simplified inventories. |

Important findings:

- Italian syllabi differ: CILS adult B1 is narrower than Urbino’s B1 course
  for some verb topics. Rai also explicitly teaches present subjunctive at B1.
  Recommend a bounded present-subjunctive introduction; keep the full system
  deferred. Do not label all subjunctive use B2 by assumption. [I1, I2, I5]
- For French, assess bounded subjunctive, pluperfect, pronoun order and
  participle agreement explicitly instead of silently dropping them. [F1, F2]
- In both languages, English tense names are unreliable shortcuts. Explain
  the intended situation and show contrasting contexts. [I4, F3]

Systematic authoring method:

1. Extract each baseline’s grammar checklist, retaining its level and
   receptive/productive distinctions.
2. Map every checklist item to a proposed topic or an explicit deferral or
   exclusion. Add an English-interference rationale and a retrieval question.
3. Resolve source disagreements by choosing and documenting the intended
   depth; a source omission alone does not establish a topic’s level.
4. For each accepted topic, attach a grammar reference at section/page level,
   a normal-case probe and a counterexample to any simplification.
5. Author original card/dialog content, then have a separate linguistic
   reviewer inspect all units, tables, examples and translations.

The inventories below are candidate outlines. Full item-by-item syllabus
mapping and individual level assignments are **NOT RUN**, so baseline
completeness is not claimed.

## 4. Proposed content outline

Use four views, provisionally `forms`, `verbs`, `sentences`, `connections`.
These fit the existing generator’s three-to-five-view contract. Finalize
topic IDs and section/card anchors when accepting each plan; preserve them
after publication. IDs below are proposed, not already reserved in a deck.

Depth policy: first-layer cards show the decision trigger, essential form,
glossed example and any limit needed to prevent a false rule. Dialogs contain
contrast pairs and bounded exceptions. Do not force a fixed card count if a
topic needs splitting to satisfy that contract.

### Italian: proposed 30 units

Primary learner questions: Which ending/article? Which present or past form?
Where does the pronoun go? Which preposition? How do I ask, negate or request?
How do I connect clauses?

| Proposed IDs | View | Candidate units | English-audience emphasis |
| --- | --- | --- | --- |
| IT-01–03 | forms | Gender/plural; definite articles; indefinite/partitive articles | Learn nouns with gender; avoid one-to-one mapping to English articles |
| IT-04–06 | forms | Possessives; demonstratives; adjective agreement/position | Possessor versus possessed noun; visible limits on position shortcuts |
| IT-07–08 | forms | Comparison; quantifiers/indefinites | Bounded irregular forms and common function words |
| IT-09–10 | verbs | Present patterns/essential irregulars; subject omission and tu/Lei | English subject habits; respectful address |
| IT-11–13 | verbs | Reflexives; modals/infinitives; piacere-type construction | Verb patterns rather than word-for-word English syntax |
| IT-14–16 | verbs | Passato prossimo; imperfetto; past-tense choice | Auxiliary/agreement decisions; event versus background |
| IT-17–19 | verbs | Future reference; present conditional; imperative | Contrast present/future choices; requests, advice and negative commands |
| IT-20 | verbs | Bounded present subjunctive | Frequent triggers and same-subject infinitive alternative |
| IT-21–23 | sentences | Questions/negation; direct objects; indirect objects | No English do-support; pronoun position |
| IT-24–25 | sentences | ci; ne | Separate units; bounded functions, not fixed English equivalents |
| IT-26–28 | connections | Simple/articulated prepositions; time/place expressions; relatives | Retrieval by intended relationship; che versus preposition + cui |
| IT-29–30 | connections | Core connectors; impersonal si | Cause/contrast/purpose; impersonal versus reflexive use |

I1 is the initial baseline for the foundational units. I2 supplements the
verb-pattern, particle and clause candidates; I3/I4/I5 are sampled accuracy
references. These references do not yet establish every row’s final depth.

Explicit decisions still needed during baseline mapping:

- Pluperfect, double pronouns, adverb formation, numbers/date/time grammar:
  assess bounded units against I2 and the complete I1 checklist; do not lose
  them because the initial outline has 30 slots.
- Recommend deferring full subjunctive tense sequencing, hypothetical
  multi-tense systems and an inventory of idiomatic pronominal verbs. Reopen
  when a concrete retrieval need justifies separate units.
- Recommend deferring a full passato-remoto paradigm. Any recognition note
  must acknowledge contemporary regional usage; do not call it solely literary.

### French: proposed 30 units

Primary learner questions: Which determiner/agreement? Which present or past
form? Where do objects go? How do I ask/negate? Which time/place expression?
How do I express a condition or link a clause?

| Proposed IDs | View | Candidate units | English-audience emphasis |
| --- | --- | --- | --- |
| FR-01–03 | forms | Gender/plural; definite/indefinite articles; partitives/quantity | Agreement and article choices absent from English |
| FR-04–06 | forms | Possessives/demonstratives; adjective agreement/position; comparison | Agreement follows the noun; position shortcuts need limits |
| FR-07–09 | verbs | Present/essential irregulars; subject pronouns/on/tu/vous; reflexives | Required subjects and formal/plural address |
| FR-10–12 | verbs | Passé composé; imparfait; past-tense choice | Auxiliary/agreement decisions; avoid English present-perfect equivalence |
| FR-13–15 | verbs | Future reference; present conditional; imperative | Present/near/simple-future contrast; polite requests; object placement |
| FR-16 | verbs | Bounded present subjunctive | Frequent obligation/emotion triggers; explicit indicative contrast |
| FR-17–19 | sentences | Questions; negation; c’est/il est/il y a | No do-support; label spoken ne-omission; separate introducing/describing |
| FR-20–23 | sentences | Direct objects; indirect objects; y; en | Position before the verb and clearly bounded replacement functions |
| FR-24 | sentences | Common double-pronoun order | One decision table; imperative exceptions kept visible |
| FR-25–27 | connections | Place/article contractions; duration/time; relative pronouns | depuis versus English “for”; qui/que/où/dont |
| FR-28–30 | connections | Real/unreal conditions; core connectors; verb + preposition/infinitive | Bounded si patterns; meaning before English word matching |

F1 supplies level-oriented candidates; F2 supplies the broader reference
checklist. F3/F4 are sampled accuracy references. Full source-to-topic mapping
still needs to separate subtopics inside the grouped units.

Explicit decisions still needed during baseline mapping:

- Pluperfect, past-participle agreement with preceding objects, passive,
  gerund, possessive/demonstrative pronouns, indefinites and adverbs: decide
  individual coverage/depth or a documented deferral. Some can extend an
  existing unit; none should disappear silently. [F1, F2]
- Recommend deferring full reported-speech backshift, past conditional and
  complex relative systems; reconsider when a bounded retrieval need appears.
- Recommend excluding productive literary-tense paradigms from this release;
  decide recognition coverage separately. This remains a selective lookup deck.

For both pairs, open vocabulary lists, audio and a general pronunciation course
remain proposed exclusions. Orthography that determines a grammatical form
(elision, apostrophe, accents) stays with the affected unit. Reopen wider
categories only when the product boundary changes.

## 5. Verified implementation implications

| Area | Finding and planned action |
| --- | --- |
| Generator | Metadata and `site.json` already drive arbitrary target/audience pairs. No replacement architecture needed. |
| New source/output | Create `content/decks/it-en.json`, `content/decks/fr-en.json`; plans and generated pages under `it/en/` and `fr/en/`. |
| English scaffold | Reuse the English UI wording pattern from `de-en`; replace target content, metadata and search hints deliberately. `meta.lang=en`; `meta.target_lang=it` or `fr`. |
| Project menu string | Since commit `05eed47`, every deck must include `strings.menu_issue`; both new English-audience decks use `"Submit issue"`. The existing renderer supplies the GitHub/issue links in both menu variants; no pair-specific menu implementation is needed. |
| Registry | Add `it`/`Italiano` and `fr`/`Français`, each with English audience and `script: latin`. Register only terminology actually needed by authored cards. |
| Landing | Update cards, target-menu markup and `DECKS`. Add IT/FR card copy in **every existing LANDING locale**: `applyLocale` reads copy even for hidden cards. Update titles/descriptions that currently enumerate only German/English. |
| Pair filtering | English locale becomes DE/IT/FR; Russian remains DE/EN; German remains EN. Do not route RU/DE users silently to English explanations. |
| Existing pages | Regenerate all four existing pages after the registry edit, as well as the two new pages: their menus use the same registry. |
| Icons | `FONT` currently contains A/D/E/N/a only. In-memory probes for IT/FR fail with KeyError. Add I/T/F/R glyphs, generate both pair-local PNG sets and author their favicon SVGs. |
| Manifests | Author pair-local manifests with English names/descriptions and `lang: en`, relative start/scope/icons. The page generator does not create these or the SVG favicon. |
| Typography | Existing Latin unicode ranges include common Italian/French accents and Œ/œ. Verify both skins visually; no additional font downloads are indicated by the inspected CSS. |
| Search | Runtime currently lowercases and performs literal matching; it does not fold accents. Use English intent terms and real target terms. Do not promise accentless French search. Any normalization change would touch all decks and require a separate shared-contract decision. |
| Validator | Latin audiences use strict search hygiene and explicit target-text markup. Check accented/elided text and ligatures: the token regex is not a general Unicode word matcher. A failing real content case should drive any bounded fix. |
| Offline | Add each page URL, index, manifest, favicon and PNG assets to APP_SHELL; bump CACHE_VERSION. One broken precache URL can prevent the whole new worker installing. |
| Documentation | Update README URLs, AGENTS inventory/routing, CHANGELOG and accepted-plan links. Log any actual shared-UI contract change in `.design/decisions.md`. |

Two playbook command details need correction when implementation updates the
procedure: its `de-*.json`/`en-*.json` loop omits new targets; its `*.json`
loop also selects `schema.json` and `site.json`. Use `*-*.json` for current
deck filenames. `--check-shell` does not prove localized copy/menu completeness
or HTTP asset success; keep those verification steps.

## 6. Delivery sequence and exit criteria

1. **Resolve content scope for both pairs.** Complete the source checklist
   mappings and borderline decisions above. Record open questions in
   CONTENT_AUDIT; promote settled scope to `it/en/SITE_PLAN.md` and
   `fr/en/SITE_PLAN.md` before authoring JSON. Each required unit needs a
   learner question, level/depth, surface and acceptance criteria. Deferred
   and excluded items need rationale and a reconsideration trigger.
2. **Author Italian, then French.** The order follows the requested pair
   order, not a linguistic dependency. Work in small view/topic groups;
   validate each deck structurally. Keep unready pairs out of published
   navigation. Registry edits for local rendering can remain uncommitted
   until the corresponding assets and review are ready.
3. **Review content independently.** For each deck, inspect all cards,
   dialogs, tables, formulas and English glosses. Record exact revision,
   sources, reviewer, probes, findings and all four gates in CONTENT_AUDIT.
   Partial inspection cannot produce a full-gate PASS.
4. **Integrate the completed pair(s).** Add the icon glyphs/assets,
   manifests, landing and registry updates; regenerate every live deck;
   update the worker and owner documents. A pair can ship separately if
   only its own complete integration is exposed.
5. **Verify runtime and release.** Run structural checks, then the AGENTS
   runtime checklist for new and affected existing pages. Publish only
   after content and runtime gates pass; follow the authorized release
   process and verify the deployed subpath URLs.

Implementation-time commands, after the planned files exist:

```bash
python3 tools/make_icons.py --mark IT --out it/en
python3 tools/make_icons.py --mark FR --out fr/en

for deck in content/decks/*-*.json; do
  python3 tools/build_pages.py "$deck" || exit 1
  python3 tools/build_pages.py "$deck" --check || exit 1
done
python3 tools/build_pages.py content/decks/de-ru.json --check-shell
python3 tools/build_pages.py content/decks/de-ru.json --check-siblings
```

Sibling checks protect the existing DE/EN pairs; they do not validate Italian
against French or certify either new deck’s grammar.

Runtime priorities: all six deck menus; locale filtering/persistence; 390px
overflow; both skins and all theme modes; English/target-term search; dialog
controls and anchors; manifests/icons; clean console; offline reload under
the GitHub Pages subpath. Follow AGENTS browser/server cleanup requirements.

## 7. Evidence from this research session

- Four existing deck `--check` commands: **PASS**.
- Existing `--check-shell`: **PASS**.
- Missing icon letters: reproduced without writing generated assets.
- Current generator, landing, service worker, font ranges and strict-search
  behavior: inspected statically; source/reference samples fetched live.
- New IT/FR Baseline, Coverage, Accuracy and Teaching gates: **NOT RUN**.
- Browser, offline, installed-PWA and deployed-page verification: **NOT RUN**.

Only this research document is added. Existing dirty AGENTS.md, `.mcp.json`,
`designs/` and `research/lovable-approach.md` were preserved. The next concrete
deliverables are the two sourced, decision-sufficient language plans.

## Implementation handoff — 2026-10-23

The owner subsequently authorized implementation using the language agents'
recommended bounded scope. Accepted targets now live in
[Italian SITE_PLAN](../it/en/SITE_PLAN.md) and
[French SITE_PLAN](../fr/en/SITE_PLAN.md); detailed language research is in
[it-en-plan.md](it-en-plan.md) and [fr-en-plan.md](fr-en-plan.md).
The preceding investigation remains a record of its stated baseline, not a
current feature-status matrix. Missing glyphs, registry/landing integration,
menu strings and explicit target-run handling have been addressed in the
implementation. Current content findings/gates belong only in
[CONTENT_AUDIT](../CONTENT_AUDIT.md), and runtime results in
[UI_AUDIT](../UI_AUDIT.md). Implementation does not imply content acceptance.
