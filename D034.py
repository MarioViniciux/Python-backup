salario = float(input('Qual o salário do funcionário? R$'))

if salario > 1.250:
    aumento = salario * 10 / 100
    novo = salario + aumento 
    print('O novo salário será de R${:.2f}' .format(novo))
else:
    aumento = salario * 15 / 100
    novo = salario + aumento
    print('O novo salário será de R${:.2f}' .format(novo))