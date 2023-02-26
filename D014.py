salario = float(input('Insira o salário do funcionário: R$'))
aumento = salario * 115 / 100

print('O salário desse funcionário, com aumento de 15%, irá de R${:.2f}, para R${:.2f}.' .format(salario, aumento))