dados = dict()
dadostotal = list()
mulheres = []
tot = 0
media = 0
while True:
    dados["nome"] = str(input('Digite seu nome: '))
    dados["sexo"] = str(input('Qual o seu sexo: [M/F]')).strip().upper()
    if dados["sexo"] == 'F':
        mulheres.append(dados["nome"])
    dados["idade"] = int(input('Quantos anos voce tem? '))
    dadostotal.append(dados.copy())
    dados.clear()
    tot += 1
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(f'No total {tot} pessoas foram cadastradas')
print(f'As pessoas com idade acima da média são')
for p in range(tot):
    media += dadostotal[p]["idade"]
media = media / tot
for c in range(tot):
    if dadostotal[c]["idade"]>media:
        print(dadostotal[c])
print(f'A média de idade foi {media} anos')
print(f'A lista com todas as mulheres {mulheres}')

