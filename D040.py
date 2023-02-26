m1 = float(input('Digite a primeira nota do aluno:'))
m2 = float(input('Agora digite a segunda nota:'))
m3 = float(input('Agora ponha a ultima nota:'))
média = (m1 + m2 + m3) / 3

if média >= 7:
    print('O aluno ficou com {:.1f}, e foi APROVADO' .format(média))
elif média < 5:
    print('O aluno ficou com {:.1f}, e foi REPROVADO' .format(média))
else:
    print('O aluno ficou com {:.1f}, e está em RECUPERAÇÃO' .format(média))
