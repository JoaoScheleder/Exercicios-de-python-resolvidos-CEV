todos = [[],[]]
contador = 0
x = []
for p in range(1,8):
    x.append(int(input(f'Digite o {p} valor')))
    if x[contador] % 2 == 0:
        todos[0].append(x[contador])
    else:
        todos[1].append(x[contador])
    contador += 1
todos[0].sort()
todos[1].sort()
print(f'Voce digitou {p} numeros')
print(f'Os numeros pares foram {todos[0]}')
print(f'Os numeros impares foram {todos[1]}')
