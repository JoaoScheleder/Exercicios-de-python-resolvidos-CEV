def fatorial(num,show=False):
    f = 1
    for c in range(num,0,-1):
        f *= c
        if show:
            print(c,end='')
            if c > 1:
                print(' X ',end='')
            else:
                print(' = ',end='')
    return f


print(fatorial(5,True))