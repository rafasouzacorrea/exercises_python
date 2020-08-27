"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

n = (int(input('Valor 1: ')), int(input('Valor 1: ')), int(input('Valor 1: ')), int(input('Valor 1: ')))
c = 0
if 3 and 9 in n:
    print(f'O número 9 apareceu {n.count(9)} vezes \nO primeiro valor 3 está na posição {n.index(3) + 1} '
        f'\nOs números pares são: ', end='')
elif 9 in n:
    print(f'O número 9 apareceu {n.count(9)} vezes \nNaõ foi digitado o número 3'
          f'\nOs números pares são: ', end='')
else:
    print(f'Não foi digitado o número 9 \nNaõ foi digitado o número 3'
          f'\nOs números pares são: ', end='')
while c < 4:
    if n[c] % 2 == 0:
        print(f'{n[c]}, ', end='')
    c += 1
