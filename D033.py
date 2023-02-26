n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
n3 = int(input('Digite novamente outro valor:'))

if n2 > n3 and n2 > n1:
    print('O maior número é {}' .format(n2))
elif n3 > n2 and n3 > n1:
    print('O maior número é {}' .format(n3))
else:
   print('O maior numéro é {}' .format(n1))


if n2 < n3 and n2 < n1:
    print('O menor número é {}' .format(n2))
elif n3 < n2 and n3 < n1:
    print('o menor número é {}' .format(n3))
else:
    print('O menor número é {}' .format(n1))
