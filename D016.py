km = int(input('Quantos quilomêtros foram percorridos? '))
dia = int(input('Por quantos dias o carro foi alugado?'))
dias = 60 * dia
k = 0.15 * km

print('Você terá que pagar R${} pelos dias, e R${} pelos quilomêtros andados.' .format(dias, k))
print('Resultando em um total de R${}.' .format(dias + k))

