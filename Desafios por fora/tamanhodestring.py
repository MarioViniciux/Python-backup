from modu.texto import *

text_one = input('Type something: ')
text_two = input('Type sonething else: ')
linha1 = quantidade(text_one)
linha2 = quantidade(text_two)

print(f'String one: In this line, you typed: "{text_one}". It have {linha1} characters.')
print(f'String two: In this line, you typed: "{text_two}". It have {linha2} characters.')
comprimento(text_one, text_two)
conteudo(text_one, text_two)

