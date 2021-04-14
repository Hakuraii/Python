#CPO
#Conseil de classe
import math

count = 1
Notes = []
while count != 31:
    note = int(input("Note ?\n"))
    Notes.append(note)
    count += 1

moyenne = sum(Notes) / len(Notes)

print("\nMoyenne :", round(moyenne, 2))

NoteMin = min(Notes)
NoteMax = max(Notes)

print ("\nNote mini :", NoteMin)
print ("Note maxi :", NoteMax)

Etendue = NoteMax - NoteMin

print("\nEtendue :", Etendue)

NoteInfDix = sum(map(lambda x: x<10, Notes))

print("\nNombre de notes inferieurs a dix :", NoteInfDix)

Medianne = Notes[math.ceil((len(Notes) + 1) / 2)]

print("\nLa valeur médianne est :", Medianne)

while Notes.count(NoteMin) > 0:
    Notes.remove(NoteMin)
while Notes.count(NoteMax) > 0:
    Notes.remove(NoteMax)

moyenne = sum(Notes) / len(Notes)

print("\nMoyenne élaguée :", round(moyenne, 2))