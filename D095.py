def voto():
    from datetime import date
    hoje = date.today().year
    nasc = int(input('Em que ano você nasceu?'))

    maior = f'Com {hoje - nasc}, o voto é OBRIGATÓRIO.'
    optar = f'Com {hoje - nasc}, o voto é OPCIONAL.'
    menor = f'Com {hoje - nasc}, NÃO VOTA.'


    if hoje - nasc >= 18:
        return print(maior)
    elif hoje - nasc >= 16 and hoje- nasc <= 17:
        return print(optar)
    elif hoje - nasc >= 65:
        return print(optar)
    else:
        return print(menor)


voto()