#programa que classifica nadadores com base na idade
from datetime import date
ano = int(input('Em que ano voce nasceu?'))
hoje = date.today().year
idade = hoje-ano
if idade <= 9:
    print('sua categoria é MIRIM')
elif idade <=14:
    print('sua categoria é INFATIL')
elif idade <=19:
    print('sua categoria é JUNIOR')
elif idade == 20:
    print('sua categoria é SENIOR')
else:
    print('sua categoria é MASTER')
