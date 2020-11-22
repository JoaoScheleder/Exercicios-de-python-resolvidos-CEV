# simulador de caixa eletronico
print('BEM VINDO AO BANCO COE')

while True:
    saque = int(input('Qual o valor a ser sacado?'))
    c50 = saque//50
    if c50 > 0:
        saque = saque-(c50*50)

    c20 = saque//20
    if c20>0:
        saque = saque -(c20*20)
    c10 = saque//10
    if c10 >0:
        saque = saque -(c10*10)
    c1  = saque //1
    break
print(f'''VOCE RECEBEU
{c50} cedulas de 50.00 R$
{c20} cedulas de 20.00 R$
{c10} cedulas de 10.00 R$
{c1} cedulas de 1.00 R$''')