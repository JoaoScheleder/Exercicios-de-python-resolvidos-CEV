def ajudainterativa(msg):
    from time import sleep
    while True:
        a = str(input(f'\033[1;35m{msg}'))
        sleep(0.7)
        if a == 'fim':
            print('ENCERRANDO')
            break
        print('\033[1;31;40mAcessando ajuda interativa')
        sleep(1)
        print(help(a))


ajudainterativa('Função ou Biblioteca')
