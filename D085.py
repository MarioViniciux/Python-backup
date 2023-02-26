aluno = {}

aluno['Nome'] = input('Nome:').strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}:'))

if aluno['Média'] < 6:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'


print('=-' * 25)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
