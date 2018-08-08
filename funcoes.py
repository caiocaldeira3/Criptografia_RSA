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
    if(n == 2 or n == 3):
        return 1
    if(n%2 == 0):
        return 0
    r = 1
    while(iter > 0):
        base = randrange(2, n-1)
        resultado = talvez_primo(base, n, n-1, 0, n-1)
        r = r and resultado
        if(r == 0):
            return 0
        iter -= 1
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
        num = randrange(2, exp)
    return num

def mdc(a, b):
    r = a%b
    if(r == 0):
        return b
    return mdc(b, r)

def mdc_ext(a, b):

	r = a%b
	q = a//b

	if r == 0:
		return (0, 1, b)

	x, y, mdc = mdc_ext(b, r)

	return(y, x-q*y, mdc)

def inverso_modular(a, b):
	x, y, mdc = mdc_ext(a, b)
	if(mdc):
	    return x
	else:
	    return 0

def codifica(a):
    result = 0
    i = 0
    for letter in a:
        result += 256**i * ord(letter)
        i += 1
    return result

def decodifica(b):
    str = ''
    while b != 0:
        str = "%s%s" %(str, chr(b%256))
        b //= 256
    return str

def criptografa(mensagem, n, e):
    M = codifica(mensagem)
    C = meu_exp_iterativo(M, e, n)
    return C

def descriptografa(C, inv, p, q):
    DC = meu_exp_iterativo(C, inv, p*q)
    mensagem = decodifica(DC)
    return mensagem
