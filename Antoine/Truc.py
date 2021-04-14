#AP
#EXPERIMENTATION

Tableau = []

Tableau.append (str(input("Parmis ces couleurs laquelle préférez vous ? : Bleue  Rouge  Vert ")))
Tableau.append (str(input("Parmis ces pokemon, lequelle choisissez vous ? : Bulbizar  Carapuce Salamèche ")))
Tableau.append (str(input("Parmis ces son lequelle detestez-vous le plus ? : Tableau qui grince   Ballon de baudruche   Jul ")))
Tableau.append (str(input("Parmis ces aliments lequelle aimez vous le plus ? : Sushis  Frite  Nutella ")))
Tableau.append (str(input("Comment vous sentez-vous vis-a-vis des autres ? : Supérieur  Pareil  Inférieur  Différent ")))

score = 0

#if (Tableau[0] == "Bleue" ):
#    score = score + 0
if (Tableau[0] == "Rouge" ):
#    score = score - 1
    score -= 1
elif(Tableau[0] == "Vert") :
#   score = score + 2
    score += 2

if (Tableau[1] == "Bulbizar"):
#    score = score + 1
    score += 1
elif(Tableau[1] == "Carapuce"):
#    score = score + 1
    score += 1
elif(Tableau[1] == "Salamèche"):
#    score = score + 1
    score += 1

if (Tableau[2] == "Tableau qui grince"):
#    score = score + 1
    score += 1
elif(Tableau[2] == "Ballon de baudruche"):
#    score = score - 1
    score -= 1
elif(Tableau[2] == "Jul"):
#    score = score + 1
    score += 1

if (Tableau[3] == "Sushis"):
#    score = score + 4
    score += 4
elif(Tableau[3] == "Frite"):
#   score = score + 2
    score += 2
elif(Tableau[3] == "nutella"):
 #   score = score + 1
    score += 1

if (Tableau[4] == "Supérieur"):
#    score = score - 3
    score -= 3
elif(Tableau[4] == "Pareil"):
#    score = score + 2
    score += 2
#if (Tableau[4] == "Inférieur"):
#    score = score + 0
elif(Tableau[4] == "Différent"):
#   score = score + 1
    score += 1

if (score >7 ):
    print ("\t \n Vous me ressemblez beaucoup")
if (score >4 and score <7 ):
    print ("\t \n On se ressemble un peu")
if (score < 4):
    print ("\t \n on se ressemble tellement pas, par contre ca m'empêche pas de t'aimer <3")

print("\t \n votre score allant de -3 à 10 :")
print("\t\n ",score)