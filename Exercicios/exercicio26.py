# programa que le frase e mostra quantas letras A tem posiçao q aparece a primeira vez e ultima vez
frase = str(input('Digite um frase:')).strip()
x = frase.upper()
print('Nessa frase a letra A aparece {} veze(s)'.format(x.count('A')))
print('Aparece a primeira vez na casa {} '.format(x.find('A')+1))
print('Aparece a ultima vez na casa {}'.format(x.rfind('A')+1))
