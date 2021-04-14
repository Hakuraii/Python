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

temps = len(L)
alt = max(L)
print(Zterme, temps, alt)