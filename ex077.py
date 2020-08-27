"""Exercício Python 077: Crie um programa que tenha uma tupla com várias
palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais."""

lista = ('banana', 'maça', 'salada', 'ferro', 'cobre', 'matematica', 'carro', 'isopor')
for palavra in lista:
    print(f'\n{palavra} → ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
