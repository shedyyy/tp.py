    BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue: "))
print("Pour faire une fondue fribourgeoise pour" , nbConvives , "personnes, il vous faut :")
print("-" , fromage * nbConvives / BASE , "gr de fromage")
print("-" , eau * nbConvives / BASE , "dl d'eau")
print("-" , ail * nbConvives / BASE , "gousse(s) d'ail")
print("-" , pain * nbConvives / BASE , "gr de pain")