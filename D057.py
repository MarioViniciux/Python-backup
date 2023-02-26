num = int(input('Insira o número pra calcular seu fatorial:'))
c = num
f = 1

print('Calculando 5! = ', end = '')
### for c in range(num, 1 , -1):
while c > 0:
    print('{}' .format(c), end = '') 
    print(' X ' if c > 1 else ' = ', end = '') 
    f *= c
    c -= 1
print('{}' .format(f))
   






