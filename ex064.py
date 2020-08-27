"""Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

n = int(input('1º Número: '))
soma = 0
c = 1
while n != 999:
    c += 1
    soma += n
    n = int(input('{}º Número: '.format(c)))
print('Foram digitado {} números \nA soma é {}'.format(c - 1, soma))
