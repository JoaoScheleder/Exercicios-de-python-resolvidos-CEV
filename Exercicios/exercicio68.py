import random
pcr = random.randint(1,10)
tot = vit = x = 0
poi = ''
e = ''
while True:
    print('-='*12)
    jog = int(input('Escolha um numero de 1 a 10 '))
    print('-=' * 12)
    if jog < 1 or jog > 10 :
         print('Escolha um numero valido')
         x += 1
         break
    else:
        tot = pcr+jog
        if tot % 2 == 0:
            poi = 'P'
            e = 'PAR'
        else:
            poi = 'I'
            e = 'IMPAR'
    print('-=' * 12)
    esc = str(input('PAR OU IMPAR [P/I]?')).upper()
    print('-=' * 12)
    if esc in 'Pp' or esc in 'Ii':
        if esc == poi:
            print(f'Computador escolheu {pcr} o total foi {tot}')
            print(f'o numero {tot} é {e}')
            print('-=' * 12)
            print('VOCE VENCEU')
            print('-=' * 12)
            vit += 1
        else:
            print(f'Computador escolheu {pcr} o total foi {tot}')
            print(f'o numero {tot} é {e}')
            print('-=' * 12)
            print('VOCE PERDEU')
            print('-=' * 12)
            break
    else:
        print('Digite um codigo valido')
        x += 1
        break
if x > 0:
    print('VOCE DIGITOU UM CODIGO INVALIDO PERDEU')
if vit >= 1:
    print(F'Parabens voce ganhou {vit} vez(es) seguidas')
else:
    print('GAME OVER VOCE NÃO VENCEU NENHUMA VEZ')


