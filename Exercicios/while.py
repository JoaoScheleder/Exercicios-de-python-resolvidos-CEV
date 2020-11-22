
x = 0
while True:
    num = int(input('Digite um numero'))

    if num == 999:
        break
    else:
        x += num
print(f'A soma dos numeros digitados vale {x}')
