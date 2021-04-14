#CPO
#Sommes des cubes

def sommescubes(chiff):
    chiffstr = str(chiff)
    somme = 0

    for nombre in chiffstr:
        somme += int(nombre)**3
    
    return somme

print(sommescubes(int(input("Choisir un nombre : "))))