#programa que analisa a forma de pagamento e muda o valor conforme a mesma
print('Ola bem vindo a lojinha do joao')
print('Digite um codigo de produto')
preço = int(input('''
[1] GELADEIRA 1200.00 REAIS
[2] COMPUTADOR GAMER 1500.00 REAIS
[3] Celular 1000.00 REAIS
'''))
if preço == 1:
    preço =1200
elif preço == 2:
    preço = 1500
elif preço == 3:
    preço = 1000
else:
    print('Digite um codigo de produto valido')

print('Digite um codigo de pagamento')
fp = int(input('''
[1] A vista 10% de desconto
[2] A vista no cartão 5% de desconto
[3] Até 2x no cartao preço normal
[4] 3x ou mais no cartao 20% de juros
'''))

if fp == 1:
    print('O preço a ser pago é de {}'.format((preço)-(preço*0.1)))
elif fp == 2:
    print('o preço a ser pago é de {}'.format(preço-(preço*0.05)))
elif fp == 3:
    print('Preço normal {}'.format(preço))
elif fp == 4:
    print('o preço sera de {}'.format(preço+(preço*0.20)))
else:
    print('Digite uma forma de pagamento valida')
cpf = str(input('CPF NA NOTA? SIM OU NAO')).upper()
if cpf == 'SIM':
    cpf = int(input('Digite seu cpf'))
    print(cpf)
else:
    print('BLZ MTO OBRIGADO VOLTE SEMPRE')


