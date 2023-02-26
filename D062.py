n = soma = count = 0

while True:
    n = int(input('Digite um número [999 para parar]:'))
    if n == 999: 
        break
    count += 1
    soma += n 
print(f'Você digitou {count} número e a soma deles é igual a {soma}')
print('Programa encerrado, volte sempre!')

