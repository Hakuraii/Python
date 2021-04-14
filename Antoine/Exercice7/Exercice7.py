#CPO
#Exercice 7 : Antoine nb mystère

from random import *

random = randint(1,20)

print("\t\t--Nombre mystère de 1 à 20--")

nombreChoisi = int(input("Choisi un nombre : "))

while(random != nombreChoisi):
    if(random < nombreChoisi):
        print("C'est moins.")
    else:
        print("C'est plus.")
    nombreChoisi = int(input("Choisi un nombre : "))

print("\nBravo tu as gagné !")