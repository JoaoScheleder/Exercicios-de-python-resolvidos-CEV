lista = []
x = int(input('Digite um numero'))
lista.append(x)
print('Valor inserido com sucesso')
while True:
    continuar = str(input('Quer adicionar um numero?[S/N]')).upper().strip()
    if continuar == 'S':
        x = int(input('Digite um numero'))

        if x in lista:
            print('Valor Duplicado!')
        else:
            lista.append(x)
            print('Valor inserido com Sucesso!')
    elif continuar == 'N':
        print('Tudo bem entao')
        break
    else:
        print('Digite uma letra valida')
lista.sort()
print(f'A lista em ordem crescente ficou {lista}')







