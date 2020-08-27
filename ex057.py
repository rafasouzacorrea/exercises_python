"""Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
até ter um valor correto."""

s = str(input('Qual seu gênero[m/f]: ')).lower().strip()[0]
g = 'feminino'
if s == 'm':
    g = 'masculino'
while s != 'm' and s != 'f':
    s = str(input('Inválido. Digite novamente: ')).lower().strip()[0]
print('Gênero: {}'.format(g))
