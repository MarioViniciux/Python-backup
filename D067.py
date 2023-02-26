sacar = int(input('Qual o valor que deseja sacar? R$'))
valores = 100
totalsaque = sacar
totalcedulas = 0

while True:
    if totalsaque >= valores:
        totalsaque -= valores
        totalcedulas += 1 
    else:
         if totalcedulas > 0:
             print(f'{totalcedulas} cédulas de {valores} reais')
         if valores == 100:
             valores = 50
             totalcedulas = 0
         elif valores == 50:
             valores = 20
             totalcedulas = 0
         elif valores == 20:
             valores = 10
             totalcedulas = 0
         elif valores == 10:
             valores = 5
             totalcedulas = 0
         elif valores == 5:
             valores = 1
             totalcedulas = 0
         if totalsaque == 0:
             break

