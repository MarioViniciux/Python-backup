city = input('Digite o nome da cidade em que você mora:').lower()
tst = 'santo' in city

if tst == True:
    print('O nome da sua cidade com "Santo", que interessante!')
else:
    print('O nome da sua cidade não se inicia com um nome bonito')