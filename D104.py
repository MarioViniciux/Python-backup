from exSistema import interface
from exSistema import arquivo


arq = 'TesteSistema.txt'

if not arquivo.arqExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    resposta = interface.opcoes(['Listar Pessoa', 'Cadastrar Pessoas', 'Encerrar Sistema'])

    if resposta == 1:
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.painel_formatado('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = interface.leia_int('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    else:
        interface.painel_formatado('Encerrando sistema, até logo')
        break
