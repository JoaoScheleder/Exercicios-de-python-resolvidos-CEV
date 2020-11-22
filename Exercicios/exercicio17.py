import math
x = float(input('Digite o cateto oposto'))
y = float(input('Digite o cateto adjacente'))
h = pow(x,2) + pow(y,2)
print('A hipotenusa vale {}'.format(math.sqrt(h)))
