import random
def achazero(m):
    cont = 0
    for i in range(0,4):
        if 0 in m[i]:
            x = m[i].index(0)
            y = i
    return y,x
def trocamatriz(m,l,c):
    a,b = achazero(m)
    if l == a+1 or l == a-1 and c == b+1 or c == b-1:
        print('MOVIMENTO INVALIDO')
    elif l == a+1 or l == a-1:
        m[a][b] = m[l][c]
        m[l][c] = 0
    elif c == b+1 or c == b-1:
        m[a][b] = m[l][c]
        m[l][c] = 0
    else:
        print('MOVIMENTO INVALIDO')


def criamatriz():
    numeros = list(range(0,16))
    matriz = [[],[],[],[]]
    for i in range(0,4):
        for c in range(0,4):
            escolha = random.choice(numeros)
            matriz[c].append(escolha)
            numeros.remove(escolha)
    print('''{}
{}
{}
{}'''.format(matriz[0], matriz[1], matriz[2], matriz[3]))

    return matriz
def mostramatriz(m):
    print('''{}
{}
{}
{}'''.format(m[0], m[1], m[2], m[3]))
    return
