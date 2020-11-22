import random
palavras = ['elefante','cachorro','girafa','rinoceronte','arara','macaco']


def escolhepalavra():
    x = random.choice(palavras)
    y = '_ '*len(x)
    return x,y.split()


def mostrabonito():
    global palavrat
    x = ''
    for caracter in palavrat:
        x += caracter
    return x.upper()


def verificaetroca():
    global palavra,palavrat
    contador = 0
    while True:
        x = str(input('Escolha uma letra de A a Z')).lower()
        if 'A'<= x >= 'Z':
            letra = x
            if letra not in palavra:
                print(f'NAO TEMOS A LETRA {letra.upper()}')
                contador += 1
                print(f'Erro {contador} de 6')
        if contador == 1:
            print('     (O.O)')
            print()
            print()
        if contador == 2:
            print('     (O.O)')
            print('       |')
            print()
        if contador == 3:
            print('     (O.O)')
            print('     / |')
            print()
        if contador == 4:
            print('     (O.O)')
            print("     / | \ ")
            print()
        if contador == 5:
            print('     (O.O)')
            print("     / | \ ")
            print('        \ ')

        if contador >= 6:
            print('     (X.X)')
            print("     / | \ ")
            print('      / \ ')
            print('GAME OVER')
            break
        for n,letraspalavra in enumerate(palavra):
            if letra == letraspalavra:
                palavrat[n] = letra
        print(mostrabonito())
        if '_' not in mostrabonito():
            print('VOCE GANHOUU!')
            break




palavra,palavrat = escolhepalavra()
verificaetroca()