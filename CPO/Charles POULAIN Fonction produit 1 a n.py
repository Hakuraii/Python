#CPO
# 3 : Fonction produit de 1 à n

def produit(n):
    somme = 1
    for i in range(1,n+1):
        somme *= i
    return somme

n = int(input("Choisissez n : "))

print("Produit des entier de 1 à", n, " :",produit(n))