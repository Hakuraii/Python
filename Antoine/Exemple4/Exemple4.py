#CPO
#Exemple 3 : Tableaux

from random import *

nombres = []

longueur = int(input("La longueur du tableau : "))

for i in range(1,longueur+1):
    nombres.append(randint(1,20))

print(nombres)
print(min(nombres))
print(max(nombres))
moyenne = round((sum(nombres) / len(nombres)),2)
print(moyenne)