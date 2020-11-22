import random
n = random.randint(0,10)
n2 = int(input('Pensei em um numero de 0 a 10 tente adivinhar : '))
tent = 1
while n2 != n:
    print('ERROU!!')
    print('TENTE NOVAMENTE')
    n2 = int(input('Tenta mais uma vez'))
    tent += 1
print('Pensei no numero {}'.format(n))
print('Parabens voce acertou em {} tentativa(s)'.format(tent))
