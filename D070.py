from random import randint

num = (randint(1, 15), randint(1, 15), randint(1, 15),
       randint(1, 15), randint(1, 15))

print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')

print(f'\nO maior número é {max(num)}')
print(f'O menor número é {min(num)}')
