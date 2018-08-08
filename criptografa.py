from funcoes import *

def criptografa(mensagem, n, e):
    M = codifica(mensagem)
    C = meu_exp_iterativo(M, e, n)
    return C

n = int(input("n = "))
e = int(input("e = "))
mensagem = input("mensagem = ")
c = criptografa(mensagem, n, e)
print(c)
