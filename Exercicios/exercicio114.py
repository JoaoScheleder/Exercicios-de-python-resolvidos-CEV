import requests
try:
    respostas = requests.get('http://pudim.com.br/')
except (requests.ConnectionError,ConnectionError,):
    print(f'O site Pudim nao esta acessivel ')
else:
    print('O site pudim esta acessivel')
