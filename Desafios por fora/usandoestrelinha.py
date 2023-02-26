def soma(todos):
    all = sum(todos)
    print(f'A soma de todos os números adicionados é: {all}.')


def Verificacao_add():
    global add
    while add.isnumeric() == False:
        print('\033[31mErro! É permitido apenas números inteiros. \033[m')
        add = input('\033[96mDigite apenas um número inteiro: \033[m').strip()
    return True


def Verificacao_num():
    global n
    while n.isnumeric() == False:
        print('\033[31mErro! É permitido apenas números inteiros. \033[m')
        n = input('\033[96mDigite apenas um número inteiro: \033[m').strip()
    return True


add = input('Quantos números quer adicionar?')
todos = list()
Verificacao_add()

while True:
    if Verificacao_add() == True:
        add = int(add)
        for c in range(0, add):
            n = input(f'{c + 1}° número: ')
            Verificacao_num()
            if Verificacao_num() == True:
                n = int(n)
                todos.append(n)
    soma(todos)
    break
