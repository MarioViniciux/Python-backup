vel = int(input('Em qual velocidade você passou?'))

if vel >= 80:
    vel = vel - 80
    multa = vel * 7
    print('Você ultrapassou o limite de velocidade, você terá que pagar R${} de multa' .format(multa))
else:
    print('Tudo bem, tenha uma boa viagem e dirija com cuidado.')

