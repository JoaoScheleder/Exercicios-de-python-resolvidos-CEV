n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1+n2)/2
if m < 5.0:
    print('\033[1;31mREPROVADO\033[m')
elif m < 7.0:
    print('\033[1;33mRECUPERAÇAO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')


