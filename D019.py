import math
ang = int(input('Digite o ângulo:'))
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print('O ângulo {}° tem o seno de {:.1f}°, cosseno de {:.1f}° e {:.1f}° de tangente' .format(ang, sen, cos, tan))
