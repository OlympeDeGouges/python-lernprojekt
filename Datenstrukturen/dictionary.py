"""
1. Erstelle ein Wörterbuch, das verschiedene Datentypen speichert,
z.B. name, age, languages ((eine Liste der Programmiersprachen,
die du kennst), und has_python_experience  (ein Boolean, der angibt, ob du Erfahrung mit Python hast:
2. Schreibe eine Funktion, die dieses Wörterbuch als Argument nimmt
und die Informationen in einer formatierten Weise in eine Textdatei schreibt.
"""

# Wörterbuch erstellen
person_info = [
    {
        "name": "David Petry",
        "age": 25,
        "languages": ["Python", "Java", "C", "C++"],
        "has_python_experience": True
    },
    {
        "name": "Daniel Hetzenauer",
        "age": 30,
        "languages": ["Python", "Java"],
        "has_python_experience": True
    }
]

def write_multiple_person_info_to_file(person_list, file_name="Persons_info.txt"):
    with open(file_name, "w") as file:
        for person in person_list:
            file.write(f"Name: {person['name']}\n")
            file.write(f"Alter: {person['age']}\n")
            file.write(f"Programmiersprachen: {', '.join(person['languages'])}\n")
            file.write(f"Python-Erfahrung: {'Ja' if person['has_python_experience'] else 'Nein'}\n")
            file.write("\n")

write_multiple_person_info_to_file(person_info)

# Rückgabe des korrigierten Pfads
"Persons_info.txt"
