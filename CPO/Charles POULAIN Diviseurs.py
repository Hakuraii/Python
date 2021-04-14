#CPO
#Diviseurs d'un nombre entier naturel

diviseursnb = []

def diviseurs(nb):
    for i in range(1, nb+1):
        if(nb % i ==0):
            diviseursnb.append(i)

nombre = int(input("Choisir un entier naturel : "))

diviseurs(nombre)

print("Les diviseurs de",nombre," sont : ")
print(diviseursnb)