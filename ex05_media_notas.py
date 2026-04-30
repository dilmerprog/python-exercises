#Desenvolvendo um programa que leia as notas de um aluno, calcule e mostre a sua média

print('Calculando notas')
nota1 = float(input('Digite a sua nota de Matematica:'))
nota2 = float(input('Digite a sua nota de Portugues:'))
nota3 = float(input('Digite a sua nota de Historia:'))
nota4 = float(input('Digite a sua nota de Filosofia:'))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 6.0:
    print('Sua nota foi {}. Sinto muito vc reprovou!!!'. format(media))
else:
    print('Sua nota foi {}. Parabéns vc passou!!!'.format(media))