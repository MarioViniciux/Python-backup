print('Vamos ver o teu IMC (Índice de Massa Corporal)?')
peso = float(input('Insira o teu peso para começarmos (em quilos):'))
altura = float(input('Agora insira a tua altura (em metros):'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('O teu IMC é {:.2f}' .format(imc))
    print('Atenção, você está na classificação ABAIXO DO PESO IDEAL, certifique-se de comer direito.')
elif imc < 26:
    print('O teu IMC é {:.2f}' .format(imc))
    print('Você está na classicação PESO IDEAL, continue saudável')
elif imc < 31:
    print('O teu IMC é {:.2f}' .format(imc))
    print('Atenção, você está na classificação SOBREPESO, cuidado com o excesso de alimentos.')
elif imc < 41:
    print('O teu IMC é {:.2f}' .format(imc))
    print('Atenção, você está na classificação OBESIDADE, trate de fazer regime e exercicios para ficar mais saudável.')
else:
    print('O teu IMC é {:.2f}' .format(imc))
    print('CUIDADO!! Você está na classificação OBESIDADE MORBIDA, você precisa regrar a alimentação urgentemente, além de manter uma rotina de treinos.')
