from math import *

def syracuse(u):
    if u % 2 == 0:
        u = u // 2
    else:
        u = 3 * u + 1
    return u

def liste_syracuse(u):
    L = [u]
    while u != 1:
        u=syracuse(u)
        L.append(u)
    return L

Zterme = 1
L = liste_syracuse(Zterme)
while len(L) <= 100:
    Zterme += 1
    L=liste_syracuse(Zterme)

V = []
V.append([Zterme, L])
Vterme = 1
A = liste_syracuse(Vterme)
while len(V) != 3:
    if((max(A) == max(V[0][1])) and Vterme != V[0][0]):
        V.append([Vterme, A])
    Vterme += 1
    A = liste_syracuse(Vterme)

for i in range(0, len(V)) :
    print(V[i][0], len(V[i][1]), max(V[i][1]))