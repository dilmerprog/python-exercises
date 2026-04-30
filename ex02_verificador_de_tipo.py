#Criando um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaçõs? ', a.isspace())
print('È um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('Está em maiúsculo? ', a.isupper())
print('Está em minusculo? ', a.islower())
print('Está capitalizada? ', a.istitle())