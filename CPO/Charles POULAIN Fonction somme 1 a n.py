#CPO
# 2 : Fonction somme de 1 à n

def somme(n):
    somme = 0
    for i in range(1,n+1):
        somme += i
    return somme

n = int(input("Choisissez n : "))

print("Somme des entier de 1 à", n, " :",somme(n))