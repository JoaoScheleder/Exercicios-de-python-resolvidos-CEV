lista = []
for p in range (0,5):
    x = int(input('Digite um valor'))
    if p == 0 or x > lista[-1]:
        print('Adicionado ao final da lista')
        lista.append(x)
    else:
        contador = 0
        while contador < len(lista):
            if x <= lista[contador]:
                lista.insert(contador,x)
                print(f'Adicionado na posiçao {p}')
                break
            contador += 1



print(lista)


