"""Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

soma = c = mil = p = 0
barato = ''
while True:
    c += 1
    print('------------------Loja------------------')
    nome = str(input('Produto: ')).strip()
    preco = float(input('Preço: R$'))
    soma += preco
    if c == 1:
        p = preco
        barato = nome
    elif preco < p:
        barato = nome
        p = preco
    if preco > 1000:
        mil += 1
    cont = input('Continuar? [s/n] ')
    while cont != 's' and cont != 'n':
        cont = input('!!Inválido!! \nContinuar? [s/n] ')
    if cont == 'n':
        break
    else:
        continue
print(f'Você comprou {c} produtos'
      f'\n{mil} deles custam mais de mil reais'
      f'\nGasto total: R${soma}'
      f'\nProduto mais barato: {barato} por R${p}')
