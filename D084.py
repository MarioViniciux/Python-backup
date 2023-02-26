list = []
dados = []

while True:
    qntd = int(input('Quantos alunos quer adicionar?'))
    
    for c in range(0, qntd):
        print('=-' * 25)
        nome = input('Nome do aluno(a):').strip()
        nota1 = float(input('1° nota do aluno:'))
        nota2 = float(input('2° nota do aluno:'))
        nota3 = float(input('3° nota do aluno:'))
        media = (nota1 + nota2 + nota3) / 3
        dados.append(nome)
        dados.append([nota1, nota2, nota3])
        dados.append(media)
        list.append(dados[:])
        nota1 = nota2 = nota3 = media = 0
        dados.clear()

    print('=-' * 25)
    adicionar = input('Deseja adicionar mais alunos?[S/N]')[0].strip()
    
    if adicionar in 'Ss':
        continue
    if adicionar in 'Nn':
        break
        


print('=-' * 25)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print('-' * 50)
for i, a in enumerate(list):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 50)
    opção = int(input('Deseja mostrar a nota de qual aluno? (999 interrompe):'))

    if opção == 999:
        print('Finalizando...')
        break
    elif opção <= len(list) - 1:
        print(f'As notas de {list[opção][0]} são {list[opção][1]}')
    else:
        print('Erro, tente novanente, mas somente com números, e ao qual exista na lista de alunos.')
    