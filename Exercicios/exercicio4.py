from datetime import date
atual = date.today().year
tot = 0
id = 0
for pess in range (1,8):
    ano = int(input('Em que ano voce nasceu'))
    id = atual - ano
    if id >= 18:
        print('Essa pessoa é de maior')
        tot += 1
    else:
        print('Essa pessoa é de menor')
print('No total {} pessoa(s) atingiram a maioridade'.format(tot))
