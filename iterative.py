f = 1
n = int(input("Valeur: "))
x = 1
a = 0
r = input("1 pour la boucle while 2 pour la for ")
if r != 1:
    while a != n:
        a = a + 1
        x = x * a
        print("La factorielle de",a,"est",x)

else:
    for i in range(1,n+1):
        f = f*i
        print("La factorielle de",i,"est",f)