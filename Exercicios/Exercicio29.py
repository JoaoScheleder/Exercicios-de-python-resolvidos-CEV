# programa que le a velocidade e multa acima de 80 km/h 7 reais por km a cima
v = int(input('O carra passou a quantos km por hora ?'))
if v<= 80:
    print('Tudo certo ,esta dentro dos limites de velocidade')
else:
    print('Esta acima do limite de velocidade, Multa de {:.2f} reais'.format((v-80)*7))