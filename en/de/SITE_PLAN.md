# English Cheat Sheet — site plan (en-de)

## Verantwortung und Status

Diese Datei besitzt den akzeptierten Produkt-Intent, das englische
Inhaltsziel, dauerhafte Scope-Entscheidungen und die sprachspezifische
Informationsarchitektur für `en/de/index.html` — Englisch erklärt auf
Deutsch. Sie ist die Publikums-Variante, neu abgeleitet aus dem englischen
kanonischen Plan ([en/ru/SITE_PLAN.md](../ru/SITE_PLAN.md)); Themen-IDs
EN-01–26, die Views und das Abschnitts-Skelett sind von dort eingefroren
(Practice ist dort inzwischen entfernt — Deferred EN-D01), während jede
Retrieval-Frage, jede Interferenzgeschichte und jede Abnahmeentscheidung
unten für deutschsprachige Lernende neu abgeleitet ist. Zum Revidieren gilt
[der Autoren-Guide](../../docs/SITE_PLAN_GUIDE.md).

Sie beweist nicht, dass die Seite dem Ziel entspricht oder dass die Inhalte
korrekt sind. Diese Ergebnisse gehören in
[CONTENT_AUDIT.md](../../CONTENT_AUDIT.md). Gemeinsames UI-Verhalten gehört
in [das Design-System](../../.design/DESIGN_SYSTEM.md), Betrieb und
Deployment in [README.md](../../README.md).

Die Seite lebt unter `<target>/<audience>/` (`en/de/`) neben ihrem
russischsprachigen Geschwister (`en/ru/`) und teilt mit ihm das englische
Target-Inventar. Abschnitts-Anker und Karten-`id`-Slugs erben das Skelett
des Geschwisters, damit publikumsübergreifende Referenzen lesbar bleiben;
nach dem Shipment sind sie für immer stabil (harte Regel 7).

Status: Dieser Plan ist das akzeptierte Inhaltsziel für das `en-de`-Publikum.
Deck-JSON, Seite und Icons sind am 2026-09-28 erschienen (Commit a0a7a70);
der interaktive Runtime-Smoke lief fehlerfrei. Coverage ist PASS (26/26
Pflichtzeilen, siehe CONTENT_AUDIT.md §5). Accuracy und Teaching sind pro
D-01 NOT RUN — ein Ganzwerk-Review fand keine Fehler, ersetzt aber nicht
das referenzgestützte Gate. Der per-Target-Basiskonjunkt (Syllabus- und Referenzvergleich, C-03/D-02)
wird mit `en/ru/` geteilt; pro ROADMAP Tier 3 wird er einmal pro Target
erledigt und von seinen Publika geerbt, während die Interferenzfallen pro
Publikum neu abgeleitet werden — diese Neuableitung ist, was dieser Plan
trägt.

## Produkt und Lernende

Das Produkt ist ein mobile-first englisches Grammatik-Lookup-Deck für
deutschsprachige A1–B1-Lernende. Übliche Grammatikentscheidungen sollen in
ein bis drei Taps abrufbar sein, die erste Ebene knapp bleiben; Installation
als PWA und Offline-Funktion nach dem ersten erfolgreichen Laden gehören zum
Produkt.

Die Erklärsprache ist Deutsch: UI-Strings, Dialoge und
Suchhinweise sind auf Deutsch geschrieben; englische Termini (Past Simple,
Present Perfect, Continuous) bleiben Englisch. Das Deck duzt durchgehend
(du-Form, direktes Anweisungsregister, Kontraktionen willkommen) — konsistent
in UI, Dialogen und Suchhinweisen. Englische Beispiele sind
registerneutral: Englisch hat kein Sie, und die du/ihr/Sie-Kollision in
*you* ist gelehrter Inhalt (EN-02), nicht die Stimme des Decks.

Es setzt keine Vertrautheit mit englischer Grammatikterminologie voraus —
aber es kann den Kasusbegriff voraussetzen, umgekehrt zur en-ru-Situation:
Englisch trägt Kasus nur noch in den Pronomen-Resten (*I → me*) und im
*'s*-Genitiv; die Grammatik lebt in fixer Wortstellung, Auxiliaren (do, be,
will, have) und Zeitformen. Das ist nahezu der Gegenhandel zum deutschen
Kasussystem: Deutschsprachige kommen mit dem Rollenkonzept (der Vorteil
gegenüber en-ru, wo der Begriff erst aus dem Nichts gebaut wird) und müssen
stattdessen fast alles neu ordnen, was Deutsch morphologisch oder
stellungstechnisch anders löst — freies Umstellen (V2, Mittelfeld) wird zu
rigidem SVO, die Verbklammer zu Auxiliar-Mustern, und es kommt Neustoff ohne
deutsches Pendant dazu: do-support, Verlaufsformen, Gerundium, *going to*,
der Nullartikel. Der *'s*-Genitiv ≈ Genitiv-s ist ein direktes Paar (*the
man's dog* ≈ *der Hund des Mannes*). Beispiele nutzen neutrales
zeitgenössisches internationales Englisch; ein britisch/amerikanischer
Unterschied wird nur gelabelt, wenn er die gelehrte Entscheidung ändert oder
einen wahrscheinlichen Fehler verhindert.

## Scope-Grenze

Erforderliche Grammatikthemen sind einmalig im Inventar unten definiert.
Kein zusätzliches Thema wird durch eine Überschrift, ein Suchkeyword oder
auf der Seite gefundene Inhalte impliziert. Die fünf Ausschlüsse sind die
dauerhaften Produktgrenzen des englischen Targets, für dieses Publikum
nachgeprüft — die Neuableitung hat keinen von ihnen geändert.

| Entscheidung | Ausgeschlossene Inhalte | Begründung | Wieder öffnen, wenn |
| --- | --- | --- | --- |
| EN-X01 | Aussprache, Phonetik und Hörverstehens-Anleitung | Das Produkt ist ein Grammatik-Lookup-Deck ohne Audio | Eine Aussprache- oder Audio-Lernfläche akzeptiert wird |
| EN-X02 | Thematischer Wortschatz, Phrasebook-Material und ein umfassendes Wörterbuch; dazu False-Friend-Listen als Vokabelstoff | Andere Retrieval- und Wartungsmodelle; die grammatiktragenden False Friends (also, actually, even) leben als Entscheidungshinweise in EN-17/18 | Das Produkt über Grammatik-Lookup hinauswächst |
| EN-X03 | Erschöpfender britisch/amerikanischer und regionaler Vergleich | Neutrale internationale Beispiele genügen für das Ziel | Ein Varietätsunterschied eine gelehrte Entscheidung ändert oder wiederholter Lernbedarf entsteht |
| EN-X04 | Erschöpfende Ausnahmen und produktive B2+-Grammatik | Dichte muss der genannten A1–B1-Zielgruppe dienen | Das unterstützte Niveau wächst oder ein Referenzvergleich eine A1–B1-Abhängigkeit zeigt |
| EN-X05 | Kurs-Sequenzierung, Mastery-Scoring und CEFR-Zertifizierung | Das Deck ist eine Lookup-Referenz, kein Kurs; Fortschritts- oder Assessment-Semantik sind außerhalb des Scopes | Das Produkt Fortschritts- oder Assessment-Semantik annimmt |

Es gibt keine akzeptierten Deferred-Themen: jedes Thema EN-01–26 ist mit
einer lebendigen Deutsch-Interferenzgeschichte neu abgeleitet. Am nächsten an
einer Aussetzung waren EN-24 und EN-25, weil die deutsche Seite ihrer
Entscheidung strukturell vertraut ist — Englisch hat eine Befehlsform, wo
Deutsch drei hat, und *while* nutzt dieselbe Zeit-und-Kontrast-Doppelnutzung
wie *während*; sie bleiben Required, weil die englischen Formen und Grenzen
trotzdem zu lehren sind (die Subjekt-Falle im Sie-Befehl; die
Registerentscheidung whereas vs while); ihre Zeilen sagen, was offensichtlich
ist. Ein Thema ist als Deferred akzeptiert:

| Entscheidung | Ausgesetzter Inhalt | Begründung | Wieder aufnehmen, wenn |
| --- | --- | --- | --- |
| EN-D01 | Die Wiederholungsansicht „Wiederholung“ (drei statische Reveal-Fragen, `#practice`) | Drei statische Aufgaben haben keinen Wiederholungswert; Practice kehrt nur als gestaltete Oberfläche mit Pool-/Shuffle-Mechanik zurück (DEBT D-03). Der am 2026-09-29 entfernte Inhalt bleibt in der Git-History wiederherstellbar. | Ein Practice-Design mit Wiederholungswert akzeptiert wird (der D-03-Auslöser) |

Unaufgelöste Kandidaten-Lücken für dieses Publikum sind Findings in
`CONTENT_AUDIT.md`, keine stillen Ausschlüsse oder Plan-Zusagen.

## Primäre Retrieval-Fragen

Die ersten drei Fragen existieren, weil die Arbeit hier umgekehrt läuft wie
bei en-ru: Rollen und Kasus kommen gratis mit — die Belastung liegt bei
Zeiten, Hilfsverben und Wortstellung.

1. Welche Zeitform passt zur Bedeutung — und braucht es eine Verlaufsform
   (Continuous)? *(EN-05, EN-07, EN-20, EN-22)*
2. Wann Past Simple, wann Present Perfect? — der Perfekt-Kalk bleibt die
   Gefahr Nr. 1. *(EN-06)*
3. Wann kommt do/does/did in Frage und Verneinung — und wo genügt be?
   *(EN-04, EN-19, EN-21)*
4. a/an, the oder kein Artikel? *(EN-01)*
5. Welches Pronomen oder welche Nomenform — Objektform, Possessiv, Plural,
   viel/viele, Vergleichsstufe? *(EN-02, EN-13–15, EN-26)*
6. Welche Präposition passt — in/on/at, Zeit, Ort, feste Verbbindung?
   *(EN-11, EN-12)*
7. Welches Muster drückt diese Bedeutung aus — Modal, Passiv, V-ing/to V,
   Bedingungssatz, Relativsatz, Imperativ? *(EN-08–10, EN-16, EN-23, EN-24)*
8. Welches Verbindungswort oder Tönungswort passt — mit False-Friend-Check
   (also, actually, even)? *(EN-17, EN-18, EN-25)*
9. Kann ich ein kurzes Beispiel sehen und bei Bedarf eine tiefere Erklärung
   öffnen?

## Informationsarchitektur

Die Seite ist ein Lookup-Deck mit fünf Bottom-Navigation-Zielen — das
Skelett des en-ru Geschwisters mit deutschen View-Beschriftungen (kurze
Nav-Formen: Artikel, Zeiten, Satzbau, Verben, Präpositionen).

| View | Stabiler Anker | Erforderliche Themen |
| --- | --- | --- |
| Artikel und Wörter | `#articles` | EN-01–02, EN-13–15, EN-26 (`#pronouns`, `#nouns`) |
| Zeiten | `#tenses` | EN-05–07, EN-20, EN-22 |
| Satzbau | `#order` | EN-03–04, EN-17–19, EN-25 |
| Verben | `#verbs` | EN-08–10, EN-16 (`#conditionals`), EN-21, EN-23–24 |
| Präpositionen | `#preps` | EN-11–12 |

`#start`, `#pronouns`, `#nouns`, `#conditionals` und `#install-help` sind
stabile direkte Anker (die Seite ist neu — nichts hier ist ein Legacy-Link,
aber die Anker behalten die Namen des Geschwisters). Ein direkter Anker
öffnet die besitzende View vor dem Scrollen. Suche deckt alle Views ab und
stellt beim Leeren die gewählte View wieder her. Die Install-Hilfe bleibt
Dialog plus Footer-Zeile statt Inhaltsabschnitt.

## Content-Vertrag

Die gemeinsamen Karten-, Dialog-, Such-, Navigations- und
Barrierefreiheits-Mechaniken definiert das Design-System. Der Inhalt für
deutschsprachige Lernende ergänzt diese Anforderungen:

- Eine Regel der ersten Ebene gibt der Lernenden einen Bedeutungs-/Gebrauchs-
  Auslöser, Form oder Position und ein kurzes natürliches Beispiel.
  Signalwörter sind sekundäre Hinweise. Eine gefährliche Vereinfachung trägt
  ihre wesentliche Grenze auf der Karte. Insbesondere: Present Perfect
  versus Past Simple entscheidet über Bedeutung und Diskurskontext; „Wurde
  eine Zeit genannt?" ist keine ausreichende Entscheidungsregel — das
  *since 2020*-Gegenbeispiel bleibt auf der Karte.
- Beispiel-Glossen folgen der Regelart, mit deutschen Glossen. Form- und
  Positionsregeln (Paradigmen, Wortstellung, V-ing/to-V-Muster) halten
  Beispiele in der Zielsprache allein, mit struktureller Annotation — fette
  Formen, Minimalpaare (*she works / she's working*); eine deutsche
  Übersetzung kann englische Morphologie und Syntax nicht zeigen — genau sie
  sind ja der Lernstoff. Bedeutungs-/Gebrauchsregeln (Artikelwahl, Perfect
  vs Past, must not vs don't have to, some/any) bekommen eine kurze deutsche
  Glosse, die den Entscheidungsunterschied trägt, keine Vollübersetzung.
  Recognition-level-Konstruktionen sind die dritte Klasse. Abnahmetiefe und
  Gloss-Klasse sind zwei Dinge: EN-16 (Typ 3) und EN-22 sind in der Tiefe
  „recognition" (erkennen statt bilden), aber ihre decodierbaren Beispiele
  glossiert die Bedeutungs-/Gebrauchsklasse — eine echte Gloss-Klasse-3-
  Einheit existiert im englischen Deck derzeit nicht; tritt eine ins Deck,
  trägt ihr Beispiel stets eine kurze deutsche Glosse — Verständniszugang zu
  dem Satz, um den die Regel geht, nicht das Entscheidungskriterium.
  Wortfragmente
  bleiben ohne Glosse. Eine Glosse ohne Entscheidungsgehalt wird entfernt.
- Englischer Mustertext bleibt Englisch; deutsche Erklärungen, kursive
  Hinweise und Glossen bleiben in deutscher Stimme. Das ist ein
  Latin-Skript-Publikum, also greift die Target-Voice-Markierung des
  Generators nur bei expliziten fett/hit-Läufen — jedes englische Fragment,
  das die Lernstimme braucht, ist fett.
- Dialoge ergänzen Begründung, Kontrast oder Ausnahmen, ohne der Karte zu
  widersprechen. Neue tappbare Erklärungen nutzen das `DETAILS`-Objekt der
  Seite (Keys kebab-case; Erklärung auf Deutsch, englische Termini auf
  Englisch). Dialog-Keys erben die Geschwister-Keys, wo derselbe Dialog
  existiert — die en-ru-Schlüssel sind bereits englische Slugs.
- Such-Metadaten mischen deutsche Fragen mit englischen Termini; die
  russischen Intent-Wörter von en-ru verschwinden vollständig — sie sind die
  Wörter des vorherigen Publikums und wären hier tote Tokens. Das ist ein
  Latin-Skript-Publikum: strikte Suche — jedes `data-search`-Token muss
  kartensichtbar oder in `site.json` registriert sein
  (`grammar_terms_common` für englische Termini; `grammar_terms[en]` ist
  aktuell leer — deutsche Sucherwörter werden über die deutschen Glossen
  kartensichtbar); das Build-Gate erzwingt das bei jedem `--check`.

## Erforderliches Inhaltsinventar

Alle Zeilen sind im aktuellen Ziel Required. „Core" heißt: Die Lernende soll
das Muster wählen oder bilden können; „recognition" heißt: erkennen und
verstehen. Jede Zeile nennt, was aus dem Deutschen überträgt, was bricht und
welches Beispiel den Punkt trägt. CEFR-Einordnung pro Thema und
Seitenabgleich brauchen weiterhin Evidenz im Content-Audit.

| ID | Lernfrage und erforderlicher Inhalt | Fläche | Abnahmetiefe |
| --- | --- | --- | --- |
| EN-01 | a/an, the oder kein Artikel? Lautregel, Bezug, Verallgemeinerung und Institutionsgebrauch | `#articles` | Kernregeln, Kontrastbeispiele und wesentliche Grenzen. Offensichtlich: die Wahl selbst — Deutsch setzt genauso Artikel (der/die/das/ein ≈ the/a), und *the* ist geschlechtslos: kein Genus zu merken; Zweiterwähnung → *the* überträgt sich direkt. Fallen — die Grenzen interferieren in BEIDE Richtungen: Deutsch MIT Artikel gegen englischen Nullartikel in festen Wendungen (*go to school, by car, at night* ≈ *in die Schule, mit dem Auto, in der Nacht* — ✗ *go to the school* als Rollen-Lesung); die Umkehrung, deutscher Nullartikel gegen englisches a/an: *Ich bin Lehrer* → *I'm **a** teacher* (Rollen nach be), *Ich habe Kopfschmerzen* → *I have a headache / a cold*; die a/an-Lautregel ist neu (Deutsch kennt keinen Wechsel: ein Apfel); Institution *in hospital* (BrE) / *in the hospital* (AmE). Beispiel trägt den Punkt: *I go to school.* (Rolle) vs. *She plays the piano.* (Instrument). |
| EN-02 | Welches Pronomen? Subjekt-, Objekt-, abhängiges/unabhängiges Possessiv und Reflexivformen | `#pronouns` | Vollständiges Paradigma der gelisteten Formen plus Verwendungsbeispiele. Offensichtlich: Kasus im Pronomen — *I/me, he/him* ist der lebende englische Rest des deutschen Kasusystems; Rollen sind sofort lesbar — gegenüber en-ru läuft die Richtung umgekehrt: Der Begriff muss hier nicht gebaut, sondern nur wiedererkannt werden; *my/mine* ≈ *mein/meins* — direktes Paar. Fallen: *you* deckt du, ihr und Sie ab — die Anrede-Differenzierung verschwindet, Plural nur über Kontext oder *you two / you guys*; *man* → *you* (*One can…* klingt steif); deutsch *sein* deckt *his* UND *its* ab, *ihr* deckt *her* UND *their* ab — beide Aufteilungen sind Neulernen. Beispiel trägt den Punkt: *I saw him. — This is his car.* |
| EN-03 | Wie sind Aussagen geordnet, Einschub von Häufigkeitsadverbien? | `#order` | SVO-Grundordnung, be-Stellung und Grenzen mit Beispielen. Offensichtlich: der einfache Aussagesatz liest sich wie Deutsch (*I see the man*). Fallen: Deutsch stellt für Betonung frei um (*Den Mann sieht der Hund*), Englisch nicht — die Wortstellung trägt allein die Rollen, weil der Kasus fehlt; Häufigkeitsadverbien stehen VOR dem Vollverb, nach be (*I always drink coffee* / *He is always late*) — das freie deutsche Mittelfeld (*Ich gehe immer…*) erzeugt ✗ *I go always*; die deutsche V2-Gewohnheit nach vorangestelltem Adverb (Nie habe ich …) erzeugt ✗ *Never I have seen* — Standardenglisch behält SVO. |
| EN-04 | Wie werden Fragen gebildet? Do/Does/Did, W-Fragen und Subjektfrage who | `#order` | Kernformeln, be/Modal-Unterscheidung und Subjektfragen-Ausnahme. Offensichtlich: W-Fragen und be/Modal-Fragen funktionieren wie deutsche Umkehrung (*Where do you live?* · *Is she…? Can you…?* ≈ *Ist sie…? Kannst du…?*); die Subjektfrage *Who lives here?* ohne do ≈ *Wer wohnt hier?* — transfer. Fallen: do-support ist die fremdartigste Mechanik des Decks — das Deutsche kehrt nur das Verb (*Mag sie Tee?*), Englisch verlangt Do/Does/Did + Grundform (✗ *Likes she tea?* ist der Signature-Fehler); nach do steht die Grundform (*Does she work?*, nicht *Does she works?*). |
| EN-05 | Present Simple oder Present Continuous? | `#tenses` | Bedeutung/Gebrauch, Form und Kontrastbeispiele; Signalwort-Grenzen; PC mit *always* = Verärgerung, nicht „now". Offensichtlich: die Simple-Form — nur die 3. Person Singular bekommt -s (Deutsch flektiert mehr Personen; die Idee der Kongruenz ist vertraut). Fallen: das Deutsche hat keine Verlaufsform — *Ich arbeite* deckt *I work* UND *I'm working* ab; die Unterscheidung ist reiner Neustoff, und das Paar *she works / she's working* trägt den Punkt; Zustandsverben ohne -ing. |
| EN-06 | Past Simple oder Present Perfect? | `#tenses` | Bedeutung/Gebrauch, Form und Kontextkontrast; den Einzel-Schlüsselwort-Kürzel ablehnen. Offensichtlich: die Form have/has + V3 existiert als haben-Perfekt (*Ich habe gesehen*). Fallen: die Gefahr Nr. 1 — gesprochenes Deutsch wählt Perfekt für BEIDE englische Vergangenheiten: *Ich habe den Film gestern gesehen* → ✗ *I have seen it yesterday*; *yesterday* erzwingt Past Simple; „Wurde eine Zeit genannt?" bleibt nur Hinweis (*I've lived here since 2020* — Zeit genannt, trotzdem Perfect); das deutsche *seit* spaltet sich in *since* (Punkt) und *for* (Dauer). |
| EN-07 | will, going to oder geplantes Präsens? | `#tenses` | Gebrauchskontrast, Formen und Beispiele. Offensichtlich: *will* ≈ *werden* (Konzeptpaar); der Fahrplan im Präsens funktioniert in beiden Sprachen (*The train leaves at 6* ≈ *Der Zug fährt um 6*). Fallen: *going to* hat kein deutsches Pendant — die Entscheidung vorher beschlossen vs. spontan ist Neustoff; der pauschale werden-Kalk für jede Zukunftsform ist der vorhersehbare Fehler. |
| EN-08 | Wie werden Modals und have to verwendet? | `#verbs` | Formen, hochfrequente Bedeutungen und mustn't versus don't have to. Offensichtlich: das deutsche Modalparadigma mapt direkt (können→can, müssen→must, dürfen→may/be allowed to, sollen→should); der müssen-Schluss (*Er muss müde sein* ≈ *He must be tired*) existiert in beiden Sprachen. Fallen: *muss nicht* ≠ *must not*! *muss nicht* = *don't have to* (keine Verpflichtung), *must not/mustn't* = *darf nicht* (Verbot) — der schärfste False Friend des Decks; das Beispielpaar trägt den Punkt. |
| EN-09 | Wie wird das Passiv gebildet? | `#verbs` | be + V3-Muster in den explizit gezeigten Zeiten mit Beispielen; keine „alle Zeiten"-Behauptung ohne Abdeckung. Offensichtlich: werden + Partizip II → be + V3 ist ein Auxiliarwechsel (*Das Haus wird gebaut* ≈ *The house is being built*). Fallen: *von* deckt of, from UND by ab — der Agens-Kalk ✗ *built from the workers* (richtig: *by*); nur die gezeigten Zeiten behaupten. |
| EN-10 | Welche Verben nehmen V-ing oder to + Verb? | `#verbs` | Gelistete hochfrequente Muster und Beispiele; bedeutungsändernde Fälle markiert. Offensichtlich: *want to do* ≈ *wollen, … zu tun* (zu + Infinitiv ≈ to + Grundform). Fallen: das Deutsche hat kein Gerundium — *enjoy doing* ist reiner Neustoff; *stop smoking* (aufhören) vs. *stop to smoke* (anhalten, um zu rauchen) als bedeutungsänderndes Paar; *look forward to* + -ing (✗ *I look forward to see you* — Kalk aus *sich freuen, dich zu sehen*). |
| EN-11 | Welche Präposition drückt Zeit oder Ort aus? | `#preps` | in/on/at-Kontraste mit Beispielen und wesentliche Ausnahmen. Offensichtlich: *in* ≈ *in* (räumlich, Großräume: *in Berlin*). Fallen: fast jede Zeitangabe kippt — *am Montag* → *on Monday* (am = on bei Tagen), *um 5 Uhr* → *at 5 o'clock*, *in der Nacht* → *at night*, *am Wochenende* → *at the weekend* (BrE) / *on the weekend* (AmE); deutsch *an* deckt at UND on ab (*am Bahnhof / an der Wand*) — die Zuordnung ist Neulernen; *at home* ≈ *zu Hause*, *at the station* ≈ *am Bahnhof*. |
| EN-12 | Welche abhängige Präposition folgt auf ein Wort? | `#preps` | Alle gelisteten Kombinationen mit Beispielen; keine Behauptung eines erschöpfenden Lexikons. Offensichtlich: Deutsche trainieren feste Verbpaare bereits (*warten auf*, *denken an*) — die Lerntechnik ist vertraut. Fallen: die englische Präposition wechselt fast nie 1:1 — *warten auf* → *wait for*, *denken an* → *think of/about*, *sich freuen auf* → *look forward to* + -ing, *abhängen von* → *depend on*, *teilnehmen an* → *take part in*. |
| EN-13 | Wie werden regelmäßige und hochfrequente unregelmäßige Plurale gebildet? | `#nouns` | Kernregeln, gelistete Unregelmäßige und Zählbarkeits-Vorbehalt. Offensichtlich: die gute Nachricht zuerst — EINE -s-Regel gegen fünf deutsche Pluralmuster (*Kind/Kinder, Haus/Häuser* → *house/houses*); *child/children* ist als englische Reliktform wiedererkennbar. Fallen: im Englischen unzählbar, im Deutschen zählbar — *Informationen* → *information* (kein -s!), *Knowledges* → *knowledge*, *Softwares* → *software*; dazu *news, advice, money*. |
| EN-14 | Ist ein Nomen zählbar, und welches Quantorwort gilt? | `#nouns` | much/many/few/little und some/any mit Interferenzfallen für Deutschsprachige. Offensichtlich: *viel/viele* mapt auf *much/many* — die Zählbarkeitsentscheidung ist aus dem Deutschen vertraute Arbeit (*viel Zeit / viele Freunde*); *few/little* ≈ *wenige/wenig*. Fallen: dieselben Schein-Unzählbaren wie EN-13 (✗ *How much people?*); *some* in Angeboten und Bitten, *any* in Verneinung und Fragen — diese Teilzuordnung ist Neulernen. |
| EN-15 | Wie werden Komparativ und Superlativ gebaut? | `#nouns` | Kernmuster, Rechtschreibgrenzen und hochfrequente Unregelmäßige. Offensichtlich: *gut–besser–am besten* = *good–better–best* — dasselbe Unregelmäßigentrio; *schneller* = *faster*. Fallen: deutsch *als* heißt *than* UND *as* — *bigger THAN* (*größer als*), *as big AS* (*so groß wie*); ✗ *bigger as* ist der vorhersehbare Fehler; Doppelsteigerung (✗ *more better*) — universeller A1-Fehler, kein deutscher Kalk; Rechtschreibregeln (*big → bigger, happy → happier, nice → nicer*). |
| EN-16 | Welcher Bedingungssatz drückt Fakt, reale Zukunft, unrealistische Gegenwart oder unrealistische Vergangenheit aus? | `#conditionals` | Typen 0–2 Kern; Typ 3 recognition; Bedeutung und Form für jeden gezeigten Typ. Offensichtlich: Typ 2 ist strukturell Konjunktiv II — *If I had time, I would help* ≈ *Wenn ich Zeit hätte, würde ich helfen*; *were* für alle Personen. Fallen: nach *if* steht kein will (*Wenn es regnen wird, …* → *If it rains, …* — das Deutsche erlaubt Futur im wenn-Satz, das Englische nicht: ✗ *If it will rain*); deutsch *wenn* deckt if UND when/whenever ab — die Aufteilung ist Neulernen (*If I have time* = falls · *When I have time* = wenn/immer wenn). |
| EN-17 | Welches Tönungswort trägt den Ton? just, actually, still, even, though | `#order` | Hochfrequentes Set mit deutschen Entscheidungsäquivalenten; begrenztes Set (EN-X02). Hier verdichtet sich die False-Friend-Zone: *actually* ≠ *aktuell* (*aktuell* = *current*); *even* ≠ *eben* (*even* = *sogar*); *just* = *gerade eben* ODER *bloß* (zwei Bedeutungen trennen); *still* vs. *yet* (*immer noch* = *still*, *noch nicht* = *not yet*); *though* am Satzende (≈ *doch*) hat keine deutsche Endposition — die Position selbst ist Neustoff. |
| EN-18 | Welches Konnektorwort verbindet die Sätze? but/however, so/therefore, meanwhile, nevertheless, although/despite | `#order` | Kernkonnektoren mit deutschen Äquivalenten; *despite* + Nomen vs. *although* + Satz; nach Verneinung *not X, but Y* = *nicht A, sondern B* (das sondern-Paar, 1:1) und *not only … but also* = *nicht nur …, sondern auch* im Linker-Dialog; begrenztes Set (EN-X02). Offensichtlich: die despite/although-Aufteilung EXISTIERT im Deutschen (*trotz* + Nomen vs. *obwohl* + Satz) — transferfreundlich; *meanwhile* = *währenddessen*, *nevertheless* = *trotzdem*. Fallen: *also* ≠ *also*! (deutsches *also* = *so/therefore*; englisches *also* = *auch*; ✗ *Also, I went…* für „Also bin ich gegangen"); Register und Komma bei *however*. |
| EN-19 | there is oder there are? | `#order` | is/are-Wahl, Verneinung und Fragen ohne do (be, nicht do-support); There's vs It's; was/were. Offensichtlich: Verneinung und Frage über be laufen wie deutsche Umkehrung. Fallen: *es gibt* deckt is UND are ab, ohne Pluralunterscheidung → ✗ *There's many people* ist der Kalk-Fehler (*There are two shops*); *There's* vs. *It's* (*es gibt* vs. *das ist*). |
| EN-20 | Past Continuous — wann? | `#tenses` | was/were + V-ing als Hintergrund vs. Past-Simple-Ereignis; parallele Handlungen; die deutsche Abbildung über *gerade*. Offensichtlich: *war/were* ≈ *war/waren* — direktes Wortpaar. Fallen: keine deutsche Verlaufsform — Deutsch markiert den Verlauf mit *gerade* (*Ich kochte gerade, als er kam*): *gerade* ≈ Past Continuous, der Nebensatz im Präteritum ≈ Past Simple; *while* = *während* — dieselbe Zeit-und-Kontrast-Doppelnutzung wie im Deutschen (transfer). |
| EN-21 | Wie verneine ich? | `#verbs` | don't/doesn't/didn't + Grundform; never ohne not; no + Nomen vs. not any. Offensichtlich: *no* + Nomen = *kein* (*I have no money* ≈ *Ich habe kein Geld* — 1:1); *never* ist bereits Verneinung, wie deutsch *nie* — die Doppelverneinungs-Falle der en-ru-Fassung (russisch «никогда не») existiert im Deutschen nicht und entfällt. Fallen: do-support in der Verneinung — Deutsch negiert das Verb direkt (*Ich sehe es nicht*), Englisch verlangt don't/doesn't/didn't + Grundform (✗ *I see not*); das *not* steht nach dem Auxiliar, nicht wie das deutsche *nicht* im Mittelfeld. |
| EN-22 | Present Perfect Continuous — wann? | `#tenses` | Recognition: have/has been + V-ing = Dauer bis jetzt oder frischer Beweis; vs. Present-Perfect-Ergebnis; Zustandsverben ohne -ing. Fallen: der seit-Satz — *Ich wohne hier seit zwei Jahren* → *I have been living here for two years*; Deutsche wählen das Präsens (✗ *I live here since two years* — Doppelkalk: falsche Zeit UND *since* statt *for*). |
| EN-23 | Relativsätze: who / which / that? | `#verbs` | Wahl nach Nomentyp; whose/where; Objekt-that-Auslassung; Kongruenz mit dem Bezugswort. Offensichtlich: *whose* = *dessen/deren* — das überlebende Genitiv-Relativ; *where* = *wo*. Fallen: der/die/das markieren Genus und Kasus, NICHT belebt/unbelebt → ✗ *The man which…* ist der typische deutsche Fehler; die who/which/that-Entscheidung ist Neulernen; *that* darf entfallen und das Komma entfällt im restriktiven Satz — das Deutsche setzt immer das Komma und lässt nie weg (*der Mann, den ich kenne* → *the man (that) I know*); die Präposition darf hinten bleiben (*the house I live in* statt *in dem ich wohne* vorn). |
| EN-24 | Imperativ? | `#verbs` | Grundform ohne Subjekt; please + Grundform (kein to); Don't + V1; Let's / Let's not. Offensichtlich: EINE Befehlsform für alle — wo Deutsch du-, ihr- und Sie-Form unterscheidet, vereinfacht Englisch (*Komm!/Kommt!/Kommen Sie!* → *Open!*); *Let's* = *Lass uns* (1:1); *Don't open it* = *Öffne es nicht*. Fallen: die deutsche Sie-Form trägt das Pronomen mit (*Setzen Sie sich*) → ✗ *Sit you down please* — im Englischen fällt das Subjekt; *bitte* ohne to. |
| EN-25 | while / whereas / on the other hand? | `#order` | Zwei-Satz-Kontrast: while (auch Zeit), whereas (formell), on the other hand (Registerpaar); begrenztes Set. Offensichtlich: *while* = *während* — dieselbe Zeit-und-Kontrast-Doppelnutzung wie im Deutschen (der leichteste Transfer des Decks); *whereas* ≈ *wohingegen*; *on the other hand* = *zum anderen/andererseits*. Bleibt Required, weil die Registerentscheidung (while vs. whereas vs. on the other hand) auch für Deutschsprachige eine echte Wahl ist. |
| EN-26 | Zahlen und Daten? | `#nouns` | Ordnungszahlen (first/second/third; die Schreibfallen fifth/twelfth/ninth), Daten on 5 May / on the 5th of May, Jahre und Jahrzehnte. Offensichtlich: Jahrzehnte *the 90s* ≈ *die 90er*; das paarweise Lesen der Jahre ist ähnlich (*nineteen eighty-five* ≈ *neunzehnhundertfünfundachtzig*). Fallen: die Ordinalsuffixe 1st/2nd/3rd und die Schreibfälle *fifth, twelfth, ninth* sind neu (deutsch regulär *fünfte*); die Datumspräposition ist *on* (*am 5. Mai* → *on 5 May*); das deutsche Datumsformat mit Punkt (*5. Mai*) → *5 May*. |

## Abnahme und Wartung

- **Diese Seite wird generiert**: `en/de/index.html` wird aus
  [`content/decks/en-de.json`](../../content/decks/en-de.json) gerendert —
  in der nächsten Phase gegen diesen Plan erstellt, nach den Konventionen
  des Geschwister-Decks, wie sie an dem Tag stehen — mit
  `python3 tools/build_pages.py content/decks/en-de.json`. Das Deck
  editieren, nicht das HTML; beides regenerieren und committen. `--check`
  schlägt fehl, wenn sie driften.
- **Registry-Edit ersetzt, statt nur zu ergänzen**: `content/decks/site.json`
  trägt beim Target `en` heute einen vorregistrierten Selbstpaar-Platzhalter
  (`en`/`en`, `"soon": true`) — ein Selbstpaar ist laut ROADMAP-Quellenmodell
  out of scope, aber `--check-shell` ignoriert `soon`-Einträge
  (`tools/shell_check.py`), also flaggt kein Gate den Stolperstein. Der
  Schritt-4-Edit für dieses Deck ERSETZT den veralteten `en/en`-soon-Eintrag
  durch `{id: "de", script: "latin"}`; nur symmetrisch angewandt (wie beim
  de-en-Flip bloß „soon droppen") würde ein Menü-Link auf die nicht
  existierende en/en-Seite live gehen. Der Landing-Spiegel (`DECKS` +
  Menü-Markup in `index.html` — dort steht `en` schon korrekt ohne en/en)
  zieht mit, und alle Deck-Seiten werden neu gerendert; danach `CACHE_VERSION`
  in `sw.js` heben (harte Regel 9).
- Diesen Plan revidieren, bevor akzeptierter Scope, Ausschlüsse,
  Inhaltstiefe, Practice-Mapping, View-Zugehörigkeit oder stabile Anker
  geändert werden.
- Unaufgelöste Vorschläge im Content-Audit halten. Erst nach einer
  akzeptierten Required-, Deferred- oder Excluded-Entscheidung hierher
  promoten.
- [Content-Validierung](../../docs/CONTENT_VALIDATION.md) nach
  Inhaltsänderungen anwenden und die rezensierte Revision, Quellen, Findings
  und Gate-Ergebnisse in `CONTENT_AUDIT.md` festhalten. Das `en-de`-Deck ist
  ein neues Deck: Es durchläuft die volle Inhaltsrezension, keine Übernahme
  von `en-ru`.
- [AGENTS.md](../../AGENTS.md) für gemeinsame Seitenänderungs- und
  Runtime-Checks folgen. Ein Runtime-Durchlauf begründet keine
  Inhaltsakzeptanz.
