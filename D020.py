from random import choice

n = input('Digite o nome do primeiro aluno:')
n1 = input('Digite o nome do segundo aluno:')
n2 = input('Digite o nome do terceiro aluno:')
n3 = input('Digite o nome do terceiro aluno:')
lista = [n, n1, n2, n3]
ran = choice(lista)

print("O (a) aluno (a) que deverá apagar o quadro é {}" .format(ran))