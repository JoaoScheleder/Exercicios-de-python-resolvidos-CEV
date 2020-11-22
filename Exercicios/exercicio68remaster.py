import random
tot = vit = x = 0
poi = ''
e = ''
while True:
    ejg = int(input('Digite um numero de 1 a 10'))
    epc = random.randint(1, 10)
    if ejg >= 1 and ejg <= 10:
        esc = str(input('VOCE QUER PAR OU IMPAR [P/I]')).upper()
        tot = epc + ejg
        if esc != 'P' and esc != 'I':
            print('Digite um codigo valido')
            break
            x += 1

        if tot % 2 == 0:
            poi = 'P'
            e = 'PAR'
        else:
            poi = 'I'
            e = 'IMPAR'
        if esc == poi:
            print(f'O computador jogou {epc}')
            print(f'O numero {tot} é {e} ')
            print('VOCE GANHOU')
            vit += 1
        else:
            print(f'O computador jogou {epc}')
            print(f'O numero {tot} é {e}')
            print('VOCE PERDEU')
            break
    else:
        print('Digite um codigo valido')
        x += 1
        break
if x >= 1:
    print('PROGRAMA ENCERRADO POR ERRO NA DIGITAÇAO')
if vit > 0:
    print(f'PARABENS VOCE GANHOU {vit} vez(es) seguidas')
else :
    print('\033[1;31mGAME OVER\033[m')
