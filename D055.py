sexo = str(input('Por favor, informe teu sexo [M/F]:')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Dados inválidos, por favor, tente novamente.')
    sexo = str(input('Por favor, informe teu sexo [M/F]:')).strip().upper()

print('Dados armazenados com sucesso!')