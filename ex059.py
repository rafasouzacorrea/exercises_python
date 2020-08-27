"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

d = 4
while d == 4 or d != 5:
    print('=-==-==-==-==-==-==-==-==-==-=')
    v1 = float(input('Primeiro valor: '))
    v2 = float(input('Segundo valor: '))
    r = 0
    d = int(input('[1]somar'
          '\n[2]multiplicar'
          '\n[3]maior'
          '\n[4]outros números'
          '\n[5]sair'
          '\nO que você quer fazer? '))
    if d == 1:
        r = v1 + v2
        print('A soma é {}'.format(r))
    elif d == 2:
        r = v1 * v2
        print('A multiplicação é {}'.format(r))
    elif d == 3:
        r = max(v1, v2)
        print('O maior número é {}'.format(r))
    elif d == 5:
        print('Você saiu.')
