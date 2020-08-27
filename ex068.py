"""Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. """

import random
c = 0
while True:
    pi = str(input('Par ou impar? [p/i]: ')).lower().strip()
    if pi == 'i' or pi == 'p':
        n = int(input('Número: '))
        v = random.randint(0, 10)
        s = n + v
        if s % 2 == 0:
            r = 'p'
        else:
            r = 'i'
        if r != pi:
            break
        else:
            print(f'Ganhou!!! \nPc jogou {v} e você jogou {n}')
            c += 1
    else:
        print('Valor inválido!')
print(f'Perdeu!! \nPc jogou {v} e você jogou {n} \nVocê teve {c} vitórias')
