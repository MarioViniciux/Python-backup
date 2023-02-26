n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

if n1 > n2:
    print('O número {} é maior' .format(n1))
    print('O número {} é menor' .format(n2))
elif n1 < n2:
    print('O número {} é maior' .format(n2))
    print('O número {} é menor' .format(n1))
else:
    print('Não número maior, ambos são iguais.')