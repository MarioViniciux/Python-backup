km = int(input('Qual a quilometragem que pretende viajar?'))
menor = km * 0.50
maior = km * 0.45

if km > 200:
    print('A passagem custará R${:.2f}' .format(maior))
else:
    print('A passagem custará R${:.2f}' .format(menor))