import random
meu_sorteio = [10,15,25,36,50,59]
sorteiomega = []
numeros_mega = list(range(1, 61))

cont = 0
while sorteiomega != meu_sorteio:
    sorteiomega = []
    for n in range (1,7):
        numeros_megacopia = numeros_mega.copy()
        aux = (random.choice(numeros_megacopia))
        sorteiomega.append(aux)
        numeros_megacopia.remove(aux)
    sorteiomega.sort()
    cont += 1
    print(cont)


print(f'Analise de  {cont} testes concluido')
print(f'Voce ganhou')
