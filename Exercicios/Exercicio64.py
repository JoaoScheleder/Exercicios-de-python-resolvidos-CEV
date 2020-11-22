#programa que soma numeros ate digitar 999
x = 0
tot = 0
nd = 0
while x != 999:
    x = int(input('Digite um numero (condiçao de parada 999)'))

    if x != 999:
        tot+=x
        nd += 1


print('Voce digitou {} numeros e a soma entre eles é de \n {}'.format(nd,tot))



