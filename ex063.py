"""Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
os N primeiros elementos de uma Sequência de Fibonacci. """

n = int(input('Número: '))
a1 = -1
a2 = 1
for c in range(0, n ):
    a3 = a1 + a2
    print(a3, end=' ')
    a1 = a2
    a2 = a3