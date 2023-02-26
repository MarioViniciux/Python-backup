from datetime import date

ano = date.today().year
maior = 0 
menor = 0 

for idade in range(1,8):
    year = int(input('Qual o ano de nascimento da {}° pessoa?' .format(idade)))
    idade = ano - year 
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} pessoas são maiores de idade, e {} são menores' .format(maior, menor))