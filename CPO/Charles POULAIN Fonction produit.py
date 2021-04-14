#CPO
# 1 : Fonction produit

def produit(a, b):
    return a * b

nombreA = int(input("Choisissez le nombre A : "))
nombreB = int(input("Choisissez le nombre B : "))

produitAB = produit(nombreA, nombreB)

print("Le produit de A et de B est :", produitAB)