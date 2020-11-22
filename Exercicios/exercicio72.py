extenso = 'ZERO','UM','DOIS','TRES','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATROZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE'
while True:
    num = int(input('Digite um numero de 0 a 20'))
    if num >= 0 and num <= 20:
        break

print(f'Voce digitou o numero {extenso[num]}')
