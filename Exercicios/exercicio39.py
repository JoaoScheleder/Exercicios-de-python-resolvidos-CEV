from datetime import date
hoje = date.today()
print(hoje)
ano = int(input('Voce nasceu em que ano'))
if hoje.year-ano > 18:
    print('ja passou do tempo de se alistar no serviço militar obrigatorio')
elif hoje.year-ano < 18:
    print('Voce ainda n se precisa se alistar')
else:
    print('Voce tem que se alistar esse ano!')

