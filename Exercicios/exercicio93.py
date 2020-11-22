dados = {}
listagols = []
jogadores = []
while True:
    dados["nome"] = str(input('Digite o nome do JOGADOR:'))
    dados["partidas"] = int(input("Quantas partidas ele jogou"))
    for c in range(dados["partidas"]):
        listagols.append(int(input(f'Quantos gols ele fez na partida {c+1}')))
        dados["gols"] = listagols[:]
    listagols.clear()
    jogadores.append(dados.copy())
    dados.clear()
    continuar = str(input('Quer continuar ? [S/N]')).strip().upper()
    if continuar == 'N':
        print('Finalizando...')
        break
for c in range(len(jogadores)):
    print(f'{c}   {jogadores[c]["nome"]}    {jogadores[c]["gols"]}    {sum(jogadores[c]["gols"])}')