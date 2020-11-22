ig = 0
hv = 0
tot = 0
hvn = ''
for p in range(1,5):
    print('-='*10)
    print('Dados da {} pessoa'.format(p))
    idade = int(input('Quantos anos vc tem'))
    ig += idade/4
    sexo = str(input('Qual o seu sexo?')).upper()
    if sexo != 'MASCULINO' and sexo != 'FEMININO':
        print('Digite um sexo valido')
    nome = str(input('Digite seu nome'))
    print('-='*12)
    if p == 1 and sexo == 'MASCULINO':
        hv = idade
        hvn = nome
    if idade>hv and sexo =='MASCULINO':
        hv = idade
        hvn = nome
    if sexo == 'FEMININO' and idade < 20:
        tot += 1
print('A media da idade do grupo é {}'.format(ig))
print('O nome do homem mais velho é {} e tem {} anos'.format(hvn,hv))
print('Temos {} mulher(es) com menos de 20 anos'.format(tot))
















