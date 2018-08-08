def meu_exp_iterativo(a, exp, n):
    resp = 1
    pot = a
    while(exp > 0):
        if(exp%2 == 1):
            resp = (resp*pot)%n
        exp //= 2
        pot = (pot*pot)%n
    return resp

a = int(input())
exp = int(input())
n = int(input())

res = meu_exp_iterativo(a, exp, n)
print(res)
