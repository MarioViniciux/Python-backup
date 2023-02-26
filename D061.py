from time import sleep

n = input('Aperte enter para prosseguir para a explicação, e logo após o programa: ')

print('\033[31m O programa a seguir irá ler vários números que forem digitados. Quando quiser encerrar, digite, [parar].\033[m')
ok = input('\033[32mEntendeu? Podemos prosseguir? \033[m').upper().strip()

soma = count = maior = menor = 0

while ok != 'S':
    n = int(input('\033[35mInsira o número: \033[m'))
    ok = input('\033[32mpara prosseguir, aperte ENTER. Ou para encerrar, digite [S]: \033[m').upper().strip()
    soma += n

    if count == 0:
        menor = n
        maior = n

    if n > maior:
        maior = n

    elif n < menor:
        menor = n
    count += 1    
    
print('Você digitou {} números' .format(count))
print('A média dos números é igual a {:.2f}' .format(soma / count))
print('O maior número é {}, e o menor é {}' .format(maior, menor))
sleep(1)
print('Encerrado')
