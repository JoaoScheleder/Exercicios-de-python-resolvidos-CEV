dados = []
pessoas = []
continuar = 'S'
escolha = 0
tot = 0
x = 0
while continuar == 'S':
    dados.append(str(input('Digite o nome a ser cadastrado')).strip())
    dados.append(int(input('Quantos anos a pessoa tem? ')))
    pessoas.append(dados[x:])
    tot += 1
    x += 2
    continuar = str(input('Mais alguem para cadastrar? [S/N]')).strip().upper()

    if continuar == 'N':
        print('Tudo bem')
        while True:
            escolha = (int(input('''QUER VER OS DADOS DE QUAL PESSOA
            [1][2][3]...''')))
            if escolha <= tot:
                print(pessoas[escolha-1])
            else:
                print(f'A pessoa numero {escolha} ainda nao foi cadastrada')
    elif continuar != 'N' and continuar != 'S':
        print('Digite [S/N] porfavor')
        continuar = str(input('QUER CONTINUAR [S/N]')).strip().upper()





