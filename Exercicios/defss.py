from time import sleep
def linha(tam = 42):
    t = '-'*tam
    return t


def cabecalho(x=str):
    print(linha())
    print(x.center(42))


def menu(lst):
    sleep(0.5)
    print(linha())
    c = 1
    for item in lst:
        print(f'{c}--{lst[c-1]}')
        c += 1
    print(linha())


def opcao(msg):
    x = int(input(msg))
    return x


def cadastrar(lista,dic):
    dic["nome"] = str(input('Digite o nome:'))
    dic["idade"] = int(input('Digite a idade:'))
    lista.append(dic.copy())
    dic.clear()


def mostrarcadastros(pesoa):
    cabecalho('PESSOAS CADASTRADAS!')
    linha()
    sleep(0.8)
    for c in range(0,(len(pesoa))):
        print(f'{pesoa[c]["nome"]}            {pesoa[c]["idade"]}        ')
    sleep(0.7)
    if len(pesoa) == 0:
        print('Nao há ninguem cadastrado')
    sleep(0.5)
    print('Voltando ao menu principal')
    linha()


