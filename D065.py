maior18 = homens = mulheres20menos = pessoa =  mulher = 0


while True:
    parar = 'N'
    idade = int(input('Qual a idade da pessoa:'))
    sexo = input('Qual o sexo da pessoa? [F/M]:').upper().strip()[0]
    while sexo not in 'FM':
        sexo = input('Qual o sexo da pessoa? [F/M]:').upper().strip()[0]
    pessoa += 1
    parar = input('Deseja encerrar?[S/N]').upper().strip()[0]
    while parar not in 'SN':
        parar = input('Deseja encerrar?[S/N]').upper().strip()[0]

    if idade >= 18:
        maior18 += 1
        
    if sexo == 'F':
        mulher += 1
        if idade <= 20:
            mulheres20menos += 1
    else:
        homens += 1
        
    if parar == 'S':
        break

print(f'Foram cadastradas {pessoa} pessoas, e {maior18} são maiores de idade.')
print(f'Dessas {pessoa} pessoas, {homens} são homens.')
print(f'{mulher} são mulheres, e {mulheres20menos} possuem menos de 20 anos')
