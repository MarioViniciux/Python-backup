print('''Este programa irá pedir o tamanho que 1 lata de tinta preenche, em metros.
E o tamanho e largura da parede, e assim exibirá a quantidade de latas necessárias.''')

tinta = int(input('De acordo com testes, ou com a embalagem da tinta, quantos metros 1 lata preenche?'))
largura = int(input('Insira a largura da parede:'))
tamanho = int(input('Agora insira o tamanho da parede:'))
area = largura * tamanho
qunt = area / tinta 

print('Você precisará de {} latas de tinta' .format(qunt))
