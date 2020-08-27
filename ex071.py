"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

n50 = n20 = n10 = n1 = c = 0
lista = [50, 20, 10, 1]
lista2 = [n50, n20, n10, n1]
valor = int(input('Valor: '))
while True:
    lista2[c] = valor // lista[c]
    valor = valor - lista2[c] * lista[c]
    c += 1
    if valor == 0:
        break
print(f'Você sacou R${valor} em:'
      f'\n{lista2[0]} notas de R$50'
      f'\n{lista2[1]} notas de R$20'
      f'\n{lista2[2]} notas de R$10'
      f'\n{lista2[3]} notas de R$1')
