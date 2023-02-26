n = int(input('Vamos brincar, digite um número, mas apenas 1 número, pode encerrar o programa: '))
soma = 0
qunt = 1

while n != 999:
    soma += n 
    qunt += 1
    n = int(input('Digite outro, lembrando, somente entre 1 número encerra o programa:'))
    if n < 999:
        print('É um número maior.')
    else:
        print('É um número menor.')
print('Você acertou')
print('Você precisou de {} tentativas.' .format(qunt))
print('A soma total dos números que você digitou, equivale a {}' .format(soma))
    
