#CPO
#Exemple 2  : Antoine, conditions

print("\t\t--Test inférieur supérieur--")

nombreRef = int(input("\nVeuillez saisir le nombre de référence : "))
nombre = int(input("Veuillez saisir le nombre à tester : "))

if(nombre < nombreRef):
    print(nombre,"inférieur à",nombreRef)

elif(nombre == nombreRef):
    print(nombre,"égal à",nombreRef)

else:
    print(nombre,"supérieur à",nombreRef)