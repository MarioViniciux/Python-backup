import math

opo = float(input('Qual o comprimento do cateto oposto?'))
adj = float(input('Qual o comprimento do cateto adjacente?'))
raiz = (opo * 2) + (adj * 2)
hipo = math.hypot(opo, adj)

print('Considerando o cateto oposto e o adjacente, a hipotenusa é igual a {:.1f}' .format(hipo))