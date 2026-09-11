# RESEARCH: EnglishPage verb-tense reference

Found while chasing a deck gap: our `en/ru` deck's Present Continuous card
and "Simple vs Continuous" dialog cover only the "action now" meaning and
omit the **complaint/irritation use of *always* + Continuous**
("She's always complaining"). This doc records an extended cheat-sheet
source that does teach it. Gathered 2026-09-11.

## EnglishPage — present continuous

<https://www.englishpage.com/verbpage/presentcontinuous.html>

EnglishPage organizes every tense as a numbered **USE 1…N** reference —
the "extended cheat sheet" shape (four uses for the present continuous):

1. **Now** — actions happening at this very moment (or explicitly not).
2. **Longer actions in progress now** — ongoing processes not happening
   at this exact second.
3. **Near future** — things that will or won't happen soon.
4. **Repetition and Irritation with Always** — frequent actions that
   annoy or shock.

USE 4 verbatim: the tense with "words such as *always* or *constantly*"
conveys "something irritating or shocking often happens"; "the meaning is
like simple present, but with negative emotion"; put *always*/*constantly*
"between *be* and verb+ing". Examples:

- "She is always coming to class late."
- "He is constantly talking. I wish he would shut up."
- "I don't like them because they are always complaining."

Value for us: the USE 4 formula note (adverb slot *between be and V-ing*)
plus the simple-vs-continuous emotion contrast ("same habit meaning, but
with negative emotion") is exactly the one-liner our card marker line or
"Simple vs Continuous" dialog is missing.

## Other sources covering the same use

Verified live this pass:

- **British Council** — word-class reference page "Talking about the
  present", use #6 "something which happens again and again" with the note
  "we normally use *always* with this use" ("They are always arguing.").
  See [`britishcouncil.md`](britishcouncil.md); BC has no dedicated
  present-continuous lesson in its A1–A2 lesson list.
- Search-verified but not fetched in depth: VOA Learning English
  ("Present Progressive Tense and Showing Annoyance" — always/constantly
  pair the progressive with annoyance),
  [native1.pl](https://native1.pl/present-continuous-always-annoyance/)
  and [teacherola.com](http://teacherola.com/top-75-present-continuous-irritating-habits/)
  (adverb set: always, constantly, continually, all the time).

Sources that do **not** cover it at the page checked: Perfect English
Grammar splits form and use across separate pages — its present-continuous
*form* page has no usage section; Cambridge Dictionary's present
continuous page returned a server error when tried (retry if needed).

## Deck note

The model sentence behind this investigation, "I'm always having a trouble
on this laptop", is itself faulty: *trouble* is uncountable ("a trouble"
✗) and idiomatic collocation is *trouble with*: **"I'm always having
trouble with this laptop."** The Continuous-with-*always* part is correct
for the complaining meaning. If the deck gains this use, that sentence —
corrected — is a good candidate example (it also ties into the
[countability] card topic).

## Re-gathering

englishpage.com fetches fine via WebFetch; the site is a plain
server-rendered reference (no SPA bundle spelunking needed). Verb-tense
pages live under `/verbpage/` (presentcontinuous, present simple,
pastsimple, presentperfect, future, conditionals…).
