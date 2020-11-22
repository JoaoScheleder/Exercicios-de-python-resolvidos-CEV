lista = []
lista.append(int(input('Digite um valor')))
qtd = 1
while True:
    esc = str(input('Quer Continuar ? [S/N]')).upper()

    if esc == 'S':
        lista.append(int(input('Digite um valor')))
        qtd += 1
    elif esc == 'N':
        print('Tudo bem')
        break
    elif esc not in 'SN':
        print('Digite S ou N porfavor')
print(f'Voce digitou {qtd} valores')
lista.sort(reverse=True)
print(f'A lista de ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista')
else:
    print('\033[1;31mO VALOR 5 NAO FOI ENCONTRADO\033[m')
