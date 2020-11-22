from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'Jogador1':randint(1,6),
           'Jogador2':randint(1,6),
           'Jogador3':randint(1,6),
           'Jogador4':randint(1,6)
}
ranking = dict()
for k,v in jogadas.items():
    print(f'O {k} tirou {v}')
    sleep(0.75)
ranking = sorted(jogadas.items() , key=itemgetter(1),reverse=True)
print(ranking)
contador = 1
for p,v in ranking:
    print(f'Em {contador} lugar {p} com {v} pontos')
    contador+= 1