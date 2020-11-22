def ficha(snome=False,sgols=False):
    nome = str(input('Digite um nome?'))
    if len(nome) >= 1:
        snome = True
    elif snome == False:
        nome = 'Desconhecido'
    gols = str(input(f'Quantos gols`{nome} fez?'))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if gols >= 1:
        sgols = True
    elif snome == False:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato')


ficha()