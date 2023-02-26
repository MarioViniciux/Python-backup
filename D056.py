from time import sleep
opção = 0
n1 = int(input('Insira o primeiro valor:'))
n2 = int(input('Insira outro  valor:'))

while opção != 7:

    print('''    1 = somar
    2 = multiplicar
    3 = subtrair
    4 = dividir 
    5 = maior 
    6 = inserir novos numeros 
    7 = encerrar programa''')
    opção = int(input('Insira o respectivo número do que deseja fazer:'))

    if opção == 1:
        print('A soma de {} e {}, é igual a {}' .format(n1, n2, n1 + n2))

    elif opção == 2:
        print('A multiplicação de {} e {}, é igual a {}' .format(n1, n2, n1 * n2))

    elif opção == 3:
        print('A subtração de {} e {}, é igual a {}' .format(n1, n2, n1 - n2))

    elif opção == 4:
        print('A divisão de {} e {}, é igual a {:.2f}' .format(n1, n2, n1 / n2))

    elif opção == 5:
        if n1 > n2:
            print('O maior é {}' .format(n1))
        elif n2 > n1: 
            print('O maior é {}' .format(n2))
        else:
            print('Não há maior entre esses dois números.')

    elif opção == 6:
        n1 = int(input('Insira o primeiro valor:'))
        n2 = int(input('Insira outro  valor:'))

    elif opção == 7:
        print('Certo, programa sendo encerrado, obrigado por usar.')
        print('ENCERRANDO...')
        sleep(1)

    else:
        print(('Opção Inválida, tente novamente'))
print('Fim do programa, volte sempre')






