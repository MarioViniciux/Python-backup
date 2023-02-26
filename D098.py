def leia_int():
    n = input('Digite um número inteiro:').strip()
    while n.isnumeric() == False:
        print('Erro! É permitido apenas números inteiros.')
        n = input('Digite apenas um número inteiro:').strip()
    print(f'Você digitou o número {n}.')
        

leia_int()