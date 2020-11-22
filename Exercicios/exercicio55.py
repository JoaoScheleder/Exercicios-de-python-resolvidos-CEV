pessomaior = 0
pessomenor = 0
for p in range(1,6):
    peso = float(input('peso da {} pessoa'.format(p)))
    if p == 1:
        pessomaior = peso
        pessomenor = peso
    else:
        if peso > pessomaior:
            pessomaior = peso
        if peso < pessomenor:
            pessomenor = peso
print('O pesso maior é {}'.format(pessomaior))
print('O pesso menor é {}'.format(pessomenor))




