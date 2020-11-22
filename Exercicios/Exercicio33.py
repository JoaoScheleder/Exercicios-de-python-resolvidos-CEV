# qual dos tres é o maior numero
n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
n3 = int(input('Digite mais um'))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor valor é {}'.format(menor))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O maior valor é {}'.format(maior))

