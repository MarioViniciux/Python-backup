nome = input('Insira o seu nome:')
minusculo = nome.lower()
f = 'silva' in minusculo

if f == True:
    print('No nome {}, possuí sim o sobrenome Silva.' .format(nome))
else:
    print('No nome {}, não possuí o sobrenome Silva.' .format(nome))
    
