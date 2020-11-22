def resumo(n,p,pd):
    a = b = c = d = n
    print('Resumo Das operações')
    print(f'Preço analsado {n:>10} ')
    p = p/100
    a += n*p
    print(f'Preço aumentado {a:>10}')
    pd = pd/100
    b -= n*pd
    print(f'`{"Preço Diminuido":<10} {b:>10}')
    c /= 2
    print(f'A metade é {c:>10}')
    d *= 2
    print(f'O dobro é {d:>10}')
    return '-----------------------'



