frase = input('Digite uma frase:').upper().strip()
palavras = frase.split()
junção = ''.join(palavras)
inverso = ''

for c in range(len(junção) - 1, -1, -1):
    inverso += junção[c]

if junção == inverso:
    print('É um palíndromo, veja a seguir:')
    print(junção, inverso)
else:
    print('Esta frase não é um Palíndromo, veja a seguir:')
    print(junção, inverso)
