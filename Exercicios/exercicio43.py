# programa de IMC
print('Bem vindo ao programa de IMC')
peso = float(input('Digite seu peso'))
altura = float(input('Digite a sua altura'))
imc = peso/(altura*altura)
print('O seu indice de massa corpora é de {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO do peso')
elif imc >=18.5 and imc < 25:
    print('Peso NORMAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')