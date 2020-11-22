#programa que converte um numero baseado na escolha do usuario
print('Bem vindo ao conversor de numeros 2.0 ')
n = int(input('Digite um numero '))
e = int(input('''
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL
Escolha uma opção'''
))
if e == 1:
    print ('o numero  {} convertido para binario é igual a {}'.format(n,bin(n)[2:]))
elif e == 2:
    print('o numero {} convertido para octal é igual {}'.format(n,oct(n)[2:]))
elif e == 3:
    print('o numero {} convertido para hexadecimal é igual a {}'.format(n,hex(n)[2:]))
elif e != [1,2,3]:
    print('Escolha apenas 1,2 ou 3 obrigado')


