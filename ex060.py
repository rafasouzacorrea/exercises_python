"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial."""

n = int(input('Número: '))
m = 1
for c in range(n, 0, -1):
    m *= c
    if c == 1:
        print('{} = {}'.format(c, m))
    else:
        print('{} x '.format(c), end='')
print('Resultado de {}! é {}'.format(n, m))

"""Outra maneira:
from math import factorial
n = int(input('Número: '))
f = factorial(n)
print('{}! = {}'.format(n, f))"""

