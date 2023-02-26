money = float(input('Informe quanto você tem na carteira: R$'))
dolar = money / 5.33
euro = money / 6.25

print('Você poderá trocar {} Reais em, {:.2f} Dolars.' .format(money, dolar))
print('Ou, caso queira Euro, poderá trocar {:.2f} Euros.' .format(euro))