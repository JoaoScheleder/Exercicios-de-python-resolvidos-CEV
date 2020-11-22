palavras = 'MARIA','MACARRAO'.upper()
for pos in palavras:
    print(f'\nNa palavra {pos.upper()} temos: ',end= ' ')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
