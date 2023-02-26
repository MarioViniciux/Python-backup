num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'

while True:

    while True:
        dig = int(input('Digite um número entre 0 e 20:'))
        if 0 <= dig <= 20:
            
            break
        print('Tente novamente', end =' ')
    print(f'Você digitou o número {num[dig]}')

    pergunta = input('Deseja encerrar o aplicativo?').lower().strip()[0]
    if pergunta in 'Ss':
        break


