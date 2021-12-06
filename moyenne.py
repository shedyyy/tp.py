nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
notes = []

for moyenne in range(nombreEtudiants):
        while True:
            note = int(input(f"Donnez la note d'étudiant {moyenne}: "))
            if note < 0 or note > 20:
                print("Note entre 0 et 20")
            else:
                break
        notes.append(note)

somme = sum(notes)
moyenne = somme / nombreEtudiants

print("Moyenne de classe:" , round(moyenne,2) , "\n")

print("Numéro de l'étudiant | note | ecart a la moyenne")
for x in range(nombreEtudiants):
    ecart = notes[x] - moyenne
    print(x, "|", notes[x] , "|" , round(ecart,3))
