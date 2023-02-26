adições = int(input('Quantos números quer adicionar?'))
numero = list()
adicionados = 0

while True:
    for n in range(0, adições):
        num = int(input('Digite o número:'))

        if num not in numero:
            numero.append(num)
            print('Valor adicionado.')
        else:
            print('Não adicionarei este número, ele já está na lista.')
           
    continuar = input('Deseja adicionar mais números? [S/N]')

    while continuar not in 'SsNn':
        print('Erro, tente novamente.')
        continuar = input('Deseja adicionar mais números? [S/N]')
    
    if continuar in 'Ss':
        amais = int(input('Quantos números a mais quer adicionar?'))

        for n in range(0, amais - adições):
            num = int(input('Digite o número:'))
            if num not in numero:
                numero.append(num)
                print('Valor adicionado.')
            else:
                print('Não adicionarei este número, ele já está na lista.')
          
    if continuar in 'Nn':
        break
    
numero.sort()
print(f'Estes foram os valores adicionados:\n{numero}')
