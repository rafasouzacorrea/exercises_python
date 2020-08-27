"""Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

""" a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
for c in range(0, 9):
    print('{}, '.format(a1 + r * c), end='')
print(a1 + r*9)
print('fim') """

a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
a11 = a1 + r * 10
for c in range(a1, a11, r):
    print(c, end=' ')