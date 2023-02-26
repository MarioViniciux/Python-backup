def modificar(msg='desconhecido'):
    msg = msg.split()

    ant = ''

    for nome in msg:
        for letra in nome:
            #print(letra)
            ant += letra 
            print(ant)

nome = input('Digite seu nome: ').strip()
modificar(nome)