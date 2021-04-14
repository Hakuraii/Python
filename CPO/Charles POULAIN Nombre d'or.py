#CPO
#Nombre d'or

from random import randrange

nombre = int(input("Choisir un nombre à 3 chiffres : "))
#nombre = randrange(100, 1000)

def echange(nombre):
    s = ''
    nombreStr = str(nombre)
    nombreRev = []
    for i in range(len(nombreStr)-1, -1, -1):
        nombreRev.append(str(nombreStr[i]))
    return int(s.join(nombreRev))

nombreRev = echange(nombre)
newNombre = 0

if(nombre > nombreRev):
    newNombre = nombre - nombreRev
else:
    newNombre = nombreRev - nombre

newNombreRev = echange(newNombre)


print(newNombre + newNombreRev)

#On constate que peut importe le nombre à 3 chiffres rentré on retombe sur 1089
#Quand le chiffre des unités = 0 le résultat est 198