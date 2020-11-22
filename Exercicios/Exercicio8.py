#programa que le uma medida em metros e mostra ela em centimetros e milimetros
x = float(input('Quantos metros vc tem'))
y = x*100
z = x*1000
print('Parece que você tem {} centimetros ou {} milimetros'.format(y,z))
