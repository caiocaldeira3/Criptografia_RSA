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
    if r == 1:
        return 1
    while(i < t):
        if r == n1:
            return 1
        i += 1
        r = (r**2)%n
    return 0

def provavelmente_primo(n, itera):
    if(n == 2 or n == 3):
        return 1
    if(n%2 == 0):
        return 0
    while(itera > 0):
        base = randrange(2, n-1)
        r = talvez_primo(base, n, n-1, 0, n-1)
        if(r == 0):
            return 0
        itera -= 1
    return 1

def primo_aleatorio(b):
    if b == 1:
        return 2
    if b == 0:
        return 0
    eprimo = 0
    exp = 2**b
    num = randrange(2, exp)
    while not provavelmente_primo(num, 20):
        print(num)
        num = randrange(2, exp)
    return num

b = int(input())
print(primo_aleatorio(b))
