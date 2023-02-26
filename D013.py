preço = float(input('Qual o valor do produto?: R$'))
rdt = (preço * 95) / 100

print('Este produto com desconto de 5%, irá de R${:.2f}, para R${:.2f}' .format(preço, rdt))