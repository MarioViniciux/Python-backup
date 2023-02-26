pessoas = []
adicionar = []
leves = pesados = maispesado = 0
maisleve = 999999999999

while True:
    tobe = int(input('Quantas pessoas quer cadastrar?'))
    print('=-' * 30)

    for c in range(0, tobe):
        adicionar.append(str(input('Qual o nome da pessoa?')))
        adicionar.append(int(input('Qual o peso da pessoa?')))
        pessoas.append(adicionar[:])
        adicionar.clear()
        print('=-' * 30)

    while True:
        tiratema = input('Deseja adicionar mais pessoa? [S/N]')[0]
        while tiratema not in 'SsNn':
            print('Erro, tente novamente.')
            tiratema = input('Deseja adicionar mais pessoa? [S/N]')[0]

        if tiratema in 'Ss':
            tobe = int(input('Quantas pessoas quer cadastrar?'))

            for c in range(0, tobe):
                adicionar.append(str(input('Qual o nome da pessoa?')))
                adicionar.append(int(input('Qual o peso da pessoa?')))
                pessoas.append(adicionar[:])
                adicionar.clear()
                print('=-' * 30)
        
        if tiratema in 'Nn':
            break

    for p in pessoas:
        if p[1] > 90:
            pesados += 1
        elif p[1] < 90:
            leves += 1
    
    for p in pessoas:
        if p[1] > maispesado:
            maispesado = p[1]
        elif p[1] < maisleve:
            maisleve = p[1]
    break

print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'Temos {leves} pessoas abaixo dos 90 quilos, e {pesados} pessoas acima.')
print(f'O maior peso cadastrado, foi {maispesado}, e o menor peso, foi {maisleve}.')

