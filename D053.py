maior = 0
menor = 0

for peso in range(1,6):
    p = float(input('Qual o peso da {}° pessoa?' .format(peso)))
    if peso == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
            
print('O menor peso é {}Kg' .format(menor))
print('O maior peso é {}Kg' .format(maior))