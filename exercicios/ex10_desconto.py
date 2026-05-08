#Criando um algaritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o valor do produto: '))
des = preco * 0.95
print('O valor do preço agora sera {}'.format(des))