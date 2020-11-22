
tot = prod = cta = pbarato = 0
barato = ' '
print('BEM VINDO A LOJINHA DO JOAO')
print('-='*14)
while True:
    produto = str(input('Qual o nome do produto :'))
    preço =  float(input('Qual o valor do produto'))
    tot += preço
    if cta == 0:
        barato = produto
        pbarato = preço
    if preço < pbarato:
        pbarato = preço
        barato = produto
    cta += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer cadastrar mais produtos?[S/N]')).upper().strip()
    if preço > 1000:
        prod += 1
    if cont == 'N':
        print('Obrigado por usar o sistema de cadastramento de produtos')
        break

print('-='*15)
print(f'O total gasto na compra foi de {tot:.2f} R$')
print(f'No total {prod} produtos valem mais de 1000.00R$')
print(f'O produto mais barato foi {barato.upper()} e o seu preço foi de {pbarato:.2f}R$')