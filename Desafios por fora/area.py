def leia_int0():
    global l
    while l.isnumeric() == False:
        print('\033[31mErro! É permitido apenas números inteiros. \033[m')
        l = input('\033[96mDigite apenas um número inteiro para definir a \033[95mlargura\033[96m do seu terreno: \033[m').strip()
    return True


def leia_int1():
    global c
    while c.isnumeric() == False:
        print('\033[31mErro! É permitido apenas números inteiros.\033[m')
        c = input('\033[96mDigite apenas um número inteiro definir o \033[95mcomprimento\033[96m do seu terreno: \033[m').strip()
    return True


def tudook(leia_int0, leia_int1):
    if leia_int0 == True:
        first = True
    if leia_int1 == True:
        second = True
    return True


def area(l, c):
    l = int(l)
    c = int(c)
    ar = l * c
    print(f'\033[92mE ele possui \033[90m{ar}m²\033[92m de área.\033[m')
    

l = input('Largura: ').strip()
c = input('Comprimento: ').strip()

while True:
    leia_int0()
    leia_int1()
    tudook(leia_int0, leia_int1)

    if tudook(leia_int0, leia_int1) == True:
        print(f'\033[92mAs dimensões do seu terreno é de \033[90m{c}m\033[92m de comprimento e \033[90m{l}m\033[92m de largura.\033[m', end = ' ')
        area(l, c)
    break