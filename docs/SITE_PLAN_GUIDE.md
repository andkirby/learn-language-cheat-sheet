# SITE_PLAN authoring guide

## Responsibility

This guide owns the questions and required structure for creating or revising
a language `SITE_PLAN.md`. A language plan owns accepted product intent,
content scope, durable exclusions, information architecture and
language-specific acceptance requirements.

This guide does not own a language's answers. It also does not prove that a
page implements its plan or that its grammar is correct:

- Accepted answers belong in that language's `SITE_PLAN.md`.
- Shared UI behavior belongs in
  [the design system](../.design/DESIGN_SYSTEM.md).
- Review procedure belongs in [content validation](CONTENT_VALIDATION.md).
- Open questions, sources and review results belong in
  [the content audit](../CONTENT_AUDIT.md).
- Deployment and local operation belong in [README.md](../README.md).

## Decision states

Every material scope item needs one of these states:

| State | Meaning | What the plan records |
| --- | --- | --- |
| Required | Part of the accepted current content target | Topic ID, learner question, intended depth and surface |
| Deferred | Valuable, but outside the current target | Rationale and concrete reconsideration trigger |
| Excluded | Deliberately outside this product | Rationale and concrete reconsideration trigger |

Unresolved ideas are not plan decisions. Keep them as open findings in
`CONTENT_AUDIT.md` until they are accepted, deferred or excluded. Do not use
“optional”, “later” or an empty cell: those labels let the same decision
recur.

## Authoring questions

### 1. Responsibility and status

- Which language page does this plan own?
- Is it an accepted target, and has page alignment been validated?
- Which document owns implementation evidence and open questions?

Never describe a target as implemented merely because it appears in the plan.

### 2. Learner and outcome

- Who is the learner, including interface language and target level band?
- Is this a lookup deck, course, assessment, phrasebook or another product?
- What should the learner retrieve or decide within one to three taps?
- What prior knowledge can the page assume?

### 3. Language policy

- Which standard or regional variety is the default?
- How are other common varieties handled?
- Which terminology remains in the target language?
- What must Russian explanations and translations preserve?
- Which register differences or learner-interference traps need labels?

### 4. Boundary and exclusions

- Which content categories are in scope: grammar, pronunciation, vocabulary,
  spelling, usage, practice or assessment?
- Which level range is productive, recognition-only or excluded?
- Is the page selective or comprehensive within that boundary?
- Which tempting adjacent topics are deliberately excluded or deferred?
- Why was each exclusion chosen, and what evidence would reopen it?

Write exclusions even when they seem obvious. Their purpose is to prevent
future authors from repeatedly reopening settled scope.

### 5. Retrieval questions and coverage

- What are the five to seven highest-value questions the learner asks?
- Which Russian-language interference problems deserve first-class treatment?
- Does every required topic answer one of those questions?
- Has the inventory been compared with a named level-appropriate syllabus and
  an authoritative grammar reference?
- Are newly discovered topics decided explicitly instead of silently omitted?

Give every required topic a stable language-prefixed ID. Use one row per
reviewable topic rather than one row for an entire grammar domain.

### 6. Depth and presentation

- What must the first-layer card contain: trigger, meaning, form, position,
  example or contrast?
- Which limits or counterexamples must remain visible on the card?
- Which details belong in a dialog?
- Which tables or formula diagrams are necessary?
- What does “covered” mean for this topic?

### 7. Information architecture and retrieval

- Which view and stable anchor owns each topic?
- Can a learner find it through navigation and likely Russian and
  target-language search terms?
- Which legacy anchors must remain stable?
- Are related topics grouped by learner question rather than textbook order?

Shared mechanics stay in the design system; the plan records only the
language-specific view map, anchors and exceptions.

### 8. Practice

- Which high-risk topic IDs are exercised?
- Does each item provide enough context for one defensible answer?
- Are accepted alternatives and explanations defined?
- Is practice clearly a retrieval aid rather than evidence of full coverage?

### 9. Acceptance and maintenance

- What must be true before the content target is accepted?
- Which content changes require plan revision before page revision?
- Which related cards, dialogs, tables and answers must be rechecked?
- Where will the reviewed revision, sources, findings and verdict be recorded?

## Required plan structure

Use the existing German and English plans as the concrete format. Each plan
must contain, in this order:

1. responsibility and verification status;
2. product goal, learner and language policy;
3. durable scope boundary with deferred and excluded decisions;
4. primary retrieval questions;
5. language-specific information architecture and stable anchors;
6. content-unit and practice requirements;
7. required-topic inventory with stable IDs, planned surface and acceptance
   depth;
8. maintenance triggers and links to validation evidence.

Do not copy shared tokens, generic accessibility rules, deployment steps,
review results or unresolved proposals into the plan. Link to their owners.

## Completion check

A plan is decision-sufficient when:

- its responsibility and target status are explicit;
- every accepted topic has an ID, learner question, depth and surface;
- adjacent categories and known candidate topics are required, deferred or
  excluded with rationale and reconsideration triggers;
- practice maps to named topic IDs;
- no shared contract or review evidence is duplicated;
- the baseline gate in `CONTENT_VALIDATION.md` has a recorded result.

The last item may remain NOT RUN while drafting, but the plan must say so and
must not claim completeness.
