par = 0
impar = 0 

for n in range(1,7):
    num = int(input('Digite um número, para um teste'))
    if num % 2 == 0:
        par += num
    elif num % 2 != 0:
        impar += 1

print('A soma somente de número pares, foi igual a {}' .format(par))
print('Em contraposição, {} numeros foram ignorados por serem impares' .format(impar))

