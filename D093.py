def maior(*num):
    count = maior = 0

    for valor in num:
        if count == 0:
            maior = valor
        else:
            if valor > maior: 
                maior = valor
        count += 1
    print('-' * 50)
    print(f'Ao todo foram informados {len(num)} números. \nSendo eles: {num}')
    print(f'O maior valor informado foi: {maior}')
    
maior(3, 5, 1, 7, 9, 4, 2, 73)
maior(7, 3, 5)
maior(4, 5)
