from random import randrange

def meu_exp_iterativo(a, exp, n):
    resp = 1
    pot = a
    while(exp > 0):
        if(exp%2 == 1):
            resp = (resp*pot)%n
        exp //= 2
        pot = (pot*pot)%n
    return resp

def talvez_primo(a, n, n1, t, q):
    while(q%2 != 1):
        q //= 2
        t += 1
    i = 0
    r = meu_exp_iterativo(a, q, n)
    if i == 0 and r == 1:
        return 1
    while(i < t):
        if r == n1:
            return 1
        i += 1
        r = (r**2)%n
    return 0

def provavelmente_primo(n, iter):
    while(iter > 0):
        base = randrange(2, n-1)
        r = talvez_primo(base, n, n-1, 0, n-1)
        if(r == 0):
            return 0
        iter -= 1
    return 1

n = int(input("Num. Ímpar "))
iter = int(input("Iterações "))
print(provavelmente_primo(n, iter))
