# Coffee Corp BrewLedger - Workflow File

Coffee Corp verwaltet Kaffeebohnen und Lagerbestände mit **BrewLedger**.
Dieses Repository enthält eine kleine Python-Anwendung, die den Service darstellt.

Der Service ist für diese Challenge allerdings **egal** - eure Aufgabe ist
unter [Ziel](#ziel) beschrieben!

> [!IMPORTANT]
> Dieses Repository ist **public**. Postet keine persönlichen oder anderweitig
> schützenswerten Daten in dieses Repository.

## Ziel

**🚩 Dein Ziel ist es, eine Datei im Verzeichnis `/flags/` auf dem `main`-Branch
anzulegen.**

- ✅ Als Consultant von Coffee Corp hast du bereits `push`-Zugriff auf das
  Repository. Du kannst daher Branches und Commits pushen und sogar **Pull
  Requests mergen**.
- ⚠️ Coffee Corp hat mit Insider Threats gerechnet und einige
  Sicherheitsmaßnahmen eingerichtet.

Die Sicherheitsmaßnahmen sind:

- Auf `main` kann nicht direkt gepusht werden. Das Pushen eines neuen Branches und das
  Öffnen eines Pull Requests sind zwingend erforderlich.
- **Force-Pushes**, mit denen bestehende Commits überschrieben werden könnten,
  sind auf dem `main`-Branch blockiert, auf anderen Branches aber weiterhin
  erlaubt. Dort kann frei gearbeitet werden.
- Das Mergen eines Pull Requests erfordert, dass der Workflow
  `check-pr-author.yaml` erfolgreich abgeschlossen wurde. Details stehen im
  Abschnitt [Check PR Author Workflow](#check-pr-author-workflow).
- Für Pull Requests sind keine manuellen Approvals erforderlich. *Das
  Repository enthält keine `CODEOWNERS`-Datei.*

### Check PR Author Workflow

Dieser Workflow ist die Sicherheitsmaßnahme von Coffee Corp gegen nicht
autorisierte Pull-Request-Autoren. Er prüft den von GitHub bereitgestellten
Login des Pull-Request-Autors.

Ein Login wie `student_coffeecorp` ist erlaubt. Ein Login wie `student` ist
ungültig, weil es nicht auf `_coffeecorp` endet.
Ein Unterstrich im GitHub-Username zeigt, dass dieser Name von einem externen
Identity Provider kommt. Ihr könnt diesen Namen nicht einfach registrieren.

> [!TIP]
> Diese Challenge lässt sich sowohl lokal auf deinem Rechner als auch über den
> Dateieditor im GitHub Repository lösen.

## Git Cheat Sheet

`git` bietet sehr viele Funktionen. Die folgenden Befehle können hilfreich sein:

- `git clone <repository>` kopiert dieses Repository auf deinen lokalen Rechner.
- `git checkout -b <name>` erstellt einen neuen Branch.
- `git add <files>` fügt Dateien zum nächsten Commit hinzu.
- `git commit -m '<your message>'` erstellt einen Commit auf dem aktiven Branch
  mit allen Dateien, die seit dem letzten Commit per `git add` vorgemerkt wurden.
- `git config` konfiguriert `git` nur für das aktuelle Repository. Mit
  `git config --global` würdest du die Einstellung für deinen lokalen Benutzer
  setzen; das ist hier nicht erforderlich.
- `git push --set-upstream origin <name>` pusht einen neuen lokalen Branch in
  das Remote-Repository. Danach reicht für denselben Branch einfach `git push`.

## Repository Layout

- `.github/workflows/check-pr-author.yaml` enthält die erforderliche
  Prüfung des Pull-Request-Autors - dieser Wert ist nicht wirklich manipulierbar...

Alle übrigen Dateien sind kleine Beispieldateien, damit das Repository wie eine
kleine Anwendung aussieht. Sie sind absichtlich einfach gehalten, damit der
Workflow der interessante Teil dieser Übung bleibt.
