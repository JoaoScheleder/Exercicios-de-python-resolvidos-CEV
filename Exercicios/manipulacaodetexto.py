from random import randint
from time import sleep
sorteio = []
jogos = int(input('Quantos jogos voce quer sortear? '))
contador = 0
for p in range(0,jogos):
    while contador < 6:
        x = randint(0,60)
        if x not in sorteio:
            sorteio.append(x)
            contador += 1
            x = 0

    contador = 0
    sleep(0.5)
    print(f'SORTEIO NUMERO{p+1:^5} ')
    print(sorteio)
    sorteio.clear()
print('='*20)
print('      BOA SORTE      ')


