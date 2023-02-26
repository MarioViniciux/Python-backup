compra = preço = maisqmil = maiscaro = 0 
menorpreço = 'pão'
preçomenor = 9999999999999

while True:
    nome = input('Nome do produto:').upper().strip()
    preço = int(input('Preço do produto. R$:'))
    compra += preço
    if preço >= 1000:
        maisqmil += 1
    if preço <= preçomenor:
        preçomenor = preço
        menorpreço = nome
    continuar = input('Deseja continuar?[S/N]:').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar?[S/N]:').upper().strip()[0]
    if continuar == 'N':
        break

print(f'O preço total das compras deu R${compra}')
print(f'O nome do mais barato, é {menorpreço}')
print(f'O produto mais barato, custa R${preçomenor}')
print(f'{maisqmil} custam mais do que mil reais.')

