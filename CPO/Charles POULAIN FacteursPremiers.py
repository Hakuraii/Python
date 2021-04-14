#CPO
#Facteurs premiers

def facteurs(nb):
    if(nb == 1):
        return "Vous avez rentré 1 qui n'est pas décomposable !"
    else:
        d = 2
        F = []
        while(d < nb + 1):
            while(nb % d == 0):
                F.append(d)
                r = nb // d
                nb = r
            d += 1
        return F

nombre = int(input("Choisir un nombre entier : "))
affichage = str(facteurs(nombre)).replace(",", " *").replace("[", "").replace("]", "")

print(nombre, " = ", affichage)