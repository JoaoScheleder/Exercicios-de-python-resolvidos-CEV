import random
import funcoes_jogo_matriz as jog


# PROGRAMA PRINCIPAL
x = jog.criamatriz()
matrizganhou = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

while True:
    linha = int(input('Digite a linha do numero a ser trocado com o 0'))
    coluna = int(input('Digite a coluna do numero a ser trocado com o 0'))
    jog.trocamatriz(x,linha,coluna)
    jog.mostramatriz(x)
    if x == matrizganhou:
        print('PARABENS JOGO FINALIZADO')
        break
print('Voce ganhou')