"""Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

r = 's'
c = 0
soma = 0
maior = ''
menor = ''
while r == 's':
    n = int(input('Número: '))
    r = str(input('Quer continuar a digitar valores? [s] [n]: ')).lower().strip()
    c += 1
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
print('Média: {} \nMaior: {} \nMenor: {}'.format(soma / c, maior, menor))
