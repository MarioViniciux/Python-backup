def maior_e_menor(*num):
    count = maior = menor = 0

    for valor in num:
        if count == 0:
            maior = valor
            menor = valor
        else:
            if valor > maior: 
                maior = valor
            if valor < menor:
                menor = valor
        count += 1
    print('-' * 50)
    print(f'Ao todo foram informados {len(num)} números. \nSendo eles: {num}.')
    print(f'O maior valor informado foi: {maior}.')
    print(f'O menor valor informado foi {menor}.')
    
maior_e_menor(3, 5, 1, 7, 9, 4, 2, 73, 64, 1, 0, -1, 23)
