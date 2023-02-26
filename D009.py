m = int(input('Digite a distância em metros:'))
km = m / 1000
hm = m / 100
dc = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('Em {} possui {} quilômetros' .format(m, km))
print('Em {} possui {} hectômetros' .format(m, hm))
print('Em {} possui {} decâmetros' .format(m, dc))
print('Em {} possui {} decímetros' .format(m, dm))
print('Em {} possui {} centímetros' .format(m, cm))
print('Em {} possui {} milímetros' .format(m, mm))
