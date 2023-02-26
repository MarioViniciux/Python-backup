from exSistema import interface
from time import sleep

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try: 
        a = open(nome, 'wt+')
        a.close()
        sleep(0.5)
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} foi criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        interface.painel_formatado('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            sleep(0.5)
    finally:
        a.close()


def cadastrar(arquivo, pessoa = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na aberturad do arquivo.')
    else:
        try:
            a.write(f'{pessoa};{idade}\n')
            sleep(0.5)
        except:
            print('Houve um erro ao adicionar o cadastro.')
        else:
            print(f'Cadastro de {pessoa} realizado com sucesso.')
            sleep(0.7)
            a.close()
