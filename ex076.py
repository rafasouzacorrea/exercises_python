"""Exercício Python 076: Crie um programa que tenha uma tupla única com
nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular."""

produtos = ('Acém bovino', 19.98, 'Bisteca bovina', 22.98,
            'Coxão duro', 24.68, 'Paleta bovina', 21.98, 'Bisteca bovina', 22.98)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}R$', end='')
    else:
        print(produtos[c])