# Content audit record — meaning support in all four pairs (2026-10-20/21)

Historical evidence moved verbatim from the root audit. Current status,
findings ledger and record index: [CONTENT_AUDIT.md](../../CONTENT_AUDIT.md).

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
