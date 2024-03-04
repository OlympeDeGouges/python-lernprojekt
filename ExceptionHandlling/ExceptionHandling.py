"""
1.	Schreibe eine Funktion, die eine Datei einliest.
Die Funktion sollte in der Lage sein, mit Situationen umzugehen,
in denen die Datei nicht existiert, und eine benutzerdefinierte Fehlermeldung ausgeben.
2.	Erweitere die Funktion, indem du die Zeilen der Datei einliest
und die Anzahl der Wörter pro Zeile zählst. Gib ein Dictionary zurück,
dass die Zeilennummern und die entsprechende Anzahl der Wörter enthält.
3.	Füge eine weitere Funktionalität hinzu, die es ermöglicht,
nach einem bestimmten Wort in der Datei zu suchen und die Zeilennummern auszugeben,
in denen das Wort vorkommt.
"""

def lese_datei_zahle_woerter(dateipfad, suchwort=None):
    try:
        zeilen_wörter_zähler = {}
        zeilen_mit_suchwort = []
        with open(dateipfad, 'r') as datei:
            for zeilennummer, zeile in enumerate(datei, start=1):
                wörter = zeile.split()
                zeilen_wörter_zähler[zeilennummer] = len(wörter)

                if suchwort and suchwort in wörter:
                    zeilen_mit_suchwort.append(zeilennummer)

        if suchwort:
            return zeilen_wörter_zähler, zeilen_mit_suchwort
        else:
            return zeilen_wörter_zähler
    except FileNotFoundError:
        return f"Die Datei unter '{dateipfad}' konnte nicht gefunden werden."

dateipfad = "datei.txt"
suchwort = "Python"

ergebnis = lese_datei_zahle_woerter(dateipfad, suchwort)
print(ergebnis)
