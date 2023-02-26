termo = int(input('Qual o primeiro termo da progressão aritmética?'))
razão = int(input('Qual a razão da progressão aritmética?'))

for n in range(termo, razão * 11, razão):
    print('{}' .format(n), end = ' > ')
print('Fim da progressão')