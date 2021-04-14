#CPO
#Application A p225 Occurence d'une lette dans un message

message = str(input("Messsage : "))
n = len(message)
i = 0
cpt = 0

while(i < n):
    if(message[i] == "a"):
        cpt += 1
    i += 1

print(cpt)