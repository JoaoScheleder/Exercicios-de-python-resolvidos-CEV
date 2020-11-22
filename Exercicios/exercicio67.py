while True:
    num = int(input('Digite um numero'))
    if num < 0:
        break
    print('A tabuada do numero {}'.format(num))
    for cont in range (1,11):
        print(f' {num} X {cont} = {num*cont}')
print('Obrigado por usar o programa TABUADA 3.0, Volte sempre')

