def modificar(msg='desconhecido'):
    msg = msg.split()
    ant = []
    already = {}

    for nome in msg:
        for letra in nome:
            ant.append(letra)
            #print(ant)

    already = ant.copy()

    for nome in range(len(ant)):
        join = ''.join(already)
        print(join)
        already.pop()

nome = input('Digite seu nome: ').strip()
modificar(nome)