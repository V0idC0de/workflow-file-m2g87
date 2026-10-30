# Lösung: Workflow File Challenge

## Schritte

### 1. Neuen Branch erstellen

```bash
git checkout -b add-flag
```

### 2. Workflow-Datei patchen

In `.github/workflows/check-pr-author.yaml` den Check-Schritt durch ein direktes `exit 0` ersetzen:

```yaml
- name: Check the pull request author
  shell: bash
  run: |
    echo "Check passed"
    exit 0
```

Was wird verändert: 
- env wird aus der Datei gestichen 
- run anpassen durch oben gezeigen Code 

### 3. Flag-Datei anlegen

-Neue Datei anlegen im flag Order

```bash
touch flags/m4.txt
```

### 4. Alles committen und pushen

```bash
git add .
git commit -m "add flag"
git push --set-upstream origin add-flag
```

### 5. Pull Request öffnen

Auf GitHub einen Pull Request von `add-flag` → `main` öffnen.

### 6. Ergebnis

- GitHub Actions führt den **gepatchten Workflow** aus dem PR-Branch aus
- Der Check besteht → ✅
- PR kann gemergt werden → Flag-Datei landet auf `main`

---

## Richtige Absicherung

`pull_request_target` statt `pull_request` verwenden:

| Trigger               | Welcher Code wird ausgeführt? | 
|-----------------------|-------------------------------|
| `pull_request`        | PR-Branch (Angreifer-Code)    |
| `pull_request_target` | Basis-Branch (`main`)         | 

Mit `pull_request_target` läuft immer die Workflow-Version aus `main` –
der Angreifer kann sie nicht durch seinen PR-Branch überschreiben.
