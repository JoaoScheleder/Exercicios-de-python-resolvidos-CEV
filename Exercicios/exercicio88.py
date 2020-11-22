from random import randint
from time import sleep
sorteio = []
jogos = int(input('Quantos jogos voce quer sortear? '))
numeros = []
contador = 0
for p in range(0,jogos):
    while contador < 6:
        numeros.append(randint(0,60))
        if numeros[contador] not in sorteio:
            sorteio.append(numeros[contador])
            contador += 1
    contador = 0
    sleep(1)
    print(f'SORTEIO NUMERO{p+1:^5} ')
    print(sorteio)
    sorteio.clear()
    numeros.clear()



