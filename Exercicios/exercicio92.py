from datetime import date
import time
hoje = date.today().year
dados = dict()
dados["nome"] = str(input('Digite seu nome: '))
dados["ano"] = 2020 - int(input('Digite o ano de nascimento: '))
dados["ct"] = int(input('Digite o numero da carteira de trabalho :'))
if dados["ct"] != 0:
    dados["anocontrato"] = 2020 - int(input('Qual foi o ano de sua contrataçao'))
    dados["salario"] = int(input('Digite o seu salario'))
    dados["aposentadoria"] = dados["anocontrato"]

print(dados)
print(f'Nome tem valor {dados["nome"]}')
print(f'Idade tem valor {dados["ano"]}')
print(f'Carteira tem valor {dados["ct"]}')
if dados ["ct"] != 0:
    print(f'Anos de contribuiçao tem valor {dados["anocontrato"]}')
    print(f'Salario tem valor {dados["salario"]}')
    print(f'Aposentadoria tem valor {35 - dados["aposentadoria"]}')

