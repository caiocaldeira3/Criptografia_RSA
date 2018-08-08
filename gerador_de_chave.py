from funcoes import *

p = primo_aleatorio(2048)
print("p = ", p)
q = primo_aleatorio(2048)
print("q = ", q)
phi = (p-1)*(q-1)
print("phi = ", phi)
n = p*q
print("n = ", n)

e = 65537

while(mdc(e, phi) != 1):
    e += 2

print("e = ", e)

d = inverso_modular(e, phi)%phi
print("d = ", d)
