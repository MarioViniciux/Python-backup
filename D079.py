
exp = str(input('Digite uma expressão:'))
pilha = []

for símb in exp:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('A expressão é válida.')
else:
    print('A expressão é inválida.')



