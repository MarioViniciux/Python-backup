from random import randint
from time import sleep
from operator import itemgetter

juego = {'jogador1': randint(1,6), 
         'jogador2': randint(1,6), 
         'jogador3': randint(1,6),  
         'jogador4': randint(1,6)}
ranked = []
print('Valores sorteados:')

for k, i in juego.items():
    print(f'{k} tirou {i} no dado.')
    sleep(0.5)
ranked = sorted(juego.items(), key=itemgetter(1), reverse=True)

print('=-' * 20)
print('RANKING DOS JOGADORES')
print('=-' * 20)
for i, v in enumerate(ranked):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
    