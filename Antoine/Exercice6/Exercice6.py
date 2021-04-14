#CPO
#Exercice 6 : Tableaux

from random import *

nombres = []

longueur = int(input("Rentrez une longueur de tableaux : "))

for i in range(1,longueur+1):
    nombres.append(randint(1,20))

print(nombres)
print(max(nombres))
print(min(nombres))
input()