print('Controle de Terreno')
print('=-' * 30) 

l = float(input('Qual a largura do terreno? (m)'))
c = float(input('Qual o comprimento do terreno? (m)'))

def área(l,c):
    area = l * c
    print(f'O terreno possui {l}m de largura, e {c}m de comprimento, resultando em uma área de {area:.1f}m².')

área(l, c)