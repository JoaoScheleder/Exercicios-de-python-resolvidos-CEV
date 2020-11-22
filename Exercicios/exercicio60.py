num = int(input('Digite um numero'))
fat = 1

for c in range (num,0,-1):
    print('{}'.format(c),end='')
    print(' X' if c > 1 else '=',end=' ')
    fat *= c
    c-= 1
    if c < 1:
        print(fat)

