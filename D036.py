casa = float(input('Quanto custa a casa que deseja comprar? R$'))
salario = float(input('Qual é o seu salário?'))
meses = float(input('Em quantos meses pretende pagar a casa?'))
prestação = casa / meses
maximo = salario * 30 / 100

if prestação > maximo:
    print('Você não teve seu emprestimo aprovado, pois a prestação excede 30% do seu salário.')
else:
    print('Seu crédito foi aprovado!')
    print('Lembrando que são {:.0f} prestações de R${:.2f}' .format(meses, prestação))
