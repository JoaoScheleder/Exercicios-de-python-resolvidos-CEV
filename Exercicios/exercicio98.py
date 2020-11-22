from time import sleep



def contador(a,b,c):
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a>b:
        while a >= b:
            sleep(0.5)
            print(a, end=' ')
            a -= c
    elif a<b:
         while a <= b:
            sleep(0.5)
            print(a, end=' ')
            a += c



contador(1,10,1)
print()
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem')
inicio = int(input('INICIO:'))
fim = int(input('FIM:'))
passos = int(input('PASSOS:'))
contador(inicio,fim,passos)

