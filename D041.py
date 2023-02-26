idade = int(input('Qual idade do atleta?'))

if idade < 10:
    print('um atleta com {} anos está na classificação Mirim' .format(idade))
elif idade < 15:
    print('um atleta com {} anos está na classificação Infantil' .format(idade))
elif idade < 20:
    print('um atleta com {} anos está na classificação Junior' .format(idade))
elif idade < 26:
    print('um atleta com {} anos está na classificação Master' .format(idade))
else:
    print('um atleta com {} anos está na classificação Senior' .format(idade))