num = (int(input('Digite um número:')), int(input('Outro número:')),
       int(input('Mais um número:')), int(input('O último:')))

print(f'O número 9 apareceu {num.count(9)} vez(es)')

if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}° posição')
else:
    print('Não possui o valor 3.')

print('Os números pares digitados foram:')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
