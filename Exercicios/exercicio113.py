def leiaint(msg):
    x = int(input(msg))
    return x

def leiafloat(msg):
    x = float(input(msg))
    return x

# programa principal


y = 0
while True:
    try:
        y = leiaint('Digite um numero inteiro')
        break
    except ValueError:
        print('\033[1;31mDigite um numero inteiro valido\033[m')
while True:
    try:
        t = leiafloat('Digite um numero real')
        break
    except ValueError:
        print('\033[1;31mDigite um numero real valido\033[m')
print(f'Voce digitou o numero {y} inteiro e o numero {t} real')