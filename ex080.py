"""Exercício Python 080: Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

lista = []
a = 0
for c in range(0, 5):
    a = int(input('Digite um valor: '))
    if c == 0:
        lista.append(a)
    else:
        if a >= lista[-1]:
            lista.append(a)
        elif a <= lista

