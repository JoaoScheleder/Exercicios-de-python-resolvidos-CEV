lista = []
posmaior =[]
posmenor = []
for cont in range(0,5):
    lista.append(int(input('Digite um numero para posiçao {}'.format(cont))))
for pos , valores in enumerate(lista):
    if valores == max(lista):
        posmaior.append(pos)
    if valores == min(lista):
        posmenor.append(pos)
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} e esta nas posiçoes {posmaior}')
print(f'O menor valor digitado foi {min(lista)} e esta nas posiçoes {posmenor}')






