lista = ('Pão', 0.50,
         'Leite', 5.30,
         'Café', 7.20,
         'Leite Condensado', 5.25,
         'Arroz', 5.30,
         'Açai', 15.70,
         'Hambúrguer', 23.40)

for pos in range(0, len(lista)):
        if pos % 2 == 0:
                print(f'{lista[pos]:.<30}', end='')
        elif pos % 1 == 0:
                print(f'R${lista[pos]}')
