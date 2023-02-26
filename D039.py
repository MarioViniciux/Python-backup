from datetime import date

print('''Por favor, nos informe o seu sexo:
[1] MASCULINO
[2] FEMININO
[3] PREFIRO NÃO IDENTIFICAR''')
sexo = int(input('Insira somente o número:'))

if sexo == 2 or 3:
    print('No Brasil, somente o alistamento militar masculino é obrigatório.')
    opção = input('Sabendo disso, deseja prosseguir?').lower().strip()
    if opção == 'sim' or 's':
            ano = int(input('Em qual ano você nasceu?'))
            atual = date.today().year
            idade = atual - ano 

            if idade < 18:
                print('Vocẽ ainda não está em tempo de se alistar.')
            elif idade == 18:
                print('Você tem que se alistar esse ano!')
            else:
                print('Você já está além do tempo de se alistar')
    else:
        print('Compreendo, até uma próxima então.')
else:
    ano = int(input('Em qual ano você nasceu?'))
    atual = date.today().year
    idade = atual - ano 

    if idade < 18:
        print('Vocẽ ainda não está em tempo de se alistar.')
    elif idade == 18:
        print('Você tem que se alistar esse ano!')
    else:
        print('Você já está além do tempo de se alistar')


