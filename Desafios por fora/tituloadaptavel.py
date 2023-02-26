def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


msg = input('Digite a frase para o titulo: ').strip() 
escreva(msg)