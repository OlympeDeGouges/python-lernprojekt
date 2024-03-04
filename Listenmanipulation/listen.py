"""
1.	Gegeben sei eine Liste von Dictionaries, wobei jedes Dictionary Informationen über einen Studenten enthält
(z.B. Name, Matrikelnummer, und Noten in verschiedenen Fächern).
2.	Schreibe eine Funktion, die die Durchschnittsnote jedes Studenten
berechnet und diese Information in einem neuen Dictionary zusammen mit dem Namen und der Matrikelnummer speichert.
3.	Sortiere die Liste der neuen Dictionaries basierend auf der Durchschnittsnote in absteigender
Reihenfolge und drucke die Informationen jedes Studenten aus.
"""

studenten_info = [
    {"name": "David Petry", "matrikelnummer": "123456", "note": [1, 2, 1, 2, 1]},
    {"name": "Daniel Hetzenauer", "matrikelnummer": "456789", "note": [1, 3, 2, 2, 1]},
    {"name": "Tatjana Brankovic", "matrikelnummer": "741852", "note": [1, 2, 3, 2, 3]}
]

#note berechnen

def durchschnitt_und_speichern(studenten_liste):
    ergebnis_liste = []
    for student in studenten_liste:
        durchschnitt = sum(student["note"]) / len(student["note"])
        ergebnis_liste.append({
            "name": student["name"],
            "matrikelnummer": student["matrikelnummer"],
            "durchschnittsnote": durchschnitt
        })
    return ergebnis_liste

def sort_und_drucke(studenten_liste):
    sortierte_liste = sorted(studenten_liste, key=lambda x: x["durchschnittsnote"], reverse=True)
    for student in sortierte_liste:
        print(f"Name: {student['name']}, Matrikelnummer: {student['matrikelnummer']}, Durchschnittsnote: {student['durchschnittsnote']:.2f}")

neue_studenten_info = durchschnitt_und_speichern(studenten_info)
sort_und_drucke(neue_studenten_info)
