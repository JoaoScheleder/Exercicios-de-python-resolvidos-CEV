# programa que le um angulo e mostre seu seno cosseno e tangente
import math
x = int(input('Digite um angulo qualquer'))
s = math.sin(math.radians(x))
c = math.cos(math.radians(x))
t = math.tan(math.radians(x))
print('O seno do angulo {:.2f} é {:.2f} seu cosseno é {:.2f} e a tangente {:.2f}'.format(x,s,c,t))
