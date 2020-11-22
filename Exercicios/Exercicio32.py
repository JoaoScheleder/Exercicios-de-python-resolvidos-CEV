ano = int(input('Ola usuario, em que ano estamos'))
anod = ano % 4
if anod == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')
