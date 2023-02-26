soma = 0
media = 0
homemvelho = 0
nomehomem = ''
totmulher20 = 0

for c in range(1,6):
    print('-' * 5, '{}° pessoa' .format(c), '-' * 5)
    nome = input('Qual o nome da {}° pessoa?' .format(c))
    idade = int(input('Idade da pessoa:'))
    sexo = input('M/F:').upper().strip()
    soma += idade
    if c == 1 and sexo == 'M':
        homemvelho = idade
        nomehomem = nome
    if sexo == 'M' and idade > homemvelho:
        homemvelho = idade
        nomehomem = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

media = soma / 5
print('A média de idade do grupo é {:.1f} anos' .format(media))
print('O homem mais velho tem {} anos e chama {}' .format(homemvelho, nomehomem))
print('Possue(m) {} mulher(es) com menos de 20 anos' .format(totmulher20))