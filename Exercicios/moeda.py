def aumentar(n,p=0,formato = False):
    p = p/100
    n += n*p
    return n  if formato is False else moeda(n)


def diminuir(n,p=0,formato = False):
    p = p/100
    n -= n*p
    return n if formato is False else moeda(n)


def metade(n,formato = False):
    n /= 2
    return n if formato is False else moeda(n)


def dobro(n,formato= False):
    n *= 2
    return n if formato is False else moeda(n)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')
