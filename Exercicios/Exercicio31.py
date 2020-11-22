# programa que cobra viagem dependendo da distancia
dist = float(input('A viagem foi de quantos kilometros? '))
if dist > 200:
    print('O valor da viagem foi de {} reais'.format((dist)*0.45))
else:
    print('O valor da viagem foi de {} reais '.format((dist)*0.5))