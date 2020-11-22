frase = str(input('Digite um frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('É UM PALINDROMO')
else:
    print('NAO É UM PALINDROMO')

