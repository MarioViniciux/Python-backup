from time import sleep

def contador(i, f, p):

    if p < 0:
            p *= -1
    if p == 0:
            p = 1

    print('=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)

    if i < f:
        count = i
        while count <= f:
            print(f'{count}', end = ' ')
            sleep(0.5)
            count += p
        print('FIM DA CONTAGEM!')

    else:
        count = i
        while count >= f:
            print(f'{count}', end = ' ')
            sleep(0.5)
            count -= p
        print('FIM DA CONTAGEM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora personalize a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)


