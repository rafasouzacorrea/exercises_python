"""Exercício Python 052: Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo."""

n = int(input('Digite um número inteiro: '))
"""if n == 2 or n == 3:
    print('{} é um número primo'.format(n))
elif n / n == 1 and n % 2 !=0 and n % 3 != 0:
    print('{} é um número primo!!!'.format(n))
else:
    print('{} não é um número primo'.format(n))"""

a = 0
for c in range(1, n + 1):
    if n % c == 0:
        a += 1
if a == 2:
    print('O número {} é primo!!!'.format(n))
else:
    print('O número {} é divisível por {} números, portanto não é primo'.format(n, a))
