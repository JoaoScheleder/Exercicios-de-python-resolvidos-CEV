s = cont = 0
while True:
    num = int(input('Digite um numero'))
    if num == 999:
        break
    s += num
    cont += 1
print(f'Voce digitou {cont} valores e a soma vale {s}')

