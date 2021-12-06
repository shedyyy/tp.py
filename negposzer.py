nmbent = int(input("Entrez un nombre entier: "))
if nmbent == 0:
    print("Le nombre est zéro(et il est pair)")
if nmbent > 0 and (nmbent % 2 == 0):
    print("Le nombre est positif et pair")
if nmbent > 0 and (nmbent % 2) == 1:
    print("Le nombre est positif et impair")
if nmbent < 0 and (nmbent % 2) == 0:
    print("Le nombre est négatif et pair")
if nmbent < 0 and (nmbent % 2) == 1:
    print("Le nombre est négatif et impair")


