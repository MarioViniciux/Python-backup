pessoa = dict()
todos = list()
idade = 0

while True:
    add = int(input('Quantas pessoas deseja adicionar? '))

    # repetição para adicionar as pessoas no dicionário, e repassar para a lista, e após, limpar o dicionário para repetir o processo.
    for c in range(0, add):
        pessoa.clear()
        print('=-' * 30)
        pessoa['Nome'] = input('Qual o nome da pessoa? ').strip()
        pessoa['Idade'] = int(input(f'Qual a idade de {pessoa["Nome"]}? '))
        idade += pessoa['Idade']
        while True:
            pessoa['Sexo'] = input(f'Qual o sexo de {pessoa["Nome"]}? [F/M] ').upper().strip()[0]
            if pessoa['Sexo'] not in 'FfMm':
                print('ERRO! Tente novamente, somente com F para FEMININO e M para MASCULINO.')
            else:
                break
        todos.append(pessoa.copy())
        
    # verificação pra saber se a pessoa deseja adicionar mais pessoas do que foi passado no inicio do código.
    while True:
        print('=-' * 30)
        continuar = input('Deseja adicionar mais pessoas? [S/N] ').strip().upper()[0]
        if continuar not in 'SsNn':
            print('ERRO! Tente novamente utilizando S para SIM e N para NÃO.')
        else:
            break
    
    if continuar == 'N':
        break
    else:
        continue

print('=-' * 30)
print(f'A) Temos um total de {len(todos)} pessoas cadastradas.')
print(f'B) A média de idade é de {idade / len(todos):.2f}')
print(f'C) As mulheres cadastradas foram:', end = ' ')
for p in todos:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end = '; ')
print()
print(f'D) As pessoas com a idade acima da média são:', end = ' ')
for p in todos:
    if p['Idade'] > (idade / len(todos)):
        print(f'{p["Nome"]}, que é do sexo {p["Sexo"]}, e possui {p["Idade"]} anos.', end = '; ')
