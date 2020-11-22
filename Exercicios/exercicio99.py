from time import sleep


def analisador(lst):
    sleep(1)
    print('Analisando os valores')
    for p in range(0,len(lst)):
        sleep(0.5)
        print(lst[p], end = ' ')
        if p == 0:
            maior = lst[0]
        else:
            if lst[p]> maior:
                maior = lst[p]
    sleep(1)
    print()
    print(f'Foram analisados {len(lst)} ao todo')
    sleep(1)
    print(f'O maior valor é {maior}')

lista = [2,3,8,1,0]
analisador(lista)
lista = [2,10,1000]
analisador(lista)