num = str(input('Digite um numero')).zfill(4)
x = num.strip()
print('milhar {}'.format(x[0]))
print('Centena {}'.format(x[1]))
print('Dezena {}'.format(x[2]))
print('Unidade {}'.format(x[3]))

