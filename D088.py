jogador = dict()
partidas = list()
todos_jogadores = list()

while True:
    add = int(input('Quantos jogadores quer adicionar?'))

    for c in range(0, add):
        partidas.clear()
        jogador.clear()
        print('=-' * 30)
        jogador['Nome'] = input('Qual o nome do jogador?').strip()
        tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
        jogador['Partidas'] = tot
        for c in range(0, tot):
            partidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez no {c + 1}° jogo?')))
        jogador['Gols'] = partidas[:]
        jogador['Total'] = sum(partidas)
        todos_jogadores.append(jogador.copy())
        
    while True:
        print('=-' * 30)
        addmais = input('Deseja adicionar mais pessoas? [S/N]').upper().strip()[0]
        if addmais not in 'SN':
            print('ERRO! Tente novamente, usando somente S para SIM, e N para NÃO.')
        else:
            break

    if addmais == 'N':
        break
    else:
        continue

print('cod', end = '    ')
for i in jogador.keys():
    print(f'{i:<30}', end ='')
print()
for k, v in enumerate(todos_jogadores):
    print(f'{k :> 2}', end = '  ')
    for d in v.values():
        print(f'{str(d):<30}', end = '  ')
    print()


while True:
    veri = int(input('Os dados de qual jogador devem ser priorizados? (Utilize o número de código do jogador, e 999 para encerrar)'))
    if veri == 999:
        break
    if veri >= len(todos_jogadores):
        print(f'ERRO! O número {veri} não existe na lista de jogadores.')
    else:
        print('-' * 50 )
        print(f'O nome do jogador é: {todos_jogadores[veri]["Nome"]}')
        print(f'Ele fez {todos_jogadores[veri]["Total"]} gols em {todos_jogadores[veri]["Partidas"]} jogos, tendo um aproveitamento de', end = ' ')
        print(f'{todos_jogadores[veri]["Total"] / todos_jogadores[veri]["Partidas"]:.1f} gols por jogo.')
        print('-' * 50)

print('Aplicativo encerrado, até a próxima.')