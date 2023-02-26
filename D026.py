phrase = input('Digite uma frase:').upper()
print('A letra "A" aparece {} vezes.' .format(phrase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.' .format(phrase.find('A') + 1))
print('A letra "a" aparece pela última vez na posição {}.' .format(phrase.rfind('A') + 1))
