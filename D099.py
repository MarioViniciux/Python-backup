def notas(*n, sit=False):
    '''notas(*n, sit=False)
    -> Funçao para analisar notas e situaçoes de vários alunos.
    para n: uma ou mais notas dos alunos (aceita várias).
    para sit: valor opcional, indicando se deve ou nao adicionar a situaçao.
    return: dicionário com várias informaçoes sobre a situaçao da turma.    
    '''

    dic = dict()

    media = sum(n) / len(n)

    if media > 8:
        situação = 'BOA'
    if media > 6:
        situação = 'RAZOÁVEL'
    if media < 6:
        situação = 'RUIM'
    if media < 4:
        situação = 'HORRIVEL'

    dic['Total de notas'] = len(n)
    dic['Maior nota'] = max(n)
    dic['Menor nota'] = min(n)
    dic['Média'] = media
    if sit == True:
        dic['Situação'] = situação

    print(dic)

resp = notas(6, 9, 7, 9, 1, 1)
help(notas)
