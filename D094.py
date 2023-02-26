from random import randint

numeros = list()
somadp = list()
soma = 0

def sorteio():
    for c in range(0, 5):
        n = randint(1, 10000)
        if n % 2 == 0:
            somadp.append(n)
        numeros.append(n)
        print(f'O {c + 1}° número sorteado foi {numeros[c]}')
        print('/' * 50)
        
def SomaPar(soma):
    for i, v in enumerate(somadp):
        soma += v
    print(f'A soma de todos os números pares sorteados é igual a: {soma}')

sorteio()
SomaPar(soma)
