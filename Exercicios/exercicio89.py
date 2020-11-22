from time import sleep
alunonota = [[],[],[]]
y = contador = contador2 = esc = 0
while True:
    alunonota[0].append(str(input('Digite o nome do aluno :')))
    alunonota[1].append(int(input('Digite a primeira nota:')))
    alunonota[1].append(int(input('Digite a segunda nota:')))
    x = (alunonota[1][contador]+alunonota[1][contador+1])/2
    alunonota[2].append(x)
    x = 0
    continuar = str(input('Quer continuar ? [S/N]')).strip().upper()
    contador+=2
    if continuar == 'N':
        break
print('=*'*30)
print('No. NOME             MÉDIA')
for p in range (len(alunonota[0])):
    print(f' {p}  {alunonota[0][p]:<10}{alunonota[2][p]:_>15}')
print('Esse é o boletim!!!')
while esc != 999:
    print('Digite o numero do aluno para ver suas notas separadamente. (999 para encerrar)')
    esc = int(input(''))
    if esc > len(alunonota[0])-1 and esc != 999:
        print('Aluno Nao CADASTRADO !!!')
    if esc == 0  and esc < len(alunonota[0]):
        print(f'As notas do aluno(a) {alunonota[0][esc]} foram {alunonota[1][esc]} e {alunonota[1][esc+1]}')
    elif esc != 0 and esc < len(alunonota[0]):
        print(f'As notas do aluno(a) {alunonota[0][esc]} foram {alunonota[1][esc+esc]} e {alunonota[1][esc+esc+1]}')
sleep(0.5)
print('ENCERRANDO O PROGRAMA...')
sleep(1)
print('PROGRAMA ENCERRADO')
sleep(0.5)
print('VOLTE SEMPRE')

