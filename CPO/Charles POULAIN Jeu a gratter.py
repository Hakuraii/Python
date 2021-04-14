#CPO
#Jeu a gratter
import random

C = 0
N = []
while len(N) < 5:
    N.append(random.randint(1,5))

if sum(N) % 2 == 0:
    C += 1
if max(N) == 2:
    C += 2

for i in range (1, len(N)):
    if N.count(N[i]) >= 3:
        C += 5
        break

print(N)
print(C)