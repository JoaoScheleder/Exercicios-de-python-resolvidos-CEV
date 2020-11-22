from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando os numeros:')
    sleep(1)
    for p in range(0,5):
        lst.append(randint(1,10))
        print(lst[p],end= ' ')
        sleep(0.5)


def somapar(x):
    print('A soma dos pares é:')
    sleep(1)
    for p in range(0,5):
        if lista[p] % 2 == 0:
            x += lista[p]
    print(x)


lista = []
total = 0
sorteia(lista)
somapar(total)

