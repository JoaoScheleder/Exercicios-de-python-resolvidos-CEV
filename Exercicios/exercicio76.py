pp = 'Pao',3 ,'Leite',4.5, 'Arroz',7,'30 ovos',10
print('-'*40)
print('{:^40}'.format('LISTA DE PRODUTOS'))
print('-'*40)
for pos in range(0,(len(pp))):
    if pos % 2 == 0 :
        print(f'{pp[pos]:.<32}',end=' ')
    else:
        print(f'{pp[pos]:>5.2f}')


