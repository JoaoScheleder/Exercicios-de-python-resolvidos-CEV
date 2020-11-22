# jokenpo com o computador
import random
from time import sleep
j1 = str(input('PEDRA,PAPEL,OU TESOURA')).upper()
p1 = ['PEDRA','PAPEL','TESOURA']
pce = (random.choice(p1))
sleep(0.5)
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print('PO ')
sleep(0.5)
if j1 == 'TESOURA' and pce == 'PAPEL':
    print ('escolhi {}'.format(pce))
    print('Jogador Ganhou')
elif j1 == 'TESOURA' and pce == 'PEDRA':
    print('escolhi {}'.format(pce))
    print('COMPUTADOR GANHOU')

elif j1 == 'PAPEL' and pce == 'PEDRA':
    print ('escolhi {}'.format(pce))
    print('Jogador Ganhou')
elif j1 == 'PAPEL' and pce == 'TESOURA':
    print('escolhi {}'.format(pce))
    print('COMPUTADOR GANHOU')

elif j1 == 'PEDRA' and pce == 'TESOURA':
    print ('escolhi {}'.format(pce))
    print('Jogador Ganhou')
elif j1 == 'PEDRA' and pce == 'PAPEL':
    print('escolhi {}'.format(pce))
    print('COMPUTADOR GANHOU')

else:
    print('JOGADOR ESCOLHEU {} E COMPUTADOR TAMBEM'.format(j1))
    print('EMPATE')
