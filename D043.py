preço = float(input('Seja bem vindo(a) as nossas lojas, por favor, informe o preço do produto que deseja comprar:'))
opção = int(input('''
[1] À VISTA NO DINHEIRO/CHEQUE \033[0;36m(10% de desconto)\033[m
[2] À VISTA NO CARTÃO \033[0;36m(5% de desconto)\033[m
[3] EM ATÉ 2x NO CARTÃO \033[0;36m(preço normal)\033[m
[4] 3x VEZES OU MAIS NO CARTÃO \033[0;36m(20% de juros)\033[m
Por favor, selecione a opção de pagamento que deseja:'''))

while opção != 1 and opção != 2 and opção != 3 and opção != 4:
     opção = int(input('Número inválido, por favor, vejas as opções com mais atenção. Insira a opção novamente:'))

if opção == 1:
    desconto = preço * 90 / 100
    print('O produto sairá por R${}' .format(desconto))
elif opção == 2:
    desconto = preço * 95 / 100
    print('O produto sairá por R${}' .format(desconto))
elif opção == 3:
    print('O produto sairá por R${}' .format(preço))
elif opção == 4:
    juros = preço * 120 / 100
    print('O produto sairá por R${}' .format(juros))
