from time import sleep 
from  random import randint

pc = randint(1,20)
player = int(input('Escolha um número e tente adivinhar o número que o pc "pensou":'))
ten = 1

while player != pc:
    ten += 1
    if player > pc:
        print('PROCESSANDO...')
        sleep(1)
        #print('Menos... tente de novo.')
        player = int(input('Escolha um número e tente adivinhar o número que o pc "pensou":'))
    elif player < pc:
        print('PROCESSANDO...')
        sleep(1)
        #print('Mais... tente de novo.')
        player = int(input('Escolha um número e tente adivinhar o número que o pc "pensou":'))
print('PROCESSANDO...')
sleep(1)
print('Você acertou em {} tentativas.' .format(ten))