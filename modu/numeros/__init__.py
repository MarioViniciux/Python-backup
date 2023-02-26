def ler_moeda(msg):
    valido = False

    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mErro: \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
    return float(entrada)
    

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


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[91mERRO: digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('A entrada de dados foi interrompida pelo usuário.')
            return 0
        else:
            return n