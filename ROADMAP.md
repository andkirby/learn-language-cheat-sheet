# Roadmap — candidate topics and standing scope rules

## Responsibility

This file owns the forward-looking content pipeline: candidate topics for
both decks, a recommended order, and the standing decision rules that let a
working session add bounded topics **without a per-item owner round-trip**.

It does not own accepted scope — that is the language plans
([German](de/ru/SITE_PLAN.md), [English](en/ru/SITE_PLAN.md)); it does not own
evidence or open questions — that is [CONTENT_AUDIT.md](CONTENT_AUDIT.md);
procedure lives in [content validation](docs/CONTENT_VALIDATION.md). When an
item ships or the owner rejects it, its row here is updated (and the audit
gets the §5 record).

Status: composed 2026-09-13 by the ZCode session (owner asked for a standing
vision so probes stop blocking on answers). Standing rules below are
**pre-authorized by the owner** from that conversation.

## Standing decision rules

**ADD without asking** when a candidate meets all of:

1. grammar or a closed class of function words — never open vocabulary;
2. A1–B1 for the deck's audience;
3. answers a one-to-three-tap retrieval question;
4. fits **one card + one dialog** with the simplification limit on the card;
5. has a Russian-interference angle or fills a plan-required gap.

Process per add: plan row first (AGENTS rule 3) → deck slice → `--check` ×2
+ browser smoke → audit scope row (Decided) + §5 record → `CACHE_VERSION`
bump → local commit. Push rides with the next authorized push.

**DEFER** (record here, no build) when it needs a multi-card series, B2+
density, or assessment-like structure.

**ASK the owner** when it changes product intent: practice redesign (D-03),
new target language or audience, view/navigation restructure, audio.

## Where the decks stand (2026-09-13)

18/18 required topics per language, Coverage PASS, search hygiene gated by
the generator. The center of gravity is A2. The honest gap: **the A1 core
that every card assumes** (verb conjugation, negation) is not taught on the
page, and English lacks a narrative past tense. That is what Tier 1 fixes.

## Tier 1 — recommended next (bounded, high value)

| Candidate | Source | View | Slice |
| --- | --- | --- | --- |
| DE present conjugation + sein/haben | DE-G01 | `#forms` | Regular endings table (≤6 rows) + sein/haben; dialog: stem changes (du arbeitest, du liest), -t/-st limits |
| DE negation: nicht vs kein + placement | DE-G02 | `#forms` | kein follows the ein-pattern; nicht for everything else; placement pairs (Ich komme heute nicht) |
| EN there is/are + be-negation | EN-G01 | `#order` | there is/are = «есть/находится»; There's vs It's; negatives without do |
| EN Past Continuous | EN-G03 | `#tenses` | was/were + -ing = был в процессе; interrupted-action pair with Past Simple |
| DE imperative | DE-G03 | `#order` | du/ihr/Sie forms, sein exception; vowel-change du-form noted |
| DE Präteritum (recognition) | DE-G04 | `#verbs` | war/hatte/wollte/konnte/musste + regular -te; «в речи — Perfekt, в тексте — Präteritum» boundary; recognition-level → glossed |
| DE comparatives/superlatives | DE-G05 | `#extras` | -er/-am -sten, umlaut group, gut/besser/am besten, viel/mehr/am meisten |
| EN Present Continuous + always (irritation) | EN-G08 | `#tenses` | One-liner on the PC card + dialog block; closes the long-pending decision — recommended Required |

## Tier 2 — bounded extensions (lean-add when Tier 1 lands)

| Candidate | Source | Lean |
| --- | --- | --- |
| DE verb + preposition pairs (warten auf, denken an…) | DE-G06 | Small pairs card;RU-preposition interference is the hook |
| DE plural formation (−e/¨-er/−s/−n + umlaut) | DE-G05 | One pattern card; «нет одного правила» limit |
| EN relative clauses (who/which/that) | EN-G05 | One card; object-relative omission in dialog |
| EN question tags (…, isn't it?) | new | RU «не так ли?» is the trap; tail copies the auxiliary |
| EN numbers/dates/time | EN-G07 | Defer-leaning: more lookup than grammar; small card ok |
| EN reported speech basics | EN-G06 | Defer-leaning: B1+ density; backshift is a series, not a card |
| DE weder…noch / sowohl…als auch | new | Defer-leaning: B1 connector pair, only if Tier 1 lands clean |

## Tier 3 — product-level (explicit owner decision, pre-scoped here)

- **Practice pool + shuffle** (D-03): replay value vs the three-item contract.
- **Phase 3 audience**: `de-en` deck (content-as-data machinery is ready;
  landing registry flips EN from «скоро»).
- **New target language** (uk: term exemptions already registry-based in
  `site.json`; the script check needs the generalization below).
- Audio/pronunciation and course sequencing: reaffirmed **excluded**
  (DE-X01/EN-X01, DE-X05/EN-X05).

### Multi-place edit tax (measured 2026-09-13, owner question)

Where an edit lands today:

| Edit type | Places | Status |
| --- | --- | --- |
| Content inside a language | 1 — the deck JSON, then regenerate + `CACHE_VERSION` | Solved by Phase 2; `--check` guards drift |
| Shared UI/generator behaviour | 1 — `tools/deck_*.py` + `page_template.html` (+ `base.css`), applies to every deck | Solved by the shared template |
| Content policy (e.g. gloss rules) | 3 — guide + both SITE_PLANs | By design: contracts are per-audience |
| New target×audience pair | ~6 — deck JSON, its SITE_PLAN, `site.json` flip, **landing `index.html` by hand** (`DECKS` + menu markup), `sw.js` APP_SHELL, icons run | Partially manual; landing has **no drift check** |
| Validator script exemption | code — Cyrillic range `\u0400-\u04FF` hardcoded as «audience script» | Breaks for Latin-script audiences (en-de): German data-search words would be flagged as invisible target words |

Pre-Phase-3 automations (small, kill most of the tax):

1. **Landing sync**: generate the landing from `site.json`, or at minimum a
   `--check-landing` that parses `DECKS`/menu markup and compares to the
   registry.
2. **Audience script as data**: per-audience `script`/`lang` in `site.json`;
   the validator replaces the hardcoded Cyrillic range with it.
3. **APP_SHELL from the registry**: emit or check the shell list against
   `site.json` live pairs.

After those three, a new pair costs: deck JSON + its plan + one `site.json`
line — everything else is generated or checked.

## What the format cannot take (design limits, not gaps)

- Tables beyond ~6 rows strain a 390px card (pronouns already scrolls).
- Pragmatic nuance beyond decision-equivalents does not compress — the
  particles card teaches 7, not 25, on purpose.
- No audio → nothing whose rule is pronunciation-only.
- Static practice cannot validate retention — audit probes cover that.

## Maintenance trigger

Revise this file when: an item ships or is rejected (update its row), a new
candidate appears (file it in CONTENT_AUDIT first if it is a probe), or the
owner changes the standing rules. The plans and the audit stay the authority
for accepted scope and evidence respectively.
