def leia_int():
    global n
    while n.isnumeric() == False:
        print('Erro! É permitido apenas números inteiros.')
        n = input('Digite apenas um número inteiro:').strip()
    return True


def cavalos(n):
    patas = n * 4
    print(f'Serão necessárias {patas} ferraduras para os {n} cavalos')


while True:
    n = input('Qual a quantidade de cavalos? ').strip()

    if leia_int() == True:
        n = int(n)
        cavalos(n)
    break
