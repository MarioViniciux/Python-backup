print('Este programa converterá uma temperatura em Celsius, para Fahrenheit.')

C = float(input('Insira a temperatura atual, em Celsius:'))
F = C * 1.8 + 32

print('A temperatura de {:.1f}°C (Celsius) convertida, é igual a {:.1f}°F (Fahrenheit).' .format(C, F))