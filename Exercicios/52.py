num = int(input('Digite um numero inteiro'))
tot = 0
for c in range (1,num+1):
    if num % c == 0 :
        print('\033[1;32m',end=' ')
        tot += 1
    else:
        print('\033[1;36m', end=' ')
    print(c, end= ' ')
print('O numero {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele Não é primo')

