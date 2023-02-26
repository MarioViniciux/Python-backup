def modificar(msg='desconhecido'):
    msg = msg.split()
    

    for nome in msg:
        for letra in nome:
            print(letra)

nome = input('Digite seu nome: ').strip()
modificar(nome)


#mario m a r i o