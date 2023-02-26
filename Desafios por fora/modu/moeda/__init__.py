def aumentar(p = 0, t = 1, formato = False):
    p = (p * (100 + t)) / 100
    return p if formato is False else moeda(p)


def dobro(p = 0, formato = False):
    p = p * 2 
    return p if formato is False else moeda(p)


def metade(p = 0, formato = False):
    p = p / 2
    return p if not formato else moeda(p)


def diminuir(p = 0, t = 1, formato = False):
    p = (p * (100 - t)) / 100
    return p if not formato else moeda(p)
    

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p = 0, aumento = 10, redução = 5):
    print('=-' * 30)
    print('RESUMO DO VALOR'.center(60))
    print('=-' * 30)
    print(f'Valor: \t\t\t\t{moeda(p)}')
    print(f'Dobro do preço: \t\t{dobro(p, True)}')
    print(f'Metade do preço: \t\t{metade(p, True)}')
    print(f'Valor com {aumento}% de juros: \t{aumentar(p, aumento, True)}')
    print(f'Valor com {redução}% de desconto: \t{diminuir(p, redução, True)}')
    print('=-' * 30)

