#CPO
# 4 : Fonction suite fibonacci

def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(1, n):
        sauv = n1 + n2
        n1 = n2
        n2 = sauv
        print(sauv)

n = int(input("Choisissez n : "))
fibonacci(n)