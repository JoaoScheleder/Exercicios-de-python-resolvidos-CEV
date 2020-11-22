lista = list()
maior = menor = 0
posMaior = 0
posMenor = 0
for cont in range(0,5):
    x = int(input('Digite um numero para posiçao {}'.format(cont)))
    lista.append(x)
    if cont == 0:
        maior = x
        menor = x
        posMaior = posMenor = cont

    else:
        if x < menor:
            menor = x
            posMenor = cont
        if x > maior :
            maior = x
            posMaior = cont
print(f'Voce digitou os valores {lista}')
print(f'O menor valor digitado foi {menor} e esta na posiçao {posMenor}')
print(f'O maior valor digitado foi {maior} e esta na posiçao {posMaior}')
