sum = 0
count = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        sum += num
        count += 1
print('A soma dos {} valores, é igual a {}' .format(count, sum))