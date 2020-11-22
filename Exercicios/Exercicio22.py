# Programa que le um nome mostre ele maisculo , minusculo ,quantas letras sem contar os espaços,
# quantas letras tem o primeiro nome
nome = str(input('Digite o seu nome')).strip()
dividido = nome.split()
dividido1 = dividido[0].strip()
print ('Seu nome minusculo {}'.format(nome.lower()))
print ('Seu nome Maiusculo {}'.format(nome.upper()))
print ('Seu primeiro nome tem {} letras'.format(len(dividido1)))
print ('Seus nomes tem no total {} letras'.format(len(nome) - nome.count(' ')))
 # ou pode achar o espaço
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

