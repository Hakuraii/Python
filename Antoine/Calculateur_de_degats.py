#AP
#Calculateur_de_dégats_dofus

#Tableau

reponse = []

reponse.append (int(input("Quel sont les dégats minimum de votre sort ? ")))                           #0
reponse.append (int(input("Quel sont les dégats maximum de votre sort ?")))                            #1
reponse.append (int(input("Combien avez vous dans la caractéristique concerné par votre sort ?")))     #2
reponse.append (int(input("Combien avez vous de dommages fixes dans cet éléments ?")))                 #3
reponse.append (int(input("Combien avez vous de % de dommages dans l'élément concerné ?")))            #4

#Calculs
dgtCaraMin = (( reponse[0] / 10 ) * (reponse[2] / 10)) + reponse[0]
dgtCaraMax = (( reponse[1] / 10 ) * (reponse[2] / 10)) + reponse[1]

dgtPourcentMin = (reponse[0] * (reponse[4] / 100))
dgtPourcentMax = (reponse[1] * (reponse[4] / 100))

dgtTotalMin = dgtCaraMin + dgtPourcentMin + reponse[3]
dgtTotalMax = dgtCaraMax + dgtPourcentMax + reponse[3]

#Affichage
print ("dégats suplémentaires minimum grâce aux pourcentages", dgtPourcentMin)
print ("dégats suplémentaires maximum grâce aux pourcentages", dgtPourcentMax)
print ("dégats finaux minimum", dgtTotalMin)
print ("dégats finaux maximun", dgtTotalMax)