def leia_int_menor3(msg):
    while True:
        try:
            opc = int(input(msg))
            if opc > 3 or opc < 1:
                print('\033[91mERRO: digite um número que esteja nas opções.\033[m')
                continue
        except (ValueError, TypeError):
            print('\033[91mERRO: digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('A entrada de dados foi interrompida pelo usuário.')
            return 0
        else:
            return opc


def painel_formatado(msg):
    print('-' * 50)
    print(f'{msg:^50}')
    print('-' * 50)


def opcoes(lista):
    painel_formatado('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('-' * 50)
    opc = leia_int_menor3('Sua opção: ')
    return opc
    

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[91mERRO: digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('A entrada de dados foi interrompida pelo usuário.')
            return 0
        else:
            return n