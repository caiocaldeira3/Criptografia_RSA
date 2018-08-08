from funcoes import *

def descriptografa(C, inv, p, q):
    DC = meu_exp_iterativo(C, inv, p*q)
    mensagem = decodifica(DC)
    return mensagem

p = int(input("p = "))
q = int(input("q = "))
inv = int(input("inv = "))
C = int(input("C = "))

nova = descriptografa(C, inv, p, q)
print(nova)
