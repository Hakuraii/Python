#CPO
#QCM

score = 0

rep = int(input("Tu es dans une ruelle, tu entends un bruit, que fais du tu ? \n1. Je m'enfui en courant.\n2. Je prends mon courage à deux mains.\n\nRéponse : "))

if(rep == 1):
    score = score + 10
elif(rep == 2):
    score = score + 5

print(score)