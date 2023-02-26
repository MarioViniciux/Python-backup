times = 'Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América Mineiro', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense'

print(f'Os 5 primeiros colocados foram: {times[0:5]}')
print(f'Os ultimos 4 colocados foram: {times[16:]}')
print(f'Os times em ordem alfabética ficam da seguinte forma: {sorted(times)}')

for pos, times in enumerate(times):
    if times == 'Chapecoense':
        print(f'O time da {times}, está na {pos + 1}° colocação')
