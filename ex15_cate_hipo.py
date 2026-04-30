#Programa que ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
print('Programa de comprimento')
cateto1 = float(input('Digite o numero do cateto 1: '))
cateto2 = float(input('Digite o numero do cateto 2: '))
resul1 = math.pow(cateto1, 2)
resul2 = math.pow(cateto2,2)
res = (resul1 + resul2)
raiz = math.sqrt
print('A ipotenusa sera {:.2f}'.format(raiz))