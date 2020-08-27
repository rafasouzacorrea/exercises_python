"""Exercício Python 048: Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

v = 0
a = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        a += 1
        v += c
print('Dos {} valores, \nA soma é de: {}'.format(a, v))
