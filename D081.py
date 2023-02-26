lista = [[],[]]

while True:
    for c in range(0,7):
        valor = int(input('Digite um número:'))
        if valor % 2 == 0:
            lista[0].append(valor)
        else:
            lista[1].append(valor)
    break

print(f'Os valores PARES são: {lista[0]}')
print(f'OS valores ÍMPARES são: {lista[1]}')

 