def leiaint(msg):
    ok=False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok=True
        else:
            print('ERRO')
        if ok:
            break
    return valor



n = leiaint('Digite um numero')
print(f'Voce digitou o numero {n}')