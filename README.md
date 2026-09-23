# Flask Blog Application

Ein einfaches Web-Anwendungsprojekt auf Basis von **Python** und **Flask**, das grundlegende CRUD-Funktionalitäten (Create, Read, Update, Delete) für Blogbeiträge demonstriert. Die Speicherung der Daten erfolgt über eine lokale JSON-Datei.

> ⚠️ **WICHTIGER HINWEIS & WARNUNG**
> * **Nicht für den Produktionseinsatz gedacht:** Dieses Projekt ist ausschließlich eine **Lern- und Abgabeaufgabe im Rahmen meines Kurses zur Benotung**. Es erfüllt keine Sicherheits- oder Performance-Standards für den Live-Betrieb.
> * **Anfänger-Projekt:** Ich befinde mich aktuell am Anfang meiner Lernreise mit Python und Flask.
> * **Kein Referenzcode:** Bitte nutze diesen Code **nicht** als Vorlage.

---

## 🚀 Features

* **Anzeigen:** Auflistung aller vorhandenen Blogbeiträge auf der Startseite (`/index`).
* **Erstellen:** Hinzufügen neuer Beiträge über ein Formular (`/add`).
* **Bearbeiten:** Aktualisieren bestehender Beiträge inkl. vorausgefüllter Formularfelder (`/update/<id>`).
* **Löschen:** Entfernen von Beiträgen per `POST`-Anfrage (`/delete/<id>`).
* **Persistenz:** Speicherung aller Einträge in einer JSON-Datei mit UTF-8-Codierung.

---

## 🛠️ Technologien

* **Python 3**
* **Flask** (Micro-Web-Framework)
* **Jinja2** (HTML-Templating)
* **HTML5 & CSS3**

---

## 🏁 Schnellstart / Anwendung ausführen

1. **Repository klonen:**
   ```bash
   git clone [https://github.com/carpenterrollo-ops/masterblog.git](https://github.com/carpenterrollo-ops/masterblog.git)
   cd masterblog

2. **Abhängigkeiten installieren:**
   ```bash
   pip install flask
   

3. **Anwendung über das Terminal starten:**
   ```bash
   python3 app.py
