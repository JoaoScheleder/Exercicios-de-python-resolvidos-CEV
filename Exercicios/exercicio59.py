x = 0
mn = 0
n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro'))
while x != 5:
    if n1 > n2:
        mn = n1
    else:
        mn = n2
    print('''[1]SOMA\n[2]MULTIPLICAÇAO\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA''')
    x = int(input('sua opcão é ?'))
    print ('-='*10)
    if x == 1:
        print('SOMA')
        print('A soma dos numeros resultou em {}'.format(n1+n2))
        print('-='*10)
    elif x == 2:
        print('MULTIPLICAÇÃO')
        print('A multiplicaçao do numero {} pelo numero {} resultou em {}'.format(n1,n2,n1*n2))
        print('-='*10)
    elif x == 3:
        print('O maior numero é {}'.format(mn))
        print('-='*10)
    elif x == 4:
        n1 = int(input('Digite outro valor'))
        n2 = int(input('Digite outro tambem'))
    elif x != 5:
        print('Digite um codigo valido')
print('SAINDO DO PROGRAMA .........')

