"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(c)))
    if peso > maior:
        maior = peso
        menor = peso
    elif peso < menor:
        menor = peso
print('Maior Peso: {}'
      '\nMenor Peso: {}'.format(maior, menor))
