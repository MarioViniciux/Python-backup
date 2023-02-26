from random import randint

lista = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
pcl = lista[pc]
jogador = input('Qual você quer jogar? Pedra, papel ou tesoura?').lower().strip()

while jogador != 'papel' and jogador != 'pedra' and jogador != 'tesoura':
    print('Opção inválida, provavelmente houve um erro de digitação. Tente novamente, mas, com mais atenção.')
    jogador = input('Qual você quer jogar? Pedra, papel ou tesoura?').lower().strip()

while jogador == pcl :
    print('Empate, vamos tentar de novo.')
    lista = ('pedra', 'papel', 'tesoura')
    pc = randint(0,2)
    pcl = lista[pc]
    jogador = input('Qual você quer jogar? Pedra, papel ou tesoura?').lower().strip()

if jogador == 'pedra' and pcl == 'tesoura':
    print('Escolhi {}, você GANHOU.' .format(pcl))
elif jogador == 'pedra' and pcl == 'papel':
    print('Escolhi {}, você PERDEU.' .format(pcl))
elif jogador == 'papel' and pcl == 'pedra':
    print('Escolhi {}, você GANHOU.' .format(pcl))
elif jogador == 'papel' and pcl == 'tesoura':
    print('Escolhi {}, você PERDEU.' .format(pcl))
elif jogador == 'tesoura' and pcl == 'papel':
    print('Escolhi {}, você GANHOU.' .format(pcl))
elif jogador == 'tesoura' and pcl == 'pedra':
    print('Escolhi {}, você PERDEU.' .format(pcl))

