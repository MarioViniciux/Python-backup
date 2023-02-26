num = int(input('Qual o número que deseja ver se é primo?'))

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end = ' ')
    else:
        print('\033[m', end = ' ')
    print('{}' .format(c))

if num != 1 and num != 2 and num != 3:
    if num % num == 0 and num % 2 != 0 and num % 3 != 0:
        print('\033[35m{} é um número primo' .format(num))
    else:
        print('\033[35m{} é um número não primo' .format(num))
else:
    print('\033[35m{} é um número primo' .format(num))