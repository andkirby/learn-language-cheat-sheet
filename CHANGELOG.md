# Changelog

One entry per user-visible change, newest first. UI rationale lives in
`.design/decisions.md`, content review evidence in `CONTENT_AUDIT.md`.
Append the entry in the same commit that ships the change.

## 2026-09-11

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
