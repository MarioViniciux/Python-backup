from random import randint

while True:
    qntd = int(input('Quantos jogos serão feitos?'))
    count = 0
    all = []
    gerados = []
    
    for c in range(0, qntd):
        while True:
            n = (randint(1,60))
            if n not in gerados:
                gerados.append(n)
                count += 1
            if count >= 6:
                break
        all.append(gerados[:])
        gerados.clear()
        count = 0

    break

for c in range(0, qntd):
    print(f'Os números sorteados para a {c + 1}° jogada foram: {all[c]}')
    