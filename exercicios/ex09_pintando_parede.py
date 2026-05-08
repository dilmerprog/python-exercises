#Programa que ler largura e aaltura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
tinta = area / 2
print('A quantidade de tinta necessaaria para pintar sera: {}'. format(tinta))