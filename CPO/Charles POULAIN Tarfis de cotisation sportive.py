#CPO
#Tarifs de cotisation sportive

Tarifs = {"Senior (21 ans et +)" : 233, "Junior (18 à 20 ans)" : 203, "Cadet (16 à 17 ans)" : 175, "Minime (14 à 15 ans)" : 149, "Benjamin (12 à 13 ans)" : 125, "Poussin (9 à 11 ans)" : 103, "Pousset (7 à 9 ans)" : 83}

print("Les différentes catégorie disponible sont :\n")

for Categorie in Tarifs:
    print(Categorie)

Cat = input("\nQuelle est votre catégorie ? \n")

for Categorie in Tarifs:
    T = Categorie.split(" ")
    if T[0] == Cat:
        Cotisation = Tarifs[Categorie]

if "Cotisation" in locals():
    print("\nVotre cotisation s'élève à", Cotisation, " euros.")
else:
    print("La catégorie renseignée est incorrecte.")