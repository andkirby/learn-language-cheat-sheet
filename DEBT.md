# Debt register

Deliberately deferred work, each row with its owner and a concrete trigger.
Clear a row by doing the work (and updating the linked owner) or by recording
an explicit decision to drop it. Do not silently delete rows.

| ID | Debt | Owner of decision/evidence | Act when |
| --- | --- | --- | --- |
| D-01 | All four content gates NOT RUN for both languages; the 2026-09-11 page changes are author-reviewed only | `CONTENT_AUDIT.md` (review records) | An independent review session runs |
| D-02 | Baseline reference comparison unresolved: DE-G01–06 and EN-G01–07 candidate topics have no Required/Deferred/Excluded decision | `CONTENT_AUDIT.md` (open scope questions) | A language's scope or content expands |
| D-03 | Practice pool + shuffle (replay value) — currently excluded by the three-item practice contract | `deutsch/SITE_PLAN.md` + `english/SITE_PLAN.md` (DE-X05/EN-X05) | Practice is reopened as a product topic |
| D-04 | Mechanical content preflight (chip↔dialog bijection, `data-search` coverage, practice counts, view integrity) exists only as ad-hoc session scripts | would be `tools/content_check.py` (stdlib) | The next content-change session |
| D-05 | EN-16 (conditionals) is no longer exercised in practice after the 2026-09-11 remap to EN-01/04/06 | `CONTENT_AUDIT.md` (2026-09-11 record) | The practice mapping is revised |
