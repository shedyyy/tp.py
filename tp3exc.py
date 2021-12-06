cpt1 = 0
cpt2 = 0
cpt3 = 0
for i in range(10) :
    x = int(input("Saisis les 10 valeurs: "))
    while x not in range(21):
        print("")
        x = int(input("Saisis les 10 valeurs: "))

    if x < 10:
        cpt1 +=1
        print(x, "strictement inferieur a 10")
    elif x >= 10 and x <= 15:
        cpt2 +=1
        print(x, "est entre 10 et 15")
    else:
        x > 15
        cpt3 +=1
        print(x, "superieur a 15")
print(cpt1,"strictement inferieur a 10," ,cpt2, "entre 10 et 15,",cpt3, "superieur a 15.")