# Changelog

One entry per user-visible change, newest first. UI rationale lives in
`.design/decisions.md`, content review evidence in `CONTENT_AUDIT.md`.
Append the entry in the same commit that ships the change.

## 2026-09-11

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
