lista = list()

for cont in range(1,6):
    lista.append(int(input('Digite um valor:')))

lista_b = lista[:]

lista.sort()
menor = lista[0]
lista.sort(reverse=True)
maior = lista[0]

print(f'O menor número presente na lista é {menor}, e está localizado na(s) posição(ões): ', end='')
for i, v in enumerate(lista_b):
    if v == menor:
        print(f'{i}', end=' ')

print()

print(f'O maior número na lista é {maior}, e ele está na(s) posição(ões):', end='')
for i, v in enumerate(lista_b):
        if v == maior:
            print(f'{i}', end=' ')
