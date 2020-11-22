tot = thom = mule= maiori = 0
while True:
    idade = int(input('Qual sua idade'))
    tot += 1
    sexo = ' '
    cont = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]')).strip().upper()
    if sexo in 'Mm':
        thom+= 1
    elif sexo in'Ff' and idade < 20:
        mule+= 1
    if idade >= 18:
        maiori += 1
    while cont not in 'SN':
     cont = str(input('Voce quer cadastrar mais pessoas?[S/N]')).strip().upper()
    if cont == 'N':
        print('Muito obrigado por usar o sistema de cadastramento de pessoas aleatorias')
        break
print(f'Voce cadastrou no total {tot} pessoa(s)')
print('-='*13)
print(f'Temos {maiori} pessoas maiores de 18 anos')
print('-='*13)
print(f'{thom} Homens foram cadastrados')
print('-='*13)
print(f'{mule} Mulheres menores de 20 anos cadastradas')
print('-='*13)


