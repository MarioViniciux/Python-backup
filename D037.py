n = int(input('Digite um número para conversão:'))
print('''Essas são as opções, por favor, selecione uma:
[1] converter para HEXADECIMAL
[2] converter para BINÁRIO
[3] converter para OCTAL''')
opção = int(input('Use a numeração para a seleção:')) 

while opção != 1 and opção != 2 and opção != 3:
    print('Valor inválido, tente novamente')
    print('''Essas são as opções, por favor, selecione uma:
[1] converter para HEXADECIMAL
[2] converter para BINÁRIO
[3] converter para OCTAL''')
    opção = int(input('Lembrando, somente as opções acima são válidas. Agora insira o número para a base de conversão desejada:'))

if opção == 1:
    print('O número {} convertido para hexadecimal, é igual a {}' .format(n, hex(n)))
elif opção == 2:
    print('O número {} convertido para binário, é igual a {}' .format(n, bin(n)))
elif opção == 3:
    print('O número {} convertido para octal, é igual a {}' .format(n, oct(n)))

