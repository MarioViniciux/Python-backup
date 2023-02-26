n = int(input('Digite um número inteiro entre 1 e 9999.'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10 

print('A casa unitária de {}, é {}.' .format(n, u))
print('A casa decimal de {}, é {}.' .format(n, d))
print('A casa centenária de {}, é {}.' .format(n, c))
print('A casa de milhar de {}, é {}.' .format(n, m))