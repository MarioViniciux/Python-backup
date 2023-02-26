lista = list()
lista2 = list()
lista3 = list()

while True:
    adicionar = int(input('Quantos números quer adicionar?'))

    for n in range(0, adicionar):
        lista.append(int(input('Digite o número:')))
    
    continuar = input('Deseja adicionar mais números? [S/N]')[0]

    while continuar not in 'SsNn':
        print('Erro, tente novamente.')
        continuar = input('Deseja adicionar mais números? [S/N]')[0]

    while continuar in 'Ss':
        adicionar = int(input('Quantos números quer adicionar?'))

        for n in range(0, adicionar):
            lista.append(int(input('Digite o número:')))

        continuar = input('Deseja adicionar mais números? [S/N]')
        
        if continuar in 'Nn':
            break 

    for i, v in enumerate(lista):
        if v % 2 == 0:
            lista2.append(v)
        else:
            lista3.append(v)

    break

print(f'Os números na lista são: \n{lista}')
print(f'Os números pares são: \n{lista2}')
print(f'Os números impares são: \n{lista3}')    