#CPO
#Codage affine p226

alphabet = "abcdefghijklmnopqrstuvwxyz"

mot = str(input("Saisir le mot : "))

nouveaumot = ""

choix = int(input("Coder ou décoder ? 1/2 "))
while(choix != 1 and choix != 2):
    print("Erreur, choix incorrect.")
    choix = int(input("Coder ou décoder ? 1/2 "))

if(choix == 1):
    for i in range(0, len(mot)):
        if(mot[i] not in alphabet):
            nouveaumot = nouveaumot + mot[i]
        else:
            indice = alphabet.index(mot[i])
            nouvelindice = (indice + 3) % 32
            nouveaumot = nouveaumot + alphabet[nouvelindice]
else:
    for i in range(0, len(mot)):
        if(mot[i] not in alphabet):
            nouveaumot = nouveaumot + mot[i]
        else:
            indice = alphabet.index(mot[i])
            nouvelindice = (indice - 3) % 32
            nouveaumot = nouveaumot + alphabet[nouvelindice]

print("\n",nouveaumot)