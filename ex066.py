"""Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre elas (desconsiderando o flag)."""
soma = 0
c = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    else:
        soma += n
        c += 1
print(f'Você digitou {c} números e a soma deles é {soma}')
