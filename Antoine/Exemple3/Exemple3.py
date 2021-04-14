#CPO
#Exemple 3 : Antoine boucle For

nombre = int(input("Quelle table voulez vous afficher ? "))

print("\nCalcul de la table de", nombre)

for i in range(1,11):
    calcul = i * nombre
    print(i,"*",nombre,"=",calcul)

input("Appuyer sur entrer pour quitter...")