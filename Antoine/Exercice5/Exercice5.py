#CPO
#Exercice 5 : Tables de multiplication

nombre = int(input("Choisissez la table voulue ? "))

print("\n\nCalcul de la table de", nombre)

for i in range(1, 11):
    print("\n", i, "x", nombre, "=", (nombre * i))

input("\n\nAppuyer sur entrer pour quitter...")