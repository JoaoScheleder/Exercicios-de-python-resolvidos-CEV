matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac = maior = 0
for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = (int(input(f'Digite um numero para posição [{l} , {c}]')))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            somac += matriz[l][c]
    if l == 1:
        for s in range(0,3):
            if s == 0:
                maior = matriz[l][s]
            else:
                if matriz[l][s] > maior:
                    maior = matriz[l][s]
print('='*25)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end= '' )
    print()
print(f'A soma dos valores pares foi de {somap}')
print(f'A soma da coluna 3 foi de {somac}')
print(f'O maior valor da 2 linha foi {maior}')