#Criando um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

import math
print("Porção Inteira")
real = float(input('Digite um numero real: '))
flo = math.floor(real)
print("Tem a porta inteira de {}".format (flo))