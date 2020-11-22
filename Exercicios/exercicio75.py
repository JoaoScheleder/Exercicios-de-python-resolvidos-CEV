x = int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: '))
print(x)
if x.count(9) > 0:
    print(f'O numero 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'O primeiro numero 3 apareceu na posiçao {x.index(3)+1}')
else:
    print('O valor 3 nao aparece nenhuma vez')
print('Os numeros pares sao',end= ' ')
for n in x:
    if n % 2 == 0:
        print(n,end= ' ')

