from random import randint 

while True:
    n = randint(0, 100)
    jogada = int(input('Try to hit the number: '))
        
    while True:
        while jogada != n:
            if jogada != n:
                if jogada > n:
                    print('\033[94mVery high, try a lower number.\033[m')
                    jogada = int(input('Try again, consider the tip: '))
                elif jogada < n:
                    print('\033[94mVery low, try a higher number.\033[m')
                    jogada = int(input('Try again, consider the tip: '))
        break
    break

print('\033[92mCorrect! You got it right.\033[m')
