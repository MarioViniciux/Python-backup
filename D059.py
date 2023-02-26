count = 1
t1 = 0
t2 = 1
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)

termos = int(input('Quantos termos quer mostrar? '))

print('{} > {}' .format(t1, t2) , end = ' > ')
while count <= termos:
    count += 1
    t3 = t1 + t2
    print('{}' .format(t3) , end = ' > ')
    t1 = t2
    t2 = t3
print('FIM')
    
