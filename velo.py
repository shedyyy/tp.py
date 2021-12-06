h_tarif1=1
h_tarif2=0
while True:
    debut=int(input("Donnez l’heure de début de la location (un entier) : "))
    fin=int(input("Donnez l’heure de fin de la location (un entier) : " ))
    if (debut==fin):
        print("Attention ! l’heure de fin est identique à l’heure de début.")
    elif (debut > 24 or debut < 0 or fin < 0 or fin > 24):
        print("Les heures doivent être comprises entre 0 et 24 !")
    elif (debut>fin):
        print("Attention ! le début de la location est après la fin ...")
    else:
        break

print("Vous avez loué votre vélo pendant")
for i in range(debut,fin):
    if (i < 7 or i >= 17):
        h_tarif1+=1
    else:
        h_tarif2+=1
if (h_tarif1 > 0):
    print(h_tarif1 , "heure(s) au tarif horaire de 1.0 euro(s)")
if (h_tarif2 > 0):
    print(h_tarif2 , "heure(s) au tarif horaire de 2.0 euro(s)")
    print("Le montant total à payer est de" , (h_tarif1 + h_tarif2 * 2) , "euro (s).")