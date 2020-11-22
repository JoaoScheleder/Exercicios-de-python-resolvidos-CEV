def teste(x=1):
    f = 1
    for c in range(x,0,-1):
        f *= c
    return f
r1 = teste(4)
r2 = teste(6)
print(f'Os resultados valem {r1} e {r2}')