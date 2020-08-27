"""Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

hom = m20 = id18 = 0
u = '-' * 42
while True:
    print('------------CADASTRE UMA PESSOA-----------')
    idade = int(input('Idade: '))
    sex = str(input('Sexo: [M/F]: ')).lower().strip()
    while sex != 'm' and sex != 'f':
        sex = str(input(f'!!!Resposta inválida!!!\nSexo: [M/F]: ')).lower().strip()
    if sex == 'm':
        hom += 1
    if sex == 'f' and idade < 20:
        m20 += 1
    if idade >= 18:
        id18 += 1
    p = str(input('Continuar? [s/n]: ')).lower().split()[0]
    while p != 's' and p != 'n':
        p = str(input(f'!!!Resposta inválida!!!\nContinuar: [s/n]: ')).lower().strip()
    if p == 'n':
        break
    if p == 's':
        continue
print(f'{u}\nMaiores de idade: {id18}'
      f'\nHomens cadastrados: {hom}'
      f'\nMulheres com menos de 20 anos cadastradas: {m20} \n{u}')
