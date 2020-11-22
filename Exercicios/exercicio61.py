# progressao aritmetica 1.0
a1 = int(input('Primeiro termo'))
r = int(input('Digite a razao'))
termo = a1
cont = 1
while cont <= 10:
    print('{}'.format(termo),end='--')
    termo += r
    cont += 1

if cont >= 10:
    mt = str(input('Quer mostrar mais alguns termo[S/N]')).upper()
    if mt == 'S':
        qdt = int(input('Voce quer mostrar mais quantos termos'))
        while cont <= (qdt+10):
            print('{}'.format(termo),end=' ')
            termo+=r
            cont +=1
    else:
        print('Tudo bem, Tchau!')



print('FIM')
