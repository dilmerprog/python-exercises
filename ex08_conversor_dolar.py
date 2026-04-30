#Criando um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode ter

real = float(input('Digite o valor atual na sua carteira:'))
dolar = real / 5.48
print('Você pode ter {:.2f} em dolar'.format(dolar))