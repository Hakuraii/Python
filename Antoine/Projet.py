#AP
#Projet_Dofus_rentablité


def Renta(bene, xp):
    Rentabilite = bene + xp * 10
    return Rentabilite

tableau = []

couts = 0
r = "o"
while( r !="n" ):
    couts += int(input("Couts element de recette : "))
    r = str(input( "Encore  ? "))

PrixDeVente = int(input("Prix de vente de la ressource voulu : "))

XpGagné = int(input("Combien d'xp ?"))


print("couts", couts)
print("Prix de vente", PrixDeVente)
benefice = PrixDeVente - couts
print ("Bénéfice", benefice)

print ("Rentabilité", Renta(benefice, XpGagné))