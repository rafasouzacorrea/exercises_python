"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
cont = 0
cont2 = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input('Ano de nascimento da {}º pessoa: '.format(c)))
    if atual - ano >= 18:
     cont += 1
    else:
        cont2 += 1
print('Das pessoas analisadas, {} são menores e {} são maiores de idade'.format(cont2, cont))
