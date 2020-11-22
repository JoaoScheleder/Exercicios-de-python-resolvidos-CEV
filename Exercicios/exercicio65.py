# programa que le varios numeros mostre a media entre eles e o menor e maior valor digitados
maior = 0
continuar = 'S'
cont = 0
num = 0
x = 0

while continuar != 'N':
    num = int(input('Digite um numero :'))
    continuar = str(input('Quer continuar S/N')).upper()
    cont += 1
    x += num

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Voce digitou {} valores e a media entre eles foi de {}'.format(cont,(x/cont)))
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
