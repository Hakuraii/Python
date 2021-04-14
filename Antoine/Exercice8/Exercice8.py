#CPO
#Exercice 8 : Antoine les tableaux et while

print("\t\t--Liste de course--")

courses = []
rep = str(input("Voulez vous créer une liste de course ? (O/N) "))

while(rep.lower() == "o"):
    courses.append(input("Ajouter un aliment a votre panier : "))
    rep = str(input("Voulez vous rajouter un aliment ? (O/N) "))

if(len(courses) > 0):
    print("\nVotre liste de courses : \n", courses)

print("\nBonne journée !")
input()