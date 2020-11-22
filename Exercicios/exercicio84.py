pessoas = []
dados = []
continuar = 'S'
total = 0
pp = pl = pessomaior = pessomenor = 0
pessoaspesadas = []
pessoasleves = []
while True:
    dados.append(str(input('Nome :')))
    dados.append(int(input('Peso :')))
    pessoas.append(dados[:])
    if dados[1] >=100:
        pessoaspesadas.append(dados[0])
    elif dados [1] <= 70:
        pessoasleves.append(dados[0])
    dados.clear()
    total += 1
    for p in pessoas:
        if p == pessoas[0]:
            pessomaior= p[1]
            pessomenor =p[1]
            pp = pl = p[0]
        else:
            if p[1] > pessomaior:
                pessomaior= p[1]
                pp = p[0]
            elif p[1]< pessomenor:
                pessomenor = p[1]
                pl = p[0]
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        print('Obrigado por usar nosso software!')
        break

print(f'Foram cadastradas {total} pessoas!')
print(f'O menor peso cadastrado foi {pessomenor:.2f} da pessoa {pl}')
print(f'O maior peso cadastrado foi {pessomaior:.2f} da pessoa {pp}')
print(f'As pessoas mais pesadas foram {pessoaspesadas}')
print(f'As pessoas mais leves foram {pessoasleves}')
