l1 = int(input('Digite um comprimento'))
l2 = int(input('Digite outro'))
l3 = int(input('E mais um'))
if (l2-l3)<l1<(l2+l3) and (l1-l3)<l2<(l1+l3) and (l1-l2)<l3<(l1+l2):
    print('Os comprimentos informados podem formar um triangulo')
    if l1 == l2 == l3:
      print ('Todos os lados sao iguais triangulo EQUILATERO')
    elif l1 != l2 != l3 != l1:
      print ('Todos os lados sao diferentes triangulo ESCALENO')
    else:
      print ('Dois angulos iguais triangulo ISOSCELES')



else:
    print('comprimentos informados \033[1;31mNÃO\033[m podem formar um triangulo')