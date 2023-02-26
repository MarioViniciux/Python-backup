def fatorial():
    """fatorial 
    --> Calcula o fatorial de um número.
    --> Para o valor número, você insere o número ao qual quer saber o fatorial.
    --> Para o valor show, sempre vai haver uma pergunta de se quer ou não ver a conta, apenas se digitar SIM a conta será mostrada.
    --> Return um número n."""

    num = int(input('Quer saber a fatorial de qual valor?'))
    veri = input('Deseja ver a conta ou não? [S/N]').strip().upper()[0]
    c = num
    f = 1
    
    if veri in 'S':
        print(f'A fatoração de {num}, é:', end = ' ')
        while c > 0:
            print('{}' .format(c), end = '') 
            print(' X ' if c > 1 else ' = ', end = '') 
            f *= c
            c -= 1
        print('{}' .format(f))
    else:
        while c > 0:
            f *= c
            c -= 1
        print(f'O resultado da fatorial de {num}, é:', end = ' ')
        print(f)


fatorial()  
      