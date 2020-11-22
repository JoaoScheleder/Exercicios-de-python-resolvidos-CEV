lista = []
pares = []
impares = []
esc = 'S'
while esc == 'S':
    x = int(input('Digite um numero'))
    lista.append(x)
    if x % 2 == 0:
        print(f'O valor {x} é par ')
        pares.append(x)
    else:
        print(f'O valor {x} é impar')
        impares.append(x)
    esc = str(input('Quer continuar [S/N]')).strip().upper()
    if esc == 'N':
        print('Programa encerrador')
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares {impares}')


