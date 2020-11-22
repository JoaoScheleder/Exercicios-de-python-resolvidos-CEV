#programa que aumenta o salario dependendo do mesmo
sal = float(input('Digite o seu salario'))
if sal >= 1250:
    sal = (sal*0.1)+sal
if sal < 1250:
    sal = (sal*0.15)+sal
print ('o seu salario sofreu um reajuste e subiu para {:.2f} reais'.format(sal))
