import random
deviner=int(input("Choisissez un nombre: "))
x=random.randint(0,101)
compteur=0
while deviner != x:
    print("Raté")

    if deviner > x:
        print("Plus petit")

    else:
        print("Plus grande")
    print("Vous avez essayé", compteur , "fois")
    deviner = int(input("Essayez de nouveau: "))
    compteur = compteur + 1
print("Vous avez reussi en" , compteur , "essaies")
