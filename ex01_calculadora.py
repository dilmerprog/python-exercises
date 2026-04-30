#Criando um programa que leia dois números e mostre a soma, subtração, multiplicação e divisão.

n1 = int(input('Numero 1:'))
n2 = int(input('Numero 2:'))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
print('O resultado de {} + {}= {}' .format(n1, n2, soma))
print('O resultado de {} - {}= {}'. format(n1 , n2, subtracao))
print('O Resultadod de {} * {}= {}'. format(n1, n2, multiplicacao))
print('O resultado de {} / {}= {}'. format(n1, n2, divisao))