from datetime import date
dados = {}

dados['Nome'] = input('Nome: ').strip().capitalize()
nascimento = int(input('Ano de nascimento: ')) 
dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho (digite 0 caso não tenha): '))
dados['Idade'] = date.today().year - nascimento

if dados['Carteira de Trabalho'] == 0:
    for k, i in dados.items():
        print(f'{k}: {i}')    
else:
    dados['Ano de contratação'] = int(input('Insira o ano ao qual foi contratado(a) para o emprego:'))
    dados['Salário'] = float(input('Qual era o salário recebido? R$'))    
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - date.today().year)

    for k, i in dados.items():
        print(f'{k}: {i}')




