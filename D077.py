import contextlib
lista = list()

while True:
    adicionados = 0
    cinco = False
    adicionar = int(input('Quantos números quer adicionar?'))

    for n in range(0, adicionar):
        lista.append(int(input('Digite o número:')))
        adicionados += 1

    continuar = input('Deseja adicionar mais números? [S/N]')[0]

    while continuar not in 'SsNn':
        print('Erro, tente novamente.')
        continuar = input('Deseja adicionar mais números? [S/N]')[0]

    while continuar in 'Ss':
        adicionar = int(input('Quantos números quer adicionar?'))

        for n in range(0, adicionar):
            lista.append(int(input('Digite o número:')))
            adicionados += 1

        continuar = input('Deseja adicionar mais números? [S/N]')
        
        if continuar in 'Nn':
            break
    
    if 5 in lista:
        cinco = True
    else:
        cinco = False

    lista.sort(reverse=True)

    break

print(f'A lista foi composta por {adicionados} números, sendo eles: \n{lista}')

if cinco == True:
    print('O número 5 foi digitado e está presente na lista.')
else:
    print('O número 5 não foi digitado.')
