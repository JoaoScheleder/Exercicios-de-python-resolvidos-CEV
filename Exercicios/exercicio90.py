dados = dict()
dados['nome'] = str(input('Digite o nome do aluno: '))
dados['média'] = float(input('Digite a média: '))
if dados['média'] < 7.0:
    dados['situação'] = '\033[1;31mREPROVADO\033[m'
else:
    dados['situação'] = '\033[1;32mAPROVADO\033[m'
print(f'O nome é igual a {dados["nome"]}')
print(f'A média é igual a {dados["média"]}')
print(f'E a situação é de {dados["situação"]}')