nome = str(input('Insira seu nome completo:'))
name = nome.split()
jun = ''.join(name) 

print('Este é seu nome todo em maiusculo: ', nome.upper())
print('Este é seu nome todo em minusculo: ', nome.lower())
print('Seu nome possuí',len(jun), 'caracteres')
print('O primeiro nome possuí', len(name[0]), 'caracteres.')