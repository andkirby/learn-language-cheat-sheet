# Content audit record — Italian/French shared context and final verdict (2026-10-23)

Historical evidence moved verbatim from the root audit. Current status,
findings ledger and record index: [CONTENT_AUDIT.md](../../CONTENT_AUDIT.md).

## 2026-10-23 — Italian/French English-audience implementation and independent review

Scope: new `it-en` and `fr-en` decks, accepted plans and generated pages;
shared registry/landing/template/assets integration is runtime evidence in
[UI_AUDIT](../../UI_AUDIT.md#2026-10-23--italianfrench-integration-and-target-language-fragments).
The owner authorized the recommended bounded targets after the research.
No reciprocal audience, explanation locale or practice system was added.
This is acceptance of the selected scope, not a full CEFR/exam curriculum.

Git base: `05eed47bf715288739f35ef63d8859a1f72758b0`. These additions are
uncommitted working-tree files; HEAD alone does not identify the reviewed
content. Italian author: `thr_pfrpzvtcz9`, independent reviewer:
`thr_4bsuy4n7xv`. French author: `thr_4bsuy4n7xv`, independent reviewer:
`thr_pfrpzvtcz9`. Parent `thr_bktaq44cyt` integrated shared files and
independently checked the final Italian markup-only boundary.

Owned dirty paths: `content/decks/{it-en,fr-en}.json`, `it/en/`, `fr/en/`,
the three IT/FR research files, registry/landing/worker/icon generator and
page template; all six generated pages, eight emphasis-only source
runs in `de-en`/`en-de`, shared authoring/design docs and current audits.
Pre-existing unrelated `.mcp.json`, `designs/`, `research/lovable-approach.md`
and unrelated AGENTS hunks were preserved. No commit or push was performed.

### Inspected scope and baseline

Italian: all 36 normalized CILS rows and 31 Urbino grammar rows compared
with the publisher references. All 53 Required units mapped both directions:
51 cards in 20 sections, 307 card blocks, 180 form-list rows, 51 paired
examples and 52 dialogs/201 blocks, including the two hosted recognition
units IT-51/52 and help. Eight deferrals and six exclusions are explicit.
Selective B1 extensions and productive versus recognition depth are
identified as product allocations rather than universal CEFR claims.

French: all 94 A1/A2/B1 grammar bullets (35/29/30) independently compared
with Eaquals/CIEP 2015 Annex E and inspected grammar references. All 63
Required IDs map to 62 cards in 24 sections, 372 card blocks and 248
form-list rows; FR-01/02 share an owner, FR-61 nominalisation is Deferred.
All 63 dialogs, forms, English meanings, exception prose and scope limits
were read. Original snapshot: 347 dialog blocks; correction moves target
material from scalar leads to supported rich bodies without expanding scope.
Final corrected block counts and retest boundary are in the
[French review record](2026-10-23-french-review.md#french-final-independent-correction-retest--2026-10-23).

Every owned card/dialog block and paradigm member was inspected, not only
its example probe. No practice/hidden-answer surface exists. Per-unit
coverage/probe ledgers and exact primary-reference locations/access dates
are retained in the [Italian](2026-10-23-italian-review.md) and
[French](2026-10-23-french-review.md) review records. Raw snapshots, complete run inventories and independent
reports are in the linked BB storage records; their source hashes identify
the exact reviewed material. Structural validators do not certify grammar.

### Findings and closure

| Finding | Original observed problem | Final disposition |
| --- | --- | --- |
| IT F1 | Any modified family noun was said to retain its possessive article | CLOSED: bounded diminutive/prenominal rule plus postposed-modifier variation; independently matched against Messina DICO |
| IT F2 | Taught Italian mentions remained in plain English runs | CLOSED: explicit target runs; full correction retest plus final 22-container markup-only boundary |
| IT F3 | English subject was said to control an Italian ending | CLOSED: Italian grammatical subject; related subject/piacere forms rechecked |
| FR R1 | Repeated French fragments lacked explicit target markup in rule/notice/lead prose | CLOSED: complete markup retest, including English-on regression and residual trouver lemma |
| FR R2 | Awkward English tell-command gloss | CLOSED: natural English tell-command gloss, unchanged French forms |
| FR R3 | Two Annex D page locators and Required typo | CLOSED: independently reopened printed p.51 / PDF p.53 and confirmed unchanged scope |

Historical FAIL entries in the initial ledgers (Italian and French
records) remain evidence of the found defects; they do not override the dated correction retests. Existing
DE/EN Baseline findings C-03/D-02 are outside this new-language acceptance
and remain open; eight b→i audience-hint adaptations do not alter their grammar.

Per-language evidence records: [Italian](2026-10-23-italian-review.md) ·
[French](2026-10-23-french-review.md).

### Final current verdict and revision

| Gate | Italian | French |
| --- | --- | --- |
| Baseline | PASS | PASS |
| Coverage | PASS | PASS |
| Accuracy | PASS | PASS |
| Teaching | PASS | PASS |

No open new-language scope/content blocker remains. Existing DE/EN findings
are unaffected. This accepts the bounded plans; it does not certify all
A1–B1 grammar or learner outcomes.

| Final artifact | SHA256 |
| --- | --- |
| `content/decks/it-en.json` | `82cde794ceb7989ba159fa38327808836cf2e3ef46ae800c0aa3e5d2e90786db` |
| `it/en/SITE_PLAN.md` | `87019300d29a75b3ed92a32b9a43e818498b57cf99986cb54b2fa97137df723d` |
| `it/en/index.html` | `6a09ec249a7efdcca1ced4e934ea381d8ea44488b1e692cec4167c6127268885` |
| `content/decks/fr-en.json` | `545c2b7f6f9807180a8ddbd340d3643afe502e0e46cf2cff90781fd34fecfec2` |
| `fr/en/SITE_PLAN.md` | `3d0eb58cd3c3fac8b08046ffd0c8df84fec605794c7c42bfd6c8be3eda343a2c` |
| `fr/en/index.html` | `1a5adde4ba03a6036af1cf63cbe1eb9a4b77ce2c825b48274d277d27474f6d63` |

The reviewed Italian plan was `1c3a074bafef5ca48ff69d1a02a19a3ba5b88ca3d03ad59600585de18f43fc5f`;
French was `a6e3a7281022b2d577c57bd0fa068343d322e8d40c1a6fdd5f53f5d6509c1277`.
Parent subsequently replaced only their stale NOT RUN/pending introduction
with links to these canonical audits. Byte comparison confirms each accepted
target body from Product onward is unchanged. Those status-only edits do not
alter the inspected scope, mappings, rules or source locators.

Final shared review: ACCEPT, 51 static checks, S1 German comparison -t CLOSED;
see [UI_AUDIT](../../UI_AUDIT.md). Canonical page/shell checks, existing sibling table
invariants, browser/search/theme/dialog checks and origin-down offline checks
passed separately. Final cached FR/EN and EN/DE HTML hashes match the generated
files; all six decks, landing and four legacy redirects work with origin down.
All temporary task resources were closed; unrelated work was preserved.
Real-device standalone installation and deployed-site verification: NOT RUN.
No staging, commit or push was performed during the review.
