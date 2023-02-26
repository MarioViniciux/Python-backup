termo = int(input('Qual o primeiro termo da progressão aritmética?'))
razão = int(input('Qual a razão da progressão aritmética?'))
ter = termo
count = 1
amais = 10
total = 0 

while amais != 0:
    total = total + amais 
    while count <= total :
        print('{}' .format(ter), end = ' > ') 
        ter += razão 
        count += 1
    print('PAUSA')
    amais = int(input('Quantos termos a mais você quer ver?'))
print('FIM')
print('Ao final do programa, foram mostrados {} termos' .format(total))

