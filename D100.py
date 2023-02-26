def texto0(phrase):
    print('\033[0;33m~' * len(phrase))
    print(phrase)
    print('~' * len(phrase))
    print('\033[m')


def texto1(basic):
    print('\033[35m-' * len(basic))
    print(basic)
    print('-' * len(basic))
    print('\033[m')


def ajuda(msg, texto0, texto1):
    texto0(phrase)
    print(help(msg))
    texto1(basic)


while True:
    despedida = 'ATÉ LOGO!'
    basic = 'SISTEMA DE AJUDA PyHELP'
    msg = str(input('Biblioteca ou função:')).lower().strip()
    if msg == 'fim':    
        print('\033[0;34m=' * len(despedida))
        print(despedida)
        print('=' * len(despedida))
        print('\033[m')
        break
    phrase = f'Acessando o manual do comando "{msg}".'
    ajuda(msg, texto0, texto1)
