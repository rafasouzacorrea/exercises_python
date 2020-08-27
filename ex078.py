"""Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista. """

lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
lista.sort(reverse=True)
print(lista)
print(f'Maior número foi {lista[0]} \nMenor número foi {lista[-1]}')

