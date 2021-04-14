#CPO
#Sommes des cubes v2

def sommescubesv2(chiff):
    if(chiff % 3 != 0):
        return "Chiffre non divisible par 3."
    else:
        chiffstr = str(chiff)
        somme = 0
        for nombre in chiffstr:
            somme += int(nombre)**3
        return somme

chiffre = sommescubesv2(int(input("Choisir un chiffre : ")))
boucle = 1
while chiffre != 153 and (type(chiffre) is not str):
    chiffre = sommescubesv2(chiffre)
    boucle += 1

print(chiffre)
print("La boucle a tourné", boucle, "fois")