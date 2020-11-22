# programa que le seis numeros e mostra a soma apenas dos numeros pares
soma = 0
cont = 0
for c in range (0,6):
    num=int(input('Digite um numero'))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce informou {} numeros PARES e o resultado foi {}'.format(cont,soma))

