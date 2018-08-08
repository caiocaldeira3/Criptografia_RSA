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
    if n%2 == 0:
        if n == 2:
            return 1
        return 1
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


a = int(input("Base "))
n = int(input("Num. ímpar "))
print(talvez_primo(a, n, n-1, 0, n-1))
