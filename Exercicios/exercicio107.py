import moeda

num = float(input(f'Digite um preço R$:'))
por = int(input('Quanto voce quer aumentar(%):'))
pord =int(input('Quanto voce quer diminuir(%):'))
print(f'O valor aumentado em {por}% é {moeda.aumentar(num,por,True)}')
print(f'O valor diminuido em {pord}% é {moeda.diminuir(num,pord,True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num,True):}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num,False)}')