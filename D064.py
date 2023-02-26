from random import randint

v = 0

while True:
    pc = randint(0,100)
    n = int(input('Diga um número:'))
    opção = ' '
    soma = pc + n

    while opção not in 'PI':
        opção = input('Par ou impar?[P/I]').strip().upper()[0]

    print('Deu par.'if soma % 2 == 0 else 'Deu impar.')
    if opção == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {pc}, e a soma deu {soma}.')
            print('VOCÊ GANHOU')
            v += 1
        else: 
            print(f'Você jogou {n} e o computador {pc}, e a soma deu {soma}.')
            print('VOCÊ PERDEU')
            break
    elif opção == 'I':
        if soma % 2 == 1:
            print(f'Você jogou {n} e o computador {pc}, e a soma deu {soma}.')
            print('VOCÊ GANHOU')
            v += 1
        else:
            print(f'Você jogou {n} e o computador {pc}, e a soma deu {soma}.')
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar de novo, só paro quando eu (o computador) ganhar!')
print(f'GAME OVER!! Você ganhou {v} vezes. Mas isso não precisa ser comentado.')
