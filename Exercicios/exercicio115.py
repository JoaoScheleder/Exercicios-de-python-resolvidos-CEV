import defss
defss.cabecalho('Sistema de Cadastramento')
menu = ['Pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do sistema']
pessoas = []
pessoa = {}
while True:
    defss.menu(menu)

    try:
        y = defss.opcao('Sua opção?')

    except (ValueError, NameError):
        defss.linha()
        print('Opção invalida use apenas [1],[2],[3]')
        continue
    if y == 3:
        print('Saindo do sistema')
        print(defss.linha())
        break
    elif y == 2:
        while True:
            defss.cabecalho('Cadastrando novo integrante')
            print(defss.linha())
            defss.cadastrar(pessoas,pessoa)
            x = str(input('Quer continuar?[S/N]')).strip().upper()
            if x == 'N':
                print(defss.linha())
                print('Voltando ao menu....')
                break
    elif y == 1:
        defss.mostrarcadastros(pessoas)
    else:
        defss.linha()
        print('Digite uma opção valida')
print('Obrigado por usar o sistema de cadastramento 1.0v')
