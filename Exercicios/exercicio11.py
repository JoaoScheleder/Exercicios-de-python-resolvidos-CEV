#programa que le a area de uma parede e mostre quanto de tinta sera necessario para pinta la
x = float(input('quantos metros de altura tem a parede?'))
y = float(input('quantos metros de largura tem a parede?'))
z = x*y

print ('A area da parede é de {} e serao necessario(s) {} lata(s) de tinta para pinta la'.format(z,z/2))