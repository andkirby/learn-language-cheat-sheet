# Changelog

One entry per user-visible change, newest first. UI rationale lives in
`.design/decisions.md`, content review evidence in `CONTENT_AUDIT.md`.
Append the entry in the same commit that ships the change.

## 2026-09-11

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
