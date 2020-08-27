"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos."""
lista = []
velho = 0
cont = 0
soma = 0
nome = ''
for c in range(1, 5):
    print('-------------{}ª pessoa------------'.format(c))
    n = input('Nome: ')
    ida = int(input('Idade: '))
    gen = str(input('Gênero[F/M]: ')).lower().strip()
    soma += ida
    if gen in 'f' and ida < 20:
        cont += 1
    if ida > velho:
        if gen == 'm':
            nome = n
    velho = ida
print('Média de idade do grupo: {}'
      '\nNome do homem mais velho: {}'
      '\nNúmero de mulheres com menos de 20 anos: {}'.format(soma / 5, nome, cont))
