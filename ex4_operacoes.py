#Criando algaritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

print('Dobro, triplo e raiz quadrada')
n = int(input('Digite um nurmero:'))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O dobro de {} e {}'.format(n, dobro))
print('O triplo de {} e {}'.format(n, triplo))
print('A raiz quadrada de {} e {}'.format(n, raiz))