print('O número 0, e números negativos encerram o aplicativo')
print('-'*50)
n = int(input("De qual número quer saber a tabuada?"))
print('-'*50)
count = 0

while True:

    for num in range(n, n * 11, n):
        count += 1
        print(f'{n} x {count} = {num}')

    print('-'*50)
    n = int(input("De qual número quer ver a tabuada agora ?"))
    print('-'*50)
    count = 0

    if n <= 0:
        break

print('Encerrado')