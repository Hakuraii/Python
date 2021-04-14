#CPO
#Temps de vol par la suite de syracuse

#Définition de la fonction temps de vol
def tempsVol(n):
    #Initialisation du tableau
    tempsDeVol = [n]
    #Tant que la dernière valeur indexée de tempsDeVol est différente de 1
    while(tempsDeVol[len(tempsDeVol) - 1] != 1):
        #Si la dernière valeur de tempsDeVol modulo 2 est strictement égale à 0
        if(tempsDeVol[len(tempsDeVol) - 1]%2 == 0):
            #On ajoute la dernière valeur divisée par deux à tempsDeVol
            tempsDeVol.append(tempsDeVol[len(tempsDeVol) - 1] / 2)
        else:
            #Sinon on la multiplie par 3 et on ajoute 1 pour l'ajouter ensuite au tableau
            tempsDeVol.append(tempsDeVol[len(tempsDeVol) - 1] * 3 + 1)
        print(tempsDeVol)
    #Création du résultat compsé de la longueur du tableau tempsDeVol - 1, et de la valeur max de ce dernier
    result = [len(tempsDeVol) - 1, sorted(tempsDeVol)[len(tempsDeVol) - 1]]
    return result

nb = int(input("Veuillez choisir un nombre : "))
print(tempsVol(nb))