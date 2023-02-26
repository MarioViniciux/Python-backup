numeros = [[0, 0, 0], [0, 0, 0], [0, 0,0]]
sumpar = sumcol = bigger = 0

for l in range(0,3):
    for c in range(0,3):
        numeros[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))

print('=-' * 30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{numeros[l][c]:^5}]', end='')
        if numeros[l][c] % 2 == 0:
            sumpar += numeros[l][c]
    print()

print('=-' * 30)

for l in range(0,3):
    sumcol += numeros[l][2]

for c in range(0,3):
    if c == 0:
        bigger = numeros[1][c]
    elif numeros[1][c] > bigger:
        bigger = numeros[1][c]

print(f'O maior número da linha 2 é {bigger}')
print(f'A soma de todos os números pares é igual a: {sumpar}')
print(f'A soma dos valores da coluna 3, é igual a: {sumcol}')
