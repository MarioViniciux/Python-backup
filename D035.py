seg1 = int(input('Adicione o primeiro segmento:'))
seg2 = int(input('Adicione o segundo segmento:'))
seg3 = int(input('Adicione o terceiro e último segmento:'))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Estes valores de segmentos podem formar um triânguilo.')
    if seg1 == seg2 == seg3:
        print('E será um triângulo equilatero')
    elif seg1 != seg2 != seg3 != seg1:
        print('E será um triângulo escaleno')
    else:
        print('E será um triângulo isoceles')
else:
    print('Estes valores não podem formar um triângulo.')