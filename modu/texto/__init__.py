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
   
    
def quantidade(msg):
    qntd = len(msg)
    return qntd


def comprimento(msg, msgg):
    if len(msg) == len(msgg):
        print('They have same lenght')
    else:
        print("They haven't same lenght")
