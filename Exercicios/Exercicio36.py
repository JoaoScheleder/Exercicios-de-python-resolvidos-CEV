#programa que aprova ou nao emprestimos
e = int(input('Qual o valor do emprestimo?'))
s = float(input('Quanto é a sua renda mensal?'))
a = int(input('Em quantos anos o senhor deseja pagar?'))*12
if e/a < s*0.3:
    print('O seu emprestimo foi \033[1;32mAPROVADO\033[m')
    print('A parcela sera de {:.2f} Reais '.format(e/a))
else:
    print('Infelizmente seu emprestimo foi \033[1;31mNEGADO\033[m')


















