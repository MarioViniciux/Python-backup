n = input('Digite o seu nome completo:').strip()
nome = n.split()
primeiro = nome[0]
ultimo = nome[len(nome)-1]
print('O seu primeiro nome é {}.' .format(primeiro))
print('O seu último nome é {}.' .format(ultimo))
