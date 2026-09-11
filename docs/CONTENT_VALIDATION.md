# Content validation protocol

Purpose: establish whether the selected grammar content is accurate, useful
and sufficiently covered for Russian-speaking A1–B1 learners. This is a
focused reference, not a complete course or a claim of CEFR certification.
UI checks in `AGENTS.md` remain a separate gate.

## Responsibility

This file owns the review procedure, evidence requirements and pass criteria
for language content. It does not own accepted scope, authoring questions or
review results:

- [The SITE_PLAN guide](SITE_PLAN_GUIDE.md) owns how to craft a plan.
- Each language's `SITE_PLAN.md` owns accepted scope, durable exclusions and
  the required-topic inventory.
- [CONTENT_AUDIT.md](../CONTENT_AUDIT.md) owns observed results, references,
  unresolved questions, findings and review provenance.

Do not treat the plan as evidence that the page implements it. Do not promote
an unresolved audit finding into the plan until its scope decision is accepted.

## 1. Establish the coverage baseline

Compare the plan with a named level-appropriate syllabus or course contents
and an authoritative grammar reference, independently of the existing page.
Record exact title, edition/URL, section/page and access date in the audit;
name-dropping a publisher is not evidence. Level assignments need a syllabus
source: a grammar reference alone does not establish CEFR level.

Check that every topic has a stable ID, learner question, intended level/depth
and an accepted state defined by the authoring guide. Break broad topics into
reviewable subtopics when needed. Record newly discovered topics as open audit
findings until they are accepted as Required, Deferred or Excluded. Accepted
exclusions need a rationale and reconsideration trigger in the plan so the
same decision is not repeatedly reopened.

The initial inventories are provisional. Resolve their open candidates and
level assignments before claiming baseline completeness. Add required topics
to the plan before changing the page; do not automatically expand the deck to
every topic in a reference book. Validate exclusions against the stated
product boundary as well as the reference comparison.

## 2. Compare the page in both directions

When page inspection is within the task's allowed scope:

1. Map every required topic to actual section + card title, `DETAILS` keys,
   table and practice identifiers as applicable. A section anchor alone is
   not sufficient evidence of coverage.
2. Inventory every actual rule, table, formula, example, translation, dialog
   and practice answer, including content outside the plan. Map it back to
   a topic or record a scope discrepancy.
3. Assign coverage: unverified, missing, partial, covered, or excluded.
   Use covered only when the agreed depth is present; excluded needs the
   scope rationale from the plan. Track linguistic verdict separately.

Do not infer presence from a plan, or correctness from a matching keyword.
If inspection is limited to Markdown, record page checks as NOT RUN.

## 3. Review accuracy and teaching quality

Check every content unit, including every table cell and hidden answer:

- Rule, form, position and trigger agree with the cited reference.
- Simplifications state their limits; test an ordinary example and a
  counterexample to shortcuts or absolute wording. Keep necessary caveats
  visible wherever a standalone card would otherwise teach a false rule.
- Examples are natural, demonstrate the stated rule and agree with the
  Russian explanation. Translations preserve the relevant meaning.
- Formulas account for the constructions they claim to cover; cases,
  endings, spelling, person/number and tense are consistent throughout.
- Language variety, register and exceptions are identified when relevant.
- A learner can tell when to use the pattern; cards remain concise and
  dialogs provide useful depth without contradicting the card.
- Practice has sufficient context, correct answers and explanations, and
  accepts valid alternatives. Map each item to topic IDs. Three learner
  exercises are a UI choice, not full validation coverage.

Review probes may live in the audit rather than increasing on-page practice.
Use a separate reviewer from the content author for the linguistic pass;
record who reviewed it and which material they inspected. Automated checks
can establish structural coverage, not certify naturalness or correctness.

## 4. Record results and decide

Each review records date, reviewer, exact revision (plus dirty paths if any),
scope, topic/content-unit counts, inspected locations, reference evidence,
probe + expected result + observed result, findings and verdict.

| Gate | PASS requires |
| --- | --- |
| Baseline | All candidate gaps decided; levels/depth justified by sources; every required topic inventoried; exclusions have rationale and reconsideration triggers |
| Coverage | Every required topic covered; all actual content mapped back to scope; no unexplained omissions |
| Accuracy | Every actual content unit reviewed; no unresolved wrong rules, misleading shortcuts, incorrect examples/translations or answers |
| Teaching | Triggers and relevant limits clear; examples and practice support the rule; card/dialog consistency checked |

Use PASS, FAIL, or NOT RUN for each gate. Partial inspection is NOT RUN for
the full gate, with reviewed items listed separately. Overall PASS requires
all four gates to pass. An excluded topic is an explicit product boundary,
not a finding that can excuse incorrect content already on the page.

Findings contain ID, topic/location, evidence, consequence, needed action,
status and retest result. Cosmetic suggestions may remain open; anything
affecting correctness or required coverage blocks content acceptance.

## 5. Keep the result current

Run a full review for the initial baseline and every new language. After a
content change, recheck changed units and all related cards, dialogs, tables
and answers, plus both-direction coverage. Carry forward unaffected results
only with a named prior reviewed revision and an inspected change boundary.
Scope changes reopen baseline review. A broad rewrite or an unknown change
boundary requires a full review. A past PASS never silently covers new text.

Content acceptance does not replace runtime checks, and runtime success does
not establish content acceptance.
