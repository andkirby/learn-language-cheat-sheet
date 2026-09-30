# Changelog

One entry per user-visible change, newest first. Entries are written in
English; target-language examples and Russian glosses stay as authored.
UI rationale lives in
`.design/decisions.md`, content review evidence in `CONTENT_AUDIT.md`.
Append the entry in the same commit that ships the change.

## 2026-09-30 (one dialog, one entry button)

- **Cards no longer show a stack of buttons that all open the same
  dialog.** Term inventories (particles, linking adverbs, flavor words,
  linkers, preposition strips, verb+preposition pairs) now render as a
  static `.legend` line — bold term, muted meaning — with a single
  «Разбор…» entry button instead of up to eight duplicate buttons. All
  four language pages affected (16 cards). Side effect: the inventories
  are now visible in print and without JavaScript, where chip rows were
  hidden. A new `legend` block type is available to deck authors; the
  build rejects any card that still opens one dialog from more than one
  button.

## 2026-09-30 (tables size to content)

- **Tables no longer force a horizontal scrollbar when their content
  fits.** The fixed `min-width: 560px` floor on `table` is now
  `min-content`: short tables (e.g. the personal-pronoun paradigm)
  fill their container, wide declension paradigms scroll inside
  `.table-scroll` as before. Applies to every page and layout variant;
  service-worker cache v43.

## 2026-09-29 (layout lab preview: three page compositions)

- **Preview-only layout lab** on the deck pages: open any deck with
  `?layout=bento`, `?layout=sidebar` or `?layout=spread` (or switch
  live from the small `Layout` dock that appears only inside a lab
  session) to compare three fully designed page compositions against
  the production stack — Bento workspace (varied tile mosaic), Study
  sidebar (persistent category rail + lesson canvas on desktop,
  category strip on phones) and Editorial spread (featured rule +
  numbered hairline index). Production visitors are unaffected: no
  parameter means no lab, no extra bytes, identical rendering. The
  experiment and its promotion/removal path are recorded in
  `.design/decisions.md` and DEBT D-09. `CACHE_VERSION` v42.

## 2026-09-29 (one-line header + practice removed)

- **Practice view removed** from all four decks (plans DE-D01/EN-D01,
  DEBT D-03): three static questions had no replay value, so the view,
  its footer links and its search-token exemptions are gone; practice
  returns only as a designed pool/shuffle surface. DE decks now navigate
  with four destinations, EN keep five.
- **One-line header**: phones get burger → search → theme; brand,
  languages, help and install live in the burger popover (still usable
  without JavaScript). ≥720px the whole header is inline on one row. The
  search field carries a persistent DE/EN chip that survives typing.
- **Install nudge**: a quiet one-time prompt appears for browser-tab
  visitors after ~25 seconds (never in the installed app, never twice);
  on phones the install button itself lives in the burger.
- Sweep: help-dialog navigation copy, footer install hints, scroll
  anchor offsets and the design-system/style-guide specimens follow.
  Service-worker cache: v38 (practice removal), v39 (header).
- **Fixes from the whole-work review**: a concurrent experiment had
  leaked a WIP stylesheet into the service-worker `APP_SHELL` and a
  layout-lab script into the shared template — both reverted (the stale
  precache entry would have broken the SW install in production);
  `--check-shell` now fails when an `APP_SHELL` URL is missing from the
  tree, the validator rejects retired `practice`/`footer_practice`/
  `reveal_*` data instead of ignoring it, the install nudge keeps its
  own button on browsers without `beforeinstallprompt`, and the landing
  header keeps its full-width row inside the new flex header.
  `CACHE_VERSION` v40.
- **Field/menu polish**: the ⌕ glyph left the search field (the DE/EN chip
  alone marks it) and the burger's help row dropped its pseudo-italic "i" —
  it read as a stray letter next to the label, not as an icon; the desktop
  (i) button keeps its glyph. `CACHE_VERSION` v41.

## 2026-09-29 (sibling-drift gate + scope correction)

- **New gate**: `build_pages.py --check-siblings` diffs each target's
  live audience decks — table-row drift exits 1 (head rows may be
  localized), formula/example divergence is reported normalized (markup
  stripped) for review judgment (CONTENT_VALIDATION §3). It exists
  because a red-team review caught a real sibling divergence that prose
  checklists had missed (next bullet).
- **Content fixes**: the de-ru particle example now uses the natural
  «Wie heißt du denn?» — yesterday's de-en fix had silently left the
  Russian deck with the marked order in both the card and the dialog —
  and en-de no longer coins «Kalk»/«kalkt»/«Neustoff» for calque/new
  material (natural «typischer deutscher Fehler», «Falle», «komplett
  neu» instead; the English audit rows say «calque»). `CACHE_VERSION`
  v35.
- **Scope correction (core extraction, DEBT D-07)**: the earlier
  «~15 blocks / 8–9%» headline measured markup conventions, not shared
  content. Re-measured with the content lens: the core is 54/179 (DE)
  and 61/168 (EN) aligned blocks — roughly a quarter to a third of a
  deck — with 47/38 content-identical and the rest separated by
  audience-language labels, localized headers and markup. The deferral
  stands, on machinery cost (four parameterization axes) and a low
  observed drift rate, not on thinness; ROADMAP and DEBT D-07 restated.

## 2026-09-28 (audience variants)

- **New page (German, explained in English)**: `de/en/` — the German deck
  re-derived for English speakers: all 28 topics re-angled (cases built from
  the I → me remnant, der → den as the visible case marker, professions
  drop the article — the opposite of English…), English UI, dialogs, glosses
  and practice (DE-03/07/08), with its own PWA icons, manifest and plan.
  Adapted, not translated — no Russian-audience wording was carried over.
  `CACHE_VERSION` v30, v31 after the smoke fixes.
- **New page (English, explained in German)**: `en/de/` — the English deck
  re-derived for German speakers: all 26 topics re-angled (rigid SVO instead
  of the free German order, do-support as the signature trap, muss nicht ≠
  mustn't as the sharpest false friend, the Perfekt-Kalk as Gefahr Nr. 1…),
  German UI (du-form) with English terms kept English, practice deliberately
  remapped to EN-04/05/06. The registry's dead `en/en` self-pair placeholder
  was replaced by the live German audience. `CACHE_VERSION` v32.
- **New (shared)**: target-language tagging is per-audience — the page
  script follows the registry `script` key: Cyrillic audiences keep the
  script heuristic, Latin audiences (de-en, en-de) tag only explicit
  bold/hit runs, so target-language study-voice fragments are bold in the
  source and explanation prose stays in the audience voice. Latin×Latin
  search stays strict by design: every search token must be card-visible or
  registered in `site.json` (`grammar_terms`).
- **Records**: CONTENT_AUDIT gained one per-deck record each — page↔deck
  `--check` and `--check-shell` PASS, Coverage PASS (28/28 and 26/26),
  Accuracy/Teaching NOT RUN per D-01. ROADMAP marks the Phase-3 pair shipped
  and records the two-layer core extraction for the German target as now
  due (DEBT D-07); AGENTS.md and README.md list the new URLs.
- **Review round (both new pages)**: fixes from the independent deck
  reviews — en-de section badges normalized to German (Artikel, Pronomen,
  Wortstellung, Zeiten, Verben, Präpositionen, Nomen, If-Sätze), «№1» →
  «Nr. 1», the particle example corrected to the natural «Wie heißt du
  denn?», the Präteritum dialog's gloss list completed (durfte → was
  allowed to), the dieser dialog's neutral-der example fixed, the EN-02
  you two / you guys hint added, the passive dialog now claims exactly
  its five tenses, and the search-token gate now also covers practice
  cards. `CACHE_VERSION` v33.
- **Follow-up nits (same day, after a whole-work review)**: «sein Auto»
  gloss corrected to “his car / its car”, both new plans' status
  paragraphs synced with the shipped state (Coverage PASS), the en-de
  audit record corrected (the interactive smoke ran clean), AGENTS.md
  structure line updated. `CACHE_VERSION` v34.
- **Scope decision (core extraction)**: the three-sample trigger fired,
  the boundary was measured on the real pairs — the shareable core is only
  ~15 blocks per target (~8–9% of a deck, dialogs 0/83 identical) — so the
  two-layer extraction is deferred with explicit re-triggers (third
  audience, drift incident, or a large cross-audience fix) instead of
  running now; until then every review diffs sibling
  tables/formulas/examples (DEBT D-07, ROADMAP source model).
- **Review fixes (whole-work pass on the decision record)**: the
  audience-variant playbook now teaches "measure the core boundary" at a
  second audience instead of the old extract-now rule; the sibling-diff
  check is anchored to the measured baseline (tables cell-wise on
  target-language data, formulas as text once markup conventions differ)
  so it stays signal instead of noise; the D-07 runbook gained the
  `--check-siblings` step and the three parameterization axes.

## 2026-09-28 (design)

- **Improved readability:** larger supporting text in cards, examples, tables,
  language cards and bottom navigation, with more breathing room between lines.
- **Clearer search:** both decks show the number of matching cards. While
  results span views, the bottom nav no longer suggests one view is selected;
  clearing search restores the selected view.
- **Clearer screen-reader navigation:** decorative grammar cues in the bottom
  nav no longer repeat before the destination names.

## 2026-09-24 (content)

- **New (both languages, Tier 2)**: German verb+preposition pairs (warten
  auf, denken an… — case comes from the preposition), the der/ein/kein
  choice (professions without an article), and seit vs vor (duration with
  Präsens vs a past point — not like the English Perfect). English:
  negation (don't/never/no — double-negative trap), Present Perfect
  Continuous (recognition), relative clauses (who/which/that, whose,
  object-that omission), imperative (base form, Let's), while/whereas/on
  the other hand, and numbers and dates (ordinals, dates, decades).
  Inventories: DE 28, EN 26 topics — no open scope questions remain.
  `CACHE_VERSION` v27.

## 2026-09-24 (style)

- **Changed**: dialog commentary no longer runs into the sentence as one
  undifferentiated line — separable explanations («После denn остаётся
  обычный V2.», translations, error breakdowns) moved to their own muted
  line under the text, like the example glosses on cards. 30 German and
  11 English blocks affected; commentary woven into paradigm lines stays
  inline by design.

## 2026-09-24 (fix)

- **Fixed**: bold words mid-sentence in dialogs (e.g. *bin* in
  «Ich bleibe, denn ich **bin** müde.») each broke onto their own line —
  every `<b>` inside a detail block was made block-level, not just its
  label. The label is now the only block-level child (`.detail-label`),
  text flows as one line, and bold/strike target-language fragments in
  dialogs gained the study voice and screen-reader pronunciation.

## 2026-09-24

- **New (German)**: the «Не отправляют глагол в конец» card gained the
  **nicht/kein …, sondern …** = «не A, а B» pair (*Sie kommt nicht aus
  Bukarest, sondern aus Deva.*) and a «sondern vs aber» dialog: after a
  negation — sondern (correction), plain contrast — aber (with the
  *Er mag keinen Fisch, aber Fleisch* error breakdown), the
  *nicht nur …, sondern auch* pattern, and a word-order note. The negation
  dialog now names that «а» = sondern.
- **New (English)**: the linkers card gained the **not X, but Y** =
  «не X, а Y» and **not only … but also** = «не только …, но и» patterns
  with a «not …, but» dialog: both patterns, the plain-but boundary, and
  a note that these constructions live inside the sentence, unlike
  however-style linkers.

## 2026-09-23

- **New (German)**: the «Притяжательные» dialog (card «ein / kein /
  mein…») now shows how a possessive is built — the stem follows the
  owner (du → dein · Sie → Ihr, вежливое, с большой буквы · sie → ihr,
  её/их), and the ending comes from the ein-word table (die Adresse →
  deine / Ihre Adresse). Searching «Ihre», «Ihr», «Ваш» now surfaces the
  card. `CACHE_VERSION` v23.

## 2026-09-21

- **New (German)**: demonstratives unit (DE-25, plan + deck) — the
  «dieser / diese / dieses» card (A1) next to the article tables in
  Артикли и местоимения: Russian «этот/тот» collapse into one word, and
  dieser copies the article's endings (dies- + der/die/das pattern). The
  dialog adds the full Nom/Akk/Dat model, welcher- as the same pattern
  (Welcher Bus? — Dieser), dieser-vs-der, and the das-not-dieser rule for
  «это»-phrases (Das ist schön). Card anchor `forms-dieser`, searchable by
  «этот». Inventories: DE 25, EN 20 topics. `CACHE_VERSION` v22.
- **New (both languages)**: cards carry level + kind badges (A1/A2/B1 and
  «формы», «употребление», «порядок»…) — scanning a view now tells you the
  CEFR level and what each card gives you without reading the title.
- **New (both languages)**: 25 examples became «pairs» — the German/English
  sentence stays clean with the taught form highlighted, and its short Russian
  deciding hint sits right beneath it instead of being glued to the sentence
  or buried in small print. Recognition-level items (частицы, связки,
  условные) are now always glossed.
- **New (both languages)**: search results can jump you to the hit's page.
  While searching, every hit card shows a «view · section ↗» label; tapping
  it clears the search, opens that view, scrolls to the card and plays the
  highlight — so a result now leads to its full context (related cards,
  section). Previously results were readable in place only.
- **New (both languages)**: every card is deep-linkable. All 72 cards (40
  German, 32 English) carry stable anchors like
  `…/de/ru/#verbs-doppelinfinitiv` — opening such a link switches to the
  right view, scrolls to the card and plays a one-shot accent highlight
  (CSS-only, works without JS, respects reduced motion). Share or bookmark
  the exact card; the ids are stable and never renamed.
- **New (German)**: plural-formation unit (DE-24, plan + deck) — «Plural:
  ставка по роду» card in Окончания и изменения: feminine → -en/-n,
  masculine → -e, neuter → -er (umlaut group), unchanged -er/-el/-en,
  loanwords → -s, with the honest «no single rule» limit. The dialog adds
  suffix groups (-ung/-heit/-keit…), -chen/-lein, compound nouns (plural on
  the last root) and the Dativ-Plural +n cross-reference. **Extended
  (English)**: plurals rules now cover vowel+y → +s (days) vs consonant+y →
  -ies and -f/-fe → -ves (knife → knives) with the roofs/chiefs limit.
  Inventories: DE 24, EN 20 topics. `CACHE_VERSION` v18.

## 2026-09-13

- **New (both languages, Tier-1 A1 core)**: German verb conjugation
  (spielen/sein/haben with stem-change and -t/-d limits), nicht-vs-kein
  negation with placement, imperative (du/ihr/Sie), Präteritum recognition
  (war/hatte/modals — spoken vs written boundary), comparatives
  (schneller/am schnellsten, umlaut group); English there is/are (no-do
  negatives, There's vs It's) and Past Continuous (background vs event,
  Russian-aspect mapping); Present Continuous now also covers the
  always-irritation use (EN-G08). Inventories: DE 23, EN 20 topics.
  Build tooling: new `--check-shell` gate (landing + service-worker vs the
  language registry) and per-audience script exemptions in `site.json`.
  `CACHE_VERSION` v17.
- **New (both languages)**: linking-words units (DE-18, EN-18) — German
  deshalb/trotzdem/allerdings/außerdem/währenddessen (position 1 + verb,
  trotzdem-vs-obwohl boundary) and English but/however, so/therefore,
  meanwhile, nevertheless, although/despite (despite + noun vs although +
  clause trap). Plus the English flavour-words unit (EN-17): just,
  actually (≠ «актуально»), still, even, sentence-final though. Search
  finds each card by word or Russian hint. `CACHE_VERSION` v16.
- **New (German)**: modal-particles unit (DE-17, plan + deck) — doch, mal,
  denn, ja, schon, gar, wohl with Russian decision-equivalents (ведь, же,
  ну…), a contrast dialog with placement rule, and the denn
  particle-vs-conjunction warning. Search finds it by particle or by Russian
  hint word. `CACHE_VERSION` v15.
- **Fix (content)**: the 2026-09-11 content-review findings C-13…C-20 are
  closed. English: questions now state that *be* and modals form questions
  without *do* (EN-04); comparative spellings (bigger/happier/nicer) are
  spelled out (EN-15); plurals carry a countability caveat (EN-13); every
  dependent-preposition pair has a sentence example (EN-12); the passive
  by-phrase example is a full sentence; *must* separates obligation from
  deduction; terminology unified («превосходная степень»). German: the
  declension-dialog wording «Видимо» → «Заметно» and a mixed-script dialog
  title fixed. Search keywords that promised words a card never shows were
  trimmed or surfaced (mechanical gate now in the generator); genitive
  relative pronouns (*dessen/deren*) are now taught. `CACHE_VERSION` v14.

## 2026-09-11

- **Fix (iOS)**: a Home Screen app (Add to Home Screen) could come back
  from the background rendering the desktop layout — WebKit can restore a
  resumed standalone window with a ~980px viewport, which trips the 720px
  desktop breakpoint. The page now detects that state on
  return (pageshow / visibilitychange) and forces WebKit to rebuild the
  mobile viewport; the anti-zoom `maximum-scale=1` lock stays in place.
  The landing page got the same iOS head script the deck pages already
  had (it was missing there). `CACHE_VERSION` v11.
- **Clarity**: the three paradigm tables (артикли, ein-слова, местоимения)
  each gained an anchor example («Ich sehe **den** Mann», «Kennst du **ihn**?
  — Ich helfe **ihm**») and legends that state what the highlight actually
  marks; meaning-rule examples (Konjunktiv II, um…zu vs damit, Perfekt,
  mustn't) gained short Russian deciding glosses while form-rule examples
  stay unglossed — policy recorded in both plans. Search hygiene: keywords
  that named content absent from the card were removed or made visible
  (dessen/deren, modal-verb list, W-words); the generator now rejects such
  keywords. möchte, euer→eure and она/они/Вы glosses added.
- **Structure**: pages moved to `de/ru/` and `en/ru/` — one folder per
  (target × audience) pair, ready for decks in other explanation languages;
  the landing gained a locale selector (Русский today, English — soon) that
  remembers the choice. Old addresses (`/deutsch/`, `/english/`, `/de/`,
  `/deutsch.html`) redirect, including offline for already-installed apps.
  The German page is now generated from `content/decks/de-ru.json` like the
  English one. `CACHE_VERSION` v9.
- **Clarity**: every table now labels its bold convention — «Жирным —
  формы-ловушки» legend under all four tables with hot cells; the
  convention was documented for developers only (finding C-10).
- **Clarity**: ein-words table gets a reading key — new «Почему meinen?»
  chip explains that the endings mirror the definite article
  (den→meinen, dem→meinem), with the three empty cells and the
  Akk./Dat. reading rules (finding C-09).
- **Clarity**: possessives card now states the one-model rule on the card
  («mein — модель для всех: kein, dein, sein… основа + окончание»), dialog
  adds a `dein` example (finding C-08).
- **UX**: the usage intro line is now a compact (i) button in the header
  («Как пользоваться», opens the standard bottom sheet); noscript keeps the
  plain line.
- **UX**: one language menu in the topbar of every page — `DE · RU ▾`
  opens two flat groups: «Язык обучения» (Deutsch / English) and «Язык
  объяснений» (Русский; English — скоро). On the landing it replaced the
  mid-page selector and remembers the language you study; native details,
  works without JS. `CACHE_VERSION` v10.
- **Style**: study-voice serif retuned — Charter on macOS, New York on iOS,
  Sitka/Cambria on Windows, Noto Serif on Android (system stacks only, no
  downloaded fonts). `CACHE_VERSION` v7.
- **Style**: shared `assets/base.css` replaces the per-page inline copies;
  target-language text (German/English examples, answers, declension tables)
  now renders in a serif study voice via the `lang` attribute — Russian
  explanations stay sans; new `style-guide.html` documents tokens,
  components and class roles with live specimens. `CACHE_VERSION` v6.
- **Refactor/style**: shared `assets/base.css` (tokens + components, one
  source instead of three inlined copies), target-language text now set in a
  serif study voice, new `style-guide.html` component specimens; service
  worker shell includes the stylesheet.
- **Clarity**: teaching-quality pass after learner feedback — German dialogs
  now name the two-object verbs, gloss TeKaMoLo terms in Russian, exemplify
  the haben/sein exceptions, and contrast wo/wohin with a jogging pair;
  English SVO dialog typo fixed. `CACHE_VERSION` v6 (finding C-07).
- **Content**: pages aligned with the accepted plans — German gains the
  Konjunktiv II card and the modal-perfect double-infinitive note (DE-12,
  DE-14); English Perfect-vs-Past Simple is reworked meaning-first with the
  «время названо?» limit stated (C-02); practice on both pages is remapped
  to topic IDs. `CACHE_VERSION` v5.
- **Governance docs**: content validation protocol, rewritten language plans
  (stable topic IDs, explicit exclusions), content/UI audit ledgers, plan
  authoring guide, debt register, this changelog.

## 2026-09-10

- **Fix**: iOS standalone relaunch-zoom bug (iOS-only `maximum-scale=1`).
- **Navigation**: bottom nav switches category views; search is global
  across views; hero and numbered headings removed.
- **Hub**: German + English self-contained pages, landing, shared service
  worker, manual theme toggle.
- **Init**: German grammar cheatsheet PWA.
